from sqlite3.dbapi2 import DatabaseError
from PyQt5 import QtCore
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QMessageBox
from DataBase.DataBase import DataBase
from Funcoes.genericas import caminho_db, converter_string_para_float, inserir_dados_cb, mascara_dinheiro, verificar_vazio
from Funcoes.poupup import Erro

class Financeiro:

    def __init__(self, ui):
        self.ui = ui

        self.tela_home()

        self.ui.fin_btn_home.clicked.connect(self.tela_home)
        self.ui.fin_btn_mov.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentIndex(2))
        self.ui.fin_btn_novo.clicked.connect(self.tela_novo)
        self.novo = Novo(self.ui)

    def tela_home(self):
        Home(self.ui).inserir_valor_conta()
        self.ui.stackedWidget_6.setCurrentIndex(0)

    def tela_novo(self):
        self.novo.preencher_tipo()
        self.novo.mudar_tela()
        self.ui.stackedWidget_6.setCurrentIndex(2)


class Novo(Financeiro):

    def __init__(self, ui):
        self.ui = ui

        self.preencher_tipo()
        self.mudar_tela()

        self.ui.fin_novo_mov.currentIndexChanged.connect(lambda: self.mudar_tela())
        self.ui.fin_novo_desp_btn_inserir.clicked.connect(lambda: self.inserir_nova_despesa())
        self.ui.fin_novo_ent_btn_inserir.clicked.connect(lambda: self.inserir_nova_entrada())
        self.ui.fin_novo_transf_btn_inserir.clicked.connect(lambda: self.inserir_nova_transferencia())


    def mudar_tela(self):
        if self.ui.fin_novo_mov.currentText() == "DESPESA":
            self.ui.stackedWidget_8.setCurrentIndex(0)
            self.limpar_campos_despesa()
            self.ultimos_lancamentos("Despesas")
        elif self.ui.fin_novo_mov.currentText() == "TRANSFERÊNCIA":
            self.ui.stackedWidget_8.setCurrentIndex(1)
            self.limpar_campos_transferencia()
            self.ultimos_lancamentos("Transferencia")
        elif self.ui.fin_novo_mov.currentText() == "ENTRADA":
            self.ui.stackedWidget_8.setCurrentIndex(2)
            self.limpar_campos_entrada()
            self.ultimos_lancamentos("Entrada")
    
    def inserir_db(self, querry):
        DataBase(caminho_db()).querry_generica(querry)
    
    def ultimos_lancamentos(self, tabela):
        campos = [
            [self.ui.widget_33, self.ui.label_156, self.ui.label_157],
            [self.ui.widget_42, self.ui.label_158, self.ui.label_159],
            [self.ui.widget_45, self.ui.label_160, self.ui.label_161],
            [self.ui.widget_48, self.ui.label_162, self.ui.label_163],
            [self.ui.widget_54, self.ui.label_166, self.ui.label_167],
        ]
        self.limpar(campos)
        if tabela == "Despesas":
            img = "image: url(:/icons/img07.png);"
        elif tabela == "Entrada":
            img = "image: url(:/icons/img08.png);"
        elif tabela == "Transferencia":
            img = "image: url(:/icons/img10.png);"

        dados = DataBase(caminho_db()).select_generico("SELECT codigo, descricao, valor FROM {} ORDER BY codigo DESC LIMIT 5 ".format(tabela))
        for campo, dado in zip(campos, dados):
            campo[0].setStyleSheet("""border: 0px;padding: 5px;{}""".format(img))
            campo[1].setText(dado[1].title())
            campo[2].setText(mascara_dinheiro(dado[2]))

    def limpar(self, campos):
        for campo in campos:
            campo[0].setStyleSheet("""border: 0px;padding: 5px;""")
            campo[1].setText("")
            campo[2].setText("")

    def inserir_movimentacao(self, tabela):
        data = QDate.currentDate().toString("yyyy-MM-dd")
        codigo = DataBase(caminho_db()).select_generico("SELECT codigo FROM {} ORDER BY codigo DESC LIMIT 1".format(tabela))
        self.inserir_db("INSERT INTO Movimentacoes (data, tipo, id) VALUES('{}', '{}', '{}')".format(data, tabela, codigo[0][0]))
   
    ##DESPESA
    def inserir_nova_despesa(self):
        try: 
            dados = []
            dados.append(self.ui.fin_novo_desp_status.currentText())
            dados.append(self.ui.fin_novo_desp_data.date().toString("yyyy-MM-dd"))
            dados.append(self.ui.fin_novo_desp_tipo.currentText())
            dados.append(self.ui.fin_novo_desp_desc.text())
            dados.append(converter_string_para_float(self.ui.fin_novo_desp_valor.text()))
            dados.append(self.ui.fin_novo_desp_conta.currentText())

            if verificar_vazio(dados) == False:
                self.inserir_db("INSERT INTO Despesas (status, data, tipo, descricao, valor, conta) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(*dados))
                self.inserir_movimentacao("Despesas")
                if dados[0] == "Pago":
                    Transacao(dados[4]).despesa(dados[5])
                Erro("Despesa inserida com sucesso!", QMessageBox.Information)
                self.mudar_tela()
                self.limpar_campos_despesa()
            else:
                Erro("Preencha todos os campos", QMessageBox.Information, titulo="ERRO")

        except ValueError:
            Erro("Preencha os campos corretamente", QMessageBox.Information, titulo="ERRO")

    def limpar_campos_despesa(self):
        self.ui.fin_novo_desp_status.setCurrentIndex(0)
        self.ui.fin_novo_desp_data.setDate(QDate.currentDate())
        self.ui.fin_novo_desp_tipo.setCurrentIndex(0)
        self.ui.fin_novo_desp_desc.setText("")
        self.ui.fin_novo_desp_valor.setText("")
        self.ui.fin_novo_desp_conta.setCurrentIndex(0)

    def preencher_tipo(self):
        dados = DataBase(caminho_db()).select_generico("SELECT DISTINCT tipo FROM Despesas")
        inserir_dados_cb(self.ui.fin_novo_desp_tipo, dados)

    ##ENTRADA
    def inserir_nova_entrada(self):
        try:
            dados= []
            dados.append(self.ui.fin_novo_ent_data.date().toString("yyyy-MM-dd"))
            dados.append(self.ui.fin_novo_ent_desc.text())
            dados.append(converter_string_para_float(self.ui.fin_novo_ent_valor.text()))
            dados.append(self.ui.fin_novo_ent_conta.currentText())

            if verificar_vazio(dados) == False:
                self.inserir_db("INSERT INTO Entrada (data, descricao, valor, conta) VALUES ('{}', '{}', '{}', '{}')".format(*dados))
                self.inserir_movimentacao("Entrada")
                self.limpar_campos_entrada()
                Transacao(dados[2]).entrada(dados[3])
                Erro("Entrada inserida com sucesso!", QMessageBox.Information)

                self.mudar_tela()
            else:
                Erro("Preencha todos os campos", QMessageBox.Information, titulo="ERRO")

        except ValueError:
            Erro("Preencha os campos corretamente", QMessageBox.Information, titulo="ERRO")

    def limpar_campos_entrada(self):
            self.ui.fin_novo_ent_data.setDate(QDate.currentDate())
            self.ui.fin_novo_ent_desc.setText("")
            self.ui.fin_novo_ent_valor.setText("")
            self.ui.fin_novo_ent_conta.setCurrentIndex(0)
    
    ##TRANSFERENCIA
    def inserir_nova_transferencia(self):
        try: 
            dados = []
            dados.append(self.ui.fin_novo_transf_data.date().toString("yyyy-MM-dd"))
            dados.append(self.ui.fin_novo_transf_de.currentText())
            dados.append(self.ui.fin_novo_transf_para.currentText())
            dados.append(self.ui.fin_novo_transf_desc.text())
            dados.append(converter_string_para_float(self.ui.fin_novo_transf_valor.text()))

            if verificar_vazio(dados) == False:
                self.inserir_db("INSERT INTO Transferencia (data, de, para, descricao, valor) VALUES ('{}', '{}', '{}', '{}', '{}')".format(*dados))
                self.inserir_movimentacao("Transferencia")
                self.limpar_campos_transferencia()
                Transacao(dados[4]).transferencia(dados[1], dados[2])
                Erro("Transferência inserida com sucesso!", QMessageBox.Information)
                self.mudar_tela()
            else:
                Erro("Preencha todos os campos", QMessageBox.Information, titulo="ERRO")

        except ValueError:
            Erro("Preencha os campos corretamente", QMessageBox.Information, titulo="ERRO")
    
    def limpar_campos_transferencia(self):
            self.ui.fin_novo_transf_data.setDate(QDate.currentDate())
            self.ui.fin_novo_transf_de.setCurrentIndex(0)
            self.ui.fin_novo_transf_para.setCurrentIndex(0)
            self.ui.fin_novo_transf_desc.setText("")
            self.ui.fin_novo_transf_valor.setText("")


class Home(Financeiro):

    def __init__(self, ui):
        self.ui = ui

        self.inserir_valor_conta()
        self.inserir_contas_vencer()
        self.inserir_contas_pagas()
        self.ui.stackedWidget_6.setCurrentIndex(0)

        self.ultimos_lancamentos()

    def inserir_valor_conta(self):
        self.ui.fin_home_cx_posto.setText(self.consultar_valor_conta("Caixa Posto"))
        self.ui.fin_home_cx_banco.setText(self.consultar_valor_conta("Conta Inter"))

    def atualizar_tela(self):
        self.inserir_valor_conta()
        self.inserir_contas_vencer()

    def inserir_contas_vencer(self):
        self.ui.label_119.setText(self.contas_a_vencer("Hoje"))
        self.ui.label_120.setText(self.contas_a_vencer("Mês"))
    
    def inserir_contas_pagas(self):
        self.ui.label_122.setText(self.contas_pagas("Hoje"))
        self.ui.label_124.setText(self.contas_pagas("Mês"))

    def consultar_valor_conta(self, conta):
        dado =  DataBase(caminho_db()).querry_generica("SELECT valor FROM Contas WHERE conta = '{}'".format(conta))
        return mascara_dinheiro(int(dado[0][0]))
    
    def contas_a_vencer(self, periodo):
        if periodo == "Hoje":
            dados = DataBase(caminho_db()).querry_generica("SELECT valor FROM Despesas WHERE data = '{}' AND status = 'Em Aberto' ".format(QDateTime.currentDateTime().toString('yyyy-MM-dd')))
        if periodo == "Mês":
            data = "{}-31".format(QDateTime.currentDateTime().toString('yyyy-MM'))
            dados = DataBase(caminho_db()).querry_generica("SELECT valor FROM Despesas WHERE data BETWEEN '{}' AND '{}' AND status = 'Em Aberto' ".format(QDateTime.currentDateTime().toString('yyyy-MM-dd'), data))
        total = 0
        for dado in dados:
            total+= int(dado[0])
        return mascara_dinheiro(total)
    
    def ultimos_lancamentos(self):
        campos = [
            [self.ui.widget_29, self.ui.label_116, self.ui.label_121],
            [self.ui.widget_34, self.ui.label_127, self.ui.label_126],
            [self.ui.widget_36, self.ui.label_129, self.ui.label_128],
            [self.ui.widget_38, self.ui.label_131, self.ui.label_130],
        ]
        self.limpar(campos)
        dados = self.consultar_movimentacao()

        for campo, dado in zip(campos, dados):
            if dado[0] == "Despesas":
                img = "image: url(:/icons/img07.png);"
            elif dado[0] == "Entrada":
                img = "image: url(:/icons/img08.png);"
            elif dado[0] == "Transferencia":
                img = "image: url(:/icons/img10.png);"

            campo[0].setStyleSheet("""border: 0px;padding: 5px;{}""".format(img))
            campo[1].setText(dado[1][1].title())
            campo[2].setText(mascara_dinheiro(dado[1][2]))

    def consultar_movimentacao(self):
        dados = []
        mov = DataBase(caminho_db()).select_generico("SELECT codigo, tipo, id FROM Movimentacoes ORDER BY codigo DESC LIMIT 4 ")
        for i in mov:
            dado = DataBase(caminho_db()).select_generico("SELECT codigo, descricao, valor FROM {} WHERE codigo = {} ".format(i[1], i[2]))
            dados.append([i[1], dado[0]])
        return dados

    def limpar(self, campos):
        for campo in campos:
            campo[0].setStyleSheet("""border: 0px;padding: 5px;""")
            campo[1].setText("")
            campo[2].setText("")
    
    def contas_pagas(self, periodo):
        if periodo == "Hoje":
            dados = DataBase(caminho_db()).querry_generica("SELECT valor FROM Despesas WHERE data = '{}' AND status = 'Pago' ".format(QDateTime.currentDateTime().toString('yyyy-MM-dd')))
        if periodo == "Mês":
            data_ini = "{}-01".format(QDateTime.currentDateTime().toString('yyyy-MM'))
            data_fim = "{}-31".format(QDateTime.currentDateTime().toString('yyyy-MM'))
            dados = DataBase(caminho_db()).querry_generica("SELECT valor FROM Despesas WHERE data BETWEEN '{}' AND '{}' AND status = 'Pago' ".format(data_ini, data_fim))
        total = 0
        for i in dados:
            total+= i[0]
        return mascara_dinheiro(total)

class Transacao:

    def __init__(self, valor):
        self.valor = valor

    def entrada(self, conta):
        DataBase(caminho_db()).querry_generica("UPDATE Contas SET valor = valor + {} WHERE conta = '{}'".format(self.valor, conta))

    def transferencia(self, conta1, conta2):
        DataBase(caminho_db()).querry_generica("UPDATE Contas SET valor = valor - {} WHERE conta = '{}'".format(self.valor, conta1))
        DataBase(caminho_db()).querry_generica("UPDATE Contas SET valor = valor + {} WHERE conta = '{}'".format(self.valor, conta2))
    
    def despesa(self, conta):
        DataBase(caminho_db()).querry_generica("UPDATE Contas SET valor = valor - {} WHERE conta = '{}'".format(self.valor, conta))