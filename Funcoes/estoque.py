from datetime import date
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui, QtWidgets
from GUI.ui_GUI import Ui_Sistema
from Funcoes.poupup import Erro
from Funcoes.genericas import inserir_dados_cb, limpar_campos, limpar_tabela, mascara_dinheiro, preencher_tabela, preencher_ln, preencher_cb, receber_dados_campos, converter_string_para_float


class Estoque(Ui_Sistema):

    def __init__(self, ui):
        self.ui = ui
        self.dados_tab = []
        self.id_edicao = 0

        self.ui.est_consult_tab.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.est_consult_tab.horizontalHeader().setStretchLastSection(False)
        self.ui.est_consult_tab.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        #Navegação
        self.ui.est_btn_novo.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentIndex(1))
        self.ui.est_btn_entrada.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentIndex(2))
        self.ui.est_btn_consulta.clicked.connect(lambda: self.nav_consulta())

        #Cadastro
        self.ui.btn_est_cadastrar.clicked.connect(lambda: self.cadastrar_novo_produto())

        #Entrada
        self.ui.est_new_btn_cadastrar.clicked.connect(lambda: self.adicionar_entrada())

        #Consulta
        self.ui.est_const_btn_pesquisar.clicked.connect(lambda: self.consultar_dados())
        self.ui.est_const_btn_editar.clicked.connect(lambda: self.inserir_dados())

        #Editar
        self.ui.est_edt_btn_salvar.clicked.connect(lambda: self.salvar_edicao())
        self.ui.est_edt_btn_cancelar.clicked.connect(lambda: self.limpar_edicao())

        #Limpeza
        self.ui.est_btn_novo.clicked.connect(lambda: self.limpar_cadastro())
        self.ui.est_btn_entrada.clicked.connect(lambda: self.limpar_entrada())

    #Cadastro Produto
    def receber_dados_novo_produto(self):
        dados = {
            'tipo' : self.ui.est_cb_tipo.currentText(),
            'marca' : self.ui.est_cb_marca.currentText(),
            'produto' : self.ui.ln_est_produto.text().upper(),
            'unidade' : self.ui.est_cb_unidade.currentText(),
            'p_compra' : converter_string_para_float(self.ui.ln_est_pCompra.text()),
            'p_venda' : converter_string_para_float(self.ui.ln_est_pVenda.text()),
            'quantidade' : converter_string_para_float(self.ui.ln_est_qnt.text()),
            'cod_barras' : self.ui.ln_est_codBarras.text(),
        }

        return dados

    def cadastrar_novo_produto(self):       
            dados = self.receber_dados_novo_produto()
            self.ui.db.querry_generica(f"INSERT INTO Estoque (tipo, marca, produto, unidade, quantidade, cod_barras, preço_compra, preço_venda) VALUES ('{dados['tipo']}', '{dados['marca']}', '{dados['produto']}', '{dados['unidade']}', '{dados['quantidade']}', '{dados['cod_barras']}', '{dados['p_compra']}', '{dados['p_venda']}')")
            Erro("Produto adicionado com sucesso!", QMessageBox.Information, titulo="Sucesso!")
            self.ui.stackedWidget_7.setCurrentIndex(0)
            self.limpar_cadastro()
    
    def limpar_cadastro(self):
        limpar_campos([
            self.ui.ln_est_produto, self.ui.ln_est_qnt, self.ui.ln_est_codBarras, self.ui.ln_est_pCompra, self.ui.ln_est_pVenda])
        self.atualizar_cb("SELECT DISTINCT tipo FROM Estoque", self.ui.est_cb_tipo)
        self.atualizar_cb("SELECT DISTINCT marca FROM Estoque", self.ui.est_cb_marca)
    
    #Entrada Produto
    def receber_dados_entrada(self):
        dados = {
            'quantidade' : converter_string_para_float(self.ui.est_new_ln_qnt.text()),
            'produto' : self.ui.est_new_cb_produto.currentText(),
            'data' : date.today().isoformat()
        }
        return dados

    def adicionar_entrada(self):
        dados = self.receber_dados_entrada()
        self.ui.db.querry_generica(f"UPDATE Estoque SET quantidade = quantidade + '{dados['quantidade']}' WHERE produto = '{dados['produto']}'")
        self.ui.db.querry_generica(f"INSERT INTO entrada_produtos (data, produto, quantidade) VALUES ('{dados['data']}', '{dados['produto']}', '{dados['quantidade']}')")
        Erro("Entrada de produto adicionada com sucesso!", QMessageBox.Information, titulo="Sucesso!")
        self.limpar_entrada()

    def limpar_entrada(self):
        limpar_campos([self.ui.est_new_ln_qnt])
        self.atualizar_cb("SELECT DISTINCT produto FROM Estoque", self.ui.est_new_cb_produto)
    
    #Consulta Produto
    def nav_consulta(self):
        limpar_tabela(self.ui.est_consult_tab)
        self.ui.stackedWidget_7.setCurrentIndex(3)
    
    def receber_dados_consulta(self):
        dados = [self.ui.est_const_cb_filtro.currentText(), self.ui.est_const_ln_filtro.text()]
        return dados

    def criar_querry_consulta(self, dados):
        querry = "SELECT * FROM Estoque WHERE "
        if dados[0] == "Produto":
            return querry + "produto LIKE '%{}%'".format(dados[1]) 
        elif dados[0] == "Tipo":
            return querry + "tipo LIKE '%{}%'".format(dados[1]) 
        elif dados[0] == "Cod.":
            return querry + "codigo LIKE '%{}%'".format(dados[1]) 
        elif dados[0] == "Marca":
            return querry + "marca LIKE '%{}%'".format(dados[1]) 
        elif dados[0] == "Cod. Barras":
            return querry + "cod_barras LIKE '%{}%'".format(dados[1])
        
    def consultar_dados(self):
        dados = self.receber_dados_consulta()
        self.dados_tab = self.ui.db.querry_generica(self.criar_querry_consulta(dados))
        limpar_tabela(self.ui.est_consult_tab)
        self.limpar_consulta()
        preencher_tabela(self.inserir_mascara_dinheiro(self.dados_tab), self.ui.est_consult_tab)

    def limpar_consulta(self):
        self.ui.est_consult_tab.horizontalHeader().setVisible(True)
        limpar_campos([self.ui.est_const_ln_filtro])

    def inserir_mascara_dinheiro(self, dados):
        lista = []
        for dado in dados:
            dado = list(dado)
            dado[-1] = mascara_dinheiro(dado[-1])
            dado[-2] = mascara_dinheiro(dado[-2])
            lista.append(dado)
        return lista
    
    #Editar Produto
    def inserir_dados(self):
        dados = self.selecionar_dados_tabela()
        self.id_edicao = dados[0]
        cb = [self.ui.est_edt_cb_tipo, self.ui.est_edt_cb_marca, self.ui.est_edt_cb_unidade]
        ln = [self.ui.est_edt_ln_produto, self.ui.est_edt_ln_qnt, self.ui.est_edt_ln_codBarras, self.ui.est_edt_ln_pCompra, 
            self.ui.est_edt_ln_pVenda]

        self.atualizar_cb("SELECT DISTINCT tipo FROM Estoque", self.ui.est_edt_cb_tipo)
        self.atualizar_cb("SELECT DISTINCT marca FROM Estoque", self.ui.est_edt_cb_marca)

        dados_cb = dados[1:5]
        dados_cb = list(dados_cb)
        dados_cb.pop(2)

        dados_ln = dados[3:]
        dados_ln = list(dados_ln)
        dados_ln.pop(1)
        
        
        preencher_ln(ln, dados_ln)
        preencher_cb(cb, dados_cb)

        self.ui.stackedWidget_7.setCurrentIndex(4)
        
    def selecionar_dados_tabela(self):
        row = self.ui.est_consult_tab.currentRow()
        return self.dados_tab[int(row)]

    def salvar_edicao(self):
        dados = {
            'id' : self.id_edicao,
            'tipo' : self.ui.est_cb_tipo.currentText(),
            'marca' : self.ui.est_cb_marca.currentText(),
            'produto' : self.ui.ln_est_produto.text().upper(),
            'unidade' : self.ui.est_cb_unidade.currentText(),
            'p_compra' : converter_string_para_float(self.ui.ln_est_pCompra.text()),
            'p_venda' : converter_string_para_float(self.ui.ln_est_pVenda.text()),
            'quantidade' : converter_string_para_float(self.ui.ln_est_qnt.text()),
            'cod_barras' : self.ui.ln_est_codBarras.text(),
        }

        self.ui.db.querry_generica(f"UPDATE Estoque SET tipo = '{dados['tipo']}', marca = '{dados['marca']}', produto = '{dados['produto']}', unidade = '{dados['unidade']}', preço_compra = '{dados['p_compra']}', preço_venda = '{dados['p_venda']}', quantidade = '{dados['quantidade']}', cod_barras = '{dados['cod_barras']}' WHERE codigo = '{dados['id']}'")
        dados = receber_dados_campos([self.ui.est_edt_cb_tipo.currentText(), self.ui.est_edt_cb_marca.currentText(), 
            self.ui.est_edt_ln_produto.text(), self.ui.est_edt_ln_pCompra.text(), self.ui.est_edt_ln_pVenda.text(), self.ui.est_edt_ln_qnt.text(), 
            self.ui.est_edt_ln_codBarras.text()])
        self.ui.db.atualizar_produto(dados, self.id_edicao)
        Erro("Dados editados com sucesso!", QMessageBox.Information, titulo="Sucesso")
        self.ui.stackedWidget_7.setCurrentIndex(0)

    def limpar_edicao(self):
        self.ui.est_edt_cb_tipo.setCurrentText("")
        self.ui.est_edt_cb_marca.setCurrentText("")
        limpar_campos([self.ui.est_edt_ln_produto, self.ui.est_edt_ln_pCompra, self.ui.est_edt_ln_pVenda, self.ui.est_edt_ln_qnt, 
            self.ui.est_edt_ln_codBarras])
        self.ui.stackedWidget_7.setCurrentIndex(0)

    #Genericos
    def atualizar_cb(self, querry, widget):
        dados = self.ui.db.querry_generica(querry)
        inserir_dados_cb(widget, dados)

