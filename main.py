from PyQt5 import *
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow
from DataBase.DataBase import DataBase
from Funcoes.financeiro import Financeiro, Home
from GUI.ui_GUI import Ui_Sistema
import sys

from Funcoes.login import Login
from Funcoes.caixa import Caixa
from Funcoes.consulta import Consulta
from Funcoes.vendas import Vendas
from Funcoes.registro_ponto import RegistroPonto
from Funcoes.permissoes import Permissoes
from Funcoes.estoque import Estoque
from Funcoes.genericas import caminho_db
from Funcoes.configuracoes import Configuracoes

try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class Window(QMainWindow, Ui_Sistema):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.stackedWidget.setCurrentIndex(1)

        self.btn_entrar.clicked.connect(lambda: self.acessar_sistema())
        self.btn_entrar.setAutoDefault(True)
        self.db = DataBase(caminho_db())

        #Navegação Principal
        self.btn_inicio.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.btn_consulta.clicked.connect(lambda: self.window_consulta())
        self.btn_caixa.clicked.connect(lambda: self.acesso_caixa())
        self.btn_estoque.clicked.connect(lambda: self.acesso_estoque())
        self.btn_vendas.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(5))
        self.btn_config.clicked.connect(lambda: self.acesso_config())
        self.btn_financeiro.clicked.connect(lambda: self.acesso_financeiro())
        self.btn_lancamentos.clicked.connect(lambda: self.acesso_lancamentos())

        self.btn_logout.clicked.connect(lambda: self.logout())

        self.ini_btn_ponto.clicked.connect(lambda: self.registrar_ponto())

    def acesso_lancamentos(self):
        self.stackedWidget_2.setCurrentIndex(6)
        Financeiro(self).tela_novo()
        self.fin_btn_home.setEnabled(False)
        self.fin_btn_mov.setEnabled(False)
        self.fin_btn_novo.setEnabled(False)

    def nivel_tanque(self):
        nivel = self.db.select_generico(f"SELECT quantidade FROM Valor_combustivel WHERE codigo = 1")
        if int(nivel[0][0]) < 3000:
            self.lb_ini_data_6.setText("Nivel do tanque abaixo do aceitavel.")
            self.lb_ini_data_6.setStyleSheet("""background-color: rgb(255, 0, 0);
                                                border-radius: 20px;
                                                margin-left: 100px;
                                                color: rgb(255, 255, 255);""")
            self.lb_ini_data_6.setMaximumWidth(400)
        else:
            self.lb_ini_data_6.setMaximumWidth(0)

    def acessar_sistema(self):
        #Faz validação dos dados de login no sistema
        self.login = Login(self.in_usuario.text(), self.in_senha.text())
        dados = self.login.validar_dados()
        if dados[0] == True:
            self.dados = dados[1]
            self.nivel_tanque()
            self.controle_acesso()
            self.atualizar_pagina_login()

        else:
            self.lb_info.setText("Usuário ou senha Incorretos!")
    
    def acesso_estoque(self):
        self.stackedWidget_2.setCurrentIndex(4)
        self.stackedWidget_7.setCurrentIndex(0)
    
    def acesso_financeiro(self):
        Home(self).atualizar_tela()
        self.stackedWidget_2.setCurrentIndex(6)
        self.stackedWidget_6.setCurrentIndex(0)

    def atualizar_pagina_login(self):
        self.Horario()
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.lb_info.setText("")
        self.lb_ini_funcionario.setText(self.dados['nome'])

        self.caixa = Caixa(self, self.dados)
        self.consulta = Consulta(self)
        self.estoque = Estoque(self)
        self.vendas = Vendas(self)
        self.config = Configuracoes(self)
        self.financeiro = Financeiro(self)

    def window_consulta(self):
        self.stackedWidget_2.setCurrentIndex(1)
        self.nav_consultas.setCurrentIndex(0)
        self.cons_lb_nav.setText("")

    def Horario(self):
        #Define data e hora do sistema
        self.hora = QTimer(self)
        self.hora.setInterval(1000)
        self.hora.timeout.connect(lambda: self.lb_ini_data.setText(QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm:ss ")))
        self.hora.start()

    def acesso_caixa(self):
        #Acessa a aba caixa
        self.stackedWidget_2.setCurrentIndex(2)
        self.caixa.atualizar_tela()

    def registrar_ponto(self):
        self.ponto = RegistroPonto(self)
        self.ponto.show()
    
    def controle_acesso(self):
        Permissoes(self, self.dados['tipo'])
    
    def logout(self):
        self.stackedWidget.setCurrentIndex(1)
        self.in_usuario.setText("")
        self.in_senha.setText("")

    def acesso_config(self):
        self.stackedWidget_2.setCurrentIndex(3)
        self.stackedWidget_12.setCurrentIndex(0)
        self.stackedWidget_11.setCurrentIndex(2)

root = QApplication(sys.argv)
app = Window()
app.showMaximized()
app.setWindowIcon(QtGui.QIcon('logo.ico'))

sys.exit(root.exec_())
