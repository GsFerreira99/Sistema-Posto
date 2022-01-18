from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from Funcoes.genericas import calculo_horas, inserir_dados_cb, mascara_dinheiro, preencher_cb

from DataBase.DataBase import DataBase
from Funcoes.genericas import caminho_db
from Funcoes.caixa import Caixa
from Funcoes.poupup import Erro


class Consulta:

    def __init__(self, ui):
        self.ui = ui
        self.ui.nav_consultas.setCurrentIndex(1)
        self.graf = None
        self.db = DataBase(caminho_db())

        self.dados_atuais_tabela = None
        self.dados_atuais_tabela_retirada = None
        self.dados_atuais_tabela_ponto = None

        #Navegação
        self.ui.cons_btn_vendas.clicked.connect(lambda: self.navegação_principal(1, "> Gráficos"))
        self.ui.cons_btn_tabela.clicked.connect(lambda: self.navegação_principal(2, "> Tabelas"))
        self.ui.cons_btn_tabela.clicked.connect(lambda: Tabela.preencher_cb_funcionario(self))
        self.ui.cons_btn_retiradas.clicked.connect(lambda: self.navegação_principal(3, "> Retiradas"))
        self.ui.cons_btn_retiradas.clicked.connect(lambda: Retirada.preencher_cb_nome(self))
        self.ui.cons_btn_ponto.clicked.connect(lambda: self.navegação_principal(4, "> Ponto"))
        self.ui.cons_btn_ponto.clicked.connect(lambda: Ponto.preencher_cb_funcionario(self))
        

        #Widget Periodo
        self.ui.cons_cb_periodo.currentIndexChanged.connect(lambda: self.intervalo_data())
        self.ui.cons_cb_tab_periodo.currentIndexChanged.connect(lambda: self.intervalo_data())
        self.ui.cons_cb_tab_retiradas.currentIndexChanged.connect(lambda: self.intervalo_data())

        #widget Filtro
        #self.ui.cons_cb_bomba_2.currentIndexChanged.connect(lambda: Retirada.comboBox_filtro(self))

        self.ui.cons_btn_ok.clicked.connect(lambda: self.receber_info_grafico())
        self.ui.cons_btn_tab_ok.clicked.connect(lambda: self.definir_tabela())
        self.ui.cons_btn_ok_2.clicked.connect(lambda: self.definir_tabela_retiradas())
        self.ui.cons_btn_tab_ret.clicked.connect(lambda: self.pesquisar_retirada_especifica())
        self.ui.cons_ponto_btn_ok.clicked.connect(lambda: self.definir_tabela_ponto())

    def definir_tabela(self):
        self.dados_atuais_tabela = Tabela.receber_dados_tabela(self)

    def pesquisar_retirada_especifica(self):
        info = Tabela.selecionar_dados(self)
        dados = Retirada.retirada_especifica(self, info)
        if dados != []:
            Retirada.inserir_dados_tabela_retiradas(self, dados)
            Retirada.preencher_total(self, self.dados_atuais_tabela_retirada)
            self.navegação_principal(3, "> Retiradas")
            Retirada.preencher_cb_nome(self)
        else:
            Erro("Não há retiradas cadastradas neste caixa.", QMessageBox.Warning, titulo="Alerta")

    def definir_tabela_retiradas(self):
        self.dados_atuais_tabela_retirada = Retirada.receber_dados_retirada(self)
        Retirada.preencher_total(self, self.dados_atuais_tabela_retirada)

    def navegação_principal(self, info, texto):
        self.intervalo_data()
        self.ui.nav_consultas.setCurrentIndex(info)
        self.ui.cons_lb_nav.setText(texto)
        self.ui.cons_tab_total.setText("")

    def intervalo_data(self):
        #Gráficos
        if self.ui.cons_cb_periodo.currentText() == "Selecionar Período":
            self.ui.stackedWidget_3.setCurrentIndex(0)
            self.ui.stackedWidget_3.setMaximumSize(200, 30)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(1)
            self.ui.stackedWidget_3.setMaximumSize(0, 0)

        #Tabelas
        if self.ui.cons_cb_tab_periodo.currentText() == "Selecionar Período":
            self.ui.stackedWidget_4.setCurrentIndex(0)
            self.ui.stackedWidget_4.setMaximumSize(200, 30)
        else:
            self.ui.stackedWidget_4.setCurrentIndex(1)
            self.ui.stackedWidget_4.setMaximumSize(0, 0)
        
        #Retiradas
        if self.ui.cons_cb_tab_retiradas.currentText() == "Selecionar Período":
            self.ui.stackedWidget_5.setCurrentIndex(0)
            self.ui.stackedWidget_5.setMaximumSize(200, 30)
        else:
            self.ui.stackedWidget_5.setCurrentIndex(1)
            self.ui.stackedWidget_5.setMaximumSize(0, 0)

    def receber_info_grafico(self):
        dados = []
        
        dados.append(self.receber_info_bomba(self.ui.cons_cb_bomba.currentText()))
        
        datas = self.tratar_datas(self.ui.cons_cb_periodo.currentText(), 
                                    self.ui.cons_dt_inicio.date().toString("yyyy-MM-dd"), 
                                    self.ui.cons_dt_fim.date().toString("yyyy-MM-dd"))
        dados.append(self.tratar_filtro(self.ui.cons_cb_informacao.currentText()))

        db = self.db.select_generico(
            "SELECT strftime('%d', data), {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format(
                dados[1], dados[0], datas[0], datas[1],))
        self.criar_grafico(db, self.ui.cons_cb_informacao.currentText())

    def tratar_filtro(self, filtro):
        if filtro == "Total Vendas":
            return "total"
        elif filtro == "Dinheiro":
            return "dinheiro_caixa"
        elif filtro == "Pix":
            return "pix"
        elif filtro == "Cartão":
            return "cartao"
        elif filtro == "Litros":
            return "litros"
        elif filtro == "Saídas":
            return "retiradas"

    def receber_info_bomba(self, info):
        if info == "Bomba 01":
            bomba = 1
        elif info == "Bomba 02":
            bomba = 2
        else:
            bomba = "Tudo"

        return bomba

    def criar_grafico(self, dados, tipo):
        self.limpar_graf()
        self.graf = Grafico_Vendas(dados, tipo)
        self.ui.cons_tab_total.setText(self.graf.total)
        self.grafico = self.ui.cons_gr_vendas.addWidget(self.graf)
        
    def limpar_graf(self):
        self.ui.cons_gr_vendas.removeWidget(self.graf)
    
    def tratar_datas(self, periodo, dat_ini, dat_fim):
        data = QDateTime.currentDateTime()
        dia = data.toString("dd")
        if periodo == "Mês Atual":
            data_inicio = "{}-01".format(data.toString("yyyy-MM"))
            data_fim = "{}-31".format(data.toString("yyyy-MM"))

        elif periodo == "Mês Anterior":
            mes = data.toString("MM")
            mes = "{}".format(int(mes)-1)
            data_inicio = "{}-{}-01".format(data.toString("yyyy"), mes)
            data_fim = "{}-{}-31".format(data.toString("yyyy"), mes)

        elif periodo == "Selecionar Período":
            data_inicio = dat_ini
            data_fim = dat_fim
        
        elif periodo == "Dia Atual":
            data_inicio = data.toString("yyyy-MM-dd")
            data_fim = data.toString("yyyy-MM-dd")

        elif periodo == "Ultima Semana":
            data_fim = "{}".format(data.toString("yyyy-MM-dd"))
            dia = (int(dia)-7)
            if len(str(dia)) == 1:
               dia = f"0{dia}"
            data_inicio = "{}-{}".format(data.toString("yyyy-MM"), dia)

        elif periodo == "Ultima Quinzena":
            data_fim = "{}".format(data.toString("yyyy-MM-dd"))
            dia = (int(dia)-15)
            if len(str(dia)) == 1:
               dia = f"0{dia}"
            data_inicio = "{}-{}".format(data.toString("yyyy-MM"), dia)

        return data_inicio, data_fim

    def limpar_tabela(self, tabela):
        while (tabela.rowCount() > 0):
            tabela.removeRow(0)

    def preencher_tabela(self, dados, tabela):
        for i, j in enumerate(dados):
            rowPosition = tabela.rowCount()
            tabela.insertRow(rowPosition)
            for i, s in enumerate(j):
                dado = QTableWidgetItem(str(s))
                tabela.setItem(rowPosition, i, dado)

    def mascara_data(self, data):
        dia = "{}".format(data[-2]+ data[-1])
        mes = "{}".format(data[-5]+ data[-4])
        ano = "{}".format(data[-10]+ data[-9]+ data[-8]+ data[-7])
        mascara_data = "{}/{}/{}".format(dia, mes, ano)

        return mascara_data
    
    def definir_tabela_ponto(self):
        self.dados_atuais_tabela_ponto = Ponto.receber_dados_ponto(self)
        #Ponto.preencher_total(self, self.dados_atuais_tabela_ponto)

class Tabela(Consulta):

    def receber_dados_tabela(self):
        dados = []
        
        dados.append(self.receber_info_bomba(self.ui.cons_cb_tab_filtro.currentText()))
        
        datas = self.tratar_datas(self.ui.cons_cb_tab_periodo.currentText(), 
                                    self.ui.cons_dt_tab_inicio.date().toString("yyyy-MM-dd"), 
                                    self.ui.cons_dt_tab_fim.date().toString("yyyy-MM-dd"))
        dados.append(self.ui.cons_cb_tab_funcionario.currentText())

        if dados[1] != "":
            db = self.db.select_generico(
                """ SELECT codigo, data, bomba, funcionario, litros, valor, dinheiro_caixa, pix, cartao, resto, retiradas
                    FROM Caixa 
                    WHERE bomba={} AND data BETWEEN '{}' AND '{}' AND funcionario = '{}' """.format(dados[0], datas[0], datas[1], dados[1]))
        else:
            db = self.db.select_generico(
                """ SELECT codigo, data, bomba, funcionario, litros, valor, dinheiro_caixa, pix, cartao, resto, retiradas
                    FROM Caixa 
                    WHERE bomba={} AND data BETWEEN '{}' AND '{}' """.format(dados[0], datas[0], datas[1], dados[1]))
        
        Tabela.inserir_dados_tabela(self, db)
        Tabela.preencher_total(self, db)

        return db

    def inserir_dados_tabela(self, dados):
        self.limpar_tabela(self.ui.cons_tb)
        dados = Tabela.inserir_mascara_dados(self, dados)
        self.ui.cons_tb.horizontalHeader().setVisible(True)
        self.preencher_tabela(dados, self.ui.cons_tb)

    def preencher_total(self, db):
        total = 0
        for i in db:
            total+= (i[6] + i[7] + i[8])
        self.ui.cons_tab_total.setText(mascara_dinheiro(total))

    def inserir_mascara_dados(self, dados):
        info = []
        for i in dados:
            info.append([])
            info[-1].append(self.mascara_data(i[1]))
            info[-1].append(i[2])
            info[-1].append(i[3])
            info[-1].append(i[4])
            info[-1].append("R$ {:.2f}".format(float(i[5])))
            info[-1].append("R$ {:.2f}".format(float(i[6])))
            info[-1].append("R$ {:.2f}".format(float(i[7])))
            info[-1].append("R$ {:.2f}".format(float(i[8])))
            info[-1].append("R$ {:.2f}".format(float(i[9])))

            if i[10] != None:
                info[-1].append("R$ {:.2f}".format(float(i[10])))
            else:
                info[-1].append("R$ 0.00")

        return info

    def selecionar_dados(self):
        row = self.ui.cons_tb.currentRow()
        caixa = self.dados_atuais_tabela[int(row)]
        return caixa[0]

    def preencher_cb_funcionario(self):
        inserir_dados_cb(self.ui.cons_cb_tab_funcionario, self.db.select_generico("SELECT DISTINCT funcionario FROM Caixa"))

class Retirada(Consulta):

    def receber_dados_retirada(self):
        dados = []
        
        dados.append(self.ui.cons_cb_nome_2.currentText())
        dados.append(self.ui.ln_cons_info_2.text())
        
        datas = self.tratar_datas(self.ui.cons_cb_tab_retiradas.currentText(), 
                                    self.ui.cons_dt_tab_inicio_2.date().toString("yyyy-MM-dd"), 
                                    self.ui.cons_dt_tab_fim_2.date().toString("yyyy-MM-dd"))

        dados.append(datas)

        db = Retirada.consultar_dados(self, dados)

        Retirada.inserir_dados_tabela_retiradas(self, db)

        return db

    def consultar_dados(self, dados):
        datas = dados[2]
        if dados[0] == "" and dados[1] == "":
            db = self.db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Caixa.data BETWEEN '{}' AND '{}'""".format(datas[0], datas[1]))
        elif dados[0] == "" and dados[1] != "":
            db = self.db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Caixa.data BETWEEN '{}' AND '{}' AND Retiradas.descricao LIKE '%{}%' """.format(datas[0], datas[1], dados[1]))
        elif dados[1] == "":
            db = self.db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Retiradas.nome = '{}' AND Caixa.data BETWEEN '{}' AND '{}'""".format(dados[0], datas[0], datas[1]))
        elif dados[1] != "":
            db = self.db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Retiradas.nome = '{}' AND Caixa.data BETWEEN '{}' AND '{}' AND Retiradas.descricao LIKE '%{}%' """.format(dados[0], datas[0], datas[1], dados[1]))

        return db

    def retirada_especifica(self, caixa):
        db = self.db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Retiradas.caixa = {}""".format(caixa))
        self.dados_atuais_tabela_retirada = db
        return db

    def inserir_dados_tabela_retiradas(self, dados):
        self.limpar_tabela(self.ui.cons_tb_retiradas)
        dados = Retirada.inserir_mascara_dados(self, dados)
        self.ui.cons_tb_retiradas.horizontalHeader().setVisible(True)
        self.preencher_tabela(dados, self.ui.cons_tb_retiradas)

    def inserir_mascara_dados(self, dados):
        info = []
        for i in dados:
            info.append([])
            info[-1].append(i[2])
            info[-1].append(self.mascara_data(i[1]))
            info[-1].append(i[3])
            info[-1].append("R$ {:.2f}".format(float(Caixa.converter_string_para_float(self, i[4]))))
            info[-1].append(i[5])

        return info

    def preencher_cb_nome(self):
        inserir_dados_cb(self.ui.cons_cb_nome_2, self.db.select_generico("SELECT DISTINCT nome FROM Retiradas"))

    def preencher_total(self, db):
        total = 0
        for i in db:
            total+= i[4]
        self.ui.cons_tab_total.setText(mascara_dinheiro(total))

class Ponto(Consulta):

    def preencher_cb_funcionario(self):
        inserir_dados_cb(self.ui.cons_ponto_cb_funcionario, self.ui.db.select_generico("SELECT nome FROM Usuarios WHERE tipo = 2"))

    def receber_dados_ponto(self):
        #dados.append(self.ui.cons_ponto_cb_filtro.currentText())
        nome = self.ui.cons_ponto_cb_funcionario.currentText()

        datas = self.tratar_datas(self.ui.cons_ponto_cb_periodo.currentText(), 
                                    self.ui.cons_ponto_dt_inicio.date().toString("yyyy-MM-dd"), 
                                    self.ui.cons_ponto_dt_fim.date().toString("yyyy-MM-dd"))
    
        db = Ponto.acessar_db(self, nome, datas)
        
        Ponto.inserir_dados_tabela_ponto(self, db)

        return db

    def acessar_db(self, nome, datas):
        if nome == "":
            db = self.ui.db.select_generico("SELECT * FROM Registro_ponto WHERE data BETWEEN '{}' AND '{}'".format(datas[0], datas[1]))
        else:
            db = self.ui.db.select_generico("SELECT * FROM Registro_ponto WHERE funcionario = '{}' AND data BETWEEN '{}' AND '{}'".format(nome, datas[0], datas[1]))
        return db

    def inserir_dados_tabela_ponto(self, dados):
        self.limpar_tabela(self.ui.cons_ponto_tb)
        dados = Ponto.inserir_mascara_dados(self, dados)
        self.ui.cons_ponto_tb.horizontalHeader().setVisible(True)
        self.preencher_tabela(dados, self.ui.cons_ponto_tb)

    def inserir_mascara_dados(self, dados):
        info = []
        for i in dados:
            info.append([])
            info[-1].append(self.mascara_data(i[1]))
            info[-1].append(i[2])
            info[-1].append(i[3])
            info[-1].append(i[4])
            info[-1].append(i[5])
            info[-1].append(i[6])

        return info

    def preencher_total(self, db):
        total = datetime(1, 1, 1, 0, 0, 0)
        for i in db:
            total+= calculo_horas(i[3:])
        #self.ui.cons_tab_total.setText(total.time())

class Grafico_Vendas(FigureCanvas):
    def __init__(self, db, tipo, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        self.db = db
        dados = self.tratamento_dados()

        datas = dados[0]
        valor = dados[1]

        valores = list(map(lambda x: float(x), valor))
        
        self.total = "0"

        x = np.arange(len(datas))
        self.ax.set_facecolor(("#D3D3D3"))
        self.fig.set_facecolor(("#eeeeee"))

        self.ax.bar(x, valores, 0.35, label='R$')
        self.ax.set_xticks(x)

        font = 10
        if len(datas) >= 10:
            font = 8

        for pos, valor in enumerate(valores):
            if tipo == "Litros":
                self.ax.text(pos, valor + 2, (f"{valor:.2f}"),  horizontalalignment='center', fontsize=font)
                self.total = str(sum(int(i) for i in valores))
            else:
                self.ax.text(pos, valor + 2, mascara_dinheiro(valor), horizontalalignment='center', fontsize=font)
                self.total = mascara_dinheiro(sum(int(i) for i in valores))
        self.ax.set_xticklabels(datas)
        self.fig.suptitle(f"{tipo.upper()}" ,size=15)
        self.ax.set_ylabel("Valor")
        self.ax.set_xlabel("Dia")


    def tratamento_dados(self):
        dados = [[], []]
        
        for i in self.db:
            data = dados[0]
            valor = dados[1]
            try:
                if i[0] != data[-1]:
                    dados[0].append(i[0])
                    dados[1].append(i[1])
                else:
                    valor[-1]+= i[1]
            except IndexError:
                    dados[0].append(i[0])
                    dados[1].append(i[1])
        return dados