from Funcoes.genericas import atualizar_cb, converter_string_para_float, limpar_campos, mascara_dinheiro, preencher_tabela
from PyQt5 import QtWidgets
from Funcoes.poupup import Poup

from GUI.ui_GUI import Ui_Sistema


class Vendas(Ui_Sistema): 

    def __init__(self, ui):
        self.ui = ui

        self.produto = []
        self.qnt = 1
        self.lista_produtos = []

        self.ui.vend_tb.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.vend_tb.horizontalHeader().setStretchLastSection(False)
        self.ui.vend_tb.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.ui.btn_vendas.clicked.connect(lambda: atualizar_cb(self.ui.db, "SELECT DISTINCT produto FROM Estoque", self.ui.vend_cb_codigo))
        

        self.ui.vend_cb_codigo.currentIndexChanged.connect(lambda: self.editar_campos())
        self.ui.vend_ln_qnt.editingFinished.connect(lambda: self.ui.vend_ln_subtotal.setText(mascara_dinheiro(str(self.calculo_subtotal()))))

        self.ui.vend_btn_adicionar.clicked.connect(lambda: self.inserir_dados_venda())
        self.ui.vend_btn_cancelar.clicked.connect(lambda: self.deletar())

    def editar_campos(self):
        dado = self.ui.vend_cb_codigo.currentText()
        if dado != "":
            produto = self.ui.db.querry_generica("SELECT * FROM Estoque WHERE codigo = '{}' OR produto = '{}' OR cod_barras = '{}'".format(dado, dado, dado))
            self.produto = produto[0] 
            self.qnt = 1.00

            self.ui.vend_cb_codigo.setCurrentText(self.produto[3])
            self.ui.vend_ln_qnt.setText(str(self.qnt))
            self.ui.vend_ln_preco.setText(mascara_dinheiro(self.produto[8]))

            self.ui.vend_ln_subtotal.setText(mascara_dinheiro(str(self.calculo_subtotal())))
        
    def calculo_subtotal(self):
        self.qnt = self.ui.vend_ln_qnt.text()
        return round(converter_string_para_float(self.qnt) * converter_string_para_float(self.produto[8]), 2)
    
    def inserir_dados_venda(self):
        info = [(self.ui.vend_tb.rowCount()+1), self.produto[0],  self.produto[3], self.produto[4], converter_string_para_float(self.qnt), mascara_dinheiro(self.produto[8]), self.ui.vend_ln_subtotal.text()]
        self.lista_produtos.append(info)
        preencher_tabela([info], self.ui.vend_tb)
        self.ui.vend_ln_total.setText(self.atualizar_total())
        self.limpar_campos()

    def atualizar_total(self):
        total = 0
        for produto in self.lista_produtos:
            valor = produto[-1]
            total += converter_string_para_float(valor.replace("R$ ", ""))
        return mascara_dinheiro(round(total, 2))

    def limpar_campos(self):
        self.qnt = 1
        limpar_campos([self.ui.vend_ln_qnt, self.ui.vend_ln_preco, self.ui.vend_ln_subtotal])
        self.ui.vend_cb_codigo.setCurrentIndex(0)
    
    def deletar(self):
        if Poup.confirma("Deseja deletar?", QtWidgets.QMessageBox.Information) == True:
            row = self.ui.vend_tb.currentRow()
            self.ui.vend_tb.removeRow(row)
            self.lista_produtos.pop(row)
            self.ui.vend_ln_total.setText(self.atualizar_total())

    def produto(self, produto):
        produto = self.ui.db.select_generico(f"SELECT codigo, produto, unidade, cod_barras, preço_venda, quantidade FROM Estoque WHERE produto = '{produto}' OR codigo = '{produto}' OR cod_barras = '{produto}'")
        produto = {
            'codigo': produto[0][0],
            'descrição': produto[0][1],
            'unidade': produto[0][2],
            'cod_barras': produto[0][3],
            'preço_venda': converter_string_para_float(produto[0][4]),
            'estoque' : produto[0][5],
        }
        return produto

    def subtotal(self, produto, quantidade):
        return produto['preço_venda'] * quantidade 