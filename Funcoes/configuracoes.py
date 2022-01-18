from PyQt5.QtWidgets import QMessageBox
from GUI.ui_GUI import Ui_Sistema
from Funcoes.genericas import atualizar_cb, caminho_db, converter_string_para_float, limpar_campos, mascara_dinheiro
from DataBase.DataBase import DataBase
from Funcoes.poupup import Erro


class Configuracoes(Ui_Sistema):

    def __init__(self, ui):        
        #inicia as variaveis basicas
        self.ui = ui
        
        #Principal
        self.ui.config_comb_btn.clicked.connect(lambda: Aba_Combustivel(self.ui))
        self.ui.config_user_btn.clicked.connect(lambda: Aba_Usuario(self.ui))

    def aba_home(self):
        self.ui.stackedWidget_12.setCurrentIndex(0)
        self.ui.stackedWidget_10.setCurrentIndex(2)


class Aba_Combustivel(Configuracoes):

    def __init__(self, ui):
        super().__init__(ui)
        self.ui.stackedWidget_10.setCurrentIndex(1)
        self.ui.stackedWidget_11.setCurrentIndex(2)
        self.ui.stackedWidget_12.setCurrentIndex(1)

        #Navegação
        self.ui.config_comb_voltar.clicked.connect(lambda: self.aba_home())
        self.ui.config_comb_editar.clicked.connect(lambda: self.aba_editar())
        self.ui.config_comb_info_2.clicked.connect(lambda: self.aba_informacoes())

        self.ui.config_comb_edit_combustivel.currentIndexChanged.connect(lambda: self.consultar_valor(self.ui.config_comb_edit_combustivel, self.ui.config_comb_edit_antigo))
        self.ui.config_comb_edit_combustivel_2.currentIndexChanged.connect(lambda: self.consultar_valor(self.ui.config_comb_edit_combustivel_2, self.ui.config_comb_edit_novo_2))
        self.ui.config_comb_edit_combustivel_3.currentIndexChanged.connect(lambda: self.consultar_tanque(self.ui.config_comb_edit_combustivel_3, self.ui.config_comb_edit_novo_3))


        self.ui.config_comb_edit_btn.clicked.connect(lambda: self.atualizar_valor_combustivel())
    
    def aba_informacoes(self):
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_edit_combustivel_2)
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_edit_combustivel_3)
        self.ui.stackedWidget_11.setCurrentIndex(0)

    def aba_editar(self):
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_edit_combustivel)
        self.ui.stackedWidget_11.setCurrentIndex(1)
        self.limpar_edicao()
    
    def consultar_valor(self, cb, ln):
        combustivel = cb.currentText()
        if combustivel == "":
            ln.setText("")
            return
        else: 
            valor = DataBase(caminho_db()).valor_combustivel(combustivel)
            ln.setText(str(valor)) 

    def atualizar_valor_combustivel(self):
        combustivel = self.ui.config_comb_edit_combustivel.currentText()
        try:
            novo = converter_string_para_float(self.ui.config_comb_edit_novo.text())
            if novo != "" and combustivel != "":
                DataBase(caminho_db()).querry_generica("UPDATE Valor_combustivel SET valor = {} WHERE combustivel = '{}'".format(novo, combustivel))
                Erro("Preço do combustível editado com sucesso.", QMessageBox.Information)
                self.limpar_edicao()
                self.ui.stackedWidget_11.setCurrentIndex(2)
            else:
                Erro("Preencha todos os campos.", QMessageBox.Warning, "Aviso!")
        except ValueError:
            Erro("Preencha todos os campos.", QMessageBox.Warning, "Aviso!")

    def limpar_edicao(self):
        limpar_campos([self.ui.config_comb_edit_novo])
        self.ui.config_comb_edit_combustivel.setCurrentIndex(0)

    def consultar_tanque(self, cb, ln):
        combustivel = cb.currentText()
        if combustivel == "":
            ln.setText("")
            return
        else: 
            valor = DataBase(caminho_db()).select_generico("SELECT quantidade FROM Valor_combustivel WHERE combustivel = '{}'".format(combustivel))
            ln.setText(str(valor[0][0])) 

class Aba_Usuario(Configuracoes):

    def __init__(self, ui):
        super().__init__(ui)
        self.ui.stackedWidget_10.setCurrentIndex(0)
        self.ui.stackedWidget_12.setCurrentIndex(2)
        self.ui.stackedWidget_13.setCurrentIndex(0)


        #Navegação
        self.ui.config_user_voltar.clicked.connect(lambda: self.aba_home())
        self.ui.config_user_lista_2.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentIndex(2))
        self.ui.config_user_novo_btn.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentIndex(1))