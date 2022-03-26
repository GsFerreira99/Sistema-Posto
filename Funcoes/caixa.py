from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from GUI.ui_GUI import Ui_Sistema
from PyQt5.QtCore import QDateTime
from DataBase.DataBase import DataBase

from Funcoes.genericas import caminho_db, mascara_dinheiro, remover_masc_dinheiro

from Funcoes.poupup import Poup, Erro


class Caixa(Ui_Sistema):

    def __init__(self, ui, dados):        
        #inicia as variaveis basicas
        self.db = DataBase(caminho_db())
        self.gasolina = self.db.valor_combustivel("Gasolina Comum")

        self.dados_usuario = dados
        self.ui = ui

        #Insere informações na tela
        self.ui.cb_bomba.currentIndexChanged.connect(lambda: self.redefinir_campo_leitura_anterior())
        self.atualizar_tela()
        self.preencher_nome()

        #Ação dos botões
        self.ui.btn_cx_inserir.clicked.connect(lambda: self.calculo_caixa())
        self.ui.btn_cx_inserir.setAutoDefault(True)
        self.ui.btn_cx_fechar.clicked.connect(lambda: self.inserir_dados())
        self.ui.btn_cx_fechar.setAutoDefault(True)
        self.ui.btn_cx_ret_inserir.clicked.connect(lambda: self.inserir_retirada())
        self.ui.btn_cx_ret_inserir.setAutoDefault(True)

        self.ui.ln_cx_din.editingFinished.connect(lambda: self.definir_campo_troco())
        self.ui.ln_cx_pix.editingFinished.connect(lambda: self.definir_campo_troco())
        self.ui.ln_cx_cartao.editingFinished.connect(lambda: self.definir_campo_troco())

    def atualizar_tela(self):
        self.limpar_dados()
        self.inserir_informacoes_tela()
        self.inserir_info_cb_bombas()
        self.inserir_nomes_cb_retiradas()

    def limpar_dados(self):
        self.dados = {
            'codigo' : 0,
            'digital_anterior': '',
            'analogico_anterior': '',
            'valor_gasolina' : self.gasolina,
        }
        self.dados_fechamento_caixa = {
            'data' : '',
            'bomba' : '',
            'funcionario' : '',
            'digital_anterior': '',
            'analogico_anterior': '',
            'digital_atual' : '',
            'analogico_atual' : '',
            'litros' : '',
            'valor' : '',
            'dinheiro_caixa' : '',
            'pix' : '',
            'cartao' : '',
            'total' : '',
            'resto' : '',
            'retiradas' : {},
        }
        self.dados_retiradas = {}

    def inserir_informacoes_tela(self):
        self.ui.cx_nome.setCurrentText(self.dados_usuario['nome'])
        self.ui.cx_data.setDateTime(QDateTime.currentDateTime())

    def redefinir_campo_leitura_anterior(self):
        self.consultar_leitura_anterior()
        self.ui.ln_ana_anterior.setText(str(self.dados['analogico_anterior']))
        self.ui.ln_digi_anterior.setText(str(self.dados['digital_anterior']))

    def consultar_leitura_anterior(self):
        dados = self.db.select_caixa_anterior(self.ui.cb_bomba.currentText())
        leitura_anterior = dados[0]
        self.dados['codigo'] = dados[1]
        if leitura_anterior[0] > 1000.000:
            anterior = leitura_anterior[0] - 1000
        else: anterior = leitura_anterior[0]
        self.dados['digital_anterior'] = self.converter_string_para_float("{:.3f}".format(anterior)) 
        self.dados['analogico_anterior'] = self.converter_string_para_float(leitura_anterior[1]) 

    def calculo_caixa(self):
        campos_vazios = False
        campos_vazios = self.receber_dados_leitura_fechamento()

        if campos_vazios == False:
            self.receber_dados_leitura_anterior()

            analogico = (self.dados_fechamento_caixa['analogico_atual'] - self.dados_fechamento_caixa['analogico_anterior']) * 1000
            digital = self.dados_fechamento_caixa['digital_atual'] - self.dados_fechamento_caixa['digital_anterior']

            self.dados_fechamento_caixa['litros'] = float("{:.2f}".format((analogico + (digital)) / 2))

            self.dados_fechamento_caixa['valor'] = self.converter_string_para_float("{:.2f}".format(self.dados_fechamento_caixa['litros'] * self.dados['valor_gasolina']))

            self.inserir_valores_finais()
        else:
            Erro("Preencha todos os campos corretamente.", QMessageBox.Warning)

    def calculo_tanque(self, litros):
        DataBase(caminho_db()).querry_generica("UPDATE Valor_combustivel SET quantidade = quantidade - {} WHERE combustivel = 'Gasolina Comum'".format(litros))

    def inserir_valores_finais(self):
        self.ui.ln_cx_litros.setText(f"{self.dados_fechamento_caixa['litros']}")
        self.ui.ln_cx_valor.setText(f"{self.dados_fechamento_caixa['valor']}")
        
        campos = [self.ui.ln_cx_din, self.ui.ln_cx_pix, self.ui.ln_cx_cartao]
        for campo in campos:
            campo.setText("0.0")

    def receber_dados_leitura_fechamento(self):
        try:
            self.dados_fechamento_caixa['analogico_atual'] = self.converter_string_para_float(self.ui.ln_ana_atual.text())
            self.dados_fechamento_caixa['digital_atual'] = self.converter_string_para_float(self.ui.ln_digi_atual.text())
            return False
        except ValueError:
            return  True

    def receber_dados_leitura_anterior(self):
        self.dados_fechamento_caixa['analogico_anterior'] = self.dados['analogico_anterior']
        self.dados_fechamento_caixa['digital_anterior'] = self.dados['digital_anterior']

    def definir_campo_troco(self):
        try: 
            self.dados_fechamento_caixa['dinheiro_caixa'] = self.converter_string_para_float(self.ui.ln_cx_din.text())
            self.dados_fechamento_caixa['pix'] = self.converter_string_para_float(self.ui.ln_cx_pix.text())
            self.dados_fechamento_caixa['cartao'] = self.converter_string_para_float(self.ui.ln_cx_cartao.text())
 
            try:
                self.dados_fechamento_caixa['total'] = self.dados_fechamento_caixa['dinheiro_caixa'] + self.dados_fechamento_caixa['pix'] + self.dados_fechamento_caixa['cartao'] + self.calcular_total_retiradas()
                self.dados_fechamento_caixa['resto'] = self.dados_fechamento_caixa['total'] - self.dados_fechamento_caixa['valor']
                self.ui.ln_cx_resto_2.setText((f"{self.dados_fechamento_caixa['total']:.2f}"))
                self.ui.ln_cx_resto.setText((f"{self.dados_fechamento_caixa['resto']:.2f}"))
            except ValueError or TypeError:
                Erro("Valor inválido.", QMessageBox.Warning)
                self.ui.ln_cx_din.setText("0")
                self.ui.ln_cx_pix.setText("0")
                self.ui.ln_cx_cartao.setText("0")
                self.ui.ln_cx_resto_2.setText("0")

        except ValueError:
            Erro("Preencha os campos corretamente.", QMessageBox.Warning, "Erro")

    def converter_string_para_float(self, num):
        try:
            n = num
            n = n.replace(",", ".")
            return float(n)
        except AttributeError:
            return float(n)

    def preencher_nome(self):
        nomes = self.db.querry_generica('SELECT DISTINCT funcionario FROM Caixa')
        for nome in nomes:
            self.ui.cx_nome.addItem(nome[0])

    def calcular_total_retiradas(self):
        total = 0
        if self.dados_retiradas.values() != {}:
            for dado in self.dados_retiradas.values():
                total += remover_masc_dinheiro(dado['valor'])
                total = total
        return total

    def inserir_dados(self):
        if self.dados_retiradas != {}:
            self.dados_fechamento_caixa['retiradas'] = {
                'codigo' : self.dados['codigo'],
                'total' : self.calcular_total_retiradas(),
                'retiradas' : self.dados_retiradas
                }
        else:
            self.dados_fechamento_caixa['retiradas'] = {'total' : 0}

        self.dados_fechamento_caixa['data'] = self.ui.cx_data.date().toString('yyyy-MM-dd')
        self.dados_fechamento_caixa['bomba'] = self.ui.cb_bomba.currentText()
        self.dados_fechamento_caixa['funcionario'] = self.ui.cx_nome.currentText()

        vazio = self.verifica_campos_vazios(self.dados_fechamento_caixa)

        if vazio == False:
            campos_vazios = Poup.confirma("Deseja completar o fechamento de caixa?", QMessageBox.Warning)

            if campos_vazios == True:
                self.db.inserir_caixa(self.dados_fechamento_caixa)
                self.inserir_conta()
                self.calculo_tanque(self.dados_fechamento_caixa['litros'])
                if len(self.dados_fechamento_caixa['retiradas']) > 1:
                    self.db.inserir_retiradas(self.dados_fechamento_caixa['retiradas'])

                #self.db.close_db()
                self.limpar_campos_caixa()
                self.limpar_campos_retiradas()
                while (self.ui.tb_cx.rowCount() > 0):
                    self.ui.tb_cx.removeRow(0)
                self.ui.stackedWidget_2.setCurrentIndex(0)
        
        else:
            Erro("Preencha todos os campos corretamente.", QMessageBox.Warning)

    def inserir_conta(self):
        self.db.querry_generica("UPDATE Contas SET valor = valor + {} WHERE conta = 'Caixa Posto'".format(self.dados_fechamento_caixa["dinheiro_caixa"]))
        if self.dados_fechamento_caixa["pix"] != 0 or self.dados_fechamento_caixa["cartao"] != 0:
            self.db.querry_generica("UPDATE Contas SET valor = valor + {} WHERE conta = 'Conta Inter'".format(self.dados_fechamento_caixa["pix"] + self.dados_fechamento_caixa["cartao"]))

    def limpar_campos_caixa(self):
        self.ui.ln_digi_anterior.setText("")
        self.ui.ln_digi_atual.setText("")
        self.ui.ln_ana_anterior.setText("")
        self.ui.ln_ana_atual.setText("")
        self.ui.ln_cx_litros.setText("")
        self.ui.ln_cx_valor.setText("")
        self.ui.ln_cx_din.setText("")
        self.ui.ln_cx_pix.setText("")
        self.ui.ln_cx_cartao.setText("")
        self.ui.ln_cx_resto_2.setText("")
        self.ui.ln_cx_resto.setText("")
 
    def limpar_campos_retiradas(self):
        self.ui.ln_cx_desc.setText("")
        self.ui.ln_cx_ter_valor.setText("")
        self.ui.cb_cx_nome.setCurrentIndex(0)

    def inserir_retirada(self):
        vazio = False
        indice = (len(self.dados_retiradas) + 1)

        info = self.receber_dados_retiradas()
        vazio, dados = info[0], info[1]
        vazio = self.verifica_campos_vazios(dados)

        if vazio == False:
            self.dados_retiradas[indice] = dados
            info = self.dados_retiradas[indice]
            self.preencher_tabela_retiradas(info)
            self.ui.ln_cx_retiradas.setText(str(self.calcular_total_retiradas()))
            self.definir_campo_troco()
            
            self.limpar_campos_retiradas()
        else:
            Erro("Preencha todos os campos corretamente.", QMessageBox.Warning)

    def verifica_campos_vazios(self, dados):
        for i in dados.values():
            if i == '':
                return True 
        return False

    def receber_dados_retiradas(self):
        dados = {'nome' : '', 'valor' : '', 'descricao' : '',}
        try:
            dados['valor'] = self.converter_string_para_float(self.ui.ln_cx_ter_valor.text())
            dados['nome'] = self.ui.cb_cx_nome.currentText()
            dados['descricao'] = self.ui.ln_cx_desc.text()
            return False, dados
        except ValueError:
            return True, dados

    def preencher_tabela_retiradas(self, dados):
        rowPosition = self.ui.tb_cx.rowCount()
        self.ui.tb_cx.insertRow(rowPosition)
        for i, info in enumerate(dados.values()):
            dado = QTableWidgetItem(str(info))
            self.ui.tb_cx.setItem(rowPosition, i, dado)

    def inserir_info_cb_bombas(self):
        dados = self.db.consulta_bombas()
        self.ui.cb_bomba.clear()
        #self.ui.cb_bomba.addItem("")
        for i in dados:
            self.ui.cb_bomba.addItem(str(i[0]))
    
    def inserir_nomes_cb_retiradas(self):
        dados = self.db.consulta_retirada()
        self.ui.cb_cx_nome.clear()
        self.ui.cb_cx_nome.addItem("")
        for i in dados:
            self.ui.cb_cx_nome.addItem(str(i[0]))