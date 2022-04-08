from PyQt5.QtWidgets import QMessageBox
from GUI.ui_GUI import Ui_Sistema
from PyQt5.QtCore import QDateTime
from DataBase.DataBase import DataBase
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt

from Funcoes.genericas import caminho_db, converter_string_para_float, inserir_dados_cb, limpar_tabela, remover_masc_dinheiro, mascara_dinheiro
from Funcoes.vendas import Vendas

from Funcoes.poupup import Poup, Erro


class Caixa(Ui_Sistema):

    def __init__(self, ui, dados):        
        #inicia as variaveis basicas
        self.db = DataBase(caminho_db())
        self.gasolina = self.db.valor_combustivel("Gasolina Comum")
        self.dados_usuario = dados
        self.ui = ui
        self.caixa_venda = CaixaVenda(self)
        self.lista_produtos = {}
        self.total = 0

        #Insere informações na tela
        self.ui.cb_bomba.currentIndexChanged.connect(lambda: self.redefinir_campo_leitura_anterior())
        self.atualizar_tela()
        self.preencher_nome()

        #Ação dos botões
        self.ui.btn_cx_inserir.clicked.connect(lambda: self.calculo_caixa())
        self.ui.btn_cx_inserir.setAutoDefault(True)
        self.ui.btn_cx_fechar.clicked.connect(lambda: self.inserir_dados())
        self.ui.btn_cx_fechar.setAutoDefault(True)

        self.ui.ln_cx_din.editingFinished.connect(lambda: self.definir_campo_troco())
        self.ui.ln_cx_pix.editingFinished.connect(lambda: self.definir_campo_troco())
        self.ui.ln_cx_cartao.editingFinished.connect(lambda: self.definir_campo_troco())

        #VENDAS
        self.ui.cb_cx_ven_cod.currentIndexChanged.connect(lambda: self.nova_venda())
        self.ui.cb_cx_ven_qnt.editingFinished.connect(lambda: self.caixa_venda.atualizar_subtotal())
        self.ui.cb_cx_ven_adc.clicked.connect(lambda: self.adicionar_venda())
        self.ui.cb_cx_ven_inserir.clicked.connect(lambda: self.deletar_venda())

        self.ui.ln_cx_vendas_din.editingFinished.connect(lambda: self.calculo_vendas())
        self.ui.ln_cx_vendas_cart.editingFinished.connect(lambda: self.calculo_vendas())

    def atualizar_tela(self):
        self.limpar_dados()
        self.inserir_informacoes_tela()
        self.inserir_info_cb_bombas()

    def nova_venda(self):
        self.caixa_venda.preencher_campos()

    def adicionar_venda(self):
        if self.ui.cb_cx_ven_cod.currentIndex() != 0:
            if self.venda_produto['quantidade'] <= self.venda_produto['produto']['estoque']:
                self.lista_produtos[len(self.lista_produtos)] = self.venda_produto
                self.caixa_venda.tabela_vendas(self.lista_produtos)
                self.caixa_venda.limpar()
            else:
                Erro('Quantidade indisponivel no estoque.', QMessageBox.Warning)
        else:
            Erro('Nenhum produto selecionado.', QMessageBox.Warning)
    def deletar_venda(self):
        produto = self.ui.cb_cx_ven_tab.selectedItems()
        for j, i in self.lista_produtos.items():
            if i != {}:
                if i['produto']['descrição'] == produto[0].text() and str(i['quantidade']) == produto[2].text():
                    self.lista_produtos[j] = {}
                    self.caixa_venda.tabela_vendas(self.lista_produtos)
                    return

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
            'valor' : 0,
            'dinheiro_caixa' : 0,
            'pix' : 0,
            'cartao' : 0,
            'total' : 0,
            'resto' : 0,
            'vendas' : None,
        }

        self.dados_vendas = {

        }
        self.fechamento_vendas = {
            'dinheiro' : 0,
            'cartao' : 0,
        }
        self.venda_produto = {}
        self.total = 0
        self.lista_produtos = {}

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
                self.dados_fechamento_caixa['total'] = self.dados_fechamento_caixa['dinheiro_caixa'] + self.dados_fechamento_caixa['pix'] + self.dados_fechamento_caixa['cartao']
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
            if num == "":
                return 0
            n = num
            n = n.replace(",", ".")
            return float(n)
        except AttributeError:
            return float(n)

    def preencher_nome(self):
        nomes = self.db.querry_generica('SELECT DISTINCT funcionario FROM Caixa')
        for nome in nomes:
            self.ui.cx_nome.addItem(nome[0])

    def inserir_dados(self):
        self.dados_fechamento_caixa['data'] = self.ui.cx_data.date().toString('yyyy-MM-dd')
        self.dados_fechamento_caixa['bomba'] = self.ui.cb_bomba.currentText()
        self.dados_fechamento_caixa['funcionario'] = self.ui.cx_nome.currentText()

        vazio = self.verifica_campos_vazios(self.dados_fechamento_caixa)
        vazio2 = False
        if self.lista_produtos != {}:
            vazio2 = self.verifica_campos_vazios_venda(self.fechamento_vendas)

        if vazio == False and vazio2 == False:
            campos_vazios = Poup.confirma("Deseja completar o fechamento de caixa?", QMessageBox.Warning)

            if campos_vazios == True:
                if self.lista_produtos != {}:
                    self.dados_fechamento_caixa['vendas'] = self.inserir_vendas()
                self.db.inserir_caixa(self.dados_fechamento_caixa)
                self.inserir_conta()
                self.calculo_tanque(self.dados_fechamento_caixa['litros'])
                #self.db.close_db()
                self.limpar_campos_caixa()
                self.caixa_venda.limpar_tudo()
                self.ui.stackedWidget_2.setCurrentIndex(0)
        
        else:
            Erro("Preencha todos os campos corretamente.", QMessageBox.Warning)

    def verifica_campos_vazios_venda(self, dados):
        for i in dados.values():
            if i != 0:
                return False 
        return True

    def calculo_vendas(self):
        try:
            self.fechamento_vendas['dinheiro'] = self.converter_string_para_float(self.ui.ln_cx_vendas_din.text())
            self.fechamento_vendas['cartao'] = self.converter_string_para_float(self.ui.ln_cx_vendas_cart.text())

            self.fechamento_vendas['total'] = self.fechamento_vendas['dinheiro'] + self.fechamento_vendas['cartao'] - self.total
            self.ui.ln_cx_vendas_total.setText(mascara_dinheiro(self.fechamento_vendas['total']))
        except:
            Erro("Preencha os campos corretamente.", QMessageBox.Warning)

    def inserir_vendas(self):
        self.db.querry_generica(f"INSERT INTO vendas (data, valor, dinheiro, cartao) VALUES ('{self.dados_fechamento_caixa['data']}', '{self.total}', '{self.fechamento_vendas['dinheiro']}', '{self.fechamento_vendas['cartao']}')")
        venda = self.db.select_generico(f"SELECT MAX(id) FROM vendas")
        for produto in self.lista_produtos.values():
            if produto != {}:
                self.db.querry_generica(f"INSERT INTO venda_produtos (venda, produto, quantidade, valor) VALUES ('{venda[0][0]}', '{produto['produto']['descrição']}', '{produto['quantidade']}', '{produto['produto']['preço_venda']}')")
                self.db.querry_generica(f"UPDATE Estoque SET quantidade = quantidade - {produto['quantidade']} WHERE produto = '{produto['produto']['descrição']}'")
        return venda[0][0]

    def inserir_conta(self):
        self.db.querry_generica("UPDATE Contas SET valor = valor + {} WHERE conta = 'Caixa Posto'".format(self.dados_fechamento_caixa["dinheiro_caixa"] + self.fechamento_vendas['dinheiro']))
        if self.dados_fechamento_caixa["pix"] != 0 or self.dados_fechamento_caixa["cartao"] != 0 or self.fechamento_vendas["cartao"] != 0:
            self.db.querry_generica("UPDATE Contas SET valor = valor + {} WHERE conta = 'Conta Inter'".format(self.dados_fechamento_caixa["pix"] + self.dados_fechamento_caixa["cartao"] + self.fechamento_vendas["cartao"]))

    def limpar_campos_caixa(self):
        self.ui.ln_digi_anterior.setText("")
        self.ui.ln_digi_atual.setText("")
        self.ui.ln_ana_anterior.setText("")
        self.ui.ln_ana_atual.setText("")
        self.ui.ln_cx_litros.setText("")
        self.ui.ln_cx_valor.setText("")
        self.ui.ln_cx_din.setText("")
        self.ui.ln_cx_pix.setText("")
        self.ui.ln_cx_vendas.setText('')
        self.ui.ln_cx_cartao.setText("")
        self.ui.ln_cx_resto_2.setText("")
        self.ui.ln_cx_resto.setText("")

        self.ui.ln_cx_vendas.setText("")
        self.ui.ln_cx_vendas_din.setText("")
        self.ui.ln_cx_vendas_cart.setText("")
        self.ui.ln_cx_vendas_total.setText("")

    def verifica_campos_vazios(self, dados):
        for i in dados.values():
            if i == '':
                return True 
        return False

    def inserir_info_cb_bombas(self):
        dados = self.db.consulta_bombas()
        self.ui.cb_bomba.clear()
        #self.ui.cb_bomba.addItem("")
        for i in dados:
            self.ui.cb_bomba.addItem(str(i[0]))

    
class CaixaVenda(Vendas):

    def __init__(self, obj):
        self.obj = obj
        self.ui = obj.ui

        self.preencher_produtos()

    def preencher_produtos(self):
        produtos = self.obj.db.select_generico("SELECT produto FROM Estoque")
        inserir_dados_cb(self.ui.cb_cx_ven_cod, produtos)

    def atualizar_subtotal(self):
        self.preencher_campos(float(self.ui.cb_cx_ven_qnt.text()))

    def preencher_campos(self, qnt=1):
        self.obj.venda_produto = self.consultar_produto(qnt)
        self.ui.cb_cx_ven_qnt.setText(str(self.obj.venda_produto['quantidade']))
        self.ui.cb_cx_ven_preco.setText(mascara_dinheiro(self.obj.venda_produto['produto']['preço_venda']))
        self.ui.cb_cx_ven_subtotal.setText(mascara_dinheiro(self.obj.venda_produto['subtotal']))

    def consultar_produto(self, qnt):
        dados = {
            'produto': self.ui.cb_cx_ven_cod.currentText(),
            'quantidade': converter_string_para_float(qnt),
            'subtotal': 0
        }
        dados['produto'] = self.produto(dados['produto'])
        dados['subtotal'] = self.subtotal(dados['produto'], dados['quantidade'])
        return dados

    def tabela_vendas(self, dados):
        limpar_tabela(self.ui.cb_cx_ven_tab)
        header = self.ui.cb_cx_ven_tab.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        for value in dados.values():
            if value != {}:
                rowPosition = self.ui.cb_cx_ven_tab.rowCount()
                self.ui.cb_cx_ven_tab.insertRow(rowPosition)

                self.ui.cb_cx_ven_tab.setItem(rowPosition, 0, QTableWidgetItem(str(value['produto']['descrição'])))
                self.ui.cb_cx_ven_tab.setItem(rowPosition, 1, QTableWidgetItem(str(value['produto']['unidade'])))
                self.ui.cb_cx_ven_tab.setItem(rowPosition, 2, QTableWidgetItem(str(value['quantidade'])))
                self.ui.cb_cx_ven_tab.setItem(rowPosition, 3, QTableWidgetItem(mascara_dinheiro(value['produto']['preço_venda'])))
                self.ui.cb_cx_ven_tab.setItem(rowPosition, 4, QTableWidgetItem(mascara_dinheiro(value['subtotal'])))

            self.ui.cb_cx_ven_total.setText(mascara_dinheiro(self.total(self.obj.lista_produtos)))
            self.ui.ln_cx_vendas.setText(mascara_dinheiro(self.obj.total))

    def total(self, dados):
        self.obj.total = 0
        for value in dados.values():
            if value != {}:
                self.obj.total+= float(value['subtotal'])
        return self.obj.total

    def limpar(self):
        self.ui.cb_cx_ven_cod.setCurrentIndex(0)
        self.ui.cb_cx_ven_qnt.setText("")
        self.ui.cb_cx_ven_preco.setText("")
        self.ui.cb_cx_ven_subtotal.setText("")

    def limpar_tudo(self):
        self.limpar()
        limpar_tabela(self.ui.cb_cx_ven_tab)
        self.ui.cb_cx_ven_total.setText('')