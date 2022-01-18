from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import  QDateTime
from DataBase.DataBase import DataBase
from Funcoes.genericas import caminho_db
from Funcoes.poupup import Erro, Poup
from GUI.ponto import Ui_MainWindow


class RegistroPonto(Ui_MainWindow, QDialog):

    def __init__(self, main, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)
        self.main = main
        self.data = QDateTime.currentDateTime().toString("yyyy-MM-dd")
        self.funcionario = self.main.dados["nome"]
        self.entrada = ""
        self.saida = ""
        self.entrada_2 = ""
        self.saida_2 = ""

        self.atualizar_dados()
        self.ponto_btn.clicked.connect(lambda: self.bater_ponto())

    def bater_ponto(self):
        if self.entrada == "" or self.saida == "" or self.entrada_2 == "" or self.saida_2 == "":
            confirmacao = Poup.confirma("Confirma o registro de ponto?", QMessageBox.Information)
            if confirmacao == True:
                if self.entrada == "":
                    self.entrada = QDateTime.currentDateTime().toString("hh:mm:ss")
                elif self.saida == "":
                    self.saida = QDateTime.currentDateTime().toString("hh:mm:ss")
                elif self.entrada_2 == "":
                    self.entrada_2 = QDateTime.currentDateTime().toString("hh:mm:ss")
                elif self.saida_2 == "":
                    self.saida_2 = QDateTime.currentDateTime().toString("hh:mm:ss")
                self.salvar_dados()
                self.atualizar_dados()

                
        else:
            Erro("Registro de Ponto ja está completo.", QMessageBox.Warning, "Informação!")
    
    def salvar_dados(self):
        consulta = self.carregar_ponto()
        if consulta != []:
            self.main.db.querry_generica("UPDATE Registro_ponto SET entrada_1 = '{}', saida_1 = '{}', entrada_2 = '{}', saida_2 = '{}' WHERE data = '{}' AND funcionario = '{}'".format(self.entrada, self.saida, self.entrada_2, self.saida_2, self.data, self.funcionario))
        else:
            dados = [QDateTime.currentDateTime().toString("yyyy-MM-dd"), self.funcionario, self.entrada, self.saida, self.entrada_2, self.saida_2]
            self.main.db.inserir_ponto(dados)

    def carregar_dados(self):
        dados = self.carregar_ponto()
        if dados != []:
            dados = dados[0]
            self.entrada = dados[3]
            self.saida = dados[4]
            self.entrada_2 = dados[5]
            self.saida_2 = dados[6]

    def atualizar_dados(self):
        self.carregar_dados()
        self.ponto_ln_entrada.setText(self.entrada)
        self.ponto_ln_saida.setText(self.saida)
        self.ponto_ln_entrada_2.setText(self.entrada_2)
        self.ponto_ln_saida_2.setText(self.saida_2)
        return True

    def carregar_ponto(self):
        dado = DataBase(caminho_db()).select_generico("SELECT * FROM Registro_ponto WHERE data = '{}' AND funcionario = '{}'".format(self.data, self.funcionario))
        return dado
