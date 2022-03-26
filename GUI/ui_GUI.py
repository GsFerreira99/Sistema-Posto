# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfaceeEyhSR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import GUI.resource_rc

class Ui_Sistema(object):
    def setupUi(self, Sistema):
        if not Sistema.objectName():
            Sistema.setObjectName(u"Sistema")
        Sistema.setEnabled(True)
        Sistema.resize(1550, 840)
        font = QFont()
        Sistema.setFont(font)
        Sistema.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(173, 173, 173, 255), stop:1 rgba(231, 231, 231, 255));\n"
"")
        Sistema.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Sistema.setAnimated(True)
        self.centralwidget = QWidget(Sistema)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_27 = QGridLayout(self.centralwidget)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Conteudo = QWidget()
        self.Conteudo.setObjectName(u"Conteudo")
        self.gridLayout_6 = QGridLayout(self.Conteudo)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Conteudo)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 222, 90, 239), stop:1 rgba(255, 228, 117, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_estoque = QPushButton(self.frame)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_estoque.sizePolicy().hasHeightForWidth())
        self.btn_estoque.setSizePolicy(sizePolicy)
        self.btn_estoque.setMaximumSize(QSize(100, 60))
        font1 = QFont()
        font1.setPointSize(14)
        self.btn_estoque.setFont(font1)
        self.btn_estoque.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_estoque, 4, 0, 1, 1)

        self.btn_vendas = QPushButton(self.frame)
        self.btn_vendas.setObjectName(u"btn_vendas")
        self.btn_vendas.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_vendas.sizePolicy().hasHeightForWidth())
        self.btn_vendas.setSizePolicy(sizePolicy)
        self.btn_vendas.setMaximumSize(QSize(100, 60))
        self.btn_vendas.setFont(font1)
        self.btn_vendas.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_vendas, 5, 0, 1, 1)

        self.btn_config = QPushButton(self.frame)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMaximumSize(QSize(100, 60))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_config.setFont(font2)
        self.btn_config.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-top: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	image: url(:/icons/img03.png);\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_config, 8, 0, 1, 1)

        self.btn_inicio = QPushButton(self.frame)
        self.btn_inicio.setObjectName(u"btn_inicio")
        sizePolicy.setHeightForWidth(self.btn_inicio.sizePolicy().hasHeightForWidth())
        self.btn_inicio.setSizePolicy(sizePolicy)
        self.btn_inicio.setMaximumSize(QSize(100, 60))
        self.btn_inicio.setFont(font1)
        self.btn_inicio.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_inicio, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.btn_caixa = QPushButton(self.frame)
        self.btn_caixa.setObjectName(u"btn_caixa")
        sizePolicy.setHeightForWidth(self.btn_caixa.sizePolicy().hasHeightForWidth())
        self.btn_caixa.setSizePolicy(sizePolicy)
        self.btn_caixa.setMaximumSize(QSize(100, 60))
        self.btn_caixa.setFont(font1)
        self.btn_caixa.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_caixa, 1, 0, 1, 1)

        self.btn_consulta = QPushButton(self.frame)
        self.btn_consulta.setObjectName(u"btn_consulta")
        sizePolicy.setHeightForWidth(self.btn_consulta.sizePolicy().hasHeightForWidth())
        self.btn_consulta.setSizePolicy(sizePolicy)
        self.btn_consulta.setMaximumSize(QSize(100, 60))
        self.btn_consulta.setFont(font1)
        self.btn_consulta.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_consulta, 2, 0, 1, 1)

        self.btn_financeiro = QPushButton(self.frame)
        self.btn_financeiro.setObjectName(u"btn_financeiro")
        self.btn_financeiro.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_financeiro.sizePolicy().hasHeightForWidth())
        self.btn_financeiro.setSizePolicy(sizePolicy)
        self.btn_financeiro.setMaximumSize(QSize(100, 60))
        self.btn_financeiro.setFont(font1)
        self.btn_financeiro.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_financeiro, 3, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.Conteudo)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Inicio = QWidget()
        self.Inicio.setObjectName(u"Inicio")
        self.gridLayout_3 = QGridLayout(self.Inicio)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.Inicio)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMaximumSize(QSize(16777215, 200))
        self.frame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_7)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_13, 4, 3, 1, 1)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(50, 30))
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_17, 0, 4, 1, 1)

        self.lb_ini_data_4 = QLabel(self.frame_7)
        self.lb_ini_data_4.setObjectName(u"lb_ini_data_4")
        self.lb_ini_data_4.setMaximumSize(QSize(16777215, 30))
        self.lb_ini_data_4.setFont(font3)
        self.lb_ini_data_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lb_ini_data_4, 1, 2, 1, 1)

        self.lb_ini_funcionario = QLabel(self.frame_7)
        self.lb_ini_funcionario.setObjectName(u"lb_ini_funcionario")
        self.lb_ini_funcionario.setMaximumSize(QSize(16777215, 30))
        self.lb_ini_funcionario.setFont(font3)
        self.lb_ini_funcionario.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lb_ini_funcionario, 4, 1, 1, 1)

        self.lb_img_func = QLabel(self.frame_7)
        self.lb_img_func.setObjectName(u"lb_img_func")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_img_func.sizePolicy().hasHeightForWidth())
        self.lb_img_func.setSizePolicy(sizePolicy2)
        self.lb_img_func.setMaximumSize(QSize(128, 200))
        self.lb_img_func.setStyleSheet(u"image: url(:/icons/img02.png)")
        self.lb_img_func.setPixmap(QPixmap(u"../../../../../.designer/Downloads/17004 (1).png"))

        self.gridLayout_13.addWidget(self.lb_img_func, 0, 1, 4, 1)

        self.lb_ini_data = QLabel(self.frame_7)
        self.lb_ini_data.setObjectName(u"lb_ini_data")
        self.lb_ini_data.setMaximumSize(QSize(16777215, 30))
        self.lb_ini_data.setFont(font3)
        self.lb_ini_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lb_ini_data, 1, 3, 1, 1)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMaximumSize(QSize(100, 16777215))
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_16, 4, 0, 1, 1)

        self.lb_ini_data_5 = QLabel(self.frame_7)
        self.lb_ini_data_5.setObjectName(u"lb_ini_data_5")
        self.lb_ini_data_5.setMaximumSize(QSize(16777215, 30))
        self.lb_ini_data_5.setFont(font3)
        self.lb_ini_data_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lb_ini_data_5, 4, 2, 1, 1)

        self.frame_27 = QFrame(self.frame_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_27)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.ini_btn_ponto = QPushButton(self.frame_27)
        self.ini_btn_ponto.setObjectName(u"ini_btn_ponto")
        self.ini_btn_ponto.setMaximumSize(QSize(200, 50))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setWeight(50)
        self.ini_btn_ponto.setFont(font4)
        self.ini_btn_ponto.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_37.addWidget(self.ini_btn_ponto, 0, 1, 1, 1)

        self.btn_ponto = QLabel(self.frame_27)
        self.btn_ponto.setObjectName(u"btn_ponto")
        self.btn_ponto.setMaximumSize(QSize(16777215, 30))
        self.btn_ponto.setFont(font3)
        self.btn_ponto.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.btn_ponto, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_27, 2, 3, 1, 1)

        self.lb_ini_data_3 = QLabel(self.frame_7)
        self.lb_ini_data_3.setObjectName(u"lb_ini_data_3")
        self.lb_ini_data_3.setMaximumSize(QSize(16777215, 30))
        self.lb_ini_data_3.setFont(font3)
        self.lb_ini_data_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lb_ini_data_3, 3, 2, 1, 1)

        self.lb_ini_data_2 = QLabel(self.frame_7)
        self.lb_ini_data_2.setObjectName(u"lb_ini_data_2")
        self.lb_ini_data_2.setMaximumSize(QSize(16777215, 30))
        self.lb_ini_data_2.setFont(font3)
        self.lb_ini_data_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.lb_ini_data_2, 3, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.label_59 = QLabel(self.Inicio)
        self.label_59.setObjectName(u"label_59")
        sizePolicy1.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy1)
        self.label_59.setMaximumSize(QSize(16777215, 800))
        font5 = QFont()
        font5.setPointSize(80)
        self.label_59.setFont(font5)
        self.label_59.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"image: url(:/icons/img01.png)")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_59, 1, 0, 1, 1)

        self.frame_36 = QFrame(self.Inicio)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_36)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.frame_36)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy3)
        self.btn_logout.setMaximumSize(QSize(100, 50))
        self.btn_logout.setFont(font4)
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_48.addWidget(self.btn_logout, 0, 1, 1, 1)

        self.btn_ponto_2 = QLabel(self.frame_36)
        self.btn_ponto_2.setObjectName(u"btn_ponto_2")
        self.btn_ponto_2.setMaximumSize(QSize(16777215, 30))
        self.btn_ponto_2.setFont(font3)
        self.btn_ponto_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.btn_ponto_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_48.addWidget(self.btn_ponto_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_36, 2, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.Inicio)
        self.Consulta = QWidget()
        self.Consulta.setObjectName(u"Consulta")
        self.gridLayout_5 = QGridLayout(self.Consulta)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.nav_consultas = QStackedWidget(self.Consulta)
        self.nav_consultas.setObjectName(u"nav_consultas")
        self.nav_consultas.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.nav_consultas.addWidget(self.Home)
        self.Vendas = QWidget()
        self.Vendas.setObjectName(u"Vendas")
        self.gridLayout_17 = QGridLayout(self.Vendas)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.cons_lb_informacao = QLabel(self.Vendas)
        self.cons_lb_informacao.setObjectName(u"cons_lb_informacao")
        self.cons_lb_informacao.setMaximumSize(QSize(80, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        self.cons_lb_informacao.setFont(font6)
        self.cons_lb_informacao.setStyleSheet(u"")

        self.gridLayout_17.addWidget(self.cons_lb_informacao, 0, 2, 1, 1)

        self.stackedWidget_3 = QStackedWidget(self.Vendas)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMaximumSize(QSize(200, 30))
        self.cons_st_data = QWidget()
        self.cons_st_data.setObjectName(u"cons_st_data")
        self.gridLayout_18 = QGridLayout(self.cons_st_data)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.cons_st_data)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cons_dt_inicio = QDateEdit(self.frame_9)
        self.cons_dt_inicio.setObjectName(u"cons_dt_inicio")
        self.cons_dt_inicio.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_dt_inicio.setCalendarPopup(True)
        self.cons_dt_inicio.setDate(QDate(2021, 1, 1))

        self.horizontalLayout.addWidget(self.cons_dt_inicio)

        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(10, 16777215))
        self.label_20.setFont(font6)
        self.label_20.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_20)

        self.cons_dt_fim = QDateEdit(self.frame_9)
        self.cons_dt_fim.setObjectName(u"cons_dt_fim")
        self.cons_dt_fim.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_dt_fim.setCalendarPopup(True)
        self.cons_dt_fim.setDate(QDate(2021, 1, 1))

        self.horizontalLayout.addWidget(self.cons_dt_fim)


        self.gridLayout_18.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.cons_st_data)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget_3.addWidget(self.page_5)

        self.gridLayout_17.addWidget(self.stackedWidget_3, 0, 6, 1, 1)

        self.cons_cb_informacao = QComboBox(self.Vendas)
        self.cons_cb_informacao.addItem("")
        self.cons_cb_informacao.addItem("")
        self.cons_cb_informacao.addItem("")
        self.cons_cb_informacao.addItem("")
        self.cons_cb_informacao.addItem("")
        self.cons_cb_informacao.addItem("")
        self.cons_cb_informacao.setObjectName(u"cons_cb_informacao")
        sizePolicy3.setHeightForWidth(self.cons_cb_informacao.sizePolicy().hasHeightForWidth())
        self.cons_cb_informacao.setSizePolicy(sizePolicy3)
        self.cons_cb_informacao.setMaximumSize(QSize(120, 16777215))
        self.cons_cb_informacao.setLayoutDirection(Qt.LeftToRight)
        self.cons_cb_informacao.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_17.addWidget(self.cons_cb_informacao, 0, 3, 1, 1)

        self.cons_btn_ok = QPushButton(self.Vendas)
        self.cons_btn_ok.setObjectName(u"cons_btn_ok")
        self.cons_btn_ok.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_ok.sizePolicy().hasHeightForWidth())
        self.cons_btn_ok.setSizePolicy(sizePolicy)
        self.cons_btn_ok.setMaximumSize(QSize(30, 28))
        self.cons_btn_ok.setFont(font6)
        self.cons_btn_ok.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_17.addWidget(self.cons_btn_ok, 0, 7, 1, 1)

        self.label_10 = QLabel(self.Vendas)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(80, 16777215))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"")

        self.gridLayout_17.addWidget(self.label_10, 0, 0, 1, 1)

        self.cons_lb_periodo = QLabel(self.Vendas)
        self.cons_lb_periodo.setObjectName(u"cons_lb_periodo")
        self.cons_lb_periodo.setMaximumSize(QSize(80, 16777215))
        self.cons_lb_periodo.setFont(font6)
        self.cons_lb_periodo.setStyleSheet(u"")

        self.gridLayout_17.addWidget(self.cons_lb_periodo, 0, 4, 1, 1)

        self.cons_cb_bomba = QComboBox(self.Vendas)
        self.cons_cb_bomba.addItem("")
        self.cons_cb_bomba.setObjectName(u"cons_cb_bomba")
        sizePolicy3.setHeightForWidth(self.cons_cb_bomba.sizePolicy().hasHeightForWidth())
        self.cons_cb_bomba.setSizePolicy(sizePolicy3)
        self.cons_cb_bomba.setMaximumSize(QSize(200, 16777215))
        self.cons_cb_bomba.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_17.addWidget(self.cons_cb_bomba, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_2, 0, 8, 1, 1)

        self.cons_cb_periodo = QComboBox(self.Vendas)
        self.cons_cb_periodo.addItem("")
        self.cons_cb_periodo.addItem("")
        self.cons_cb_periodo.addItem("")
        self.cons_cb_periodo.addItem("")
        self.cons_cb_periodo.addItem("")
        self.cons_cb_periodo.addItem("")
        self.cons_cb_periodo.setObjectName(u"cons_cb_periodo")
        sizePolicy3.setHeightForWidth(self.cons_cb_periodo.sizePolicy().hasHeightForWidth())
        self.cons_cb_periodo.setSizePolicy(sizePolicy3)
        self.cons_cb_periodo.setMaximumSize(QSize(120, 16777215))
        self.cons_cb_periodo.setLayoutDirection(Qt.LeftToRight)
        self.cons_cb_periodo.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_17.addWidget(self.cons_cb_periodo, 0, 5, 1, 1)

        self.cons_btn_exportar = QPushButton(self.Vendas)
        self.cons_btn_exportar.setObjectName(u"cons_btn_exportar")
        self.cons_btn_exportar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_exportar.sizePolicy().hasHeightForWidth())
        self.cons_btn_exportar.setSizePolicy(sizePolicy)
        self.cons_btn_exportar.setMaximumSize(QSize(60, 28))
        self.cons_btn_exportar.setFont(font6)
        self.cons_btn_exportar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_17.addWidget(self.cons_btn_exportar, 0, 9, 1, 1)

        self.widget = QWidget(self.Vendas)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: 1px solid rgb(110, 110, 110);\n"
"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.cons_gr_vendas = QVBoxLayout()
        self.cons_gr_vendas.setObjectName(u"cons_gr_vendas")

        self.gridLayout.addLayout(self.cons_gr_vendas, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget, 1, 0, 1, 10)

        self.nav_consultas.addWidget(self.Vendas)
        self.Tabelas = QWidget()
        self.Tabelas.setObjectName(u"Tabelas")
        self.gridLayout_24 = QGridLayout(self.Tabelas)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.cons_btn_tab_ok = QPushButton(self.Tabelas)
        self.cons_btn_tab_ok.setObjectName(u"cons_btn_tab_ok")
        self.cons_btn_tab_ok.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_tab_ok.sizePolicy().hasHeightForWidth())
        self.cons_btn_tab_ok.setSizePolicy(sizePolicy)
        self.cons_btn_tab_ok.setMaximumSize(QSize(30, 28))
        self.cons_btn_tab_ok.setFont(font6)
        self.cons_btn_tab_ok.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.cons_btn_tab_ok, 1, 11, 1, 1)

        self.cons_cb_tab_filtro = QComboBox(self.Tabelas)
        self.cons_cb_tab_filtro.addItem("")
        self.cons_cb_tab_filtro.setObjectName(u"cons_cb_tab_filtro")
        sizePolicy3.setHeightForWidth(self.cons_cb_tab_filtro.sizePolicy().hasHeightForWidth())
        self.cons_cb_tab_filtro.setSizePolicy(sizePolicy3)
        self.cons_cb_tab_filtro.setMaximumSize(QSize(120, 16777215))
        self.cons_cb_tab_filtro.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_24.addWidget(self.cons_cb_tab_filtro, 1, 2, 1, 1)

        self.cons_btn_tab_del = QPushButton(self.Tabelas)
        self.cons_btn_tab_del.setObjectName(u"cons_btn_tab_del")
        self.cons_btn_tab_del.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_tab_del.sizePolicy().hasHeightForWidth())
        self.cons_btn_tab_del.setSizePolicy(sizePolicy)
        self.cons_btn_tab_del.setMaximumSize(QSize(60, 30))
        self.cons_btn_tab_del.setFont(font4)
        self.cons_btn_tab_del.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.cons_btn_tab_del, 1, 15, 1, 1)

        self.cons_btn_tab_detalhes = QPushButton(self.Tabelas)
        self.cons_btn_tab_detalhes.setObjectName(u"cons_btn_tab_detalhes")
        self.cons_btn_tab_detalhes.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_tab_detalhes.sizePolicy().hasHeightForWidth())
        self.cons_btn_tab_detalhes.setSizePolicy(sizePolicy)
        self.cons_btn_tab_detalhes.setMaximumSize(QSize(82, 30))
        self.cons_btn_tab_detalhes.setFont(font4)
        self.cons_btn_tab_detalhes.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.cons_btn_tab_detalhes, 1, 13, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(262, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_3, 1, 12, 1, 1)

        self.cons_cb_tab_periodo = QComboBox(self.Tabelas)
        self.cons_cb_tab_periodo.addItem("")
        self.cons_cb_tab_periodo.addItem("")
        self.cons_cb_tab_periodo.addItem("")
        self.cons_cb_tab_periodo.addItem("")
        self.cons_cb_tab_periodo.addItem("")
        self.cons_cb_tab_periodo.addItem("")
        self.cons_cb_tab_periodo.setObjectName(u"cons_cb_tab_periodo")
        sizePolicy3.setHeightForWidth(self.cons_cb_tab_periodo.sizePolicy().hasHeightForWidth())
        self.cons_cb_tab_periodo.setSizePolicy(sizePolicy3)
        self.cons_cb_tab_periodo.setMaximumSize(QSize(120, 16777215))
        self.cons_cb_tab_periodo.setLayoutDirection(Qt.LeftToRight)
        self.cons_cb_tab_periodo.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_24.addWidget(self.cons_cb_tab_periodo, 1, 6, 1, 1)

        self.cons_tb = QTableWidget(self.Tabelas)
        if (self.cons_tb.columnCount() < 10):
            self.cons_tb.setColumnCount(10)
        font7 = QFont()
        font7.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font7);
        self.cons_tb.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.cons_tb.setObjectName(u"cons_tb")
        self.cons_tb.setEnabled(True)
        self.cons_tb.setFont(font6)
        self.cons_tb.setStyleSheet(u"QTableWidget{\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid rgba(68, 119, 170, 150);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 169, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 222, 90, 239), stop:1 rgba(255, 228, 117, 255));\n"
"	\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}")
        self.cons_tb.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cons_tb.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.cons_tb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cons_tb.setTabKeyNavigation(True)
        self.cons_tb.setProperty("showDropIndicator", True)
        self.cons_tb.setDragEnabled(False)
        self.cons_tb.setDragDropOverwriteMode(True)
        self.cons_tb.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.cons_tb.setAlternatingRowColors(True)
        self.cons_tb.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cons_tb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cons_tb.setShowGrid(True)
        self.cons_tb.setGridStyle(Qt.SolidLine)
        self.cons_tb.setWordWrap(True)
        self.cons_tb.horizontalHeader().setVisible(False)
        self.cons_tb.horizontalHeader().setCascadingSectionResizes(False)
        self.cons_tb.horizontalHeader().setDefaultSectionSize(100)
        self.cons_tb.horizontalHeader().setHighlightSections(False)
        self.cons_tb.horizontalHeader().setProperty("showSortIndicator", False)
        self.cons_tb.horizontalHeader().setStretchLastSection(True)
        self.cons_tb.verticalHeader().setVisible(False)
        self.cons_tb.verticalHeader().setStretchLastSection(False)

        self.gridLayout_24.addWidget(self.cons_tb, 8, 1, 1, 15)

        self.label_12 = QLabel(self.Tabelas)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMaximumSize(QSize(80, 16777215))
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"")

        self.gridLayout_24.addWidget(self.label_12, 1, 1, 1, 1)

        self.cons_lb_periodo_2 = QLabel(self.Tabelas)
        self.cons_lb_periodo_2.setObjectName(u"cons_lb_periodo_2")
        sizePolicy3.setHeightForWidth(self.cons_lb_periodo_2.sizePolicy().hasHeightForWidth())
        self.cons_lb_periodo_2.setSizePolicy(sizePolicy3)
        self.cons_lb_periodo_2.setMaximumSize(QSize(80, 30))
        self.cons_lb_periodo_2.setFont(font6)
        self.cons_lb_periodo_2.setStyleSheet(u"")

        self.gridLayout_24.addWidget(self.cons_lb_periodo_2, 1, 5, 1, 1)

        self.stackedWidget_4 = QStackedWidget(self.Tabelas)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        sizePolicy3.setHeightForWidth(self.stackedWidget_4.sizePolicy().hasHeightForWidth())
        self.stackedWidget_4.setSizePolicy(sizePolicy3)
        self.stackedWidget_4.setMaximumSize(QSize(200, 30))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setMaximumSize(QSize(200, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cons_dt_tab_inicio = QDateEdit(self.frame_12)
        self.cons_dt_tab_inicio.setObjectName(u"cons_dt_tab_inicio")
        self.cons_dt_tab_inicio.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_dt_tab_inicio.setCalendarPopup(True)
        self.cons_dt_tab_inicio.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_2.addWidget(self.cons_dt_tab_inicio)

        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(10, 16777215))
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_21)

        self.cons_dt_tab_fim = QDateEdit(self.frame_12)
        self.cons_dt_tab_fim.setObjectName(u"cons_dt_tab_fim")
        self.cons_dt_tab_fim.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_dt_tab_fim.setCalendarPopup(True)
        self.cons_dt_tab_fim.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_2.addWidget(self.cons_dt_tab_fim)


        self.horizontalLayout_4.addWidget(self.frame_12)

        self.stackedWidget_4.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_4.addWidget(self.page_2)

        self.gridLayout_24.addWidget(self.stackedWidget_4, 1, 10, 1, 1)

        self.cons_btn_tab_ret = QPushButton(self.Tabelas)
        self.cons_btn_tab_ret.setObjectName(u"cons_btn_tab_ret")
        self.cons_btn_tab_ret.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_tab_ret.sizePolicy().hasHeightForWidth())
        self.cons_btn_tab_ret.setSizePolicy(sizePolicy)
        self.cons_btn_tab_ret.setMaximumSize(QSize(82, 30))
        self.cons_btn_tab_ret.setFont(font4)
        self.cons_btn_tab_ret.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.cons_btn_tab_ret, 1, 14, 1, 1)

        self.cons_cb_tab_funcionario = QComboBox(self.Tabelas)
        self.cons_cb_tab_funcionario.setObjectName(u"cons_cb_tab_funcionario")
        sizePolicy3.setHeightForWidth(self.cons_cb_tab_funcionario.sizePolicy().hasHeightForWidth())
        self.cons_cb_tab_funcionario.setSizePolicy(sizePolicy3)
        self.cons_cb_tab_funcionario.setMaximumSize(QSize(120, 16777215))
        self.cons_cb_tab_funcionario.setLayoutDirection(Qt.LeftToRight)
        self.cons_cb_tab_funcionario.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_24.addWidget(self.cons_cb_tab_funcionario, 1, 4, 1, 1)

        self.frame_11 = QFrame(self.Tabelas)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_24.addWidget(self.frame_11, 7, 5, 1, 1)

        self.cons_lb_periodo_5 = QLabel(self.Tabelas)
        self.cons_lb_periodo_5.setObjectName(u"cons_lb_periodo_5")
        sizePolicy3.setHeightForWidth(self.cons_lb_periodo_5.sizePolicy().hasHeightForWidth())
        self.cons_lb_periodo_5.setSizePolicy(sizePolicy3)
        self.cons_lb_periodo_5.setMaximumSize(QSize(80, 30))
        self.cons_lb_periodo_5.setFont(font6)
        self.cons_lb_periodo_5.setStyleSheet(u"")

        self.gridLayout_24.addWidget(self.cons_lb_periodo_5, 1, 3, 1, 1)

        self.nav_consultas.addWidget(self.Tabelas)
        self.Retiradas = QWidget()
        self.Retiradas.setObjectName(u"Retiradas")
        self.verticalLayout_2 = QVBoxLayout(self.Retiradas)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.Retiradas)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(80, 16777215))
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_22)

        self.cons_cb_nome_2 = QComboBox(self.frame_14)
        self.cons_cb_nome_2.setObjectName(u"cons_cb_nome_2")
        sizePolicy3.setHeightForWidth(self.cons_cb_nome_2.sizePolicy().hasHeightForWidth())
        self.cons_cb_nome_2.setSizePolicy(sizePolicy3)
        self.cons_cb_nome_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.cons_cb_nome_2.setEditable(True)

        self.horizontalLayout_5.addWidget(self.cons_cb_nome_2)

        self.label_53 = QLabel(self.frame_14)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(80, 16777215))
        self.label_53.setFont(font6)
        self.label_53.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_53)

        self.ln_cons_info_2 = QLineEdit(self.frame_14)
        self.ln_cons_info_2.setObjectName(u"ln_cons_info_2")
        self.ln_cons_info_2.setEnabled(True)
        self.ln_cons_info_2.setMaximumSize(QSize(16777215, 20))
        self.ln_cons_info_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_cons_info_2.setAlignment(Qt.AlignCenter)
        self.ln_cons_info_2.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.ln_cons_info_2)

        self.cons_lb_periodo_3 = QLabel(self.frame_14)
        self.cons_lb_periodo_3.setObjectName(u"cons_lb_periodo_3")
        self.cons_lb_periodo_3.setMaximumSize(QSize(80, 16777215))
        self.cons_lb_periodo_3.setFont(font6)
        self.cons_lb_periodo_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.cons_lb_periodo_3)

        self.cons_cb_tab_retiradas = QComboBox(self.frame_14)
        self.cons_cb_tab_retiradas.addItem("")
        self.cons_cb_tab_retiradas.addItem("")
        self.cons_cb_tab_retiradas.addItem("")
        self.cons_cb_tab_retiradas.addItem("")
        self.cons_cb_tab_retiradas.addItem("")
        self.cons_cb_tab_retiradas.addItem("")
        self.cons_cb_tab_retiradas.setObjectName(u"cons_cb_tab_retiradas")
        sizePolicy3.setHeightForWidth(self.cons_cb_tab_retiradas.sizePolicy().hasHeightForWidth())
        self.cons_cb_tab_retiradas.setSizePolicy(sizePolicy3)
        self.cons_cb_tab_retiradas.setMaximumSize(QSize(120, 16777215))
        self.cons_cb_tab_retiradas.setLayoutDirection(Qt.LeftToRight)
        self.cons_cb_tab_retiradas.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout_5.addWidget(self.cons_cb_tab_retiradas)

        self.stackedWidget_5 = QStackedWidget(self.frame_14)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        sizePolicy3.setHeightForWidth(self.stackedWidget_5.sizePolicy().hasHeightForWidth())
        self.stackedWidget_5.setSizePolicy(sizePolicy3)
        self.stackedWidget_5.setMaximumSize(QSize(200, 30))
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_6 = QHBoxLayout(self.page_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.page_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy2)
        self.frame_16.setMaximumSize(QSize(200, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cons_dt_tab_inicio_2 = QDateEdit(self.frame_16)
        self.cons_dt_tab_inicio_2.setObjectName(u"cons_dt_tab_inicio_2")
        self.cons_dt_tab_inicio_2.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_dt_tab_inicio_2.setCalendarPopup(True)
        self.cons_dt_tab_inicio_2.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_7.addWidget(self.cons_dt_tab_inicio_2)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(10, 16777215))
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_23)

        self.cons_dt_tab_fim_2 = QDateEdit(self.frame_16)
        self.cons_dt_tab_fim_2.setObjectName(u"cons_dt_tab_fim_2")
        self.cons_dt_tab_fim_2.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_dt_tab_fim_2.setCalendarPopup(True)
        self.cons_dt_tab_fim_2.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_7.addWidget(self.cons_dt_tab_fim_2)


        self.horizontalLayout_6.addWidget(self.frame_16)

        self.stackedWidget_5.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget_5.addWidget(self.page_7)

        self.horizontalLayout_5.addWidget(self.stackedWidget_5)

        self.cons_btn_ok_2 = QPushButton(self.frame_14)
        self.cons_btn_ok_2.setObjectName(u"cons_btn_ok_2")
        self.cons_btn_ok_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_ok_2.sizePolicy().hasHeightForWidth())
        self.cons_btn_ok_2.setSizePolicy(sizePolicy)
        self.cons_btn_ok_2.setMaximumSize(QSize(30, 28))
        self.cons_btn_ok_2.setFont(font6)
        self.cons_btn_ok_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.cons_btn_ok_2)

        self.horizontalSpacer_4 = QSpacerItem(257, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.Retiradas)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_13)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.cons_tb_retiradas = QTableWidget(self.frame_13)
        if (self.cons_tb_retiradas.columnCount() < 5):
            self.cons_tb_retiradas.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font7);
        self.cons_tb_retiradas.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font7);
        self.cons_tb_retiradas.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font7);
        self.cons_tb_retiradas.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font7);
        self.cons_tb_retiradas.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font7);
        self.cons_tb_retiradas.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.cons_tb_retiradas.setObjectName(u"cons_tb_retiradas")
        self.cons_tb_retiradas.setEnabled(True)
        self.cons_tb_retiradas.setFont(font6)
        self.cons_tb_retiradas.setStyleSheet(u"QTableWidget{\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid rgba(68, 119, 170, 150);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 169, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 222, 90, 239), stop:1 rgba(255, 228, 117, 255));\n"
"	\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}")
        self.cons_tb_retiradas.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cons_tb_retiradas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.cons_tb_retiradas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cons_tb_retiradas.setTabKeyNavigation(True)
        self.cons_tb_retiradas.setProperty("showDropIndicator", True)
        self.cons_tb_retiradas.setDragEnabled(False)
        self.cons_tb_retiradas.setDragDropOverwriteMode(True)
        self.cons_tb_retiradas.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.cons_tb_retiradas.setAlternatingRowColors(True)
        self.cons_tb_retiradas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cons_tb_retiradas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cons_tb_retiradas.setShowGrid(True)
        self.cons_tb_retiradas.setGridStyle(Qt.SolidLine)
        self.cons_tb_retiradas.setWordWrap(True)
        self.cons_tb_retiradas.horizontalHeader().setVisible(False)
        self.cons_tb_retiradas.horizontalHeader().setCascadingSectionResizes(False)
        self.cons_tb_retiradas.horizontalHeader().setDefaultSectionSize(100)
        self.cons_tb_retiradas.horizontalHeader().setHighlightSections(False)
        self.cons_tb_retiradas.horizontalHeader().setProperty("showSortIndicator", False)
        self.cons_tb_retiradas.horizontalHeader().setStretchLastSection(True)
        self.cons_tb_retiradas.verticalHeader().setVisible(False)
        self.cons_tb_retiradas.verticalHeader().setStretchLastSection(False)

        self.gridLayout_23.addWidget(self.cons_tb_retiradas, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.nav_consultas.addWidget(self.Retiradas)
        self.Ponto = QWidget()
        self.Ponto.setObjectName(u"Ponto")
        self.gridLayout_39 = QGridLayout(self.Ponto)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.frame_29 = QFrame(self.Ponto)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 40))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_29)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(80, 16777215))
        self.label_48.setFont(font6)
        self.label_48.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_48)

        self.cons_ponto_cb_filtro = QComboBox(self.frame_29)
        self.cons_ponto_cb_filtro.addItem("")
        self.cons_ponto_cb_filtro.setObjectName(u"cons_ponto_cb_filtro")
        sizePolicy3.setHeightForWidth(self.cons_ponto_cb_filtro.sizePolicy().hasHeightForWidth())
        self.cons_ponto_cb_filtro.setSizePolicy(sizePolicy3)
        self.cons_ponto_cb_filtro.setMaximumSize(QSize(100, 16777215))
        self.cons_ponto_cb_filtro.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout_14.addWidget(self.cons_ponto_cb_filtro)

        self.cons_ponto_cb_funcionario = QComboBox(self.frame_29)
        self.cons_ponto_cb_funcionario.setObjectName(u"cons_ponto_cb_funcionario")
        sizePolicy3.setHeightForWidth(self.cons_ponto_cb_funcionario.sizePolicy().hasHeightForWidth())
        self.cons_ponto_cb_funcionario.setSizePolicy(sizePolicy3)
        self.cons_ponto_cb_funcionario.setMaximumSize(QSize(150, 16777215))
        self.cons_ponto_cb_funcionario.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout_14.addWidget(self.cons_ponto_cb_funcionario)

        self.cons_lb_periodo_4 = QLabel(self.frame_29)
        self.cons_lb_periodo_4.setObjectName(u"cons_lb_periodo_4")
        self.cons_lb_periodo_4.setMaximumSize(QSize(80, 16777215))
        self.cons_lb_periodo_4.setFont(font6)
        self.cons_lb_periodo_4.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.cons_lb_periodo_4)

        self.cons_ponto_cb_periodo = QComboBox(self.frame_29)
        self.cons_ponto_cb_periodo.addItem("")
        self.cons_ponto_cb_periodo.addItem("")
        self.cons_ponto_cb_periodo.addItem("")
        self.cons_ponto_cb_periodo.addItem("")
        self.cons_ponto_cb_periodo.addItem("")
        self.cons_ponto_cb_periodo.addItem("")
        self.cons_ponto_cb_periodo.setObjectName(u"cons_ponto_cb_periodo")
        sizePolicy3.setHeightForWidth(self.cons_ponto_cb_periodo.sizePolicy().hasHeightForWidth())
        self.cons_ponto_cb_periodo.setSizePolicy(sizePolicy3)
        self.cons_ponto_cb_periodo.setMaximumSize(QSize(120, 16777215))
        self.cons_ponto_cb_periodo.setLayoutDirection(Qt.LeftToRight)
        self.cons_ponto_cb_periodo.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout_14.addWidget(self.cons_ponto_cb_periodo)

        self.stackedWidget_9 = QStackedWidget(self.frame_29)
        self.stackedWidget_9.setObjectName(u"stackedWidget_9")
        sizePolicy3.setHeightForWidth(self.stackedWidget_9.sizePolicy().hasHeightForWidth())
        self.stackedWidget_9.setSizePolicy(sizePolicy3)
        self.stackedWidget_9.setMaximumSize(QSize(200, 30))
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_17 = QHBoxLayout(self.page_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.page_12)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy2)
        self.frame_31.setMaximumSize(QSize(200, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.cons_ponto_dt_inicio = QDateEdit(self.frame_31)
        self.cons_ponto_dt_inicio.setObjectName(u"cons_ponto_dt_inicio")
        self.cons_ponto_dt_inicio.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_ponto_dt_inicio.setCalendarPopup(True)
        self.cons_ponto_dt_inicio.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_18.addWidget(self.cons_ponto_dt_inicio)

        self.label_49 = QLabel(self.frame_31)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(10, 16777215))
        self.label_49.setFont(font6)
        self.label_49.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.label_49)

        self.cons_ponto_dt_fim = QDateEdit(self.frame_31)
        self.cons_ponto_dt_fim.setObjectName(u"cons_ponto_dt_fim")
        self.cons_ponto_dt_fim.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cons_ponto_dt_fim.setCalendarPopup(True)
        self.cons_ponto_dt_fim.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_18.addWidget(self.cons_ponto_dt_fim)


        self.horizontalLayout_17.addWidget(self.frame_31)

        self.stackedWidget_9.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.stackedWidget_9.addWidget(self.page_13)

        self.horizontalLayout_14.addWidget(self.stackedWidget_9)

        self.cons_ponto_btn_ok = QPushButton(self.frame_29)
        self.cons_ponto_btn_ok.setObjectName(u"cons_ponto_btn_ok")
        self.cons_ponto_btn_ok.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_ponto_btn_ok.sizePolicy().hasHeightForWidth())
        self.cons_ponto_btn_ok.setSizePolicy(sizePolicy)
        self.cons_ponto_btn_ok.setMaximumSize(QSize(30, 28))
        self.cons_ponto_btn_ok.setFont(font6)
        self.cons_ponto_btn_ok.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_14.addWidget(self.cons_ponto_btn_ok)

        self.horizontalSpacer_7 = QSpacerItem(257, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)


        self.gridLayout_39.addWidget(self.frame_29, 0, 0, 1, 1)

        self.frame_28 = QFrame(self.Ponto)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_28)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.cons_ponto_tb = QTableWidget(self.frame_28)
        if (self.cons_ponto_tb.columnCount() < 6):
            self.cons_ponto_tb.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font7);
        self.cons_ponto_tb.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font7);
        self.cons_ponto_tb.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font7);
        self.cons_ponto_tb.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font7);
        self.cons_ponto_tb.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font7);
        self.cons_ponto_tb.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font7);
        self.cons_ponto_tb.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.cons_ponto_tb.setObjectName(u"cons_ponto_tb")
        self.cons_ponto_tb.setEnabled(True)
        self.cons_ponto_tb.setFont(font6)
        self.cons_ponto_tb.setStyleSheet(u"QTableWidget{\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid rgba(68, 119, 170, 150);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 169, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 222, 90, 239), stop:1 rgba(255, 228, 117, 255));\n"
"	\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}")
        self.cons_ponto_tb.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cons_ponto_tb.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.cons_ponto_tb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cons_ponto_tb.setTabKeyNavigation(True)
        self.cons_ponto_tb.setProperty("showDropIndicator", True)
        self.cons_ponto_tb.setDragEnabled(False)
        self.cons_ponto_tb.setDragDropOverwriteMode(True)
        self.cons_ponto_tb.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.cons_ponto_tb.setAlternatingRowColors(True)
        self.cons_ponto_tb.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cons_ponto_tb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cons_ponto_tb.setShowGrid(True)
        self.cons_ponto_tb.setGridStyle(Qt.SolidLine)
        self.cons_ponto_tb.setWordWrap(True)
        self.cons_ponto_tb.horizontalHeader().setVisible(False)
        self.cons_ponto_tb.horizontalHeader().setCascadingSectionResizes(False)
        self.cons_ponto_tb.horizontalHeader().setDefaultSectionSize(100)
        self.cons_ponto_tb.horizontalHeader().setHighlightSections(False)
        self.cons_ponto_tb.horizontalHeader().setProperty("showSortIndicator", False)
        self.cons_ponto_tb.horizontalHeader().setStretchLastSection(True)
        self.cons_ponto_tb.verticalHeader().setVisible(False)
        self.cons_ponto_tb.verticalHeader().setStretchLastSection(False)

        self.gridLayout_38.addWidget(self.cons_ponto_tb, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_28, 1, 0, 1, 1)

        self.nav_consultas.addWidget(self.Ponto)

        self.gridLayout_5.addWidget(self.nav_consultas, 3, 0, 1, 1)

        self.frame_8 = QFrame(self.Consulta)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMaximumSize(QSize(16777215, 120))
        self.frame_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"border-radius: 5px 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(0)
        self.gridLayout_15.setVerticalSpacing(6)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: white;\n"
"border-bottom: 1px solid rgb(166, 166, 166);\n"
"border-radius: none;\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_10)
        self.gridLayout_19.setSpacing(1)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(1, 1, 1, 1)
        self.cons_lb = QLabel(self.frame_10)
        self.cons_lb.setObjectName(u"cons_lb")
        sizePolicy1.setHeightForWidth(self.cons_lb.sizePolicy().hasHeightForWidth())
        self.cons_lb.setSizePolicy(sizePolicy1)
        self.cons_lb.setMaximumSize(QSize(155, 70))
        font8 = QFont()
        font8.setPointSize(18)
        font8.setBold(True)
        font8.setWeight(75)
        self.cons_lb.setFont(font8)
        self.cons_lb.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.cons_lb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.cons_lb, 0, 0, 1, 1)

        self.cons_lb_nav = QLabel(self.frame_10)
        self.cons_lb_nav.setObjectName(u"cons_lb_nav")
        sizePolicy1.setHeightForWidth(self.cons_lb_nav.sizePolicy().hasHeightForWidth())
        self.cons_lb_nav.setSizePolicy(sizePolicy1)
        self.cons_lb_nav.setMaximumSize(QSize(16777215, 70))
        self.cons_lb_nav.setFont(font8)
        self.cons_lb_nav.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.cons_lb_nav.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.cons_lb_nav, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.frame_10, 0, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.cons_btn_vendas = QPushButton(self.frame_8)
        self.cons_btn_vendas.setObjectName(u"cons_btn_vendas")
        sizePolicy.setHeightForWidth(self.cons_btn_vendas.sizePolicy().hasHeightForWidth())
        self.cons_btn_vendas.setSizePolicy(sizePolicy)
        self.cons_btn_vendas.setMaximumSize(QSize(90, 50))
        self.cons_btn_vendas.setFont(font2)
        self.cons_btn_vendas.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.cons_btn_vendas, 1, 0, 1, 1)

        self.cons_btn_tabela = QPushButton(self.frame_8)
        self.cons_btn_tabela.setObjectName(u"cons_btn_tabela")
        self.cons_btn_tabela.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_tabela.sizePolicy().hasHeightForWidth())
        self.cons_btn_tabela.setSizePolicy(sizePolicy)
        self.cons_btn_tabela.setMaximumSize(QSize(90, 50))
        self.cons_btn_tabela.setFont(font2)
        self.cons_btn_tabela.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.cons_btn_tabela, 1, 1, 1, 1)

        self.cons_btn_ponto = QPushButton(self.frame_8)
        self.cons_btn_ponto.setObjectName(u"cons_btn_ponto")
        self.cons_btn_ponto.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_ponto.sizePolicy().hasHeightForWidth())
        self.cons_btn_ponto.setSizePolicy(sizePolicy)
        self.cons_btn_ponto.setMaximumSize(QSize(90, 50))
        self.cons_btn_ponto.setFont(font2)
        self.cons_btn_ponto.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.cons_btn_ponto, 1, 3, 1, 1)

        self.cons_btn_retiradas = QPushButton(self.frame_8)
        self.cons_btn_retiradas.setObjectName(u"cons_btn_retiradas")
        self.cons_btn_retiradas.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cons_btn_retiradas.sizePolicy().hasHeightForWidth())
        self.cons_btn_retiradas.setSizePolicy(sizePolicy)
        self.cons_btn_retiradas.setMaximumSize(QSize(90, 50))
        self.cons_btn_retiradas.setFont(font2)
        self.cons_btn_retiradas.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.cons_btn_retiradas, 1, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_37 = QFrame(self.Consulta)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 40))
        self.frame_37.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.label_4 = QLabel(self.frame_37)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font6)

        self.horizontalLayout_13.addWidget(self.label_4)

        self.cons_tab_total = QLineEdit(self.frame_37)
        self.cons_tab_total.setObjectName(u"cons_tab_total")
        self.cons_tab_total.setMaximumSize(QSize(150, 25))
        self.cons_tab_total.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.cons_tab_total.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.cons_tab_total)


        self.gridLayout_5.addWidget(self.frame_37, 4, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.Consulta)
        self.Caixa = QWidget()
        self.Caixa.setObjectName(u"Caixa")
        self.gridLayout_4 = QGridLayout(self.Caixa)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, -1)
        self.frame_6 = QFrame(self.Caixa)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 70))
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(10)
        self.gridLayout_21.setContentsMargins(0, 0, 15, 0)
        self.cx_nome = QComboBox(self.frame_6)
        self.cx_nome.addItem("")
        self.cx_nome.setObjectName(u"cx_nome")
        self.cx_nome.setMinimumSize(QSize(200, 0))
        self.cx_nome.setMaximumSize(QSize(200, 30))
        self.cx_nome.setStyleSheet(u"color: white;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))")
        self.cx_nome.setEditable(True)

        self.gridLayout_21.addWidget(self.cx_nome, 0, 3, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QSize(115, 70))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_11.setFont(font9)
        self.label_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_11, 0, 2, 1, 1)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(350, 70))
        self.label.setFont(font8)
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label, 0, 0, 1, 1)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMaximumSize(QSize(50, 70))
        self.label_24.setFont(font9)
        self.label_24.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_31 = QLabel(self.frame_6)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMaximumSize(QSize(16777215, 70))
        self.label_31.setFont(font9)
        self.label_31.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_31, 0, 1, 1, 1)

        self.cx_data = QDateEdit(self.frame_6)
        self.cx_data.setObjectName(u"cx_data")
        self.cx_data.setMinimumSize(QSize(100, 0))
        self.cx_data.setMaximumSize(QSize(200, 30))
        self.cx_data.setFont(font6)
        self.cx_data.setStyleSheet(u"QDateEdit{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 5px;\n"
"color: white;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.cx_data.setAlignment(Qt.AlignCenter)
        self.cx_data.setCalendarPopup(True)
        self.cx_data.setDate(QDate(2021, 1, 1))

        self.gridLayout_21.addWidget(self.cx_data, 0, 5, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.Caixa)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(20)
        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMaximumSize(QSize(16777215, 30))
        self.label_40.setFont(font6)
        self.label_40.setStyleSheet(u"border: none;")
        self.label_40.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_10.addWidget(self.label_40, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cb_bomba = QComboBox(self.frame_4)
        self.cb_bomba.addItem("")
        self.cb_bomba.setObjectName(u"cb_bomba")
        self.cb_bomba.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.gridLayout_11.addWidget(self.cb_bomba, 1, 1, 1, 1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(80, 16777215))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.label_9, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 80))
        self.groupBox.setFont(font7)
        self.groupBox.setStyleSheet(u"border: 1px solid white;")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_14 = QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(17)
        self.ln_digi_anterior = QLineEdit(self.groupBox)
        self.ln_digi_anterior.setObjectName(u"ln_digi_anterior")
        self.ln_digi_anterior.setEnabled(True)
        self.ln_digi_anterior.setMaximumSize(QSize(16777215, 20))
        self.ln_digi_anterior.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_digi_anterior.setMaxLength(7)
        self.ln_digi_anterior.setAlignment(Qt.AlignCenter)
        self.ln_digi_anterior.setReadOnly(True)

        self.gridLayout_14.addWidget(self.ln_digi_anterior, 0, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"border: none;")

        self.gridLayout_14.addWidget(self.label_15, 0, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"border: none;")

        self.gridLayout_14.addWidget(self.label_14, 0, 0, 1, 1)

        self.ln_ana_anterior = QLineEdit(self.groupBox)
        self.ln_ana_anterior.setObjectName(u"ln_ana_anterior")
        self.ln_ana_anterior.setEnabled(True)
        self.ln_ana_anterior.setMaximumSize(QSize(16777215, 20))
        self.ln_ana_anterior.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_ana_anterior.setMaxLength(7)
        self.ln_ana_anterior.setAlignment(Qt.AlignCenter)
        self.ln_ana_anterior.setReadOnly(True)

        self.gridLayout_14.addWidget(self.ln_ana_anterior, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox, 2, 0, 1, 4)

        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 80))
        self.groupBox_2.setFont(font7)
        self.groupBox_2.setStyleSheet(u"border: 1px solid white;")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_16 = QGridLayout(self.groupBox_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(17)
        self.ln_ana_atual = QLineEdit(self.groupBox_2)
        self.ln_ana_atual.setObjectName(u"ln_ana_atual")
        self.ln_ana_atual.setEnabled(True)
        self.ln_ana_atual.setMaximumSize(QSize(16777215, 20))
        self.ln_ana_atual.setMouseTracking(False)
        self.ln_ana_atual.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_ana_atual.setInputMethodHints(Qt.ImhNone)
        self.ln_ana_atual.setMaxLength(32767)
        self.ln_ana_atual.setCursorPosition(0)
        self.ln_ana_atual.setAlignment(Qt.AlignCenter)
        self.ln_ana_atual.setReadOnly(False)
        self.ln_ana_atual.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_16.addWidget(self.ln_ana_atual, 0, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"border: none;")

        self.gridLayout_16.addWidget(self.label_18, 0, 2, 1, 1)

        self.ln_digi_atual = QLineEdit(self.groupBox_2)
        self.ln_digi_atual.setObjectName(u"ln_digi_atual")
        self.ln_digi_atual.setEnabled(True)
        self.ln_digi_atual.setMaximumSize(QSize(16777215, 20))
        self.ln_digi_atual.setMouseTracking(False)
        self.ln_digi_atual.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_digi_atual.setMaxLength(32767)
        self.ln_digi_atual.setCursorPosition(0)
        self.ln_digi_atual.setAlignment(Qt.AlignCenter)
        self.ln_digi_atual.setReadOnly(False)
        self.ln_digi_atual.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.ln_digi_atual.setClearButtonEnabled(False)

        self.gridLayout_16.addWidget(self.ln_digi_atual, 0, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setFont(font6)
        self.label_19.setStyleSheet(u"border: none;")

        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_2, 3, 0, 1, 4)

        self.btn_cx_inserir = QPushButton(self.frame_4)
        self.btn_cx_inserir.setObjectName(u"btn_cx_inserir")
        self.btn_cx_inserir.setMaximumSize(QSize(16777215, 25))
        self.btn_cx_inserir.setFont(font6)
        self.btn_cx_inserir.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.btn_cx_inserir, 4, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 200))
        self.groupBox_3.setFont(font7)
        self.groupBox_3.setStyleSheet(u"border: 1px solid white;")
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_20 = QGridLayout(self.groupBox_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(17)
        self.ln_cx_pix = QLineEdit(self.groupBox_3)
        self.ln_cx_pix.setObjectName(u"ln_cx_pix")
        self.ln_cx_pix.setEnabled(True)
        self.ln_cx_pix.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_pix.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_pix.setInputMethodHints(Qt.ImhNone)
        self.ln_cx_pix.setMaxLength(10)
        self.ln_cx_pix.setAlignment(Qt.AlignCenter)
        self.ln_cx_pix.setReadOnly(False)

        self.gridLayout_20.addWidget(self.ln_cx_pix, 3, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setMaximumSize(QSize(100, 30))
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_27, 0, 0, 1, 1)

        self.ln_cx_din = QLineEdit(self.groupBox_3)
        self.ln_cx_din.setObjectName(u"ln_cx_din")
        self.ln_cx_din.setEnabled(True)
        self.ln_cx_din.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_din.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_din.setInputMethodHints(Qt.ImhNone)
        self.ln_cx_din.setMaxLength(10)
        self.ln_cx_din.setAlignment(Qt.AlignCenter)
        self.ln_cx_din.setReadOnly(False)

        self.gridLayout_20.addWidget(self.ln_cx_din, 2, 1, 1, 1)

        self.ln_cx_resto_2 = QLineEdit(self.groupBox_3)
        self.ln_cx_resto_2.setObjectName(u"ln_cx_resto_2")
        self.ln_cx_resto_2.setEnabled(True)
        self.ln_cx_resto_2.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_resto_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_resto_2.setInputMethodHints(Qt.ImhDigitsOnly)
        self.ln_cx_resto_2.setMaxLength(7)
        self.ln_cx_resto_2.setAlignment(Qt.AlignCenter)
        self.ln_cx_resto_2.setReadOnly(True)

        self.gridLayout_20.addWidget(self.ln_cx_resto_2, 6, 1, 1, 1)

        self.ln_cx_cartao = QLineEdit(self.groupBox_3)
        self.ln_cx_cartao.setObjectName(u"ln_cx_cartao")
        self.ln_cx_cartao.setEnabled(True)
        self.ln_cx_cartao.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_cartao.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_cartao.setInputMethodHints(Qt.ImhNone)
        self.ln_cx_cartao.setMaxLength(10)
        self.ln_cx_cartao.setAlignment(Qt.AlignCenter)
        self.ln_cx_cartao.setReadOnly(False)

        self.gridLayout_20.addWidget(self.ln_cx_cartao, 4, 1, 1, 1)

        self.ln_cx_valor = QLineEdit(self.groupBox_3)
        self.ln_cx_valor.setObjectName(u"ln_cx_valor")
        self.ln_cx_valor.setEnabled(True)
        self.ln_cx_valor.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_valor.setMaxLength(7)
        self.ln_cx_valor.setAlignment(Qt.AlignCenter)
        self.ln_cx_valor.setReadOnly(True)

        self.gridLayout_20.addWidget(self.ln_cx_valor, 1, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setFont(font6)
        self.label_29.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_29, 7, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 30))
        self.label_30.setFont(font6)
        self.label_30.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_47 = QLabel(self.groupBox_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 30))
        self.label_47.setFont(font6)
        self.label_47.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_47, 3, 0, 1, 1)

        self.ln_cx_resto = QLineEdit(self.groupBox_3)
        self.ln_cx_resto.setObjectName(u"ln_cx_resto")
        self.ln_cx_resto.setEnabled(True)
        self.ln_cx_resto.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_resto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_resto.setInputMethodHints(Qt.ImhDigitsOnly)
        self.ln_cx_resto.setMaxLength(7)
        self.ln_cx_resto.setAlignment(Qt.AlignCenter)
        self.ln_cx_resto.setReadOnly(True)

        self.gridLayout_20.addWidget(self.ln_cx_resto, 7, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 30))
        self.label_28.setFont(font6)
        self.label_28.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_51 = QLabel(self.groupBox_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 30))
        self.label_51.setFont(font6)
        self.label_51.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_51, 4, 0, 1, 1)

        self.ln_cx_litros = QLineEdit(self.groupBox_3)
        self.ln_cx_litros.setObjectName(u"ln_cx_litros")
        self.ln_cx_litros.setEnabled(True)
        self.ln_cx_litros.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_litros.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_litros.setMaxLength(7)
        self.ln_cx_litros.setAlignment(Qt.AlignCenter)
        self.ln_cx_litros.setReadOnly(True)

        self.gridLayout_20.addWidget(self.ln_cx_litros, 0, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 30))
        self.label_52.setFont(font6)
        self.label_52.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_52, 6, 0, 1, 1)

        self.label_54 = QLabel(self.groupBox_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 30))
        self.label_54.setFont(font6)
        self.label_54.setStyleSheet(u"border: none;")

        self.gridLayout_20.addWidget(self.label_54, 5, 0, 1, 1)

        self.ln_cx_retiradas = QLineEdit(self.groupBox_3)
        self.ln_cx_retiradas.setObjectName(u"ln_cx_retiradas")
        self.ln_cx_retiradas.setEnabled(True)
        self.ln_cx_retiradas.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_retiradas.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90);")
        self.ln_cx_retiradas.setInputMethodHints(Qt.ImhNone)
        self.ln_cx_retiradas.setMaxLength(10)
        self.ln_cx_retiradas.setAlignment(Qt.AlignCenter)
        self.ln_cx_retiradas.setDragEnabled(False)
        self.ln_cx_retiradas.setReadOnly(True)

        self.gridLayout_20.addWidget(self.ln_cx_retiradas, 5, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_3, 5, 0, 1, 4)


        self.gridLayout_10.addWidget(self.frame_4, 1, 0, 1, 1)

        self.btn_cx_fechar = QPushButton(self.frame_2)
        self.btn_cx_fechar.setObjectName(u"btn_cx_fechar")
        sizePolicy.setHeightForWidth(self.btn_cx_fechar.sizePolicy().hasHeightForWidth())
        self.btn_cx_fechar.setSizePolicy(sizePolicy)
        self.btn_cx_fechar.setMaximumSize(QSize(16777215, 25))
        self.btn_cx_fechar.setFont(font6)
        self.btn_cx_fechar.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.btn_cx_fechar, 3, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(6)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_5)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)
        self.label_38.setMaximumSize(QSize(16777215, 10))
        self.label_38.setFont(font6)
        self.label_38.setStyleSheet(u"border: none;")

        self.gridLayout_12.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_39 = QLabel(self.frame_5)
        self.label_39.setObjectName(u"label_39")
        sizePolicy1.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy1)
        self.label_39.setMaximumSize(QSize(16777215, 10))
        self.label_39.setFont(font6)
        self.label_39.setStyleSheet(u"border: none;")

        self.gridLayout_12.addWidget(self.label_39, 1, 1, 1, 1)

        self.btn_cx_ret_inserir = QPushButton(self.frame_5)
        self.btn_cx_ret_inserir.setObjectName(u"btn_cx_ret_inserir")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_cx_ret_inserir.sizePolicy().hasHeightForWidth())
        self.btn_cx_ret_inserir.setSizePolicy(sizePolicy5)
        self.btn_cx_ret_inserir.setMaximumSize(QSize(16777215, 25))
        self.btn_cx_ret_inserir.setFont(font6)
        self.btn_cx_ret_inserir.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.btn_cx_ret_inserir, 3, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 150))
        self.groupBox_4.setFont(font7)
        self.groupBox_4.setStyleSheet(u"border: 1px solid white;")
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_22 = QGridLayout(self.groupBox_4)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(17)
        self.gridLayout_22.setVerticalSpacing(10)
        self.ln_cx_ter_valor = QLineEdit(self.groupBox_4)
        self.ln_cx_ter_valor.setObjectName(u"ln_cx_ter_valor")
        self.ln_cx_ter_valor.setEnabled(True)
        self.ln_cx_ter_valor.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_ter_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_cx_ter_valor.setMaxLength(7)
        self.ln_cx_ter_valor.setAlignment(Qt.AlignCenter)
        self.ln_cx_ter_valor.setReadOnly(False)

        self.gridLayout_22.addWidget(self.ln_cx_ter_valor, 2, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 30))
        self.label_34.setFont(font6)
        self.label_34.setStyleSheet(u"border: none;")

        self.gridLayout_22.addWidget(self.label_34, 2, 0, 1, 1)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 30))
        self.label_35.setFont(font6)
        self.label_35.setStyleSheet(u"border: none;")

        self.gridLayout_22.addWidget(self.label_35, 3, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 30))
        self.label_33.setFont(font6)
        self.label_33.setStyleSheet(u"border: none;")

        self.gridLayout_22.addWidget(self.label_33, 0, 0, 1, 1)

        self.cb_cx_nome = QComboBox(self.groupBox_4)
        self.cb_cx_nome.addItem("")
        self.cb_cx_nome.setObjectName(u"cb_cx_nome")
        self.cb_cx_nome.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.cb_cx_nome.setEditable(True)

        self.gridLayout_22.addWidget(self.cb_cx_nome, 0, 1, 1, 1)

        self.ln_cx_desc = QLineEdit(self.groupBox_4)
        self.ln_cx_desc.setObjectName(u"ln_cx_desc")
        self.ln_cx_desc.setEnabled(True)
        self.ln_cx_desc.setMaximumSize(QSize(16777215, 20))
        self.ln_cx_desc.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_cx_desc.setMaxLength(300)
        self.ln_cx_desc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ln_cx_desc.setReadOnly(False)

        self.gridLayout_22.addWidget(self.ln_cx_desc, 3, 1, 1, 2)

        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMaximumSize(QSize(16777215, 30))
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"border: none;")

        self.gridLayout_22.addWidget(self.label_32, 2, 2, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_4, 2, 0, 1, 3)

        self.tb_cx = QTableWidget(self.frame_5)
        if (self.tb_cx.columnCount() < 3):
            self.tb_cx.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_cx.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_cx.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_cx.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        self.tb_cx.setObjectName(u"tb_cx")
        self.tb_cx.setStyleSheet(u"QTableWidget{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    hborder: 5px solid rgba(68, 119, 170, 150);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 169, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 232, 136, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}")
        self.tb_cx.setFrameShadow(QFrame.Sunken)
        self.tb_cx.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tb_cx.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tb_cx.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_cx.setTextElideMode(Qt.ElideRight)
        self.tb_cx.setWordWrap(True)
        self.tb_cx.setCornerButtonEnabled(True)
        self.tb_cx.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_cx.horizontalHeader().setHighlightSections(True)
        self.tb_cx.horizontalHeader().setStretchLastSection(True)
        self.tb_cx.verticalHeader().setVisible(False)

        self.gridLayout_12.addWidget(self.tb_cx, 4, 0, 1, 3)


        self.gridLayout_10.addWidget(self.frame_5, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.Caixa)
        self.Configuracao = QWidget()
        self.Configuracao.setObjectName(u"Configuracao")
        self.gridLayout_42 = QGridLayout(self.Configuracao)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.frame_32 = QFrame(self.Configuracao)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 120))
        self.frame_32.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"border-radius: 5px 5px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_32)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy1.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy1)
        self.frame_33.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: white;\n"
"border-bottom: 1px solid rgb(166, 166, 166);\n"
"border-radius: none;\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_33)
        self.gridLayout_41.setSpacing(1)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(1, 1, 1, 1)
        self.cons_lb_3 = QLabel(self.frame_33)
        self.cons_lb_3.setObjectName(u"cons_lb_3")
        sizePolicy1.setHeightForWidth(self.cons_lb_3.sizePolicy().hasHeightForWidth())
        self.cons_lb_3.setSizePolicy(sizePolicy1)
        self.cons_lb_3.setMaximumSize(QSize(230, 70))
        self.cons_lb_3.setFont(font8)
        self.cons_lb_3.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.cons_lb_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.cons_lb_3, 0, 0, 1, 1)

        self.cons_lb_nav_2 = QLabel(self.frame_33)
        self.cons_lb_nav_2.setObjectName(u"cons_lb_nav_2")
        sizePolicy1.setHeightForWidth(self.cons_lb_nav_2.sizePolicy().hasHeightForWidth())
        self.cons_lb_nav_2.setSizePolicy(sizePolicy1)
        self.cons_lb_nav_2.setMaximumSize(QSize(16777215, 70))
        self.cons_lb_nav_2.setFont(font8)
        self.cons_lb_nav_2.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.cons_lb_nav_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.cons_lb_nav_2, 0, 1, 1, 1)


        self.gridLayout_40.addWidget(self.frame_33, 0, 0, 1, 3)

        self.stackedWidget_12 = QStackedWidget(self.frame_32)
        self.stackedWidget_12.setObjectName(u"stackedWidget_12")
        self.stackedWidget_12.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.config_main = QWidget()
        self.config_main.setObjectName(u"config_main")
        self.horizontalLayout_19 = QHBoxLayout(self.config_main)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.config_comb_btn = QPushButton(self.config_main)
        self.config_comb_btn.setObjectName(u"config_comb_btn")
        sizePolicy.setHeightForWidth(self.config_comb_btn.sizePolicy().hasHeightForWidth())
        self.config_comb_btn.setSizePolicy(sizePolicy)
        self.config_comb_btn.setMaximumSize(QSize(150, 80))
        self.config_comb_btn.setFont(font2)
        self.config_comb_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.config_comb_btn)

        self.config_user_btn = QPushButton(self.config_main)
        self.config_user_btn.setObjectName(u"config_user_btn")
        self.config_user_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.config_user_btn.sizePolicy().hasHeightForWidth())
        self.config_user_btn.setSizePolicy(sizePolicy)
        self.config_user_btn.setMaximumSize(QSize(150, 80))
        self.config_user_btn.setFont(font2)
        self.config_user_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}")

        self.horizontalLayout_19.addWidget(self.config_user_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.stackedWidget_12.addWidget(self.config_main)
        self.config_combustivel = QWidget()
        self.config_combustivel.setObjectName(u"config_combustivel")
        self.horizontalLayout_20 = QHBoxLayout(self.config_combustivel)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.config_comb_voltar = QPushButton(self.config_combustivel)
        self.config_comb_voltar.setObjectName(u"config_comb_voltar")
        sizePolicy.setHeightForWidth(self.config_comb_voltar.sizePolicy().hasHeightForWidth())
        self.config_comb_voltar.setSizePolicy(sizePolicy)
        self.config_comb_voltar.setMaximumSize(QSize(90, 80))
        self.config_comb_voltar.setFont(font2)
        self.config_comb_voltar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"	padding: 15px;\n"
"	image: url(:/icons/img04.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.config_comb_voltar)

        self.config_comb_editar = QPushButton(self.config_combustivel)
        self.config_comb_editar.setObjectName(u"config_comb_editar")
        sizePolicy.setHeightForWidth(self.config_comb_editar.sizePolicy().hasHeightForWidth())
        self.config_comb_editar.setSizePolicy(sizePolicy)
        self.config_comb_editar.setMaximumSize(QSize(150, 80))
        self.config_comb_editar.setFont(font2)
        self.config_comb_editar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.config_comb_editar)

        self.config_comb_info_2 = QPushButton(self.config_combustivel)
        self.config_comb_info_2.setObjectName(u"config_comb_info_2")
        sizePolicy.setHeightForWidth(self.config_comb_info_2.sizePolicy().hasHeightForWidth())
        self.config_comb_info_2.setSizePolicy(sizePolicy)
        self.config_comb_info_2.setMaximumSize(QSize(150, 80))
        self.config_comb_info_2.setFont(font2)
        self.config_comb_info_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.config_comb_info_2)

        self.config_comb_entrada = QPushButton(self.config_combustivel)
        self.config_comb_entrada.setObjectName(u"config_comb_entrada")
        sizePolicy.setHeightForWidth(self.config_comb_entrada.sizePolicy().hasHeightForWidth())
        self.config_comb_entrada.setSizePolicy(sizePolicy)
        self.config_comb_entrada.setMaximumSize(QSize(150, 80))
        self.config_comb_entrada.setFont(font2)
        self.config_comb_entrada.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.config_comb_entrada)

        self.horizontalSpacer_9 = QSpacerItem(785, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.stackedWidget_12.addWidget(self.config_combustivel)
        self.config_usuario = QWidget()
        self.config_usuario.setObjectName(u"config_usuario")
        self.horizontalLayout_22 = QHBoxLayout(self.config_usuario)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.config_user_voltar = QPushButton(self.config_usuario)
        self.config_user_voltar.setObjectName(u"config_user_voltar")
        sizePolicy.setHeightForWidth(self.config_user_voltar.sizePolicy().hasHeightForWidth())
        self.config_user_voltar.setSizePolicy(sizePolicy)
        self.config_user_voltar.setMaximumSize(QSize(90, 80))
        self.config_user_voltar.setFont(font2)
        self.config_user_voltar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	padding: 15px;\n"
"	image: url(:/icons/img04.png);\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.config_user_voltar)

        self.config_user_novo_btn = QPushButton(self.config_usuario)
        self.config_user_novo_btn.setObjectName(u"config_user_novo_btn")
        sizePolicy.setHeightForWidth(self.config_user_novo_btn.sizePolicy().hasHeightForWidth())
        self.config_user_novo_btn.setSizePolicy(sizePolicy)
        self.config_user_novo_btn.setMaximumSize(QSize(90, 80))
        self.config_user_novo_btn.setFont(font2)
        self.config_user_novo_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.config_user_novo_btn)

        self.config_user_lista_2 = QPushButton(self.config_usuario)
        self.config_user_lista_2.setObjectName(u"config_user_lista_2")
        sizePolicy.setHeightForWidth(self.config_user_lista_2.sizePolicy().hasHeightForWidth())
        self.config_user_lista_2.setSizePolicy(sizePolicy)
        self.config_user_lista_2.setMaximumSize(QSize(90, 80))
        self.config_user_lista_2.setFont(font2)
        self.config_user_lista_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.config_user_lista_2)

        self.horizontalSpacer_10 = QSpacerItem(785, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_10)

        self.stackedWidget_12.addWidget(self.config_usuario)

        self.gridLayout_40.addWidget(self.stackedWidget_12, 1, 0, 1, 3)


        self.gridLayout_42.addWidget(self.frame_32, 0, 0, 1, 1)

        self.stackedWidget_10 = QStackedWidget(self.Configuracao)
        self.stackedWidget_10.setObjectName(u"stackedWidget_10")
        self.stackedWidget_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.usuarios = QWidget()
        self.usuarios.setObjectName(u"usuarios")
        self.gridLayout_47 = QGridLayout(self.usuarios)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_13 = QStackedWidget(self.usuarios)
        self.stackedWidget_13.setObjectName(u"stackedWidget_13")
        self.config_user_home = QWidget()
        self.config_user_home.setObjectName(u"config_user_home")
        self.stackedWidget_13.addWidget(self.config_user_home)
        self.config_user_novo = QWidget()
        self.config_user_novo.setObjectName(u"config_user_novo")
        self.stackedWidget_13.addWidget(self.config_user_novo)
        self.config_user_lista = QWidget()
        self.config_user_lista.setObjectName(u"config_user_lista")
        self.stackedWidget_13.addWidget(self.config_user_lista)
        self.config_user_editar = QWidget()
        self.config_user_editar.setObjectName(u"config_user_editar")
        self.stackedWidget_13.addWidget(self.config_user_editar)

        self.gridLayout_47.addWidget(self.stackedWidget_13, 0, 0, 1, 1)

        self.stackedWidget_10.addWidget(self.usuarios)
        self.combustivel = QWidget()
        self.combustivel.setObjectName(u"combustivel")
        self.gridLayout_44 = QGridLayout(self.combustivel)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_11 = QStackedWidget(self.combustivel)
        self.stackedWidget_11.setObjectName(u"stackedWidget_11")
        self.config_comb_info = QWidget()
        self.config_comb_info.setObjectName(u"config_comb_info")
        self.gridLayout_50 = QGridLayout(self.config_comb_info)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.config_comb_info)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFont(font2)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_38)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_95 = QLabel(self.frame_38)
        self.label_95.setObjectName(u"label_95")
        sizePolicy2.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy2)
        self.label_95.setMaximumSize(QSize(90, 30))
        self.label_95.setFont(font2)
        self.label_95.setStyleSheet(u"border: none;")

        self.gridLayout_49.addWidget(self.label_95, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_49.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_38)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(550, 100))
        self.groupBox_6.setFont(font7)
        self.horizontalLayout_23 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_97 = QLabel(self.groupBox_6)
        self.label_97.setObjectName(u"label_97")
        sizePolicy2.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy2)
        self.label_97.setMaximumSize(QSize(120, 30))
        self.label_97.setFont(font2)
        self.label_97.setStyleSheet(u"border: none;")

        self.horizontalLayout_23.addWidget(self.label_97)

        self.config_comb_edit_combustivel_3 = QComboBox(self.groupBox_6)
        self.config_comb_edit_combustivel_3.addItem("")
        self.config_comb_edit_combustivel_3.setObjectName(u"config_comb_edit_combustivel_3")
        sizePolicy.setHeightForWidth(self.config_comb_edit_combustivel_3.sizePolicy().hasHeightForWidth())
        self.config_comb_edit_combustivel_3.setSizePolicy(sizePolicy)
        self.config_comb_edit_combustivel_3.setMaximumSize(QSize(200, 30))
        self.config_comb_edit_combustivel_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.config_comb_edit_combustivel_3.setEditable(True)

        self.horizontalLayout_23.addWidget(self.config_comb_edit_combustivel_3)

        self.label_94 = QLabel(self.groupBox_6)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMaximumSize(QSize(150, 30))
        self.label_94.setFont(font2)
        self.label_94.setStyleSheet(u"border: none;")

        self.horizontalLayout_23.addWidget(self.label_94)

        self.config_comb_edit_novo_3 = QLineEdit(self.groupBox_6)
        self.config_comb_edit_novo_3.setObjectName(u"config_comb_edit_novo_3")
        self.config_comb_edit_novo_3.setEnabled(True)
        self.config_comb_edit_novo_3.setMaximumSize(QSize(150, 25))
        self.config_comb_edit_novo_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.config_comb_edit_novo_3.setFrame(False)
        self.config_comb_edit_novo_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_comb_edit_novo_3.setDragEnabled(False)
        self.config_comb_edit_novo_3.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.config_comb_edit_novo_3)


        self.gridLayout_49.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.label_109 = QLabel(self.frame_38)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMaximumSize(QSize(16777215, 30))
        self.label_109.setFont(font2)
        self.label_109.setStyleSheet(u"border: none;")

        self.gridLayout_49.addWidget(self.label_109, 3, 3, 1, 1)

        self.label_92 = QLabel(self.frame_38)
        self.label_92.setObjectName(u"label_92")
        sizePolicy2.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy2)
        self.label_92.setMaximumSize(QSize(90, 30))
        self.label_92.setFont(font2)
        self.label_92.setStyleSheet(u"border: none;")

        self.gridLayout_49.addWidget(self.label_92, 2, 2, 1, 1)

        self.label_110 = QLabel(self.frame_38)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMaximumSize(QSize(16777215, 30))
        self.label_110.setFont(font2)
        self.label_110.setStyleSheet(u"border: none;")

        self.gridLayout_49.addWidget(self.label_110, 4, 3, 1, 1)

        self.groupBox_5 = QGroupBox(self.frame_38)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(550, 100))
        self.groupBox_5.setFont(font7)
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_96 = QLabel(self.groupBox_5)
        self.label_96.setObjectName(u"label_96")
        sizePolicy2.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy2)
        self.label_96.setMaximumSize(QSize(120, 30))
        self.label_96.setFont(font2)
        self.label_96.setStyleSheet(u"border: none;")

        self.horizontalLayout_21.addWidget(self.label_96)

        self.config_comb_edit_combustivel_2 = QComboBox(self.groupBox_5)
        self.config_comb_edit_combustivel_2.addItem("")
        self.config_comb_edit_combustivel_2.setObjectName(u"config_comb_edit_combustivel_2")
        sizePolicy.setHeightForWidth(self.config_comb_edit_combustivel_2.sizePolicy().hasHeightForWidth())
        self.config_comb_edit_combustivel_2.setSizePolicy(sizePolicy)
        self.config_comb_edit_combustivel_2.setMaximumSize(QSize(200, 30))
        self.config_comb_edit_combustivel_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.config_comb_edit_combustivel_2.setEditable(True)

        self.horizontalLayout_21.addWidget(self.config_comb_edit_combustivel_2)

        self.label_93 = QLabel(self.groupBox_5)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMaximumSize(QSize(70, 30))
        self.label_93.setFont(font2)
        self.label_93.setStyleSheet(u"border: none;")

        self.horizontalLayout_21.addWidget(self.label_93)

        self.config_comb_edit_novo_2 = QLineEdit(self.groupBox_5)
        self.config_comb_edit_novo_2.setObjectName(u"config_comb_edit_novo_2")
        self.config_comb_edit_novo_2.setEnabled(True)
        self.config_comb_edit_novo_2.setMaximumSize(QSize(150, 25))
        self.config_comb_edit_novo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.config_comb_edit_novo_2.setFrame(False)
        self.config_comb_edit_novo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_comb_edit_novo_2.setDragEnabled(False)
        self.config_comb_edit_novo_2.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.config_comb_edit_novo_2)


        self.gridLayout_49.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.gridLayout_50.addWidget(self.frame_38, 0, 0, 1, 1)

        self.stackedWidget_11.addWidget(self.config_comb_info)
        self.editar_combustivel = QWidget()
        self.editar_combustivel.setObjectName(u"editar_combustivel")
        self.gridLayout_45 = QGridLayout(self.editar_combustivel)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_50 = QLabel(self.editar_combustivel)
        self.label_50.setObjectName(u"label_50")
        sizePolicy1.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy1)
        self.label_50.setMaximumSize(QSize(16777215, 40))
        self.label_50.setFont(font8)
        self.label_50.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.label_50, 0, 0, 1, 1)

        self.frame_34 = QFrame(self.editar_combustivel)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(600, 16777215))
        self.frame_34.setFont(font2)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_34)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_86 = QLabel(self.frame_34)
        self.label_86.setObjectName(u"label_86")
        sizePolicy2.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy2)
        self.label_86.setMaximumSize(QSize(90, 30))
        self.label_86.setFont(font2)
        self.label_86.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_86, 5, 3, 1, 1)

        self.label_91 = QLabel(self.frame_34)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMaximumSize(QSize(16777215, 30))
        self.label_91.setFont(font2)
        self.label_91.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_91, 3, 0, 1, 1)

        self.label_105 = QLabel(self.frame_34)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(16777215, 30))
        self.label_105.setFont(font2)
        self.label_105.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_105, 6, 4, 1, 1)

        self.config_comb_edit_antigo = QLineEdit(self.frame_34)
        self.config_comb_edit_antigo.setObjectName(u"config_comb_edit_antigo")
        self.config_comb_edit_antigo.setEnabled(True)
        self.config_comb_edit_antigo.setMaximumSize(QSize(16777215, 25))
        self.config_comb_edit_antigo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.config_comb_edit_antigo.setFrame(False)
        self.config_comb_edit_antigo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_comb_edit_antigo.setDragEnabled(False)
        self.config_comb_edit_antigo.setReadOnly(True)

        self.gridLayout_43.addWidget(self.config_comb_edit_antigo, 1, 2, 1, 3)

        self.config_comb_edit_btn = QPushButton(self.frame_34)
        self.config_comb_edit_btn.setObjectName(u"config_comb_edit_btn")
        sizePolicy3.setHeightForWidth(self.config_comb_edit_btn.sizePolicy().hasHeightForWidth())
        self.config_comb_edit_btn.setSizePolicy(sizePolicy3)
        self.config_comb_edit_btn.setMaximumSize(QSize(9999999, 30))
        self.config_comb_edit_btn.setFont(font2)
        self.config_comb_edit_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_43.addWidget(self.config_comb_edit_btn, 4, 2, 1, 3)

        self.label_106 = QLabel(self.frame_34)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(16777215, 30))
        self.label_106.setFont(font2)
        self.label_106.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_106, 7, 4, 1, 1)

        self.label_85 = QLabel(self.frame_34)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(16777215, 30))
        self.label_85.setFont(font2)
        self.label_85.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_85, 1, 0, 1, 1)

        self.label_82 = QLabel(self.frame_34)
        self.label_82.setObjectName(u"label_82")
        sizePolicy2.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy2)
        self.label_82.setMaximumSize(QSize(90, 30))
        self.label_82.setFont(font2)
        self.label_82.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_82, 5, 2, 1, 1)

        self.config_comb_edit_combustivel = QComboBox(self.frame_34)
        self.config_comb_edit_combustivel.addItem("")
        self.config_comb_edit_combustivel.setObjectName(u"config_comb_edit_combustivel")
        self.config_comb_edit_combustivel.setMaximumSize(QSize(16777215, 30))
        self.config_comb_edit_combustivel.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.config_comb_edit_combustivel.setEditable(True)

        self.gridLayout_43.addWidget(self.config_comb_edit_combustivel, 0, 2, 1, 3)

        self.label_79 = QLabel(self.frame_34)
        self.label_79.setObjectName(u"label_79")
        sizePolicy2.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy2)
        self.label_79.setMaximumSize(QSize(120, 30))
        self.label_79.setFont(font2)
        self.label_79.setStyleSheet(u"border: none;")

        self.gridLayout_43.addWidget(self.label_79, 0, 0, 1, 1)

        self.config_comb_edit_novo = QLineEdit(self.frame_34)
        self.config_comb_edit_novo.setObjectName(u"config_comb_edit_novo")
        self.config_comb_edit_novo.setEnabled(True)
        self.config_comb_edit_novo.setMaximumSize(QSize(16777215, 25))
        self.config_comb_edit_novo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.config_comb_edit_novo.setFrame(False)
        self.config_comb_edit_novo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_comb_edit_novo.setDragEnabled(False)
        self.config_comb_edit_novo.setReadOnly(False)

        self.gridLayout_43.addWidget(self.config_comb_edit_novo, 3, 2, 1, 3)


        self.gridLayout_45.addWidget(self.frame_34, 1, 0, 1, 1)

        self.stackedWidget_11.addWidget(self.editar_combustivel)
        self.entrada_combustivel = QWidget()
        self.entrada_combustivel.setObjectName(u"entrada_combustivel")
        self.gridLayout_82 = QGridLayout(self.entrada_combustivel)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.label_55 = QLabel(self.entrada_combustivel)
        self.label_55.setObjectName(u"label_55")
        sizePolicy1.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy1)
        self.label_55.setMaximumSize(QSize(16777215, 40))
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_82.addWidget(self.label_55, 0, 0, 1, 1)

        self.frame_42 = QFrame(self.entrada_combustivel)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(600, 16777215))
        self.frame_42.setFont(font2)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_76 = QGridLayout(self.frame_42)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.label_144 = QLabel(self.frame_42)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMaximumSize(QSize(16777215, 30))
        self.label_144.setFont(font2)
        self.label_144.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_144, 7, 0, 1, 1)

        self.label_113 = QLabel(self.frame_42)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMaximumSize(QSize(16777215, 30))
        self.label_113.setFont(font2)
        self.label_113.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_113, 12, 4, 1, 1)

        self.label_136 = QLabel(self.frame_42)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMaximumSize(QSize(16777215, 30))
        self.label_136.setFont(font2)
        self.label_136.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_136, 1, 0, 1, 1)

        self.label_141 = QLabel(self.frame_42)
        self.label_141.setObjectName(u"label_141")
        sizePolicy2.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy2)
        self.label_141.setMaximumSize(QSize(90, 30))
        self.label_141.setFont(font2)
        self.label_141.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_141, 10, 2, 1, 1)

        self.config_comb_entrada_combustivel = QComboBox(self.frame_42)
        self.config_comb_entrada_combustivel.addItem("")
        self.config_comb_entrada_combustivel.setObjectName(u"config_comb_entrada_combustivel")
        self.config_comb_entrada_combustivel.setMaximumSize(QSize(16777215, 30))
        self.config_comb_entrada_combustivel.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.config_comb_entrada_combustivel.setEditable(True)

        self.gridLayout_76.addWidget(self.config_comb_entrada_combustivel, 0, 2, 1, 3)

        self.label_143 = QLabel(self.frame_42)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMaximumSize(QSize(16777215, 30))
        self.label_143.setFont(font2)
        self.label_143.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_143, 4, 0, 1, 1)

        self.config_comb_entrada_valor = QLineEdit(self.frame_42)
        self.config_comb_entrada_valor.setObjectName(u"config_comb_entrada_valor")
        self.config_comb_entrada_valor.setEnabled(True)
        self.config_comb_entrada_valor.setMaximumSize(QSize(16777215, 25))
        self.config_comb_entrada_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.config_comb_entrada_valor.setFrame(False)
        self.config_comb_entrada_valor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_comb_entrada_valor.setDragEnabled(False)
        self.config_comb_entrada_valor.setReadOnly(False)

        self.gridLayout_76.addWidget(self.config_comb_entrada_valor, 3, 2, 1, 3)

        self.label_108 = QLabel(self.frame_42)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(16777215, 30))
        self.label_108.setFont(font2)
        self.label_108.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_108, 3, 0, 1, 1)

        self.config_comb_entrada_quantidade = QLineEdit(self.frame_42)
        self.config_comb_entrada_quantidade.setObjectName(u"config_comb_entrada_quantidade")
        self.config_comb_entrada_quantidade.setEnabled(True)
        self.config_comb_entrada_quantidade.setMaximumSize(QSize(16777215, 25))
        self.config_comb_entrada_quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.config_comb_entrada_quantidade.setFrame(False)
        self.config_comb_entrada_quantidade.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_comb_entrada_quantidade.setDragEnabled(False)
        self.config_comb_entrada_quantidade.setReadOnly(False)

        self.gridLayout_76.addWidget(self.config_comb_entrada_quantidade, 1, 2, 1, 3)

        self.config_comb_entrada_parcelamento = QComboBox(self.frame_42)
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.addItem("")
        self.config_comb_entrada_parcelamento.setObjectName(u"config_comb_entrada_parcelamento")
        self.config_comb_entrada_parcelamento.setMaximumSize(QSize(16777215, 30))
        self.config_comb_entrada_parcelamento.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"padding-left: 20px;\n"
"")
        self.config_comb_entrada_parcelamento.setEditable(True)

        self.gridLayout_76.addWidget(self.config_comb_entrada_parcelamento, 7, 2, 1, 2)

        self.config_comb_edit_btn_2 = QPushButton(self.frame_42)
        self.config_comb_edit_btn_2.setObjectName(u"config_comb_edit_btn_2")
        sizePolicy3.setHeightForWidth(self.config_comb_edit_btn_2.sizePolicy().hasHeightForWidth())
        self.config_comb_edit_btn_2.setSizePolicy(sizePolicy3)
        self.config_comb_edit_btn_2.setMaximumSize(QSize(9999999, 30))
        self.config_comb_edit_btn_2.setFont(font2)
        self.config_comb_edit_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_76.addWidget(self.config_comb_edit_btn_2, 9, 2, 1, 3)

        self.label_88 = QLabel(self.frame_42)
        self.label_88.setObjectName(u"label_88")
        sizePolicy2.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy2)
        self.label_88.setMaximumSize(QSize(90, 30))
        self.label_88.setFont(font2)
        self.label_88.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_88, 10, 3, 1, 1)

        self.label_112 = QLabel(self.frame_42)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMaximumSize(QSize(16777215, 30))
        self.label_112.setFont(font2)
        self.label_112.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_112, 11, 4, 1, 1)

        self.label_142 = QLabel(self.frame_42)
        self.label_142.setObjectName(u"label_142")
        sizePolicy2.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy2)
        self.label_142.setMaximumSize(QSize(120, 30))
        self.label_142.setFont(font2)
        self.label_142.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_142, 0, 0, 1, 1)

        self.config_comb_entrada_data = QDateEdit(self.frame_42)
        self.config_comb_entrada_data.setObjectName(u"config_comb_entrada_data")
        sizePolicy4.setHeightForWidth(self.config_comb_entrada_data.sizePolicy().hasHeightForWidth())
        self.config_comb_entrada_data.setSizePolicy(sizePolicy4)
        self.config_comb_entrada_data.setMaximumSize(QSize(16777215, 40))
        self.config_comb_entrada_data.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.config_comb_entrada_data.setCalendarPopup(True)
        self.config_comb_entrada_data.setDate(QDate(2021, 1, 1))

        self.gridLayout_76.addWidget(self.config_comb_entrada_data, 4, 2, 1, 2)

        self.label_146 = QLabel(self.frame_42)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMaximumSize(QSize(16777215, 30))
        self.label_146.setFont(font2)
        self.label_146.setStyleSheet(u"border: none;")

        self.gridLayout_76.addWidget(self.label_146, 5, 0, 1, 1)

        self.config_comb_entrada_vencimento = QDateEdit(self.frame_42)
        self.config_comb_entrada_vencimento.setObjectName(u"config_comb_entrada_vencimento")
        sizePolicy4.setHeightForWidth(self.config_comb_entrada_vencimento.sizePolicy().hasHeightForWidth())
        self.config_comb_entrada_vencimento.setSizePolicy(sizePolicy4)
        self.config_comb_entrada_vencimento.setMaximumSize(QSize(16777215, 40))
        self.config_comb_entrada_vencimento.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.config_comb_entrada_vencimento.setCalendarPopup(True)
        self.config_comb_entrada_vencimento.setDate(QDate(2021, 1, 1))

        self.gridLayout_76.addWidget(self.config_comb_entrada_vencimento, 5, 2, 1, 2)


        self.gridLayout_82.addWidget(self.frame_42, 1, 0, 1, 1)

        self.stackedWidget_11.addWidget(self.entrada_combustivel)
        self.home_combustivel = QWidget()
        self.home_combustivel.setObjectName(u"home_combustivel")
        self.stackedWidget_11.addWidget(self.home_combustivel)

        self.gridLayout_44.addWidget(self.stackedWidget_11, 0, 0, 1, 1)

        self.stackedWidget_10.addWidget(self.combustivel)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.stackedWidget_10.addWidget(self.home)

        self.gridLayout_42.addWidget(self.stackedWidget_10, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.Configuracao)
        self.Estoque = QWidget()
        self.Estoque.setObjectName(u"Estoque")
        self.verticalLayout_3 = QVBoxLayout(self.Estoque)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_15 = QFrame(self.Estoque)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 120))
        self.frame_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"border-radius: 5px 5px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_15)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(0)
        self.gridLayout_25.setVerticalSpacing(6)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: white;\n"
"border-bottom: 1px solid rgb(166, 166, 166);\n"
"border-radius: none;\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_18)
        self.gridLayout_26.setSpacing(1)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(1, 1, 1, 1)
        self.cons_lb_2 = QLabel(self.frame_18)
        self.cons_lb_2.setObjectName(u"cons_lb_2")
        sizePolicy1.setHeightForWidth(self.cons_lb_2.sizePolicy().hasHeightForWidth())
        self.cons_lb_2.setSizePolicy(sizePolicy1)
        self.cons_lb_2.setMaximumSize(QSize(155, 70))
        self.cons_lb_2.setFont(font8)
        self.cons_lb_2.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.cons_lb_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.cons_lb_2, 0, 0, 1, 1)

        self.est_lb_nav = QLabel(self.frame_18)
        self.est_lb_nav.setObjectName(u"est_lb_nav")
        sizePolicy1.setHeightForWidth(self.est_lb_nav.sizePolicy().hasHeightForWidth())
        self.est_lb_nav.setSizePolicy(sizePolicy1)
        self.est_lb_nav.setMaximumSize(QSize(16777215, 70))
        self.est_lb_nav.setFont(font8)
        self.est_lb_nav.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.est_lb_nav.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.est_lb_nav, 0, 1, 1, 1)


        self.gridLayout_25.addWidget(self.frame_18, 0, 0, 1, 4)

        self.est_btn_entrada = QPushButton(self.frame_15)
        self.est_btn_entrada.setObjectName(u"est_btn_entrada")
        self.est_btn_entrada.setEnabled(True)
        sizePolicy.setHeightForWidth(self.est_btn_entrada.sizePolicy().hasHeightForWidth())
        self.est_btn_entrada.setSizePolicy(sizePolicy)
        self.est_btn_entrada.setMaximumSize(QSize(90, 50))
        self.est_btn_entrada.setFont(font2)
        self.est_btn_entrada.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.est_btn_entrada, 1, 1, 1, 1)

        self.est_btn_novo = QPushButton(self.frame_15)
        self.est_btn_novo.setObjectName(u"est_btn_novo")
        sizePolicy.setHeightForWidth(self.est_btn_novo.sizePolicy().hasHeightForWidth())
        self.est_btn_novo.setSizePolicy(sizePolicy)
        self.est_btn_novo.setMaximumSize(QSize(90, 50))
        self.est_btn_novo.setFont(font2)
        self.est_btn_novo.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.est_btn_novo, 1, 0, 1, 1)

        self.est_btn_consulta = QPushButton(self.frame_15)
        self.est_btn_consulta.setObjectName(u"est_btn_consulta")
        self.est_btn_consulta.setEnabled(True)
        sizePolicy.setHeightForWidth(self.est_btn_consulta.sizePolicy().hasHeightForWidth())
        self.est_btn_consulta.setSizePolicy(sizePolicy)
        self.est_btn_consulta.setMaximumSize(QSize(90, 50))
        self.est_btn_consulta.setFont(font2)
        self.est_btn_consulta.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.est_btn_consulta, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.stackedWidget_7 = QStackedWidget(self.Estoque)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.stackedWidget_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget_7.addWidget(self.page_3)
        self.novo_produto = QWidget()
        self.novo_produto.setObjectName(u"novo_produto")
        self.gridLayout_28 = QGridLayout(self.novo_produto)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_26 = QLabel(self.novo_produto)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setMaximumSize(QSize(16777215, 40))
        self.label_26.setFont(font8)
        self.label_26.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.label_26, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.novo_produto)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(600, 16777215))
        self.frame_22.setFont(font2)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_22)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_70 = QLabel(self.frame_22)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 30))
        self.label_70.setFont(font2)
        self.label_70.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_70, 7, 0, 1, 1)

        self.label_75 = QLabel(self.frame_22)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(16777215, 30))
        self.label_75.setFont(font2)
        self.label_75.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_75, 5, 0, 1, 1)

        self.ln_est_produto = QLineEdit(self.frame_22)
        self.ln_est_produto.setObjectName(u"ln_est_produto")
        self.ln_est_produto.setEnabled(True)
        self.ln_est_produto.setMaximumSize(QSize(16777215, 25))
        self.ln_est_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_est_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ln_est_produto.setDragEnabled(True)
        self.ln_est_produto.setReadOnly(False)

        self.gridLayout_34.addWidget(self.ln_est_produto, 2, 1, 1, 3)

        self.label_69 = QLabel(self.frame_22)
        self.label_69.setObjectName(u"label_69")
        sizePolicy2.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy2)
        self.label_69.setMaximumSize(QSize(90, 30))
        self.label_69.setFont(font2)
        self.label_69.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_69, 9, 1, 1, 1)

        self.ln_est_pVenda = QLineEdit(self.frame_22)
        self.ln_est_pVenda.setObjectName(u"ln_est_pVenda")
        self.ln_est_pVenda.setEnabled(True)
        self.ln_est_pVenda.setMaximumSize(QSize(16777215, 25))
        self.ln_est_pVenda.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_est_pVenda.setFrame(False)
        self.ln_est_pVenda.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ln_est_pVenda.setDragEnabled(True)
        self.ln_est_pVenda.setReadOnly(False)

        self.gridLayout_34.addWidget(self.ln_est_pVenda, 6, 1, 1, 3)

        self.btn_est_cadastrar = QPushButton(self.frame_22)
        self.btn_est_cadastrar.setObjectName(u"btn_est_cadastrar")
        sizePolicy3.setHeightForWidth(self.btn_est_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_est_cadastrar.setSizePolicy(sizePolicy3)
        self.btn_est_cadastrar.setMaximumSize(QSize(9999999, 30))
        self.btn_est_cadastrar.setFont(font2)
        self.btn_est_cadastrar.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_34.addWidget(self.btn_est_cadastrar, 9, 3, 1, 1)

        self.label_71 = QLabel(self.frame_22)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(16777215, 30))
        self.label_71.setFont(font2)
        self.label_71.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_71, 1, 0, 1, 1)

        self.est_cb_tipo = QComboBox(self.frame_22)
        self.est_cb_tipo.addItem("")
        self.est_cb_tipo.setObjectName(u"est_cb_tipo")
        self.est_cb_tipo.setMaximumSize(QSize(16777215, 30))
        self.est_cb_tipo.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_cb_tipo.setEditable(True)

        self.gridLayout_34.addWidget(self.est_cb_tipo, 0, 1, 1, 3)

        self.ln_est_qnt = QLineEdit(self.frame_22)
        self.ln_est_qnt.setObjectName(u"ln_est_qnt")
        self.ln_est_qnt.setEnabled(True)
        self.ln_est_qnt.setMaximumSize(QSize(16777215, 25))
        self.ln_est_qnt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_est_qnt.setFrame(False)
        self.ln_est_qnt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ln_est_qnt.setDragEnabled(True)
        self.ln_est_qnt.setReadOnly(False)

        self.gridLayout_34.addWidget(self.ln_est_qnt, 7, 1, 1, 3)

        self.ln_est_pCompra = QLineEdit(self.frame_22)
        self.ln_est_pCompra.setObjectName(u"ln_est_pCompra")
        self.ln_est_pCompra.setEnabled(True)
        self.ln_est_pCompra.setMaximumSize(QSize(16777215, 25))
        self.ln_est_pCompra.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_est_pCompra.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ln_est_pCompra.setDragEnabled(True)
        self.ln_est_pCompra.setReadOnly(False)

        self.gridLayout_34.addWidget(self.ln_est_pCompra, 5, 1, 1, 3)

        self.est_cb_marca = QComboBox(self.frame_22)
        self.est_cb_marca.addItem("")
        self.est_cb_marca.setObjectName(u"est_cb_marca")
        sizePolicy1.setHeightForWidth(self.est_cb_marca.sizePolicy().hasHeightForWidth())
        self.est_cb_marca.setSizePolicy(sizePolicy1)
        self.est_cb_marca.setMaximumSize(QSize(16777215, 30))
        self.est_cb_marca.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_cb_marca.setEditable(True)

        self.gridLayout_34.addWidget(self.est_cb_marca, 1, 1, 1, 3)

        self.label_68 = QLabel(self.frame_22)
        self.label_68.setObjectName(u"label_68")
        sizePolicy2.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy2)
        self.label_68.setMaximumSize(QSize(90, 30))
        self.label_68.setFont(font2)
        self.label_68.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_68, 9, 2, 1, 1)

        self.label_73 = QLabel(self.frame_22)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(16777215, 30))
        self.label_73.setFont(font2)
        self.label_73.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_73, 8, 0, 1, 1)

        self.label_77 = QLabel(self.frame_22)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(16777215, 30))
        self.label_77.setFont(font2)
        self.label_77.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_77, 0, 0, 1, 1)

        self.ln_est_codBarras = QLineEdit(self.frame_22)
        self.ln_est_codBarras.setObjectName(u"ln_est_codBarras")
        self.ln_est_codBarras.setEnabled(True)
        self.ln_est_codBarras.setMaximumSize(QSize(16777215, 25))
        self.ln_est_codBarras.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.ln_est_codBarras.setFrame(False)
        self.ln_est_codBarras.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ln_est_codBarras.setDragEnabled(True)
        self.ln_est_codBarras.setReadOnly(False)

        self.gridLayout_34.addWidget(self.ln_est_codBarras, 8, 1, 1, 3)

        self.label_72 = QLabel(self.frame_22)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(16777215, 30))
        self.label_72.setFont(font2)
        self.label_72.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_72, 2, 0, 1, 1)

        self.label_76 = QLabel(self.frame_22)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 30))
        self.label_76.setFont(font2)
        self.label_76.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_76, 6, 0, 1, 1)

        self.label_74 = QLabel(self.frame_22)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(16777215, 30))
        self.label_74.setFont(font2)
        self.label_74.setStyleSheet(u"border: none;")

        self.gridLayout_34.addWidget(self.label_74, 3, 0, 1, 1)

        self.est_cb_unidade = QComboBox(self.frame_22)
        self.est_cb_unidade.addItem("")
        self.est_cb_unidade.addItem("")
        self.est_cb_unidade.addItem("")
        self.est_cb_unidade.addItem("")
        self.est_cb_unidade.addItem("")
        self.est_cb_unidade.setObjectName(u"est_cb_unidade")
        sizePolicy1.setHeightForWidth(self.est_cb_unidade.sizePolicy().hasHeightForWidth())
        self.est_cb_unidade.setSizePolicy(sizePolicy1)
        self.est_cb_unidade.setMaximumSize(QSize(16777215, 30))
        self.est_cb_unidade.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_cb_unidade.setEditable(True)

        self.gridLayout_34.addWidget(self.est_cb_unidade, 3, 1, 1, 3)


        self.gridLayout_28.addWidget(self.frame_22, 1, 0, 1, 1)

        self.stackedWidget_7.addWidget(self.novo_produto)
        self.entrada_produto = QWidget()
        self.entrada_produto.setObjectName(u"entrada_produto")
        self.gridLayout_29 = QGridLayout(self.entrada_produto)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_36 = QLabel(self.entrada_produto)
        self.label_36.setObjectName(u"label_36")
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)
        self.label_36.setMaximumSize(QSize(16777215, 40))
        self.label_36.setFont(font8)
        self.label_36.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_36, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.entrada_produto)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(600, 16777215))
        self.frame_23.setFont(font2)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_23)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_81 = QLabel(self.frame_23)
        self.label_81.setObjectName(u"label_81")
        sizePolicy2.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy2)
        self.label_81.setMaximumSize(QSize(90, 30))
        self.label_81.setFont(font2)
        self.label_81.setStyleSheet(u"border: none;")

        self.gridLayout_35.addWidget(self.label_81, 2, 1, 1, 1)

        self.est_new_cb_produto = QComboBox(self.frame_23)
        self.est_new_cb_produto.addItem("")
        self.est_new_cb_produto.setObjectName(u"est_new_cb_produto")
        self.est_new_cb_produto.setMaximumSize(QSize(16777215, 30))
        self.est_new_cb_produto.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_new_cb_produto.setEditable(True)

        self.gridLayout_35.addWidget(self.est_new_cb_produto, 0, 1, 1, 3)

        self.est_new_ln_qnt = QLineEdit(self.frame_23)
        self.est_new_ln_qnt.setObjectName(u"est_new_ln_qnt")
        self.est_new_ln_qnt.setEnabled(True)
        self.est_new_ln_qnt.setMaximumSize(QSize(16777215, 25))
        self.est_new_ln_qnt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.est_new_ln_qnt.setFrame(False)
        self.est_new_ln_qnt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.est_new_ln_qnt.setDragEnabled(True)
        self.est_new_ln_qnt.setReadOnly(False)

        self.gridLayout_35.addWidget(self.est_new_ln_qnt, 1, 1, 1, 3)

        self.label_84 = QLabel(self.frame_23)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMaximumSize(QSize(16777215, 30))
        self.label_84.setFont(font2)
        self.label_84.setStyleSheet(u"border: none;")

        self.gridLayout_35.addWidget(self.label_84, 1, 0, 1, 1)

        self.label_103 = QLabel(self.frame_23)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(16777215, 30))
        self.label_103.setFont(font2)
        self.label_103.setStyleSheet(u"border: none;")

        self.gridLayout_35.addWidget(self.label_103, 3, 3, 1, 1)

        self.est_new_btn_cadastrar = QPushButton(self.frame_23)
        self.est_new_btn_cadastrar.setObjectName(u"est_new_btn_cadastrar")
        sizePolicy3.setHeightForWidth(self.est_new_btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.est_new_btn_cadastrar.setSizePolicy(sizePolicy3)
        self.est_new_btn_cadastrar.setMaximumSize(QSize(9999999, 30))
        self.est_new_btn_cadastrar.setFont(font2)
        self.est_new_btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_35.addWidget(self.est_new_btn_cadastrar, 2, 3, 1, 1)

        self.label_83 = QLabel(self.frame_23)
        self.label_83.setObjectName(u"label_83")
        sizePolicy2.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy2)
        self.label_83.setMaximumSize(QSize(90, 30))
        self.label_83.setFont(font2)
        self.label_83.setStyleSheet(u"border: none;")

        self.gridLayout_35.addWidget(self.label_83, 2, 2, 1, 1)

        self.label_78 = QLabel(self.frame_23)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(16777215, 30))
        self.label_78.setFont(font2)
        self.label_78.setStyleSheet(u"border: none;")

        self.gridLayout_35.addWidget(self.label_78, 0, 0, 1, 1)

        self.label_104 = QLabel(self.frame_23)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMaximumSize(QSize(16777215, 30))
        self.label_104.setFont(font2)
        self.label_104.setStyleSheet(u"border: none;")

        self.gridLayout_35.addWidget(self.label_104, 4, 3, 1, 1)


        self.gridLayout_29.addWidget(self.frame_23, 1, 0, 1, 1)

        self.stackedWidget_7.addWidget(self.entrada_produto)
        self.consultar_estoque = QWidget()
        self.consultar_estoque.setObjectName(u"consultar_estoque")
        self.gridLayout_30 = QGridLayout(self.consultar_estoque)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.frame_19 = QFrame(self.consultar_estoque)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_19)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(80, 16777215))
        self.label_37.setFont(font6)
        self.label_37.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_37)

        self.est_const_cb_filtro = QComboBox(self.frame_19)
        self.est_const_cb_filtro.addItem("")
        self.est_const_cb_filtro.addItem("")
        self.est_const_cb_filtro.addItem("")
        self.est_const_cb_filtro.addItem("")
        self.est_const_cb_filtro.addItem("")
        self.est_const_cb_filtro.setObjectName(u"est_const_cb_filtro")
        sizePolicy3.setHeightForWidth(self.est_const_cb_filtro.sizePolicy().hasHeightForWidth())
        self.est_const_cb_filtro.setSizePolicy(sizePolicy3)
        self.est_const_cb_filtro.setMaximumSize(QSize(100, 16777215))
        self.est_const_cb_filtro.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout_10.addWidget(self.est_const_cb_filtro)

        self.est_const_ln_filtro = QLineEdit(self.frame_19)
        self.est_const_ln_filtro.setObjectName(u"est_const_ln_filtro")
        self.est_const_ln_filtro.setEnabled(True)
        self.est_const_ln_filtro.setMaximumSize(QSize(16777215, 20))
        self.est_const_ln_filtro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(90, 90, 90)")
        self.est_const_ln_filtro.setMaxLength(9999)
        self.est_const_ln_filtro.setAlignment(Qt.AlignCenter)
        self.est_const_ln_filtro.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.est_const_ln_filtro)

        self.est_const_btn_pesquisar = QPushButton(self.frame_19)
        self.est_const_btn_pesquisar.setObjectName(u"est_const_btn_pesquisar")
        self.est_const_btn_pesquisar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.est_const_btn_pesquisar.sizePolicy().hasHeightForWidth())
        self.est_const_btn_pesquisar.setSizePolicy(sizePolicy)
        self.est_const_btn_pesquisar.setMaximumSize(QSize(80, 28))
        self.est_const_btn_pesquisar.setFont(font2)
        self.est_const_btn_pesquisar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.est_const_btn_pesquisar)

        self.est_const_btn_editar = QPushButton(self.frame_19)
        self.est_const_btn_editar.setObjectName(u"est_const_btn_editar")
        self.est_const_btn_editar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.est_const_btn_editar.sizePolicy().hasHeightForWidth())
        self.est_const_btn_editar.setSizePolicy(sizePolicy)
        self.est_const_btn_editar.setMaximumSize(QSize(60, 28))
        self.est_const_btn_editar.setFont(font2)
        self.est_const_btn_editar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.est_const_btn_editar)

        self.est_const_btn_deletar = QPushButton(self.frame_19)
        self.est_const_btn_deletar.setObjectName(u"est_const_btn_deletar")
        self.est_const_btn_deletar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.est_const_btn_deletar.sizePolicy().hasHeightForWidth())
        self.est_const_btn_deletar.setSizePolicy(sizePolicy)
        self.est_const_btn_deletar.setMaximumSize(QSize(60, 28))
        self.est_const_btn_deletar.setFont(font2)
        self.est_const_btn_deletar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166); \n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	color: white;\n"
"	border-radius: 10PX;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.est_const_btn_deletar)

        self.horizontalSpacer_6 = QSpacerItem(257, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.gridLayout_30.addWidget(self.frame_19, 0, 0, 1, 1)

        self.est_consult_tab = QTableWidget(self.consultar_estoque)
        if (self.est_consult_tab.columnCount() < 9):
            self.est_consult_tab.setColumnCount(9)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        font10 = QFont()
        font10.setPointSize(11)
        font10.setBold(False)
        font10.setWeight(50)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font10);
        self.est_consult_tab.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font7);
        self.est_consult_tab.setHorizontalHeaderItem(8, __qtablewidgetitem32)
        self.est_consult_tab.setObjectName(u"est_consult_tab")
        self.est_consult_tab.setEnabled(True)
        self.est_consult_tab.setFont(font6)
        self.est_consult_tab.setStyleSheet(u"QTableWidget{\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid rgba(68, 119, 170, 150);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 169, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 222, 90, 239), stop:1 rgba(255, 228, 117, 255));\n"
"	\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"}")
        self.est_consult_tab.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.est_consult_tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.est_consult_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.est_consult_tab.setTabKeyNavigation(True)
        self.est_consult_tab.setProperty("showDropIndicator", True)
        self.est_consult_tab.setDragEnabled(False)
        self.est_consult_tab.setDragDropOverwriteMode(True)
        self.est_consult_tab.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.est_consult_tab.setAlternatingRowColors(True)
        self.est_consult_tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.est_consult_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.est_consult_tab.setShowGrid(True)
        self.est_consult_tab.setGridStyle(Qt.SolidLine)
        self.est_consult_tab.setWordWrap(True)
        self.est_consult_tab.horizontalHeader().setVisible(False)
        self.est_consult_tab.horizontalHeader().setCascadingSectionResizes(False)
        self.est_consult_tab.horizontalHeader().setDefaultSectionSize(100)
        self.est_consult_tab.horizontalHeader().setHighlightSections(False)
        self.est_consult_tab.horizontalHeader().setProperty("showSortIndicator", False)
        self.est_consult_tab.horizontalHeader().setStretchLastSection(True)
        self.est_consult_tab.verticalHeader().setVisible(False)
        self.est_consult_tab.verticalHeader().setStretchLastSection(False)

        self.gridLayout_30.addWidget(self.est_consult_tab, 1, 0, 1, 1)

        self.stackedWidget_7.addWidget(self.consultar_estoque)
        self.editar_dados = QWidget()
        self.editar_dados.setObjectName(u"editar_dados")
        self.gridLayout_31 = QGridLayout(self.editar_dados)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_25 = QLabel(self.editar_dados)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setMaximumSize(QSize(16777215, 40))
        self.label_25.setFont(font8)
        self.label_25.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.label_25, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.editar_dados)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(600, 16777215))
        self.frame_21.setFont(font2)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_21)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.est_edt_ln_qnt = QLineEdit(self.frame_21)
        self.est_edt_ln_qnt.setObjectName(u"est_edt_ln_qnt")
        self.est_edt_ln_qnt.setEnabled(True)
        self.est_edt_ln_qnt.setMaximumSize(QSize(16777215, 25))
        self.est_edt_ln_qnt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.est_edt_ln_qnt.setFrame(False)
        self.est_edt_ln_qnt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.est_edt_ln_qnt.setDragEnabled(True)
        self.est_edt_ln_qnt.setReadOnly(False)

        self.gridLayout_32.addWidget(self.est_edt_ln_qnt, 6, 1, 1, 4)

        self.label_60 = QLabel(self.frame_21)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(16777215, 30))
        self.label_60.setFont(font2)
        self.label_60.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_60, 1, 0, 1, 1)

        self.label_66 = QLabel(self.frame_21)
        self.label_66.setObjectName(u"label_66")
        sizePolicy2.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy2)
        self.label_66.setMaximumSize(QSize(90, 30))
        self.label_66.setFont(font2)
        self.label_66.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_66, 8, 2, 1, 1)

        self.est_edt_ln_pCompra = QLineEdit(self.frame_21)
        self.est_edt_ln_pCompra.setObjectName(u"est_edt_ln_pCompra")
        self.est_edt_ln_pCompra.setEnabled(True)
        self.est_edt_ln_pCompra.setMaximumSize(QSize(16777215, 25))
        self.est_edt_ln_pCompra.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.est_edt_ln_pCompra.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.est_edt_ln_pCompra.setDragEnabled(True)
        self.est_edt_ln_pCompra.setReadOnly(False)

        self.gridLayout_32.addWidget(self.est_edt_ln_pCompra, 4, 1, 1, 4)

        self.label_64 = QLabel(self.frame_21)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 30))
        self.label_64.setFont(font2)
        self.label_64.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_64, 6, 0, 1, 1)

        self.est_edt_cb_marca = QComboBox(self.frame_21)
        self.est_edt_cb_marca.addItem("")
        self.est_edt_cb_marca.setObjectName(u"est_edt_cb_marca")
        sizePolicy1.setHeightForWidth(self.est_edt_cb_marca.sizePolicy().hasHeightForWidth())
        self.est_edt_cb_marca.setSizePolicy(sizePolicy1)
        self.est_edt_cb_marca.setMaximumSize(QSize(16777215, 30))
        self.est_edt_cb_marca.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_edt_cb_marca.setEditable(True)

        self.gridLayout_32.addWidget(self.est_edt_cb_marca, 1, 1, 1, 4)

        self.est_edt_btn_salvar = QPushButton(self.frame_21)
        self.est_edt_btn_salvar.setObjectName(u"est_edt_btn_salvar")
        sizePolicy3.setHeightForWidth(self.est_edt_btn_salvar.sizePolicy().hasHeightForWidth())
        self.est_edt_btn_salvar.setSizePolicy(sizePolicy3)
        self.est_edt_btn_salvar.setMaximumSize(QSize(90, 30))
        self.est_edt_btn_salvar.setFont(font2)
        self.est_edt_btn_salvar.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_32.addWidget(self.est_edt_btn_salvar, 8, 3, 1, 1)

        self.est_edt_ln_produto = QLineEdit(self.frame_21)
        self.est_edt_ln_produto.setObjectName(u"est_edt_ln_produto")
        self.est_edt_ln_produto.setEnabled(True)
        self.est_edt_ln_produto.setMaximumSize(QSize(16777215, 25))
        self.est_edt_ln_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.est_edt_ln_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.est_edt_ln_produto.setDragEnabled(True)
        self.est_edt_ln_produto.setReadOnly(False)

        self.gridLayout_32.addWidget(self.est_edt_ln_produto, 2, 1, 1, 4)

        self.est_edt_ln_codBarras = QLineEdit(self.frame_21)
        self.est_edt_ln_codBarras.setObjectName(u"est_edt_ln_codBarras")
        self.est_edt_ln_codBarras.setEnabled(True)
        self.est_edt_ln_codBarras.setMaximumSize(QSize(16777215, 25))
        self.est_edt_ln_codBarras.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.est_edt_ln_codBarras.setFrame(False)
        self.est_edt_ln_codBarras.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.est_edt_ln_codBarras.setDragEnabled(True)
        self.est_edt_ln_codBarras.setReadOnly(False)

        self.gridLayout_32.addWidget(self.est_edt_ln_codBarras, 7, 1, 1, 4)

        self.label_67 = QLabel(self.frame_21)
        self.label_67.setObjectName(u"label_67")
        sizePolicy2.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy2)
        self.label_67.setMaximumSize(QSize(90, 30))
        self.label_67.setFont(font2)
        self.label_67.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_67, 8, 1, 1, 1)

        self.est_edt_cb_tipo = QComboBox(self.frame_21)
        self.est_edt_cb_tipo.addItem("")
        self.est_edt_cb_tipo.setObjectName(u"est_edt_cb_tipo")
        self.est_edt_cb_tipo.setMaximumSize(QSize(16777215, 30))
        self.est_edt_cb_tipo.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_edt_cb_tipo.setEditable(True)

        self.gridLayout_32.addWidget(self.est_edt_cb_tipo, 0, 1, 1, 4)

        self.label_61 = QLabel(self.frame_21)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(16777215, 30))
        self.label_61.setFont(font2)
        self.label_61.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_61, 2, 0, 1, 1)

        self.label_65 = QLabel(self.frame_21)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 30))
        self.label_65.setFont(font2)
        self.label_65.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_65, 7, 0, 1, 1)

        self.est_edt_btn_cancelar = QPushButton(self.frame_21)
        self.est_edt_btn_cancelar.setObjectName(u"est_edt_btn_cancelar")
        sizePolicy3.setHeightForWidth(self.est_edt_btn_cancelar.sizePolicy().hasHeightForWidth())
        self.est_edt_btn_cancelar.setSizePolicy(sizePolicy3)
        self.est_edt_btn_cancelar.setMaximumSize(QSize(90, 30))
        self.est_edt_btn_cancelar.setFont(font2)
        self.est_edt_btn_cancelar.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout_32.addWidget(self.est_edt_btn_cancelar, 8, 4, 1, 1)

        self.label_62 = QLabel(self.frame_21)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 30))
        self.label_62.setFont(font2)
        self.label_62.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_62, 4, 0, 1, 1)

        self.est_edt_ln_pVenda = QLineEdit(self.frame_21)
        self.est_edt_ln_pVenda.setObjectName(u"est_edt_ln_pVenda")
        self.est_edt_ln_pVenda.setEnabled(True)
        self.est_edt_ln_pVenda.setMaximumSize(QSize(16777215, 25))
        self.est_edt_ln_pVenda.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.est_edt_ln_pVenda.setFrame(False)
        self.est_edt_ln_pVenda.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.est_edt_ln_pVenda.setDragEnabled(True)
        self.est_edt_ln_pVenda.setReadOnly(False)

        self.gridLayout_32.addWidget(self.est_edt_ln_pVenda, 5, 1, 1, 4)

        self.label_58 = QLabel(self.frame_21)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(16777215, 30))
        self.label_58.setFont(font2)
        self.label_58.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_63 = QLabel(self.frame_21)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 30))
        self.label_63.setFont(font2)
        self.label_63.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_63, 5, 0, 1, 1)

        self.label_90 = QLabel(self.frame_21)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMaximumSize(QSize(16777215, 30))
        self.label_90.setFont(font2)
        self.label_90.setStyleSheet(u"border: none;")

        self.gridLayout_32.addWidget(self.label_90, 3, 0, 1, 1)

        self.est_edt_cb_unidade = QComboBox(self.frame_21)
        self.est_edt_cb_unidade.addItem("")
        self.est_edt_cb_unidade.addItem("")
        self.est_edt_cb_unidade.addItem("")
        self.est_edt_cb_unidade.addItem("")
        self.est_edt_cb_unidade.addItem("")
        self.est_edt_cb_unidade.setObjectName(u"est_edt_cb_unidade")
        sizePolicy1.setHeightForWidth(self.est_edt_cb_unidade.sizePolicy().hasHeightForWidth())
        self.est_edt_cb_unidade.setSizePolicy(sizePolicy1)
        self.est_edt_cb_unidade.setMaximumSize(QSize(16777215, 30))
        self.est_edt_cb_unidade.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.est_edt_cb_unidade.setEditable(True)

        self.gridLayout_32.addWidget(self.est_edt_cb_unidade, 3, 1, 1, 4)


        self.gridLayout_31.addWidget(self.frame_21, 1, 0, 1, 1)

        self.stackedWidget_7.addWidget(self.editar_dados)

        self.verticalLayout_3.addWidget(self.stackedWidget_7)

        self.stackedWidget_2.addWidget(self.Estoque)
        self.PDV = QWidget()
        self.PDV.setObjectName(u"PDV")
        self.PDV.setStyleSheet(u"border-left: 1px solid rgb(221, 221, 221);")
        self.gridLayout_33 = QGridLayout(self.PDV)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.PDV)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_24)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.vend_tb = QTableWidget(self.frame_24)
        if (self.vend_tb.columnCount() < 7):
            self.vend_tb.setColumnCount(7)
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font11);
        self.vend_tb.setHorizontalHeaderItem(6, __qtablewidgetitem39)
        self.vend_tb.setObjectName(u"vend_tb")
        self.vend_tb.setFont(font6)
        self.vend_tb.setLayoutDirection(Qt.LeftToRight)
        self.vend_tb.setStyleSheet(u"QTableWidget{\n"
"	border: 1px solid rgb(125, 125, 125);\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	border: none;\n"
"	border-right: 1px solid rgb(147, 147, 147);\n"
"	border-left: 1px solid rgb(147, 147, 147);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget::item:alternate {\n"
"	background-color:rgb(236, 236, 236)\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 167, 214), stop:1 rgba(255, 239, 172, 255));\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: black;\n"
"	border: none;\n"
"	background-color: rgb(181, 181, 181)\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"	background-color: rgb(255, 255, 255);\n"
"	alternate-background-color: yellow\n"
"}")
        self.vend_tb.setLineWidth(1)
        self.vend_tb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.vend_tb.setTabKeyNavigation(True)
        self.vend_tb.setAlternatingRowColors(True)
        self.vend_tb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.vend_tb.setTextElideMode(Qt.ElideMiddle)
        self.vend_tb.setShowGrid(False)
        self.vend_tb.setSortingEnabled(False)
        self.vend_tb.setWordWrap(True)
        self.vend_tb.setCornerButtonEnabled(True)
        self.vend_tb.horizontalHeader().setCascadingSectionResizes(False)
        self.vend_tb.horizontalHeader().setMinimumSectionSize(50)
        self.vend_tb.horizontalHeader().setDefaultSectionSize(139)
        self.vend_tb.horizontalHeader().setProperty("showSortIndicator", False)
        self.vend_tb.horizontalHeader().setStretchLastSection(True)
        self.vend_tb.verticalHeader().setVisible(False)

        self.gridLayout_36.addWidget(self.vend_tb, 0, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMaximumSize(QSize(16777215, 55))
        self.frame_26.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.vend_btn_finalizar = QPushButton(self.frame_26)
        self.vend_btn_finalizar.setObjectName(u"vend_btn_finalizar")
        sizePolicy3.setHeightForWidth(self.vend_btn_finalizar.sizePolicy().hasHeightForWidth())
        self.vend_btn_finalizar.setSizePolicy(sizePolicy3)
        self.vend_btn_finalizar.setMaximumSize(QSize(100, 50))
        font12 = QFont()
        font12.setPointSize(14)
        font12.setBold(True)
        font12.setWeight(75)
        self.vend_btn_finalizar.setFont(font12)
        self.vend_btn_finalizar.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:			1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border: none;\n"
"	border-right: 1px solid rgb(175, 175, 175);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0.477, y1:1, x2:0.483, y2:0, stop:0 rgba(88, 88, 88, 255), stop:1 rgba(23, 23, 23, 255))\n"
"}")

        self.horizontalLayout_12.addWidget(self.vend_btn_finalizar)

        self.vend_btn_cancelar = QPushButton(self.frame_26)
        self.vend_btn_cancelar.setObjectName(u"vend_btn_cancelar")
        sizePolicy3.setHeightForWidth(self.vend_btn_cancelar.sizePolicy().hasHeightForWidth())
        self.vend_btn_cancelar.setSizePolicy(sizePolicy3)
        self.vend_btn_cancelar.setMaximumSize(QSize(100, 50))
        self.vend_btn_cancelar.setFont(font12)
        self.vend_btn_cancelar.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:			1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border: none;\n"
"	border-right: 1px solid rgb(175, 175, 175);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0.477, y1:1, x2:0.483, y2:0, stop:0 rgba(88, 88, 88, 255), stop:1 rgba(23, 23, 23, 255))\n"
"}")

        self.horizontalLayout_12.addWidget(self.vend_btn_cancelar)

        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)
        self.label_46.setMaximumSize(QSize(16777215, 30))
        self.label_46.setFont(font11)
        self.label_46.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;")

        self.horizontalLayout_12.addWidget(self.label_46)

        self.label_43 = QLabel(self.frame_26)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 30))
        self.label_43.setFont(font11)
        self.label_43.setStyleSheet(u"color: white;\n"
"border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.horizontalLayout_12.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_26)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(16777215, 30))
        font13 = QFont()
        font13.setPointSize(20)
        font13.setBold(True)
        font13.setWeight(75)
        self.label_44.setFont(font13)
        self.label_44.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;")

        self.horizontalLayout_12.addWidget(self.label_44)

        self.vend_ln_total = QLineEdit(self.frame_26)
        self.vend_ln_total.setObjectName(u"vend_ln_total")
        self.vend_ln_total.setMaximumSize(QSize(200, 50))
        self.vend_ln_total.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.vend_ln_total.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.vend_ln_total)


        self.gridLayout_36.addWidget(self.frame_26, 1, 0, 1, 1)


        self.gridLayout_33.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.PDV)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(400, 16777215))
        self.frame_25.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_25)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font11)

        self.verticalLayout.addWidget(self.label_3)

        self.vend_cb_codigo = QComboBox(self.frame_25)
        self.vend_cb_codigo.setObjectName(u"vend_cb_codigo")
        self.vend_cb_codigo.setMaximumSize(QSize(16777215, 50))
        self.vend_cb_codigo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.vend_cb_codigo.setEditable(True)

        self.verticalLayout.addWidget(self.vend_cb_codigo)

        self.label_7 = QLabel(self.frame_25)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font11)

        self.verticalLayout.addWidget(self.label_7)

        self.vend_ln_qnt = QLineEdit(self.frame_25)
        self.vend_ln_qnt.setObjectName(u"vend_ln_qnt")
        self.vend_ln_qnt.setMaximumSize(QSize(16777215, 50))
        self.vend_ln_qnt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.vend_ln_qnt)

        self.label_41 = QLabel(self.frame_25)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 30))
        self.label_41.setFont(font11)

        self.verticalLayout.addWidget(self.label_41)

        self.vend_ln_preco = QLineEdit(self.frame_25)
        self.vend_ln_preco.setObjectName(u"vend_ln_preco")
        self.vend_ln_preco.setMaximumSize(QSize(16777215, 50))
        self.vend_ln_preco.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.vend_ln_preco.setReadOnly(True)

        self.verticalLayout.addWidget(self.vend_ln_preco)

        self.label_42 = QLabel(self.frame_25)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 30))
        self.label_42.setFont(font11)

        self.verticalLayout.addWidget(self.label_42)

        self.vend_ln_subtotal = QLineEdit(self.frame_25)
        self.vend_ln_subtotal.setObjectName(u"vend_ln_subtotal")
        self.vend_ln_subtotal.setMaximumSize(QSize(16777215, 50))
        self.vend_ln_subtotal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.vend_ln_subtotal.setReadOnly(True)

        self.verticalLayout.addWidget(self.vend_ln_subtotal)

        self.vend_btn_adicionar = QPushButton(self.frame_25)
        self.vend_btn_adicionar.setObjectName(u"vend_btn_adicionar")
        self.vend_btn_adicionar.setMaximumSize(QSize(16777215, 50))
        self.vend_btn_adicionar.setFont(font12)
        self.vend_btn_adicionar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 					239), stop:1 rgba(255, 237, 162, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 216, 61, 255))\n"
"}")

        self.verticalLayout.addWidget(self.vend_btn_adicionar)


        self.gridLayout_33.addWidget(self.frame_25, 1, 1, 1, 1)

        self.frame_20 = QFrame(self.PDV)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(16777215, 80))
        self.frame_20.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_45 = QLabel(self.frame_20)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 30))
        self.label_45.setFont(font13)
        self.label_45.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;\n"
"color: white;")

        self.horizontalLayout_11.addWidget(self.label_45)


        self.gridLayout_33.addWidget(self.frame_20, 0, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.PDV)
        self.Financeiro = QWidget()
        self.Financeiro.setObjectName(u"Financeiro")
        self.gridLayout_54 = QGridLayout(self.Financeiro)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.stackedWidget_6 = QStackedWidget(self.Financeiro)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.stackedWidget_6.setStyleSheet(u"color: rgb(81, 81, 81);\n"
"border-radius: 3px;\n"
"")
        self.finan_home = QWidget()
        self.finan_home.setObjectName(u"finan_home")
        self.gridLayout_55 = QGridLayout(self.finan_home)
        self.gridLayout_55.setSpacing(30)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.widget_2 = QWidget(self.finan_home)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 80))
        self.widget_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")
        self.gridLayout_56 = QGridLayout(self.widget_2)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:rgb(0, 153, 255);\n"
"color: white;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.widget_3)
        self.label_56.setObjectName(u"label_56")
        font14 = QFont()
        font14.setPointSize(13)
        font14.setBold(True)
        font14.setWeight(75)
        self.label_56.setFont(font14)
        self.label_56.setStyleSheet(u"image: url(:/icons/img05.png);\n"
"padding: 10px;\n"
"")
        self.label_56.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label_56)

        self.label_89 = QLabel(self.widget_3)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(16777215, 25))
        font15 = QFont()
        font15.setPointSize(10)
        font15.setBold(True)
        font15.setItalic(False)
        font15.setWeight(75)
        self.label_89.setFont(font15)
        self.label_89.setStyleSheet(u"")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_89)


        self.gridLayout_56.addWidget(self.widget_3, 0, 0, 2, 1)

        self.fin_home_cx_posto = QLabel(self.widget_2)
        self.fin_home_cx_posto.setObjectName(u"fin_home_cx_posto")
        font16 = QFont()
        font16.setPointSize(22)
        font16.setBold(True)
        font16.setWeight(75)
        self.fin_home_cx_posto.setFont(font16)
        self.fin_home_cx_posto.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 119, 199);")
        self.fin_home_cx_posto.setAlignment(Qt.AlignCenter)

        self.gridLayout_56.addWidget(self.fin_home_cx_posto, 0, 1, 2, 1)


        self.gridLayout_55.addWidget(self.widget_2, 0, 0, 1, 2)

        self.widget_8 = QWidget(self.finan_home)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 125))
        self.widget_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout_59 = QGridLayout(self.widget_8)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.widget_8)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMaximumSize(QSize(16777215, 30))
        font17 = QFont()
        font17.setPointSize(17)
        font17.setBold(False)
        font17.setWeight(50)
        self.label_119.setFont(font17)
        self.label_119.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.label_119, 2, 0, 1, 2)

        self.widget_28 = QWidget(self.widget_8)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMaximumSize(QSize(16777215, 40))
        self.widget_28.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(40, 0, 40, 0)
        self.label_118 = QLabel(self.widget_28)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMaximumSize(QSize(16777215, 30))
        font18 = QFont()
        font18.setPointSize(8)
        font18.setBold(False)
        font18.setWeight(50)
        self.label_118.setFont(font18)
        self.label_118.setStyleSheet(u"")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_118)

        self.label_120 = QLabel(self.widget_28)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMaximumSize(QSize(80, 30))
        font19 = QFont()
        font19.setPointSize(8)
        font19.setBold(True)
        font19.setWeight(75)
        self.label_120.setFont(font19)
        self.label_120.setStyleSheet(u"")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_120)

        self.pushButton_8 = QPushButton(self.widget_28)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 8px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_8)


        self.gridLayout_59.addWidget(self.widget_28, 3, 0, 1, 2)

        self.label_117 = QLabel(self.widget_8)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMaximumSize(QSize(16777215, 30))
        font20 = QFont()
        font20.setPointSize(10)
        font20.setBold(True)
        font20.setWeight(75)
        self.label_117.setFont(font20)
        self.label_117.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.label_117, 0, 0, 1, 2)


        self.gridLayout_55.addWidget(self.widget_8, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.finan_home)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.widget_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")
        self.gridLayout_57 = QGridLayout(self.widget_4)
        self.gridLayout_57.setSpacing(0)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(141, 41, 255);\n"
"color: white;")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.widget_5)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font14)
        self.label_87.setStyleSheet(u"image: url(:/icons/img06.png);\n"
"padding: 5px;\n"
"")
        self.label_87.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_87)

        self.label_98 = QLabel(self.widget_5)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(16777215, 25))
        self.label_98.setFont(font14)
        self.label_98.setStyleSheet(u"")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_98)


        self.gridLayout_57.addWidget(self.widget_5, 0, 0, 2, 1)

        self.fin_home_cx_banco = QLabel(self.widget_4)
        self.fin_home_cx_banco.setObjectName(u"fin_home_cx_banco")
        self.fin_home_cx_banco.setFont(font16)
        self.fin_home_cx_banco.setStyleSheet(u"color: white;\n"
"background-color: rgb(92, 27, 166)")
        self.fin_home_cx_banco.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.fin_home_cx_banco, 0, 1, 2, 1)


        self.gridLayout_55.addWidget(self.widget_4, 0, 2, 1, 2)

        self.widget_7 = QWidget(self.finan_home)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(235, 235, 235)")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.widget_7)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(16777215, 50))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(10, 0, 10, 0)
        self.label_102 = QLabel(self.frame_43)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(16777215, 35))
        self.label_102.setFont(font4)
        self.label_102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_102)

        self.comboBox = QComboBox(self.frame_43)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(100, 30))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_63.addWidget(self.comboBox)

        self.stackedWidget_19 = QStackedWidget(self.frame_43)
        self.stackedWidget_19.setObjectName(u"stackedWidget_19")
        sizePolicy3.setHeightForWidth(self.stackedWidget_19.sizePolicy().hasHeightForWidth())
        self.stackedWidget_19.setSizePolicy(sizePolicy3)
        self.stackedWidget_19.setMaximumSize(QSize(200, 30))
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.horizontalLayout_64 = QHBoxLayout(self.page_17)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.page_17)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy2)
        self.frame_49.setMaximumSize(QSize(200, 16777215))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.financeiro_fluxo_filtro_dat1 = QDateEdit(self.frame_49)
        self.financeiro_fluxo_filtro_dat1.setObjectName(u"financeiro_fluxo_filtro_dat1")
        self.financeiro_fluxo_filtro_dat1.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.financeiro_fluxo_filtro_dat1.setCalendarPopup(True)
        self.financeiro_fluxo_filtro_dat1.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_65.addWidget(self.financeiro_fluxo_filtro_dat1)

        self.label_179 = QLabel(self.frame_49)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMaximumSize(QSize(10, 16777215))
        self.label_179.setFont(font6)
        self.label_179.setStyleSheet(u"")

        self.horizontalLayout_65.addWidget(self.label_179)

        self.financeiro_fluxo_filtro_dat2 = QDateEdit(self.frame_49)
        self.financeiro_fluxo_filtro_dat2.setObjectName(u"financeiro_fluxo_filtro_dat2")
        self.financeiro_fluxo_filtro_dat2.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.financeiro_fluxo_filtro_dat2.setCalendarPopup(True)
        self.financeiro_fluxo_filtro_dat2.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_65.addWidget(self.financeiro_fluxo_filtro_dat2)


        self.horizontalLayout_64.addWidget(self.frame_49)

        self.financeiro_fluxo_pesq = QPushButton(self.page_17)
        self.financeiro_fluxo_pesq.setObjectName(u"financeiro_fluxo_pesq")
        self.financeiro_fluxo_pesq.setMaximumSize(QSize(40, 40))
        self.financeiro_fluxo_pesq.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 8px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_64.addWidget(self.financeiro_fluxo_pesq)

        self.stackedWidget_19.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.stackedWidget_19.addWidget(self.page_18)

        self.horizontalLayout_63.addWidget(self.stackedWidget_19)


        self.verticalLayout_7.addWidget(self.frame_43)

        self.fin_home_graf = QWidget(self.widget_7)
        self.fin_home_graf.setObjectName(u"fin_home_graf")
        self.fin_home_graf.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Segoe UI Historic\";\n"
"	padding-left: 30px;\n"
"	padding-right: 50px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.fin_home_graf)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_44 = QFrame(self.fin_home_graf)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"border:none;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_31 = QWidget(self.frame_44)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMaximumSize(QSize(50, 50))
        self.widget_31.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img08.png);\n"
"padding: 5px;")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")

        self.horizontalLayout_25.addWidget(self.widget_31)

        self.label_145 = QLabel(self.frame_44)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_145)

        self.financeiro_fluxo_receita = QLabel(self.frame_44)
        self.financeiro_fluxo_receita.setObjectName(u"financeiro_fluxo_receita")
        self.financeiro_fluxo_receita.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.financeiro_fluxo_receita)


        self.verticalLayout_8.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.fin_home_graf)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"border:none;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.widget_41 = QWidget(self.frame_45)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMaximumSize(QSize(50, 50))
        self.widget_41.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img07.png);\n"
"padding: 5px;")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")

        self.horizontalLayout_40.addWidget(self.widget_41)

        self.label_147 = QLabel(self.frame_45)
        self.label_147.setObjectName(u"label_147")

        self.horizontalLayout_40.addWidget(self.label_147)

        self.financeiro_fluxo_despesa = QLabel(self.frame_45)
        self.financeiro_fluxo_despesa.setObjectName(u"financeiro_fluxo_despesa")
        self.financeiro_fluxo_despesa.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.financeiro_fluxo_despesa)


        self.verticalLayout_8.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.fin_home_graf)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"border:none;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.widget_32 = QWidget(self.frame_46)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMaximumSize(QSize(50, 50))
        self.widget_32.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img08.png);\n"
"padding: 5px;")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")

        self.horizontalLayout_41.addWidget(self.widget_32)

        self.label_150 = QLabel(self.frame_46)
        self.label_150.setObjectName(u"label_150")

        self.horizontalLayout_41.addWidget(self.label_150)

        self.financeiro_fluxo_entrada = QLabel(self.frame_46)
        self.financeiro_fluxo_entrada.setObjectName(u"financeiro_fluxo_entrada")
        self.financeiro_fluxo_entrada.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.financeiro_fluxo_entrada)


        self.verticalLayout_8.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.fin_home_graf)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"border:none;\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.widget_44 = QWidget(self.frame_47)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setMaximumSize(QSize(50, 50))
        self.widget_44.setStyleSheet(u"border: 0px;\n"
"padding: 5px;")
        self.horizontalLayout_62 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")

        self.horizontalLayout_47.addWidget(self.widget_44)

        self.label_165 = QLabel(self.frame_47)
        self.label_165.setObjectName(u"label_165")
        font21 = QFont()
        font21.setFamily(u"Segoe UI Semibold")
        font21.setPointSize(12)
        font21.setBold(False)
        font21.setItalic(False)
        font21.setWeight(7)
        self.label_165.setFont(font21)
        self.label_165.setStyleSheet(u"")

        self.horizontalLayout_47.addWidget(self.label_165)

        self.financeiro_fluxo_total = QLabel(self.frame_47)
        self.financeiro_fluxo_total.setObjectName(u"financeiro_fluxo_total")
        self.financeiro_fluxo_total.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.financeiro_fluxo_total)


        self.verticalLayout_8.addWidget(self.frame_47)


        self.verticalLayout_7.addWidget(self.fin_home_graf)


        self.gridLayout_55.addWidget(self.widget_7, 2, 0, 1, 2)

        self.widget_6 = QWidget(self.finan_home)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.widget_6)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMaximumSize(QSize(16777215, 40))
        self.label_107.setFont(font10)
        self.label_107.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.label_107.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_107)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_62 = QGridLayout(self.widget_10)
        self.gridLayout_62.setSpacing(0)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(20, 15, 20, 15)
        self.widget_29 = QWidget(self.widget_10)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy2.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy2)
        self.widget_29.setMaximumSize(QSize(50, 50))
        self.widget_29.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img08.png);\n"
"padding: 5px;")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")

        self.gridLayout_62.addWidget(self.widget_29, 0, 0, 3, 1)

        self.label_121 = QLabel(self.widget_10)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMaximumSize(QSize(16777215, 60))
        font22 = QFont()
        font22.setPointSize(10)
        font22.setBold(False)
        font22.setWeight(50)
        self.label_121.setFont(font22)
        self.label_121.setStyleSheet(u"border: 0px;")
        self.label_121.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_62.addWidget(self.label_121, 1, 1, 2, 1)

        self.widget_27 = QWidget(self.widget_10)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(50, 50))
        self.widget_27.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_27)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton)


        self.gridLayout_62.addWidget(self.widget_27, 0, 2, 3, 1)

        self.label_116 = QLabel(self.widget_10)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMaximumSize(QSize(16777215, 40))
        font23 = QFont()
        font23.setPointSize(12)
        font23.setBold(False)
        font23.setWeight(50)
        self.label_116.setFont(font23)
        self.label_116.setStyleSheet(u"border: 0px;")
        self.label_116.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.label_116, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_65 = QGridLayout(self.widget_11)
        self.gridLayout_65.setSpacing(0)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(20, 15, 20, 15)
        self.label_126 = QLabel(self.widget_11)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMaximumSize(QSize(16777215, 60))
        self.label_126.setFont(font22)
        self.label_126.setStyleSheet(u"border: 0px;")
        self.label_126.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_65.addWidget(self.label_126, 1, 1, 2, 1)

        self.widget_34 = QWidget(self.widget_11)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy2.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy2)
        self.widget_34.setMaximumSize(QSize(50, 50))
        self.widget_34.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img07.png);\n"
"padding: 5px;")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")

        self.gridLayout_65.addWidget(self.widget_34, 0, 0, 3, 1)

        self.widget_35 = QWidget(self.widget_11)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMaximumSize(QSize(50, 50))
        self.widget_35.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_35)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(50, 50))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_29.addWidget(self.pushButton_4)


        self.gridLayout_65.addWidget(self.widget_35, 0, 2, 3, 1)

        self.label_127 = QLabel(self.widget_11)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMaximumSize(QSize(16777215, 40))
        self.label_127.setFont(font23)
        self.label_127.setStyleSheet(u"border: 0px;")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.label_127, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_66 = QGridLayout(self.widget_12)
        self.gridLayout_66.setSpacing(0)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(20, 15, 20, 15)
        self.widget_36 = QWidget(self.widget_12)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy2.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy2)
        self.widget_36.setMaximumSize(QSize(50, 50))
        self.widget_36.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img10.png);\n"
"padding: 5px;")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")

        self.gridLayout_66.addWidget(self.widget_36, 0, 0, 3, 1)

        self.label_128 = QLabel(self.widget_12)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(16777215, 60))
        self.label_128.setFont(font22)
        self.label_128.setStyleSheet(u"border: 0px;")
        self.label_128.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_66.addWidget(self.label_128, 1, 1, 2, 1)

        self.widget_37 = QWidget(self.widget_12)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMaximumSize(QSize(50, 50))
        self.widget_37.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.widget_37)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_31.addWidget(self.pushButton_5)


        self.gridLayout_66.addWidget(self.widget_37, 0, 2, 3, 1)

        self.label_129 = QLabel(self.widget_12)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMaximumSize(QSize(16777215, 40))
        self.label_129.setFont(font23)
        self.label_129.setStyleSheet(u"border: 0px;")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.label_129, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_12)

        self.widget_15 = QWidget(self.widget_6)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_67 = QGridLayout(self.widget_15)
        self.gridLayout_67.setSpacing(0)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(20, 15, 20, 15)
        self.widget_38 = QWidget(self.widget_15)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy2.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy2)
        self.widget_38.setMaximumSize(QSize(50, 50))
        self.widget_38.setStyleSheet(u"border: 0px;\n"
"image: url(:/icons/img08.png);\n"
"padding: 5px;")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")

        self.gridLayout_67.addWidget(self.widget_38, 0, 0, 3, 1)

        self.label_130 = QLabel(self.widget_15)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMaximumSize(QSize(16777215, 60))
        self.label_130.setFont(font22)
        self.label_130.setStyleSheet(u"border: 0px;")
        self.label_130.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_67.addWidget(self.label_130, 1, 1, 2, 1)

        self.widget_39 = QWidget(self.widget_15)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMaximumSize(QSize(50, 50))
        self.widget_39.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget_39)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(50, 50))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_33.addWidget(self.pushButton_6)


        self.gridLayout_67.addWidget(self.widget_39, 0, 2, 3, 1)

        self.label_131 = QLabel(self.widget_15)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMaximumSize(QSize(16777215, 40))
        self.label_131.setFont(font23)
        self.label_131.setStyleSheet(u"border: 0px;")
        self.label_131.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.label_131, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_15)


        self.gridLayout_55.addWidget(self.widget_6, 1, 2, 2, 2)

        self.widget_14 = QWidget(self.finan_home)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 125))
        self.widget_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout_63 = QGridLayout(self.widget_14)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_122 = QLabel(self.widget_14)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMaximumSize(QSize(16777215, 30))
        self.label_122.setFont(font17)
        self.label_122.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_122.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.label_122, 2, 0, 1, 2)

        self.widget_30 = QWidget(self.widget_14)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(16777215, 40))
        self.widget_30.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(40, 0, 40, 0)
        self.label_123 = QLabel(self.widget_30)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMaximumSize(QSize(16777215, 30))
        self.label_123.setFont(font18)
        self.label_123.setStyleSheet(u"")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_123)

        self.label_124 = QLabel(self.widget_30)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMaximumSize(QSize(80, 30))
        self.label_124.setFont(font19)
        self.label_124.setStyleSheet(u"")
        self.label_124.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_124)

        self.pushButton_9 = QPushButton(self.widget_30)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(40, 40))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 8px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_9)


        self.gridLayout_63.addWidget(self.widget_30, 3, 0, 1, 2)

        self.label_125 = QLabel(self.widget_14)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMaximumSize(QSize(16777215, 30))
        self.label_125.setFont(font20)
        self.label_125.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.label_125, 0, 0, 1, 2)


        self.gridLayout_55.addWidget(self.widget_14, 1, 1, 1, 1)

        self.stackedWidget_6.addWidget(self.finan_home)
        self.finan_mov = QWidget()
        self.finan_mov.setObjectName(u"finan_mov")
        self.gridLayout_60 = QGridLayout(self.finan_mov)
        self.gridLayout_60.setSpacing(20)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.widget_13 = QWidget(self.finan_mov)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.widget_13.setMaximumSize(QSize(16777215, 50))
        self.widget_13.setStyleSheet(u"background-color: rgb(95, 95, 95);\n"
"color: white;")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(9, 0, 9, 0)
        self.label_169 = QLabel(self.widget_13)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setFont(font7)

        self.horizontalLayout_45.addWidget(self.label_169)

        self.comboBox_8 = QComboBox(self.widget_13)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMaximumSize(QSize(16777215, 25))
        self.comboBox_8.setFont(font7)
        self.comboBox_8.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_8.setEditable(True)

        self.horizontalLayout_45.addWidget(self.comboBox_8)

        self.stackedWidget_15 = QStackedWidget(self.widget_13)
        self.stackedWidget_15.setObjectName(u"stackedWidget_15")
        self.stackedWidget_15.setStyleSheet(u"QDateEdit{\n"
"	background-color: rgb(95, 95, 95);\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.entrada_2 = QWidget()
        self.entrada_2.setObjectName(u"entrada_2")
        self.horizontalLayout_46 = QHBoxLayout(self.entrada_2)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.label_170 = QLabel(self.entrada_2)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMaximumSize(QSize(60, 16777215))
        self.label_170.setFont(font7)

        self.horizontalLayout_46.addWidget(self.label_170)

        self.comboBox_9 = QComboBox(self.entrada_2)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMaximumSize(QSize(150, 25))
        self.comboBox_9.setFont(font7)
        self.comboBox_9.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_9.setEditable(True)

        self.horizontalLayout_46.addWidget(self.comboBox_9)

        self.comboBox_11 = QComboBox(self.entrada_2)
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        sizePolicy3.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy3)
        self.comboBox_11.setMaximumSize(QSize(200, 25))
        self.comboBox_11.setFont(font7)
        self.comboBox_11.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_11.setEditable(True)

        self.horizontalLayout_46.addWidget(self.comboBox_11)

        self.label_171 = QLabel(self.entrada_2)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMaximumSize(QSize(75, 16777215))
        self.label_171.setFont(font7)

        self.horizontalLayout_46.addWidget(self.label_171)

        self.comboBox_10 = QComboBox(self.entrada_2)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMaximumSize(QSize(150, 25))
        self.comboBox_10.setFont(font7)
        self.comboBox_10.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_10.setEditable(True)

        self.horizontalLayout_46.addWidget(self.comboBox_10)

        self.stackedWidget_16 = QStackedWidget(self.entrada_2)
        self.stackedWidget_16.setObjectName(u"stackedWidget_16")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_70 = QGridLayout(self.page_9)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.page_9)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy2)
        self.frame_39.setMaximumSize(QSize(200, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.cons_ponto_dt_inicio_6 = QDateEdit(self.frame_39)
        self.cons_ponto_dt_inicio_6.setObjectName(u"cons_ponto_dt_inicio_6")
        self.cons_ponto_dt_inicio_6.setMaximumSize(QSize(16777215, 25))
        self.cons_ponto_dt_inicio_6.setStyleSheet(u"")
        self.cons_ponto_dt_inicio_6.setCalendarPopup(True)
        self.cons_ponto_dt_inicio_6.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_48.addWidget(self.cons_ponto_dt_inicio_6)

        self.label_111 = QLabel(self.frame_39)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMaximumSize(QSize(10, 16777215))
        self.label_111.setFont(font6)
        self.label_111.setStyleSheet(u"")

        self.horizontalLayout_48.addWidget(self.label_111)

        self.cons_ponto_dt_fim_3 = QDateEdit(self.frame_39)
        self.cons_ponto_dt_fim_3.setObjectName(u"cons_ponto_dt_fim_3")
        self.cons_ponto_dt_fim_3.setMaximumSize(QSize(16777215, 25))
        self.cons_ponto_dt_fim_3.setStyleSheet(u"")
        self.cons_ponto_dt_fim_3.setCalendarPopup(True)
        self.cons_ponto_dt_fim_3.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_48.addWidget(self.cons_ponto_dt_fim_3)


        self.gridLayout_70.addWidget(self.frame_39, 0, 0, 1, 1)

        self.stackedWidget_16.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stackedWidget_16.addWidget(self.page_10)

        self.horizontalLayout_46.addWidget(self.stackedWidget_16)

        self.widget_56 = QWidget(self.entrada_2)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_46.addWidget(self.widget_56)

        self.stackedWidget_15.addWidget(self.entrada_2)
        self.transferencia_2 = QWidget()
        self.transferencia_2.setObjectName(u"transferencia_2")
        self.horizontalLayout_51 = QHBoxLayout(self.transferencia_2)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.widget_57 = QWidget(self.transferencia_2)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.widget_57)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(60, 16777215))
        self.label_172.setFont(font7)

        self.horizontalLayout_53.addWidget(self.label_172)

        self.comboBox_13 = QComboBox(self.widget_57)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setMaximumSize(QSize(150, 25))
        self.comboBox_13.setFont(font7)
        self.comboBox_13.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_13.setEditable(True)

        self.horizontalLayout_53.addWidget(self.comboBox_13)

        self.comboBox_14 = QComboBox(self.widget_57)
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        sizePolicy3.setHeightForWidth(self.comboBox_14.sizePolicy().hasHeightForWidth())
        self.comboBox_14.setSizePolicy(sizePolicy3)
        self.comboBox_14.setMaximumSize(QSize(200, 25))
        self.comboBox_14.setFont(font7)
        self.comboBox_14.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_14.setEditable(True)

        self.horizontalLayout_53.addWidget(self.comboBox_14)

        self.label_173 = QLabel(self.widget_57)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMaximumSize(QSize(75, 16777215))
        self.label_173.setFont(font7)

        self.horizontalLayout_53.addWidget(self.label_173)

        self.comboBox_12 = QComboBox(self.widget_57)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMaximumSize(QSize(150, 25))
        self.comboBox_12.setFont(font7)
        self.comboBox_12.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_12.setEditable(True)

        self.horizontalLayout_53.addWidget(self.comboBox_12)


        self.horizontalLayout_51.addWidget(self.widget_57)

        self.stackedWidget_18 = QStackedWidget(self.transferencia_2)
        self.stackedWidget_18.setObjectName(u"stackedWidget_18")
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.gridLayout_89 = QGridLayout(self.page_15)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.gridLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.page_15)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy2)
        self.frame_41.setMaximumSize(QSize(200, 16777215))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.cons_ponto_dt_inicio_11 = QDateEdit(self.frame_41)
        self.cons_ponto_dt_inicio_11.setObjectName(u"cons_ponto_dt_inicio_11")
        self.cons_ponto_dt_inicio_11.setMaximumSize(QSize(16777215, 25))
        self.cons_ponto_dt_inicio_11.setStyleSheet(u"QDateEdit{\n"
"	background-color: rgb(95, 95, 95);\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.cons_ponto_dt_inicio_11.setCalendarPopup(True)
        self.cons_ponto_dt_inicio_11.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_56.addWidget(self.cons_ponto_dt_inicio_11)

        self.label_138 = QLabel(self.frame_41)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMaximumSize(QSize(10, 16777215))
        self.label_138.setFont(font6)
        self.label_138.setStyleSheet(u"")

        self.horizontalLayout_56.addWidget(self.label_138)

        self.cons_ponto_dt_fim_8 = QDateEdit(self.frame_41)
        self.cons_ponto_dt_fim_8.setObjectName(u"cons_ponto_dt_fim_8")
        self.cons_ponto_dt_fim_8.setMaximumSize(QSize(16777215, 25))
        self.cons_ponto_dt_fim_8.setStyleSheet(u"QDateEdit{\n"
"	background-color: rgb(95, 95, 95);\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.cons_ponto_dt_fim_8.setCalendarPopup(True)
        self.cons_ponto_dt_fim_8.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_56.addWidget(self.cons_ponto_dt_fim_8)


        self.gridLayout_89.addWidget(self.frame_41, 0, 0, 1, 1)

        self.stackedWidget_18.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.stackedWidget_18.addWidget(self.page_16)

        self.horizontalLayout_51.addWidget(self.stackedWidget_18)

        self.stackedWidget_15.addWidget(self.transferencia_2)
        self.despesa_2 = QWidget()
        self.despesa_2.setObjectName(u"despesa_2")
        self.horizontalLayout_59 = QHBoxLayout(self.despesa_2)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.widget_59 = QWidget(self.despesa_2)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_176 = QLabel(self.widget_59)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMaximumSize(QSize(60, 16777215))
        self.label_176.setFont(font7)

        self.horizontalLayout_58.addWidget(self.label_176)

        self.comboBox_18 = QComboBox(self.widget_59)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMaximumSize(QSize(150, 25))
        self.comboBox_18.setFont(font7)
        self.comboBox_18.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_18.setEditable(True)

        self.horizontalLayout_58.addWidget(self.comboBox_18)

        self.comboBox_19 = QComboBox(self.widget_59)
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        sizePolicy3.setHeightForWidth(self.comboBox_19.sizePolicy().hasHeightForWidth())
        self.comboBox_19.setSizePolicy(sizePolicy3)
        self.comboBox_19.setMaximumSize(QSize(200, 25))
        self.comboBox_19.setFont(font7)
        self.comboBox_19.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_19.setEditable(True)

        self.horizontalLayout_58.addWidget(self.comboBox_19)

        self.label_177 = QLabel(self.widget_59)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMaximumSize(QSize(75, 16777215))
        self.label_177.setFont(font7)

        self.horizontalLayout_58.addWidget(self.label_177)

        self.comboBox_20 = QComboBox(self.widget_59)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMaximumSize(QSize(150, 25))
        self.comboBox_20.setFont(font7)
        self.comboBox_20.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.comboBox_20.setEditable(True)

        self.horizontalLayout_58.addWidget(self.comboBox_20)


        self.horizontalLayout_59.addWidget(self.widget_59)

        self.stackedWidget_17 = QStackedWidget(self.despesa_2)
        self.stackedWidget_17.setObjectName(u"stackedWidget_17")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_88 = QGridLayout(self.page_11)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.page_11)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy2)
        self.frame_40.setMaximumSize(QSize(200, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.cons_ponto_dt_inicio_10 = QDateEdit(self.frame_40)
        self.cons_ponto_dt_inicio_10.setObjectName(u"cons_ponto_dt_inicio_10")
        self.cons_ponto_dt_inicio_10.setMaximumSize(QSize(16777215, 25))
        self.cons_ponto_dt_inicio_10.setStyleSheet(u"")
        self.cons_ponto_dt_inicio_10.setCalendarPopup(True)
        self.cons_ponto_dt_inicio_10.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_55.addWidget(self.cons_ponto_dt_inicio_10)

        self.label_137 = QLabel(self.frame_40)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMaximumSize(QSize(10, 16777215))
        self.label_137.setFont(font6)
        self.label_137.setStyleSheet(u"")

        self.horizontalLayout_55.addWidget(self.label_137)

        self.cons_ponto_dt_fim_7 = QDateEdit(self.frame_40)
        self.cons_ponto_dt_fim_7.setObjectName(u"cons_ponto_dt_fim_7")
        self.cons_ponto_dt_fim_7.setMaximumSize(QSize(16777215, 25))
        self.cons_ponto_dt_fim_7.setStyleSheet(u"")
        self.cons_ponto_dt_fim_7.setCalendarPopup(True)
        self.cons_ponto_dt_fim_7.setDate(QDate(2021, 1, 1))

        self.horizontalLayout_55.addWidget(self.cons_ponto_dt_fim_7)


        self.gridLayout_88.addWidget(self.frame_40, 0, 0, 1, 1)

        self.stackedWidget_17.addWidget(self.page_11)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.stackedWidget_17.addWidget(self.page_14)

        self.horizontalLayout_59.addWidget(self.stackedWidget_17)

        self.stackedWidget_15.addWidget(self.despesa_2)

        self.horizontalLayout_45.addWidget(self.stackedWidget_15)

        self.pushButton_17 = QPushButton(self.widget_13)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/icon_pesquisa.png);\n"
"	padding: 8px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(79, 79, 79)\n"
"}")

        self.horizontalLayout_45.addWidget(self.pushButton_17)


        self.gridLayout_60.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.finan_mov)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_84 = QGridLayout(self.widget_9)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_84.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_14 = QStackedWidget(self.widget_9)
        self.stackedWidget_14.setObjectName(u"stackedWidget_14")
        self.tab_despesa = QWidget()
        self.tab_despesa.setObjectName(u"tab_despesa")
        self.gridLayout_85 = QGridLayout(self.tab_despesa)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.tableWidget = QTableWidget(self.tab_despesa)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem56)
        self.tableWidget.setObjectName(u"tableWidget")
        font24 = QFont()
        font24.setFamily(u"Roboto")
        font24.setPointSize(9)
        font24.setBold(False)
        font24.setItalic(False)
        font24.setWeight(50)
        self.tableWidget.setFont(font24)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	font: 9pt \"Roboto\";\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 0px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 232, 136, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: rgb(91, 91, 91);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"	border-right: 1px solid rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_85.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.stackedWidget_14.addWidget(self.tab_despesa)
        self.tab_entrada = QWidget()
        self.tab_entrada.setObjectName(u"tab_entrada")
        self.gridLayout_86 = QGridLayout(self.tab_entrada)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.tableWidget_2 = QTableWidget(self.tab_entrada)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem60)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, __qtablewidgetitem70)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFont(font24)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	font: 9pt \"Roboto\";\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 0px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 232, 136, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: rgb(91, 91, 91);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"	border-right: 1px solid rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_86.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.stackedWidget_14.addWidget(self.tab_entrada)
        self.tab_transferencia = QWidget()
        self.tab_transferencia.setObjectName(u"tab_transferencia")
        self.gridLayout_87 = QGridLayout(self.tab_transferencia)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.widget_58 = QWidget(self.tab_transferencia)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setMinimumSize(QSize(100, 50))
        self.horizontalLayout_57 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_174 = QLabel(self.widget_58)
        self.label_174.setObjectName(u"label_174")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy6)
        self.label_174.setMinimumSize(QSize(50, 0))
        self.label_174.setFont(font7)

        self.horizontalLayout_57.addWidget(self.label_174)

        self.label_139 = QLabel(self.widget_58)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(150, 30))
        self.label_139.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.horizontalLayout_57.addWidget(self.label_139)


        self.gridLayout_87.addWidget(self.widget_58, 1, 1, 1, 1)

        self.tableWidget_3 = QTableWidget(self.tab_transferencia)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem76)
        if (self.tableWidget_3.rowCount() < 2):
            self.tableWidget_3.setRowCount(2)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 3, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 5, __qtablewidgetitem90)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font24)
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
"	font: 9pt \"Roboto\";\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 0px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 232, 136, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    color: rgb(91, 91, 91);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"	border-right: 1px solid rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.gridLayout_87.addWidget(self.tableWidget_3, 0, 0, 1, 2)

        self.widget_60 = QWidget(self.tab_transferencia)
        self.widget_60.setObjectName(u"widget_60")
        sizePolicy2.setHeightForWidth(self.widget_60.sizePolicy().hasHeightForWidth())
        self.widget_60.setSizePolicy(sizePolicy2)
        self.widget_60.setMinimumSize(QSize(200, 50))
        self.horizontalLayout_60 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")

        self.gridLayout_87.addWidget(self.widget_60, 1, 0, 1, 1)

        self.stackedWidget_14.addWidget(self.tab_transferencia)

        self.gridLayout_84.addWidget(self.stackedWidget_14, 0, 0, 1, 1)


        self.gridLayout_60.addWidget(self.widget_9, 1, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.finan_mov)
        self.finan_add = QWidget()
        self.finan_add.setObjectName(u"finan_add")
        self.gridLayout_46 = QGridLayout(self.finan_add)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.widget_18 = QWidget(self.finan_add)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.gridLayout_51 = QGridLayout(self.widget_18)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setHorizontalSpacing(45)
        self.gridLayout_51.setVerticalSpacing(10)
        self.gridLayout_51.setContentsMargins(-1, 20, -1, -1)
        self.widget_55 = QWidget(self.widget_18)
        self.widget_55.setObjectName(u"widget_55")
        self.gridLayout_61 = QGridLayout(self.widget_55)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(40, -1, 40, -1)
        self.widget_17 = QWidget(self.widget_55)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"background-color: rgb(94, 94, 94);\n"
"COLOR: WHITE;")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(9, -1, 9, -1)
        self.label_168 = QLabel(self.widget_17)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setFont(font2)

        self.horizontalLayout_44.addWidget(self.label_168)

        self.fin_novo_mov = QComboBox(self.widget_17)
        self.fin_novo_mov.addItem("")
        self.fin_novo_mov.addItem("")
        self.fin_novo_mov.addItem("")
        self.fin_novo_mov.setObjectName(u"fin_novo_mov")
        self.fin_novo_mov.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_mov.setFont(font7)
        self.fin_novo_mov.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_mov.setEditable(True)

        self.horizontalLayout_44.addWidget(self.fin_novo_mov)


        self.gridLayout_61.addWidget(self.widget_17, 0, 0, 1, 1)


        self.gridLayout_51.addWidget(self.widget_55, 0, 0, 1, 1)

        self.widget_25 = QWidget(self.widget_18)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy2.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy2)
        self.widget_25.setStyleSheet(u"background-color: rgb(255, 255, 255);;")
        self.gridLayout_78 = QGridLayout(self.widget_25)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.fin_novo_wid03 = QWidget(self.widget_25)
        self.fin_novo_wid03.setObjectName(u"fin_novo_wid03")
        self.fin_novo_wid03.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_80 = QGridLayout(self.fin_novo_wid03)
        self.gridLayout_80.setSpacing(0)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gridLayout_80.setContentsMargins(20, 15, 20, 15)
        self.widget_45 = QWidget(self.fin_novo_wid03)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMaximumSize(QSize(50, 50))
        self.widget_45.setStyleSheet(u"border: 0px;\n"
"padding: 5px;")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")

        self.gridLayout_80.addWidget(self.widget_45, 0, 0, 3, 1)

        self.label_160 = QLabel(self.fin_novo_wid03)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(16777215, 60))
        self.label_160.setFont(font22)
        self.label_160.setStyleSheet(u"border: 0px;")
        self.label_160.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_80.addWidget(self.label_160, 1, 1, 2, 1)

        self.widget_46 = QWidget(self.fin_novo_wid03)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMaximumSize(QSize(50, 50))
        self.widget_46.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.widget_46)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(50, 50))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_13)


        self.gridLayout_80.addWidget(self.widget_46, 0, 2, 3, 1)

        self.label_161 = QLabel(self.fin_novo_wid03)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMaximumSize(QSize(16777215, 40))
        self.label_161.setFont(font23)
        self.label_161.setStyleSheet(u"border: 0px;")
        self.label_161.setAlignment(Qt.AlignCenter)

        self.gridLayout_80.addWidget(self.label_161, 0, 1, 1, 1)


        self.gridLayout_78.addWidget(self.fin_novo_wid03, 2, 0, 1, 1)

        self.fin_novo_wid04 = QWidget(self.widget_25)
        self.fin_novo_wid04.setObjectName(u"fin_novo_wid04")
        self.fin_novo_wid04.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_81 = QGridLayout(self.fin_novo_wid04)
        self.gridLayout_81.setSpacing(0)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setContentsMargins(20, 15, 20, 15)
        self.label_162 = QLabel(self.fin_novo_wid04)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMaximumSize(QSize(16777215, 60))
        self.label_162.setFont(font22)
        self.label_162.setStyleSheet(u"border: 0px;")
        self.label_162.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_81.addWidget(self.label_162, 1, 1, 2, 1)

        self.widget_49 = QWidget(self.fin_novo_wid04)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMaximumSize(QSize(50, 50))
        self.widget_49.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.widget_49)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(50, 50))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_39.addWidget(self.pushButton_14)


        self.gridLayout_81.addWidget(self.widget_49, 0, 2, 3, 1)

        self.label_163 = QLabel(self.fin_novo_wid04)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(16777215, 40))
        self.label_163.setFont(font23)
        self.label_163.setStyleSheet(u"border: 0px;")
        self.label_163.setAlignment(Qt.AlignCenter)

        self.gridLayout_81.addWidget(self.label_163, 0, 1, 1, 1)

        self.widget_48 = QWidget(self.fin_novo_wid04)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMaximumSize(QSize(50, 50))
        self.widget_48.setStyleSheet(u"border: 0px;\n"
"padding: 5px;")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")

        self.gridLayout_81.addWidget(self.widget_48, 0, 0, 3, 1)


        self.gridLayout_78.addWidget(self.fin_novo_wid04, 3, 0, 1, 1)

        self.fin_novo_wid01 = QWidget(self.widget_25)
        self.fin_novo_wid01.setObjectName(u"fin_novo_wid01")
        self.fin_novo_wid01.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_77 = QGridLayout(self.fin_novo_wid01)
        self.gridLayout_77.setSpacing(0)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.gridLayout_77.setContentsMargins(20, 15, 20, 15)
        self.widget_33 = QWidget(self.fin_novo_wid01)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMaximumSize(QSize(50, 50))
        self.widget_33.setStyleSheet(u"border: 0px;\n"
"padding: 5px;")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.gridLayout_77.addWidget(self.widget_33, 0, 0, 3, 1)

        self.label_156 = QLabel(self.fin_novo_wid01)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMaximumSize(QSize(16777215, 60))
        self.label_156.setFont(font22)
        self.label_156.setStyleSheet(u"border: 0px;")
        self.label_156.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_77.addWidget(self.label_156, 1, 1, 2, 1)

        self.widget_40 = QWidget(self.fin_novo_wid01)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMaximumSize(QSize(50, 50))
        self.widget_40.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.widget_40)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(50, 50))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_27.addWidget(self.pushButton_11)


        self.gridLayout_77.addWidget(self.widget_40, 0, 2, 3, 1)

        self.label_157 = QLabel(self.fin_novo_wid01)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMaximumSize(QSize(16777215, 40))
        self.label_157.setFont(font23)
        self.label_157.setStyleSheet(u"border: 0px;")
        self.label_157.setAlignment(Qt.AlignCenter)

        self.gridLayout_77.addWidget(self.label_157, 0, 1, 1, 1)


        self.gridLayout_78.addWidget(self.fin_novo_wid01, 0, 0, 1, 1)

        self.fin_novo_wid02 = QWidget(self.widget_25)
        self.fin_novo_wid02.setObjectName(u"fin_novo_wid02")
        self.fin_novo_wid02.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_79 = QGridLayout(self.fin_novo_wid02)
        self.gridLayout_79.setSpacing(0)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.gridLayout_79.setContentsMargins(20, 15, 20, 15)
        self.widget_42 = QWidget(self.fin_novo_wid02)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMaximumSize(QSize(50, 50))
        self.widget_42.setStyleSheet(u"border: 0px;\n"
"padding: 5px;")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")

        self.gridLayout_79.addWidget(self.widget_42, 0, 0, 3, 1)

        self.label_158 = QLabel(self.fin_novo_wid02)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMaximumSize(QSize(16777215, 60))
        self.label_158.setFont(font22)
        self.label_158.setStyleSheet(u"border: 0px;")
        self.label_158.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_79.addWidget(self.label_158, 1, 1, 2, 1)

        self.widget_43 = QWidget(self.fin_novo_wid02)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMaximumSize(QSize(50, 50))
        self.widget_43.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.widget_43)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(50, 50))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_35.addWidget(self.pushButton_12)


        self.gridLayout_79.addWidget(self.widget_43, 0, 2, 3, 1)

        self.label_159 = QLabel(self.fin_novo_wid02)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMaximumSize(QSize(16777215, 40))
        self.label_159.setFont(font23)
        self.label_159.setStyleSheet(u"border: 0px;")
        self.label_159.setAlignment(Qt.AlignCenter)

        self.gridLayout_79.addWidget(self.label_159, 0, 1, 1, 1)


        self.gridLayout_78.addWidget(self.fin_novo_wid02, 1, 0, 1, 1)

        self.fin_novo_wid05 = QWidget(self.widget_25)
        self.fin_novo_wid05.setObjectName(u"fin_novo_wid05")
        self.fin_novo_wid05.setStyleSheet(u"border-bottom: 1px solid rgb(235, 235, 235)")
        self.gridLayout_83 = QGridLayout(self.fin_novo_wid05)
        self.gridLayout_83.setSpacing(0)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.gridLayout_83.setContentsMargins(20, 15, 20, 15)
        self.label_166 = QLabel(self.fin_novo_wid05)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMaximumSize(QSize(16777215, 60))
        self.label_166.setFont(font22)
        self.label_166.setStyleSheet(u"border: 0px;")
        self.label_166.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_83.addWidget(self.label_166, 1, 1, 2, 1)

        self.widget_53 = QWidget(self.fin_novo_wid05)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setMaximumSize(QSize(50, 50))
        self.widget_53.setStyleSheet(u"border: 0px;")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.widget_53)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(50, 50))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/img09.png);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(247, 247, 247);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_16)


        self.gridLayout_83.addWidget(self.widget_53, 0, 2, 3, 1)

        self.label_167 = QLabel(self.fin_novo_wid05)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMaximumSize(QSize(16777215, 40))
        self.label_167.setFont(font23)
        self.label_167.setStyleSheet(u"border: 0px;")
        self.label_167.setAlignment(Qt.AlignCenter)

        self.gridLayout_83.addWidget(self.label_167, 0, 1, 1, 1)

        self.widget_54 = QWidget(self.fin_novo_wid05)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setMaximumSize(QSize(50, 50))
        self.widget_54.setStyleSheet(u"border: 0px;\n"
"padding: 5px;")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")

        self.gridLayout_83.addWidget(self.widget_54, 0, 0, 3, 1)


        self.gridLayout_78.addWidget(self.fin_novo_wid05, 4, 0, 1, 1)


        self.gridLayout_51.addWidget(self.widget_25, 1, 1, 1, 1)

        self.stackedWidget_8 = QStackedWidget(self.widget_18)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.despesa = QWidget()
        self.despesa.setObjectName(u"despesa")
        self.gridLayout_68 = QGridLayout(self.despesa)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.despesa)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy2.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy2)
        self.widget_19.setMaximumSize(QSize(500, 16777215))
        self.widget_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_58 = QGridLayout(self.widget_19)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(40, -1, 40, -1)
        self.label_114 = QLabel(self.widget_19)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMaximumSize(QSize(16777215, 50))
        font25 = QFont()
        font25.setPointSize(17)
        self.label_114.setFont(font25)
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout_58.addWidget(self.label_114, 0, 0, 1, 2)

        self.fin_novo_desp_desc = QLineEdit(self.widget_19)
        self.fin_novo_desp_desc.setObjectName(u"fin_novo_desp_desc")
        self.fin_novo_desp_desc.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_desp_desc.setFont(font7)
        self.fin_novo_desp_desc.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.gridLayout_58.addWidget(self.fin_novo_desp_desc, 4, 1, 1, 1)

        self.fin_novo_desp_conta = QComboBox(self.widget_19)
        self.fin_novo_desp_conta.addItem("")
        self.fin_novo_desp_conta.addItem("")
        self.fin_novo_desp_conta.addItem("")
        self.fin_novo_desp_conta.setObjectName(u"fin_novo_desp_conta")
        self.fin_novo_desp_conta.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_desp_conta.setFont(font7)
        self.fin_novo_desp_conta.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_desp_conta.setEditable(True)

        self.gridLayout_58.addWidget(self.fin_novo_desp_conta, 6, 1, 1, 1)

        self.fin_novo_desp_valor = QLineEdit(self.widget_19)
        self.fin_novo_desp_valor.setObjectName(u"fin_novo_desp_valor")
        self.fin_novo_desp_valor.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_desp_valor.setFont(font7)
        self.fin_novo_desp_valor.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.gridLayout_58.addWidget(self.fin_novo_desp_valor, 5, 1, 1, 1)

        self.label_80 = QLabel(self.widget_19)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font2)

        self.gridLayout_58.addWidget(self.label_80, 3, 0, 1, 1)

        self.label_100 = QLabel(self.widget_19)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font2)

        self.gridLayout_58.addWidget(self.label_100, 5, 0, 1, 1)

        self.label_57 = QLabel(self.widget_19)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)

        self.gridLayout_58.addWidget(self.label_57, 1, 0, 1, 1)

        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_64 = QGridLayout(self.widget_20)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(125, -1, 125, -1)
        self.fin_novo_desp_btn_inserir = QPushButton(self.widget_20)
        self.fin_novo_desp_btn_inserir.setObjectName(u"fin_novo_desp_btn_inserir")
        self.fin_novo_desp_btn_inserir.setMaximumSize(QSize(16777215, 30))
        self.fin_novo_desp_btn_inserir.setFont(font2)
        self.fin_novo_desp_btn_inserir.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(81, 81, 81);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout_64.addWidget(self.fin_novo_desp_btn_inserir, 0, 0, 1, 1)


        self.gridLayout_58.addWidget(self.widget_20, 8, 0, 1, 2)

        self.fin_novo_desp_tipo = QComboBox(self.widget_19)
        self.fin_novo_desp_tipo.addItem("")
        self.fin_novo_desp_tipo.setObjectName(u"fin_novo_desp_tipo")
        self.fin_novo_desp_tipo.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_desp_tipo.setFont(font7)
        self.fin_novo_desp_tipo.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_desp_tipo.setEditable(True)

        self.gridLayout_58.addWidget(self.fin_novo_desp_tipo, 3, 1, 1, 1)

        self.label_99 = QLabel(self.widget_19)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font2)

        self.gridLayout_58.addWidget(self.label_99, 4, 0, 1, 1)

        self.label_101 = QLabel(self.widget_19)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font2)

        self.gridLayout_58.addWidget(self.label_101, 6, 0, 1, 1)

        self.fin_novo_desp_data = QDateEdit(self.widget_19)
        self.fin_novo_desp_data.setObjectName(u"fin_novo_desp_data")
        self.fin_novo_desp_data.setFont(font7)
        self.fin_novo_desp_data.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(212, 212, 212);\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.fin_novo_desp_data.setCalendarPopup(True)
        self.fin_novo_desp_data.setDate(QDate(2021, 1, 1))

        self.gridLayout_58.addWidget(self.fin_novo_desp_data, 1, 1, 1, 1)

        self.label_140 = QLabel(self.widget_19)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setFont(font2)

        self.gridLayout_58.addWidget(self.label_140, 7, 0, 1, 1)

        self.fin_novo_desp_status = QComboBox(self.widget_19)
        self.fin_novo_desp_status.addItem("")
        self.fin_novo_desp_status.addItem("")
        self.fin_novo_desp_status.addItem("")
        self.fin_novo_desp_status.setObjectName(u"fin_novo_desp_status")
        self.fin_novo_desp_status.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_desp_status.setFont(font7)
        self.fin_novo_desp_status.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_desp_status.setEditable(True)

        self.gridLayout_58.addWidget(self.fin_novo_desp_status, 7, 1, 1, 1)


        self.gridLayout_68.addWidget(self.widget_19, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.despesa)
        self.transferencia = QWidget()
        self.transferencia.setObjectName(u"transferencia")
        self.gridLayout_72 = QGridLayout(self.transferencia)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.transferencia)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy2.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy2)
        self.widget_21.setMaximumSize(QSize(500, 16777215))
        self.widget_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_69 = QGridLayout(self.widget_21)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setContentsMargins(40, -1, 40, -1)
        self.fin_novo_transf_de = QComboBox(self.widget_21)
        self.fin_novo_transf_de.addItem("")
        self.fin_novo_transf_de.addItem("")
        self.fin_novo_transf_de.addItem("")
        self.fin_novo_transf_de.setObjectName(u"fin_novo_transf_de")
        self.fin_novo_transf_de.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_transf_de.setFont(font7)
        self.fin_novo_transf_de.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_transf_de.setEditable(True)

        self.gridLayout_69.addWidget(self.fin_novo_transf_de, 3, 1, 1, 1)

        self.fin_novo_transf_desc = QLineEdit(self.widget_21)
        self.fin_novo_transf_desc.setObjectName(u"fin_novo_transf_desc")
        self.fin_novo_transf_desc.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_transf_desc.setFont(font7)
        self.fin_novo_transf_desc.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.gridLayout_69.addWidget(self.fin_novo_transf_desc, 5, 1, 1, 1)

        self.fin_novo_transf_valor = QLineEdit(self.widget_21)
        self.fin_novo_transf_valor.setObjectName(u"fin_novo_transf_valor")
        self.fin_novo_transf_valor.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_transf_valor.setFont(font7)
        self.fin_novo_transf_valor.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.gridLayout_69.addWidget(self.fin_novo_transf_valor, 6, 1, 1, 1)

        self.label_135 = QLabel(self.widget_21)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font2)

        self.gridLayout_69.addWidget(self.label_135, 5, 0, 1, 1)

        self.fin_novo_transf_data = QDateEdit(self.widget_21)
        self.fin_novo_transf_data.setObjectName(u"fin_novo_transf_data")
        self.fin_novo_transf_data.setFont(font7)
        self.fin_novo_transf_data.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(212, 212, 212);\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.fin_novo_transf_data.setCalendarPopup(True)
        self.fin_novo_transf_data.setDate(QDate(2021, 1, 1))

        self.gridLayout_69.addWidget(self.fin_novo_transf_data, 1, 1, 1, 1)

        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_71 = QGridLayout(self.widget_22)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(125, -1, 125, -1)
        self.fin_novo_transf_btn_inserir = QPushButton(self.widget_22)
        self.fin_novo_transf_btn_inserir.setObjectName(u"fin_novo_transf_btn_inserir")
        self.fin_novo_transf_btn_inserir.setMaximumSize(QSize(16777215, 30))
        self.fin_novo_transf_btn_inserir.setFont(font2)
        self.fin_novo_transf_btn_inserir.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(81, 81, 81);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout_71.addWidget(self.fin_novo_transf_btn_inserir, 0, 0, 1, 1)


        self.gridLayout_69.addWidget(self.widget_22, 8, 0, 1, 2)

        self.label_115 = QLabel(self.widget_21)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMaximumSize(QSize(16777215, 50))
        self.label_115.setFont(font25)
        self.label_115.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_115, 0, 0, 1, 2)

        self.label_133 = QLabel(self.widget_21)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font2)

        self.gridLayout_69.addWidget(self.label_133, 6, 0, 1, 1)

        self.label_132 = QLabel(self.widget_21)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font2)

        self.gridLayout_69.addWidget(self.label_132, 3, 0, 1, 1)

        self.fin_novo_transf_para = QComboBox(self.widget_21)
        self.fin_novo_transf_para.addItem("")
        self.fin_novo_transf_para.addItem("")
        self.fin_novo_transf_para.addItem("")
        self.fin_novo_transf_para.setObjectName(u"fin_novo_transf_para")
        self.fin_novo_transf_para.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_transf_para.setFont(font7)
        self.fin_novo_transf_para.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_transf_para.setEditable(True)

        self.gridLayout_69.addWidget(self.fin_novo_transf_para, 4, 1, 1, 1)

        self.label_134 = QLabel(self.widget_21)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font2)

        self.gridLayout_69.addWidget(self.label_134, 1, 0, 1, 1)

        self.label_155 = QLabel(self.widget_21)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font2)

        self.gridLayout_69.addWidget(self.label_155, 4, 0, 1, 1)


        self.gridLayout_72.addWidget(self.widget_21, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.transferencia)
        self.entrada = QWidget()
        self.entrada.setObjectName(u"entrada")
        self.gridLayout_75 = QGridLayout(self.entrada)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.gridLayout_75.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.entrada)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy2.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy2)
        self.widget_23.setMaximumSize(QSize(500, 16777215))
        self.widget_23.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_73 = QGridLayout(self.widget_23)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setContentsMargins(40, -1, 40, -1)
        self.label_151 = QLabel(self.widget_23)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font2)

        self.gridLayout_73.addWidget(self.label_151, 4, 0, 1, 1)

        self.label_149 = QLabel(self.widget_23)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMaximumSize(QSize(16777215, 50))
        self.label_149.setFont(font25)
        self.label_149.setAlignment(Qt.AlignCenter)

        self.gridLayout_73.addWidget(self.label_149, 0, 0, 1, 2)

        self.label_153 = QLabel(self.widget_23)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font2)

        self.gridLayout_73.addWidget(self.label_153, 3, 0, 1, 1)

        self.fin_novo_ent_data = QDateEdit(self.widget_23)
        self.fin_novo_ent_data.setObjectName(u"fin_novo_ent_data")
        self.fin_novo_ent_data.setFont(font7)
        self.fin_novo_ent_data.setStyleSheet(u"QDateEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(212, 212, 212);\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: black;\n"
"}\n"
"\n"
"")
        self.fin_novo_ent_data.setCalendarPopup(True)
        self.fin_novo_ent_data.setDate(QDate(2021, 1, 1))

        self.gridLayout_73.addWidget(self.fin_novo_ent_data, 1, 1, 1, 1)

        self.fin_novo_ent_valor = QLineEdit(self.widget_23)
        self.fin_novo_ent_valor.setObjectName(u"fin_novo_ent_valor")
        self.fin_novo_ent_valor.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_ent_valor.setFont(font7)
        self.fin_novo_ent_valor.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.gridLayout_73.addWidget(self.fin_novo_ent_valor, 4, 1, 1, 1)

        self.fin_novo_ent_conta = QComboBox(self.widget_23)
        self.fin_novo_ent_conta.addItem("")
        self.fin_novo_ent_conta.addItem("")
        self.fin_novo_ent_conta.addItem("")
        self.fin_novo_ent_conta.setObjectName(u"fin_novo_ent_conta")
        self.fin_novo_ent_conta.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_ent_conta.setFont(font7)
        self.fin_novo_ent_conta.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"	border-bottom: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        self.fin_novo_ent_conta.setEditable(True)

        self.gridLayout_73.addWidget(self.fin_novo_ent_conta, 5, 1, 1, 1)

        self.label_154 = QLabel(self.widget_23)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font2)

        self.gridLayout_73.addWidget(self.label_154, 5, 0, 1, 1)

        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_74 = QGridLayout(self.widget_24)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gridLayout_74.setContentsMargins(125, -1, 125, -1)
        self.fin_novo_ent_btn_inserir = QPushButton(self.widget_24)
        self.fin_novo_ent_btn_inserir.setObjectName(u"fin_novo_ent_btn_inserir")
        self.fin_novo_ent_btn_inserir.setMaximumSize(QSize(16777215, 30))
        self.fin_novo_ent_btn_inserir.setFont(font2)
        self.fin_novo_ent_btn_inserir.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(81, 81, 81);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout_74.addWidget(self.fin_novo_ent_btn_inserir, 0, 0, 1, 1)


        self.gridLayout_73.addWidget(self.widget_24, 7, 0, 1, 2)

        self.fin_novo_ent_desc = QLineEdit(self.widget_23)
        self.fin_novo_ent_desc.setObjectName(u"fin_novo_ent_desc")
        self.fin_novo_ent_desc.setMaximumSize(QSize(16777215, 25))
        self.fin_novo_ent_desc.setFont(font7)
        self.fin_novo_ent_desc.setStyleSheet(u"border-bottom: 1px solid rgb(209, 209, 209);")

        self.gridLayout_73.addWidget(self.fin_novo_ent_desc, 3, 1, 1, 1)

        self.label_152 = QLabel(self.widget_23)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font2)

        self.gridLayout_73.addWidget(self.label_152, 1, 0, 1, 1)


        self.gridLayout_75.addWidget(self.widget_23, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.entrada)

        self.gridLayout_51.addWidget(self.stackedWidget_8, 1, 0, 1, 1)

        self.widget_61 = QWidget(self.widget_18)
        self.widget_61.setObjectName(u"widget_61")
        sizePolicy2.setHeightForWidth(self.widget_61.sizePolicy().hasHeightForWidth())
        self.widget_61.setSizePolicy(sizePolicy2)
        self.gridLayout_90 = QGridLayout(self.widget_61)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gridLayout_90.setContentsMargins(0, 9, 0, -1)
        self.widget_26 = QWidget(self.widget_61)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy2.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy2)
        self.widget_26.setStyleSheet(u"background-color: rgb(94, 94, 94);\n"
"COLOR: WHITE;")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, -1, 0, -1)
        self.label_175 = QLabel(self.widget_26)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font2)
        self.label_175.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_175)


        self.gridLayout_90.addWidget(self.widget_26, 0, 0, 1, 1)


        self.gridLayout_51.addWidget(self.widget_61, 0, 1, 1, 1)


        self.gridLayout_46.addWidget(self.widget_18, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.finan_add)

        self.gridLayout_54.addWidget(self.stackedWidget_6, 1, 0, 1, 1)

        self.frame_17 = QFrame(self.Financeiro)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 120))
        self.frame_17.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"border-radius: 5px 5px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_17)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.fin_btn_home = QPushButton(self.frame_17)
        self.fin_btn_home.setObjectName(u"fin_btn_home")
        sizePolicy.setHeightForWidth(self.fin_btn_home.sizePolicy().hasHeightForWidth())
        self.fin_btn_home.setSizePolicy(sizePolicy)
        self.fin_btn_home.setMaximumSize(QSize(150, 55))
        self.fin_btn_home.setFont(font2)
        self.fin_btn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_52.addWidget(self.fin_btn_home, 1, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_52.addItem(self.horizontalSpacer_13, 1, 3, 1, 1)

        self.frame_35 = QFrame(self.frame_17)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy1.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy1)
        self.frame_35.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: white;\n"
"border-bottom: 1px solid rgb(166, 166, 166);\n"
"border-radius: none;\n"
"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_35)
        self.gridLayout_53.setSpacing(1)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(1, 1, 1, 1)
        self.cons_lb_5 = QLabel(self.frame_35)
        self.cons_lb_5.setObjectName(u"cons_lb_5")
        sizePolicy1.setHeightForWidth(self.cons_lb_5.sizePolicy().hasHeightForWidth())
        self.cons_lb_5.setSizePolicy(sizePolicy1)
        self.cons_lb_5.setMaximumSize(QSize(200, 70))
        self.cons_lb_5.setFont(font8)
        self.cons_lb_5.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.cons_lb_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_53.addWidget(self.cons_lb_5, 0, 0, 1, 1)

        self.est_lb_nav_3 = QLabel(self.frame_35)
        self.est_lb_nav_3.setObjectName(u"est_lb_nav_3")
        sizePolicy1.setHeightForWidth(self.est_lb_nav_3.sizePolicy().hasHeightForWidth())
        self.est_lb_nav_3.setSizePolicy(sizePolicy1)
        self.est_lb_nav_3.setMaximumSize(QSize(16777215, 70))
        self.est_lb_nav_3.setFont(font8)
        self.est_lb_nav_3.setStyleSheet(u"\n"
"border-bottom: none;\n"
"\n"
"")
        self.est_lb_nav_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_53.addWidget(self.est_lb_nav_3, 0, 1, 1, 1)


        self.gridLayout_52.addWidget(self.frame_35, 0, 0, 1, 4)

        self.fin_btn_mov = QPushButton(self.frame_17)
        self.fin_btn_mov.setObjectName(u"fin_btn_mov")
        sizePolicy.setHeightForWidth(self.fin_btn_mov.sizePolicy().hasHeightForWidth())
        self.fin_btn_mov.setSizePolicy(sizePolicy)
        self.fin_btn_mov.setMaximumSize(QSize(150, 55))
        self.fin_btn_mov.setFont(font2)
        self.fin_btn_mov.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_52.addWidget(self.fin_btn_mov, 1, 1, 1, 1)

        self.fin_btn_novo = QPushButton(self.frame_17)
        self.fin_btn_novo.setObjectName(u"fin_btn_novo")
        sizePolicy.setHeightForWidth(self.fin_btn_novo.sizePolicy().hasHeightForWidth())
        self.fin_btn_novo.setSizePolicy(sizePolicy)
        self.fin_btn_novo.setMaximumSize(QSize(150, 55))
        self.fin_btn_novo.setFont(font2)
        self.fin_btn_novo.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-right: 1px solid rgb(166, 166, 166);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: white;\n"
"	border-radius: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_52.addWidget(self.fin_btn_novo, 1, 2, 1, 1)


        self.gridLayout_54.addWidget(self.frame_17, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.Financeiro)

        self.gridLayout_6.addWidget(self.stackedWidget_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.Conteudo)
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.gridLayout_7 = QGridLayout(self.Login)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.login = QFrame(self.Login)
        self.login.setObjectName(u"login")
        sizePolicy2.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy2)
        self.login.setFont(font)
        self.login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 231, 135, 255))")
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.login)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.in_usuario = QLineEdit(self.login)
        self.in_usuario.setObjectName(u"in_usuario")
        sizePolicy.setHeightForWidth(self.in_usuario.sizePolicy().hasHeightForWidth())
        self.in_usuario.setSizePolicy(sizePolicy)
        self.in_usuario.setMaximumSize(QSize(400, 40))
        self.in_usuario.setFont(font1)
        self.in_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.in_usuario.setMaxLength(30)
        self.in_usuario.setAlignment(Qt.AlignCenter)
        self.in_usuario.setDragEnabled(True)

        self.gridLayout_9.addWidget(self.in_usuario, 3, 0, 1, 1)

        self.lb_info_2 = QLabel(self.login)
        self.lb_info_2.setObjectName(u"lb_info_2")
        sizePolicy1.setHeightForWidth(self.lb_info_2.sizePolicy().hasHeightForWidth())
        self.lb_info_2.setSizePolicy(sizePolicy1)
        self.lb_info_2.setMaximumSize(QSize(16777215, 30))
        self.lb_info_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout_9.addWidget(self.lb_info_2, 6, 0, 1, 1)

        self.btn_entrar = QPushButton(self.login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        sizePolicy5.setHeightForWidth(self.btn_entrar.sizePolicy().hasHeightForWidth())
        self.btn_entrar.setSizePolicy(sizePolicy5)
        self.btn_entrar.setMaximumSize(QSize(16777215, 40))
        font26 = QFont()
        font26.setPointSize(16)
        self.btn_entrar.setFont(font26)
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(52, 52, 52, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(42, 42, 42, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.btn_entrar, 7, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 8, 0, 1, 1)

        self.lb_info = QLabel(self.login)
        self.lb_info.setObjectName(u"lb_info")
        sizePolicy1.setHeightForWidth(self.lb_info.sizePolicy().hasHeightForWidth())
        self.lb_info.setSizePolicy(sizePolicy1)
        self.lb_info.setMaximumSize(QSize(16777215, 30))
        font27 = QFont()
        font27.setPointSize(13)
        self.lb_info.setFont(font27)
        self.lb_info.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: red;")
        self.lb_info.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lb_info, 5, 0, 1, 1)

        self.in_senha = QLineEdit(self.login)
        self.in_senha.setObjectName(u"in_senha")
        sizePolicy.setHeightForWidth(self.in_senha.sizePolicy().hasHeightForWidth())
        self.in_senha.setSizePolicy(sizePolicy)
        self.in_senha.setMaximumSize(QSize(400, 40))
        self.in_senha.setFont(font1)
        self.in_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.in_senha.setMaxLength(30)
        self.in_senha.setEchoMode(QLineEdit.Password)
        self.in_senha.setAlignment(Qt.AlignCenter)
        self.in_senha.setDragEnabled(True)

        self.gridLayout_9.addWidget(self.in_senha, 4, 0, 1, 1)

        self.label_6 = QLabel(self.login)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMaximumSize(QSize(16777215, 100))
        font28 = QFont()
        font28.setPointSize(43)
        self.label_6.setFont(font28)
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)

        self.lb_info_3 = QLabel(self.login)
        self.lb_info_3.setObjectName(u"lb_info_3")
        sizePolicy1.setHeightForWidth(self.lb_info_3.sizePolicy().hasHeightForWidth())
        self.lb_info_3.setSizePolicy(sizePolicy1)
        self.lb_info_3.setMaximumSize(QSize(16777215, 30))
        self.lb_info_3.setFont(font6)
        self.lb_info_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: red;")
        self.lb_info_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lb_info_3, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.login, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.Login)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font29 = QFont()
        font29.setPointSize(75)
        self.label_5.setFont(font29)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"image: url(:/icons/img01.png)\n"
"")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Login)

        self.gridLayout_27.addWidget(self.stackedWidget, 0, 0, 1, 1)

        Sistema.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_46.setBuddy(self.vend_ln_total)
        self.label_43.setBuddy(self.vend_ln_total)
        self.label_7.setBuddy(self.vend_ln_qnt)
        self.label_41.setBuddy(self.vend_ln_preco)
        self.label_42.setBuddy(self.vend_ln_subtotal)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.in_senha, self.btn_entrar)
        QWidget.setTabOrder(self.btn_entrar, self.btn_inicio)
        QWidget.setTabOrder(self.btn_inicio, self.btn_caixa)
        QWidget.setTabOrder(self.btn_caixa, self.btn_consulta)
        QWidget.setTabOrder(self.btn_consulta, self.btn_estoque)
        QWidget.setTabOrder(self.btn_estoque, self.cb_bomba)
        QWidget.setTabOrder(self.cb_bomba, self.ln_ana_anterior)
        QWidget.setTabOrder(self.ln_ana_anterior, self.ln_digi_anterior)
        QWidget.setTabOrder(self.ln_digi_anterior, self.ln_ana_atual)
        QWidget.setTabOrder(self.ln_ana_atual, self.ln_digi_atual)
        QWidget.setTabOrder(self.ln_digi_atual, self.btn_cx_inserir)
        QWidget.setTabOrder(self.btn_cx_inserir, self.ln_cx_litros)
        QWidget.setTabOrder(self.ln_cx_litros, self.ln_cx_valor)
        QWidget.setTabOrder(self.ln_cx_valor, self.ln_cx_din)
        QWidget.setTabOrder(self.ln_cx_din, self.ln_cx_pix)
        QWidget.setTabOrder(self.ln_cx_pix, self.ln_cx_cartao)
        QWidget.setTabOrder(self.ln_cx_cartao, self.ln_cx_resto_2)
        QWidget.setTabOrder(self.ln_cx_resto_2, self.ln_cx_resto)
        QWidget.setTabOrder(self.ln_cx_resto, self.cb_cx_nome)
        QWidget.setTabOrder(self.cb_cx_nome, self.ln_cx_ter_valor)
        QWidget.setTabOrder(self.ln_cx_ter_valor, self.ln_cx_desc)
        QWidget.setTabOrder(self.ln_cx_desc, self.btn_cx_ret_inserir)
        QWidget.setTabOrder(self.btn_cx_ret_inserir, self.tb_cx)
        QWidget.setTabOrder(self.tb_cx, self.btn_cx_fechar)
        QWidget.setTabOrder(self.btn_cx_fechar, self.btn_config)
        QWidget.setTabOrder(self.btn_config, self.btn_vendas)
        QWidget.setTabOrder(self.btn_vendas, self.ini_btn_ponto)
        QWidget.setTabOrder(self.ini_btn_ponto, self.btn_logout)
        QWidget.setTabOrder(self.btn_logout, self.cons_btn_tabela)
        QWidget.setTabOrder(self.cons_btn_tabela, self.cons_btn_vendas)
        QWidget.setTabOrder(self.cons_btn_vendas, self.cons_btn_retiradas)
        QWidget.setTabOrder(self.cons_btn_retiradas, self.cons_btn_ponto)
        QWidget.setTabOrder(self.cons_btn_ponto, self.cons_cb_bomba)
        QWidget.setTabOrder(self.cons_cb_bomba, self.cons_dt_inicio)
        QWidget.setTabOrder(self.cons_dt_inicio, self.cons_dt_fim)
        QWidget.setTabOrder(self.cons_dt_fim, self.cons_btn_ok)
        QWidget.setTabOrder(self.cons_btn_ok, self.cons_cb_periodo)
        QWidget.setTabOrder(self.cons_cb_periodo, self.cons_cb_tab_periodo)
        QWidget.setTabOrder(self.cons_cb_tab_periodo, self.cons_btn_tab_ok)
        QWidget.setTabOrder(self.cons_btn_tab_ok, self.cons_tb)
        QWidget.setTabOrder(self.cons_tb, self.cons_cb_tab_filtro)
        QWidget.setTabOrder(self.cons_cb_tab_filtro, self.cons_btn_tab_del)
        QWidget.setTabOrder(self.cons_btn_tab_del, self.cons_dt_tab_inicio)
        QWidget.setTabOrder(self.cons_dt_tab_inicio, self.cons_dt_tab_fim)
        QWidget.setTabOrder(self.cons_dt_tab_fim, self.cons_btn_tab_ret)
        QWidget.setTabOrder(self.cons_btn_tab_ret, self.cons_cb_tab_retiradas)
        QWidget.setTabOrder(self.cons_cb_tab_retiradas, self.cons_dt_tab_inicio_2)
        QWidget.setTabOrder(self.cons_dt_tab_inicio_2, self.cons_dt_tab_fim_2)
        QWidget.setTabOrder(self.cons_dt_tab_fim_2, self.cons_btn_ok_2)
        QWidget.setTabOrder(self.cons_btn_ok_2, self.cons_tb_retiradas)
        QWidget.setTabOrder(self.cons_tb_retiradas, self.cons_ponto_cb_filtro)
        QWidget.setTabOrder(self.cons_ponto_cb_filtro, self.cons_ponto_cb_periodo)
        QWidget.setTabOrder(self.cons_ponto_cb_periodo, self.cons_ponto_dt_inicio)
        QWidget.setTabOrder(self.cons_ponto_dt_inicio, self.cons_ponto_dt_fim)
        QWidget.setTabOrder(self.cons_ponto_dt_fim, self.cons_ponto_btn_ok)
        QWidget.setTabOrder(self.cons_ponto_btn_ok, self.cons_ponto_tb)
        QWidget.setTabOrder(self.cons_ponto_tb, self.config_comb_btn)
        QWidget.setTabOrder(self.config_comb_btn, self.config_user_btn)
        QWidget.setTabOrder(self.config_user_btn, self.config_comb_voltar)
        QWidget.setTabOrder(self.config_comb_voltar, self.config_comb_editar)
        QWidget.setTabOrder(self.config_comb_editar, self.config_comb_info_2)
        QWidget.setTabOrder(self.config_comb_info_2, self.config_user_voltar)
        QWidget.setTabOrder(self.config_user_voltar, self.config_user_novo_btn)
        QWidget.setTabOrder(self.config_user_novo_btn, self.config_user_lista_2)
        QWidget.setTabOrder(self.config_user_lista_2, self.config_comb_edit_btn)
        QWidget.setTabOrder(self.config_comb_edit_btn, self.config_comb_edit_antigo)
        QWidget.setTabOrder(self.config_comb_edit_antigo, self.config_comb_edit_combustivel)
        QWidget.setTabOrder(self.config_comb_edit_combustivel, self.est_btn_novo)
        QWidget.setTabOrder(self.est_btn_novo, self.est_btn_entrada)
        QWidget.setTabOrder(self.est_btn_entrada, self.est_btn_consulta)
        QWidget.setTabOrder(self.est_btn_consulta, self.ln_est_produto)
        QWidget.setTabOrder(self.ln_est_produto, self.ln_est_pVenda)
        QWidget.setTabOrder(self.ln_est_pVenda, self.btn_est_cadastrar)
        QWidget.setTabOrder(self.btn_est_cadastrar, self.est_cb_tipo)
        QWidget.setTabOrder(self.est_cb_tipo, self.ln_est_qnt)
        QWidget.setTabOrder(self.ln_est_qnt, self.ln_est_pCompra)
        QWidget.setTabOrder(self.ln_est_pCompra, self.est_cb_marca)
        QWidget.setTabOrder(self.est_cb_marca, self.ln_est_codBarras)
        QWidget.setTabOrder(self.ln_est_codBarras, self.est_cb_unidade)
        QWidget.setTabOrder(self.est_cb_unidade, self.est_new_cb_produto)
        QWidget.setTabOrder(self.est_new_cb_produto, self.est_new_ln_qnt)
        QWidget.setTabOrder(self.est_new_ln_qnt, self.est_new_btn_cadastrar)
        QWidget.setTabOrder(self.est_new_btn_cadastrar, self.est_const_cb_filtro)
        QWidget.setTabOrder(self.est_const_cb_filtro, self.est_const_ln_filtro)
        QWidget.setTabOrder(self.est_const_ln_filtro, self.est_const_btn_pesquisar)
        QWidget.setTabOrder(self.est_const_btn_pesquisar, self.est_const_btn_editar)
        QWidget.setTabOrder(self.est_const_btn_editar, self.est_const_btn_deletar)
        QWidget.setTabOrder(self.est_const_btn_deletar, self.est_consult_tab)
        QWidget.setTabOrder(self.est_consult_tab, self.est_edt_ln_qnt)
        QWidget.setTabOrder(self.est_edt_ln_qnt, self.est_edt_ln_pCompra)
        QWidget.setTabOrder(self.est_edt_ln_pCompra, self.est_edt_cb_marca)
        QWidget.setTabOrder(self.est_edt_cb_marca, self.est_edt_btn_salvar)
        QWidget.setTabOrder(self.est_edt_btn_salvar, self.est_edt_ln_produto)
        QWidget.setTabOrder(self.est_edt_ln_produto, self.est_edt_ln_codBarras)
        QWidget.setTabOrder(self.est_edt_ln_codBarras, self.est_edt_cb_tipo)
        QWidget.setTabOrder(self.est_edt_cb_tipo, self.est_edt_btn_cancelar)
        QWidget.setTabOrder(self.est_edt_btn_cancelar, self.est_edt_ln_pVenda)
        QWidget.setTabOrder(self.est_edt_ln_pVenda, self.est_edt_cb_unidade)
        QWidget.setTabOrder(self.est_edt_cb_unidade, self.vend_tb)
        QWidget.setTabOrder(self.vend_tb, self.vend_btn_finalizar)
        QWidget.setTabOrder(self.vend_btn_finalizar, self.vend_btn_cancelar)
        QWidget.setTabOrder(self.vend_btn_cancelar, self.vend_ln_total)
        QWidget.setTabOrder(self.vend_ln_total, self.vend_cb_codigo)
        QWidget.setTabOrder(self.vend_cb_codigo, self.vend_ln_qnt)
        QWidget.setTabOrder(self.vend_ln_qnt, self.vend_ln_preco)
        QWidget.setTabOrder(self.vend_ln_preco, self.vend_ln_subtotal)
        QWidget.setTabOrder(self.vend_ln_subtotal, self.vend_btn_adicionar)
        QWidget.setTabOrder(self.vend_btn_adicionar, self.cons_cb_informacao)
        QWidget.setTabOrder(self.cons_cb_informacao, self.cons_btn_exportar)
        QWidget.setTabOrder(self.cons_btn_exportar, self.cons_btn_tab_detalhes)
        QWidget.setTabOrder(self.cons_btn_tab_detalhes, self.cons_cb_tab_funcionario)
        QWidget.setTabOrder(self.cons_cb_tab_funcionario, self.cons_tab_total)
        QWidget.setTabOrder(self.cons_tab_total, self.in_usuario)
        QWidget.setTabOrder(self.in_usuario, self.config_comb_edit_combustivel_2)
        QWidget.setTabOrder(self.config_comb_edit_combustivel_2, self.config_comb_edit_novo_2)
        QWidget.setTabOrder(self.config_comb_edit_novo_2, self.config_comb_edit_novo)

        self.retranslateUi(Sistema)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)
        self.nav_consultas.setCurrentIndex(4)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWidget_9.setCurrentIndex(0)
        self.stackedWidget_12.setCurrentIndex(1)
        self.stackedWidget_10.setCurrentIndex(1)
        self.stackedWidget_7.setCurrentIndex(3)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget_19.setCurrentIndex(0)
        self.stackedWidget_15.setCurrentIndex(2)
        self.stackedWidget_16.setCurrentIndex(0)
        self.stackedWidget_18.setCurrentIndex(0)
        self.stackedWidget_17.setCurrentIndex(0)
        self.stackedWidget_14.setCurrentIndex(2)
        self.stackedWidget_8.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Sistema)
    # setupUi

    def retranslateUi(self, Sistema):
        Sistema.setWindowTitle(QCoreApplication.translate("Sistema", u"Gerenciamento Posto", None))
        self.btn_estoque.setText(QCoreApplication.translate("Sistema", u"Estoque", None))
        self.btn_vendas.setText(QCoreApplication.translate("Sistema", u"Vendas", None))
#if QT_CONFIG(tooltip)
        self.btn_config.setToolTip(QCoreApplication.translate("Sistema", u"<html><head/><body><p><img src=\":/icons/download.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_config.setText("")
        self.btn_inicio.setText(QCoreApplication.translate("Sistema", u"Inicio", None))
        self.btn_caixa.setText(QCoreApplication.translate("Sistema", u"Caixa", None))
        self.btn_consulta.setText(QCoreApplication.translate("Sistema", u"Consultas", None))
        self.btn_financeiro.setText(QCoreApplication.translate("Sistema", u"Financeiro", None))
        self.label_13.setText("")
        self.label_17.setText("")
        self.lb_ini_data_4.setText("")
        self.lb_ini_funcionario.setText("")
        self.lb_img_func.setText("")
        self.lb_ini_data.setText("")
        self.label_16.setText("")
        self.lb_ini_data_5.setText("")
        self.ini_btn_ponto.setText(QCoreApplication.translate("Sistema", u"Bater Ponto", None))
        self.btn_ponto.setText("")
        self.lb_ini_data_3.setText("")
        self.lb_ini_data_2.setText("")
        self.label_59.setText("")
        self.btn_logout.setText(QCoreApplication.translate("Sistema", u"Sair", None))
        self.btn_ponto_2.setText("")
        self.cons_lb_informacao.setText(QCoreApplication.translate("Sistema", u"Informa\u00e7\u00e3o:", None))
        self.label_20.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.cons_cb_informacao.setItemText(0, QCoreApplication.translate("Sistema", u"Total Vendas", None))
        self.cons_cb_informacao.setItemText(1, QCoreApplication.translate("Sistema", u"Dinheiro", None))
        self.cons_cb_informacao.setItemText(2, QCoreApplication.translate("Sistema", u"Pix", None))
        self.cons_cb_informacao.setItemText(3, QCoreApplication.translate("Sistema", u"Cart\u00e3o", None))
        self.cons_cb_informacao.setItemText(4, QCoreApplication.translate("Sistema", u"Litros", None))
        self.cons_cb_informacao.setItemText(5, QCoreApplication.translate("Sistema", u"Sa\u00eddas", None))

        self.cons_btn_ok.setText(QCoreApplication.translate("Sistema", u"OK", None))
        self.label_10.setText(QCoreApplication.translate("Sistema", u"     Filtro:", None))
        self.cons_lb_periodo.setText(QCoreApplication.translate("Sistema", u"Periodo:", None))
        self.cons_cb_bomba.setItemText(0, QCoreApplication.translate("Sistema", u"Bomba 01", None))

        self.cons_cb_periodo.setItemText(0, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.cons_cb_periodo.setItemText(1, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.cons_cb_periodo.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.cons_cb_periodo.setItemText(3, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.cons_cb_periodo.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.cons_cb_periodo.setItemText(5, QCoreApplication.translate("Sistema", u"Selecionar Per\u00edodo", None))

        self.cons_btn_exportar.setText(QCoreApplication.translate("Sistema", u"Exportar", None))
        self.cons_btn_tab_ok.setText(QCoreApplication.translate("Sistema", u"OK", None))
        self.cons_cb_tab_filtro.setItemText(0, QCoreApplication.translate("Sistema", u"Bomba 01", None))

        self.cons_btn_tab_del.setText(QCoreApplication.translate("Sistema", u"Deletar", None))
        self.cons_btn_tab_detalhes.setText(QCoreApplication.translate("Sistema", u"Detalhes", None))
        self.cons_cb_tab_periodo.setItemText(0, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.cons_cb_tab_periodo.setItemText(1, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.cons_cb_tab_periodo.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.cons_cb_tab_periodo.setItemText(3, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.cons_cb_tab_periodo.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.cons_cb_tab_periodo.setItemText(5, QCoreApplication.translate("Sistema", u"Selecionar Per\u00edodo", None))

        ___qtablewidgetitem = self.cons_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Sistema", u"Data", None));
        ___qtablewidgetitem1 = self.cons_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Sistema", u"Bomba", None));
        ___qtablewidgetitem2 = self.cons_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Sistema", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem3 = self.cons_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Sistema", u"Litros", None));
        ___qtablewidgetitem4 = self.cons_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Sistema", u"Valor", None));
        ___qtablewidgetitem5 = self.cons_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Sistema", u"Dinheiro", None));
        ___qtablewidgetitem6 = self.cons_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Sistema", u"Pix", None));
        ___qtablewidgetitem7 = self.cons_tb.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Sistema", u"Cart\u00e3o", None));
        ___qtablewidgetitem8 = self.cons_tb.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Sistema", u"Resto", None));
        ___qtablewidgetitem9 = self.cons_tb.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Sistema", u"Retiradas", None));
        self.label_12.setText(QCoreApplication.translate("Sistema", u"Filtro:", None))
        self.cons_lb_periodo_2.setText(QCoreApplication.translate("Sistema", u"Periodo:", None))
        self.label_21.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.cons_btn_tab_ret.setText(QCoreApplication.translate("Sistema", u"Restiradas", None))
        self.cons_lb_periodo_5.setText(QCoreApplication.translate("Sistema", u"Funcion\u00e1rio:", None))
        self.label_22.setText(QCoreApplication.translate("Sistema", u"     Nome:", None))
        self.label_53.setText(QCoreApplication.translate("Sistema", u"     Descri\u00e7\u00e3o:", None))
        self.ln_cons_info_2.setText("")
        self.cons_lb_periodo_3.setText(QCoreApplication.translate("Sistema", u"Periodo:", None))
        self.cons_cb_tab_retiradas.setItemText(0, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.cons_cb_tab_retiradas.setItemText(1, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.cons_cb_tab_retiradas.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.cons_cb_tab_retiradas.setItemText(3, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.cons_cb_tab_retiradas.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.cons_cb_tab_retiradas.setItemText(5, QCoreApplication.translate("Sistema", u"Selecionar Per\u00edodo", None))

        self.label_23.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.cons_btn_ok_2.setText(QCoreApplication.translate("Sistema", u"OK", None))
        ___qtablewidgetitem10 = self.cons_tb_retiradas.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Sistema", u"Caixa", None));
        ___qtablewidgetitem11 = self.cons_tb_retiradas.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Sistema", u"Data", None));
        ___qtablewidgetitem12 = self.cons_tb_retiradas.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Sistema", u"Nome", None));
        ___qtablewidgetitem13 = self.cons_tb_retiradas.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Sistema", u"Valor", None));
        ___qtablewidgetitem14 = self.cons_tb_retiradas.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o", None));
        self.label_48.setText(QCoreApplication.translate("Sistema", u"     Filtro:", None))
        self.cons_ponto_cb_filtro.setItemText(0, QCoreApplication.translate("Sistema", u"Funcionario", None))

        self.cons_lb_periodo_4.setText(QCoreApplication.translate("Sistema", u"Periodo:", None))
        self.cons_ponto_cb_periodo.setItemText(0, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.cons_ponto_cb_periodo.setItemText(1, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.cons_ponto_cb_periodo.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.cons_ponto_cb_periodo.setItemText(3, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.cons_ponto_cb_periodo.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.cons_ponto_cb_periodo.setItemText(5, QCoreApplication.translate("Sistema", u"Selecionar Per\u00edodo", None))

        self.label_49.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.cons_ponto_btn_ok.setText(QCoreApplication.translate("Sistema", u"OK", None))
        ___qtablewidgetitem15 = self.cons_ponto_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Sistema", u"Data", None));
        ___qtablewidgetitem16 = self.cons_ponto_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Sistema", u"Funcionario", None));
        ___qtablewidgetitem17 = self.cons_ponto_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Sistema", u"Entrada 01", None));
        ___qtablewidgetitem18 = self.cons_ponto_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Sistema", u"Saida 01", None));
        ___qtablewidgetitem19 = self.cons_ponto_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Sistema", u"Entrada 02", None));
        ___qtablewidgetitem20 = self.cons_ponto_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Sistema", u"Saida 02", None));
        self.cons_lb.setText(QCoreApplication.translate("Sistema", u"     Consultas", None))
        self.cons_lb_nav.setText("")
        self.cons_btn_vendas.setText(QCoreApplication.translate("Sistema", u"Gr\u00e1ficos", None))
        self.cons_btn_tabela.setText(QCoreApplication.translate("Sistema", u"Tabelas", None))
        self.cons_btn_ponto.setText(QCoreApplication.translate("Sistema", u"Ponto", None))
        self.cons_btn_retiradas.setText(QCoreApplication.translate("Sistema", u"Retiradas", None))
        self.label_4.setText(QCoreApplication.translate("Sistema", u"Total:   ", None))
        self.cx_nome.setItemText(0, "")

        self.label_11.setText(QCoreApplication.translate("Sistema", u"Funcion\u00e1rio: ", None))
        self.label.setText(QCoreApplication.translate("Sistema", u"        Fechamento de Caixa", None))
        self.label_24.setText(QCoreApplication.translate("Sistema", u"Data:", None))
        self.label_31.setText("")
        self.label_40.setText("")
        self.label_8.setText(QCoreApplication.translate("Sistema", u"     Retiradas", None))
        self.label_2.setText(QCoreApplication.translate("Sistema", u"     Gasolina", None))
        self.cb_bomba.setItemText(0, "")

        self.label_9.setText(QCoreApplication.translate("Sistema", u"     Bomba: ", None))
        self.groupBox.setTitle(QCoreApplication.translate("Sistema", u"Anterior", None))
        self.ln_digi_anterior.setText("")
        self.label_15.setText(QCoreApplication.translate("Sistema", u"Digital: ", None))
        self.label_14.setText(QCoreApplication.translate("Sistema", u"Anal\u00f3gico: ", None))
        self.ln_ana_anterior.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Sistema", u"Fechamento", None))
        self.ln_ana_atual.setInputMask("")
        self.ln_ana_atual.setText("")
        self.label_18.setText(QCoreApplication.translate("Sistema", u"Digital: ", None))
        self.ln_digi_atual.setText("")
        self.label_19.setText(QCoreApplication.translate("Sistema", u"Anal\u00f3gico: ", None))
        self.btn_cx_inserir.setText(QCoreApplication.translate("Sistema", u"Inserir", None))
        self.groupBox_3.setTitle("")
        self.ln_cx_pix.setInputMask("")
        self.ln_cx_pix.setText("")
        self.label_27.setText(QCoreApplication.translate("Sistema", u"Litros", None))
        self.ln_cx_din.setInputMask("")
        self.ln_cx_din.setText("")
        self.ln_cx_resto_2.setText("")
        self.ln_cx_cartao.setInputMask("")
        self.ln_cx_cartao.setText("")
        self.ln_cx_valor.setText("")
        self.label_29.setText(QCoreApplication.translate("Sistema", u"Resto", None))
        self.label_30.setText(QCoreApplication.translate("Sistema", u"Dinheiro", None))
        self.label_47.setText(QCoreApplication.translate("Sistema", u"Pix", None))
        self.ln_cx_resto.setText("")
        self.label_28.setText(QCoreApplication.translate("Sistema", u"R$", None))
        self.label_51.setText(QCoreApplication.translate("Sistema", u"Cart\u00e3o", None))
        self.ln_cx_litros.setText("")
        self.label_52.setText(QCoreApplication.translate("Sistema", u"Total", None))
        self.label_54.setText(QCoreApplication.translate("Sistema", u"Retiradas", None))
        self.ln_cx_retiradas.setInputMask("")
        self.ln_cx_retiradas.setText(QCoreApplication.translate("Sistema", u"0.00", None))
        self.btn_cx_fechar.setText(QCoreApplication.translate("Sistema", u"Fechar", None))
        self.label_38.setText("")
        self.label_39.setText("")
        self.btn_cx_ret_inserir.setText(QCoreApplication.translate("Sistema", u"Inserir", None))
        self.groupBox_4.setTitle("")
        self.ln_cx_ter_valor.setText("")
        self.label_34.setText(QCoreApplication.translate("Sistema", u"Valor", None))
        self.label_35.setText(QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o", None))
        self.label_33.setText(QCoreApplication.translate("Sistema", u"Nome", None))
        self.cb_cx_nome.setItemText(0, "")

        self.ln_cx_desc.setText("")
        self.label_32.setText("")
        ___qtablewidgetitem21 = self.tb_cx.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Sistema", u"Nome", None));
        ___qtablewidgetitem22 = self.tb_cx.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Sistema", u"Valor", None));
        ___qtablewidgetitem23 = self.tb_cx.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o", None));
        self.cons_lb_3.setText(QCoreApplication.translate("Sistema", u"     Configura\u00e7\u00f5es", None))
        self.cons_lb_nav_2.setText("")
        self.config_comb_btn.setText(QCoreApplication.translate("Sistema", u"Combustivel", None))
        self.config_user_btn.setText(QCoreApplication.translate("Sistema", u"Usuarios", None))
        self.config_comb_voltar.setText("")
        self.config_comb_editar.setText(QCoreApplication.translate("Sistema", u"Alterar Pre\u00e7o", None))
        self.config_comb_info_2.setText(QCoreApplication.translate("Sistema", u"Informa\u00e7\u00f5es", None))
        self.config_comb_entrada.setText(QCoreApplication.translate("Sistema", u"Nova Entrada", None))
        self.config_user_voltar.setText("")
        self.config_user_novo_btn.setText(QCoreApplication.translate("Sistema", u"Novo", None))
        self.config_user_lista_2.setText(QCoreApplication.translate("Sistema", u"Lista", None))
        self.label_95.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Sistema", u"Tanque de Combustivel", None))
        self.label_97.setText(QCoreApplication.translate("Sistema", u"Tanque:", None))
        self.config_comb_edit_combustivel_3.setItemText(0, "")

        self.label_94.setText(QCoreApplication.translate("Sistema", u"     Quantidade(L): ", None))
        self.config_comb_edit_novo_3.setText("")
        self.label_109.setText("")
        self.label_92.setText("")
        self.label_110.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Sistema", u"Pre\u00e7o Combust\u00edvel", None))
        self.label_96.setText(QCoreApplication.translate("Sistema", u"Combustivel:", None))
        self.config_comb_edit_combustivel_2.setItemText(0, "")

        self.label_93.setText(QCoreApplication.translate("Sistema", u"     Valor:", None))
        self.config_comb_edit_novo_2.setText("")
        self.label_50.setText(QCoreApplication.translate("Sistema", u"Pre\u00e7o Combustivel", None))
        self.label_86.setText("")
        self.label_91.setText(QCoreApplication.translate("Sistema", u"Valor Novo:", None))
        self.label_105.setText("")
        self.config_comb_edit_antigo.setText("")
        self.config_comb_edit_btn.setText(QCoreApplication.translate("Sistema", u"Salvar", None))
        self.label_106.setText("")
        self.label_85.setText(QCoreApplication.translate("Sistema", u"Valor Antigo:", None))
        self.label_82.setText("")
        self.config_comb_edit_combustivel.setItemText(0, "")

        self.label_79.setText(QCoreApplication.translate("Sistema", u"Combustivel:", None))
        self.config_comb_edit_novo.setText("")
        self.label_55.setText(QCoreApplication.translate("Sistema", u"Entrada Combustivel", None))
        self.label_144.setText(QCoreApplication.translate("Sistema", u"Parcelamento", None))
        self.label_113.setText("")
        self.label_136.setText(QCoreApplication.translate("Sistema", u"Quantidade", None))
        self.label_141.setText("")
        self.config_comb_entrada_combustivel.setItemText(0, "")

        self.label_143.setText(QCoreApplication.translate("Sistema", u"Data entrega", None))
        self.config_comb_entrada_valor.setText("")
        self.label_108.setText(QCoreApplication.translate("Sistema", u"Valor da Nota", None))
        self.config_comb_entrada_quantidade.setText("")
        self.config_comb_entrada_parcelamento.setItemText(0, QCoreApplication.translate("Sistema", u"1", None))
        self.config_comb_entrada_parcelamento.setItemText(1, QCoreApplication.translate("Sistema", u"2", None))
        self.config_comb_entrada_parcelamento.setItemText(2, QCoreApplication.translate("Sistema", u"3", None))
        self.config_comb_entrada_parcelamento.setItemText(3, QCoreApplication.translate("Sistema", u"4", None))
        self.config_comb_entrada_parcelamento.setItemText(4, QCoreApplication.translate("Sistema", u"5", None))
        self.config_comb_entrada_parcelamento.setItemText(5, QCoreApplication.translate("Sistema", u"6", None))
        self.config_comb_entrada_parcelamento.setItemText(6, QCoreApplication.translate("Sistema", u"7", None))
        self.config_comb_entrada_parcelamento.setItemText(7, QCoreApplication.translate("Sistema", u"8", None))
        self.config_comb_entrada_parcelamento.setItemText(8, QCoreApplication.translate("Sistema", u"9", None))
        self.config_comb_entrada_parcelamento.setItemText(9, QCoreApplication.translate("Sistema", u"10", None))
        self.config_comb_entrada_parcelamento.setItemText(10, QCoreApplication.translate("Sistema", u"11", None))
        self.config_comb_entrada_parcelamento.setItemText(11, QCoreApplication.translate("Sistema", u"12", None))

        self.config_comb_edit_btn_2.setText(QCoreApplication.translate("Sistema", u"Salvar", None))
        self.label_88.setText("")
        self.label_112.setText("")
        self.label_142.setText(QCoreApplication.translate("Sistema", u"Combustivel", None))
        self.label_146.setText(QCoreApplication.translate("Sistema", u"Vencimento", None))
        self.cons_lb_2.setText(QCoreApplication.translate("Sistema", u"     Estoque", None))
        self.est_lb_nav.setText("")
        self.est_btn_entrada.setText(QCoreApplication.translate("Sistema", u"Entrada", None))
        self.est_btn_novo.setText(QCoreApplication.translate("Sistema", u"Novo", None))
        self.est_btn_consulta.setText(QCoreApplication.translate("Sistema", u"Consulta", None))
        self.label_26.setText(QCoreApplication.translate("Sistema", u"Cadastrar Novo Produto", None))
        self.label_70.setText(QCoreApplication.translate("Sistema", u"Quantidade:", None))
        self.label_75.setText(QCoreApplication.translate("Sistema", u"Pre\u00e7o Compra:      ", None))
        self.ln_est_produto.setText("")
        self.label_69.setText("")
        self.ln_est_pVenda.setText("")
        self.btn_est_cadastrar.setText(QCoreApplication.translate("Sistema", u"Cadastrar", None))
        self.label_71.setText(QCoreApplication.translate("Sistema", u"Marca:", None))
        self.est_cb_tipo.setItemText(0, "")

        self.ln_est_qnt.setText("")
        self.ln_est_pCompra.setText("")
        self.est_cb_marca.setItemText(0, "")

        self.label_68.setText("")
        self.label_73.setText(QCoreApplication.translate("Sistema", u"Cod. Barras:", None))
        self.label_77.setText(QCoreApplication.translate("Sistema", u"Tipo: ", None))
        self.ln_est_codBarras.setText("")
        self.label_72.setText(QCoreApplication.translate("Sistema", u"Produto:", None))
        self.label_76.setText(QCoreApplication.translate("Sistema", u"Pre\u00e7o Venda:", None))
        self.label_74.setText(QCoreApplication.translate("Sistema", u"Unidade: ", None))
        self.est_cb_unidade.setItemText(0, "")
        self.est_cb_unidade.setItemText(1, QCoreApplication.translate("Sistema", u"UNI", None))
        self.est_cb_unidade.setItemText(2, QCoreApplication.translate("Sistema", u"KG", None))
        self.est_cb_unidade.setItemText(3, QCoreApplication.translate("Sistema", u"CX", None))
        self.est_cb_unidade.setItemText(4, QCoreApplication.translate("Sistema", u"LT", None))

        self.label_36.setText(QCoreApplication.translate("Sistema", u"Nova Entrada", None))
        self.label_81.setText("")
        self.est_new_cb_produto.setItemText(0, "")

        self.est_new_ln_qnt.setText("")
        self.label_84.setText(QCoreApplication.translate("Sistema", u"Quantidade:", None))
        self.label_103.setText("")
        self.est_new_btn_cadastrar.setText(QCoreApplication.translate("Sistema", u"Cadastrar", None))
        self.label_83.setText("")
        self.label_78.setText(QCoreApplication.translate("Sistema", u"Produto:", None))
        self.label_104.setText("")
        self.label_37.setText(QCoreApplication.translate("Sistema", u"     Filtro:", None))
        self.est_const_cb_filtro.setItemText(0, QCoreApplication.translate("Sistema", u"Produto", None))
        self.est_const_cb_filtro.setItemText(1, QCoreApplication.translate("Sistema", u"Cod.", None))
        self.est_const_cb_filtro.setItemText(2, QCoreApplication.translate("Sistema", u"Tipo", None))
        self.est_const_cb_filtro.setItemText(3, QCoreApplication.translate("Sistema", u"Marca", None))
        self.est_const_cb_filtro.setItemText(4, QCoreApplication.translate("Sistema", u"Cod. Barras", None))

        self.est_const_ln_filtro.setText("")
        self.est_const_btn_pesquisar.setText(QCoreApplication.translate("Sistema", u"Pesquisar", None))
        self.est_const_btn_editar.setText(QCoreApplication.translate("Sistema", u"Editar", None))
        self.est_const_btn_deletar.setText(QCoreApplication.translate("Sistema", u"Deletar", None))
        ___qtablewidgetitem24 = self.est_consult_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Sistema", u"Cod.", None));
        ___qtablewidgetitem25 = self.est_consult_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Sistema", u"Tipo", None));
        ___qtablewidgetitem26 = self.est_consult_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Sistema", u"Marca", None));
        ___qtablewidgetitem27 = self.est_consult_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Sistema", u"Produto", None));
        ___qtablewidgetitem28 = self.est_consult_tab.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Sistema", u"Uni.", None));
        ___qtablewidgetitem29 = self.est_consult_tab.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Sistema", u"Qnt.", None));
        ___qtablewidgetitem30 = self.est_consult_tab.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Sistema", u"Cod. Barras", None));
        ___qtablewidgetitem31 = self.est_consult_tab.horizontalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Sistema", u"Valor Compra", None));
        ___qtablewidgetitem32 = self.est_consult_tab.horizontalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Sistema", u"Valor Venda", None));
        self.label_25.setText(QCoreApplication.translate("Sistema", u"Editar Dados", None))
        self.est_edt_ln_qnt.setText("")
        self.label_60.setText(QCoreApplication.translate("Sistema", u"Marca:", None))
        self.label_66.setText("")
        self.est_edt_ln_pCompra.setText("")
        self.label_64.setText(QCoreApplication.translate("Sistema", u"Quantidade:", None))
        self.est_edt_cb_marca.setItemText(0, "")

        self.est_edt_btn_salvar.setText(QCoreApplication.translate("Sistema", u"Salvar", None))
        self.est_edt_ln_produto.setText("")
        self.est_edt_ln_codBarras.setText("")
        self.label_67.setText("")
        self.est_edt_cb_tipo.setItemText(0, "")

        self.label_61.setText(QCoreApplication.translate("Sistema", u"Produto:", None))
        self.label_65.setText(QCoreApplication.translate("Sistema", u"Cod. Barras:", None))
        self.est_edt_btn_cancelar.setText(QCoreApplication.translate("Sistema", u"Cancelar", None))
        self.label_62.setText(QCoreApplication.translate("Sistema", u"Pre\u00e7o Compra:      ", None))
        self.est_edt_ln_pVenda.setText("")
        self.label_58.setText(QCoreApplication.translate("Sistema", u"Tipo: ", None))
        self.label_63.setText(QCoreApplication.translate("Sistema", u"Pre\u00e7o Venda:", None))
        self.label_90.setText(QCoreApplication.translate("Sistema", u"Unidade: ", None))
        self.est_edt_cb_unidade.setItemText(0, "")
        self.est_edt_cb_unidade.setItemText(1, QCoreApplication.translate("Sistema", u"UNI", None))
        self.est_edt_cb_unidade.setItemText(2, QCoreApplication.translate("Sistema", u"KG", None))
        self.est_edt_cb_unidade.setItemText(3, QCoreApplication.translate("Sistema", u"CX", None))
        self.est_edt_cb_unidade.setItemText(4, QCoreApplication.translate("Sistema", u"LT", None))

        ___qtablewidgetitem33 = self.vend_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Sistema", u"    Item    ", None));
        ___qtablewidgetitem34 = self.vend_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Sistema", u"    C\u00f3digo    ", None));
        ___qtablewidgetitem35 = self.vend_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem36 = self.vend_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Sistema", u"Uni.", None));
        ___qtablewidgetitem37 = self.vend_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Sistema", u"    Quantidade    ", None));
        ___qtablewidgetitem38 = self.vend_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Sistema", u"    Valor Unit\u00e1rio    ", None));
        ___qtablewidgetitem39 = self.vend_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Sistema", u"    Subtotal    ", None));
        self.vend_btn_finalizar.setText(QCoreApplication.translate("Sistema", u"Finalizar", None))
        self.vend_btn_cancelar.setText(QCoreApplication.translate("Sistema", u"Deletar", None))
        self.label_46.setText("")
        self.label_43.setText(QCoreApplication.translate("Sistema", u"Total da Compra  ", None))
        self.label_44.setText("")
        self.label_3.setText(QCoreApplication.translate("Sistema", u"Codigo/Descri\u00e7\u00e3o", None))
        self.label_7.setText(QCoreApplication.translate("Sistema", u"Quantidade", None))
        self.label_41.setText(QCoreApplication.translate("Sistema", u"Pre\u00e7o", None))
        self.label_42.setText(QCoreApplication.translate("Sistema", u"Subtotal", None))
        self.vend_btn_adicionar.setText(QCoreApplication.translate("Sistema", u"Adicionar", None))
        self.label_45.setText(QCoreApplication.translate("Sistema", u"     PDV", None))
        self.label_56.setText("")
        self.label_89.setText(QCoreApplication.translate("Sistema", u"Caixa Posto", None))
        self.fin_home_cx_posto.setText(QCoreApplication.translate("Sistema", u"R$ 1000,00", None))
        self.label_119.setText(QCoreApplication.translate("Sistema", u"R$ 100,00", None))
        self.label_118.setText(QCoreApplication.translate("Sistema", u"Restante do m\u00eas:", None))
        self.label_120.setText(QCoreApplication.translate("Sistema", u"R$ 600,00", None))
        self.pushButton_8.setText("")
        self.label_117.setText(QCoreApplication.translate("Sistema", u"A vencer hoje", None))
        self.label_87.setText("")
        self.label_98.setText(QCoreApplication.translate("Sistema", u"Conta Banc\u00e1ria", None))
        self.fin_home_cx_banco.setText(QCoreApplication.translate("Sistema", u"R$ 1000,00", None))
        self.label_102.setText(QCoreApplication.translate("Sistema", u"Fluxo de Caixa", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Sistema", u"Ultimo M\u00eas", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Sistema", u"Ultimo Trimestre", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Sistema", u"Ultimo Semestre", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Sistema", u"Ultimo Ano", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Sistema", u"Selecionar Periodo", None))

        self.label_179.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.financeiro_fluxo_pesq.setText("")
        self.label_145.setText(QCoreApplication.translate("Sistema", u"Receitas", None))
        self.financeiro_fluxo_receita.setText(QCoreApplication.translate("Sistema", u"R$ 000,00", None))
        self.label_147.setText(QCoreApplication.translate("Sistema", u"Despesas", None))
        self.financeiro_fluxo_despesa.setText(QCoreApplication.translate("Sistema", u"R$ 000,00", None))
        self.label_150.setText(QCoreApplication.translate("Sistema", u"Entradas", None))
        self.financeiro_fluxo_entrada.setText(QCoreApplication.translate("Sistema", u"R$ 000,00", None))
        self.label_165.setText(QCoreApplication.translate("Sistema", u"Total", None))
        self.financeiro_fluxo_total.setText(QCoreApplication.translate("Sistema", u"R$ 000,00", None))
        self.label_107.setText(QCoreApplication.translate("Sistema", u"Ultimas Movimenta\u00e7\u00f5es", None))
        self.label_121.setText(QCoreApplication.translate("Sistema", u"Vendas Combust\u00edvel", None))
        self.pushButton.setText("")
        self.label_116.setText(QCoreApplication.translate("Sistema", u"R$ 984,00", None))
        self.label_126.setText(QCoreApplication.translate("Sistema", u"Pagamento Internet", None))
        self.pushButton_4.setText("")
        self.label_127.setText(QCoreApplication.translate("Sistema", u"R$ 183,00", None))
        self.label_128.setText(QCoreApplication.translate("Sistema", u"Dep\u00f3sito Conta", None))
        self.pushButton_5.setText("")
        self.label_129.setText(QCoreApplication.translate("Sistema", u"R$ 1320,00", None))
        self.label_130.setText(QCoreApplication.translate("Sistema", u"Vendas Combust\u00edvel", None))
        self.pushButton_6.setText("")
        self.label_131.setText(QCoreApplication.translate("Sistema", u"R$ 658,00", None))
        self.label_122.setText(QCoreApplication.translate("Sistema", u"R$ 100,00", None))
        self.label_123.setText(QCoreApplication.translate("Sistema", u"Restante do m\u00eas:", None))
        self.label_124.setText(QCoreApplication.translate("Sistema", u"R$ 600,00", None))
        self.pushButton_9.setText("")
        self.label_125.setText(QCoreApplication.translate("Sistema", u"Contas pagas", None))
        self.label_169.setText(QCoreApplication.translate("Sistema", u"MOVIMENTA\u00c7\u00c3O:     ", None))
        self.comboBox_8.setItemText(0, "")
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Sistema", u"Despesa", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("Sistema", u"Entrada", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("Sistema", u"Transfer\u00eancia", None))

        self.label_170.setText(QCoreApplication.translate("Sistema", u"FILTRO:     ", None))
        self.comboBox_9.setItemText(0, "")
        self.comboBox_9.setItemText(1, QCoreApplication.translate("Sistema", u"Conta", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o", None))

        self.comboBox_11.setItemText(0, "")

        self.label_171.setText(QCoreApplication.translate("Sistema", u"PERIODO:     ", None))
        self.comboBox_10.setItemText(0, "")
        self.comboBox_10.setItemText(1, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("Sistema", u"Selecionar Periodo", None))

        self.label_111.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.label_172.setText(QCoreApplication.translate("Sistema", u"FILTRO:     ", None))
        self.comboBox_13.setItemText(0, "")
        self.comboBox_13.setItemText(1, QCoreApplication.translate("Sistema", u"Status", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("Sistema", u"Conta", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o", None))

        self.comboBox_14.setItemText(0, "")

        self.label_173.setText(QCoreApplication.translate("Sistema", u"PERIODO:     ", None))
        self.comboBox_12.setItemText(0, "")
        self.comboBox_12.setItemText(1, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.comboBox_12.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.comboBox_12.setItemText(5, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.comboBox_12.setItemText(6, QCoreApplication.translate("Sistema", u"Selecionar Periodo", None))

        self.label_138.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.label_176.setText(QCoreApplication.translate("Sistema", u"FILTRO:     ", None))
        self.comboBox_18.setItemText(0, "")
        self.comboBox_18.setItemText(1, QCoreApplication.translate("Sistema", u"Tipo", None))
        self.comboBox_18.setItemText(2, QCoreApplication.translate("Sistema", u"Conta", None))
        self.comboBox_18.setItemText(3, QCoreApplication.translate("Sistema", u"Descri\u00e7\u00e3o", None))

        self.comboBox_19.setItemText(0, "")

        self.label_177.setText(QCoreApplication.translate("Sistema", u"PERIODO:     ", None))
        self.comboBox_20.setItemText(0, "")
        self.comboBox_20.setItemText(1, QCoreApplication.translate("Sistema", u"Dia Atual", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("Sistema", u"Ultima Semana", None))
        self.comboBox_20.setItemText(3, QCoreApplication.translate("Sistema", u"Ultima Quinzena", None))
        self.comboBox_20.setItemText(4, QCoreApplication.translate("Sistema", u"M\u00eas Atual", None))
        self.comboBox_20.setItemText(5, QCoreApplication.translate("Sistema", u"M\u00eas Anterior", None))
        self.comboBox_20.setItemText(6, QCoreApplication.translate("Sistema", u"Selecionar Periodo", None))

        self.label_137.setText(QCoreApplication.translate("Sistema", u"\u00e0", None))
        self.pushButton_17.setText("")
        ___qtablewidgetitem40 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Sistema", u"VENCIMENTO", None));
        ___qtablewidgetitem41 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Sistema", u"TIPO", None));
        ___qtablewidgetitem42 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Sistema", u"VALOR", None));
        ___qtablewidgetitem43 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Sistema", u"CONTA", None));
        ___qtablewidgetitem44 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Sistema", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem45 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Sistema", u"New Row", None));
        ___qtablewidgetitem46 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Sistema", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem47 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Sistema", u"10/12/2021", None));
        ___qtablewidgetitem48 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Sistema", u"Combustivel", None));
        ___qtablewidgetitem49 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Sistema", u"R$ 10000,00", None));
        ___qtablewidgetitem50 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Sistema", u"Conta Inter", None));
        ___qtablewidgetitem51 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Sistema", u"BOLETO COMPRA GASOLINA", None));
        ___qtablewidgetitem52 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Sistema", u"13/12/2021", None));
        ___qtablewidgetitem53 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Sistema", u"Sal\u00e1rio", None));
        ___qtablewidgetitem54 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Sistema", u"R$ 1200,00", None));
        ___qtablewidgetitem55 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Sistema", u"Conta Inter", None));
        ___qtablewidgetitem56 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Sistema", u"PAGAMENTO SAL\u00c1RIO JOAQUIM REFERENTE AO M\u00caS DE NOVEMBRO", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem57 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Sistema", u"DATA", None));
        ___qtablewidgetitem58 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Sistema", u"VALOR", None));
        ___qtablewidgetitem59 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Sistema", u"CONTA", None));
        ___qtablewidgetitem60 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Sistema", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem61 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Sistema", u"New Row", None));
        ___qtablewidgetitem62 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Sistema", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem63 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Sistema", u"10/12/2021", None));
        ___qtablewidgetitem64 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Sistema", u"R$ 10000,00", None));
        ___qtablewidgetitem65 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Sistema", u"Conta Inter", None));
        ___qtablewidgetitem66 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Sistema", u"Combustivel", None));
        ___qtablewidgetitem67 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Sistema", u"13/12/2021", None));
        ___qtablewidgetitem68 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Sistema", u"R$ 1200,00", None));
        ___qtablewidgetitem69 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("Sistema", u"Conta Inter", None));
        ___qtablewidgetitem70 = self.tableWidget_2.item(1, 3)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("Sistema", u"Sal\u00e1rio", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_174.setText(QCoreApplication.translate("Sistema", u"TOTAL:     ", None))
        self.label_139.setText("")
        ___qtablewidgetitem71 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("Sistema", u"DATA", None));
        ___qtablewidgetitem72 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("Sistema", u"STATUS", None));
        ___qtablewidgetitem73 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("Sistema", u"DE", None));
        ___qtablewidgetitem74 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("Sistema", u"PARA", None));
        ___qtablewidgetitem75 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Sistema", u"VALOR", None));
        ___qtablewidgetitem76 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("Sistema", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem77 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("Sistema", u"New Row", None));
        ___qtablewidgetitem78 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("Sistema", u"New Row", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem79 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("Sistema", u"10/12/2021", None));
        ___qtablewidgetitem80 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("Sistema", u"pago", None));
        ___qtablewidgetitem81 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("Sistema", u"Combustivel", None));
        ___qtablewidgetitem82 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("Sistema", u"R$ 10000,00", None));
        ___qtablewidgetitem83 = self.tableWidget_3.item(0, 4)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("Sistema", u"Conta Inter", None));
        ___qtablewidgetitem84 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("Sistema", u"BOLETO COMPRA GASOLINA", None));
        ___qtablewidgetitem85 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("Sistema", u"13/12/2021", None));
        ___qtablewidgetitem86 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("Sistema", u"em aberto", None));
        ___qtablewidgetitem87 = self.tableWidget_3.item(1, 2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("Sistema", u"Sal\u00e1rio", None));
        ___qtablewidgetitem88 = self.tableWidget_3.item(1, 3)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("Sistema", u"R$ 1200,00", None));
        ___qtablewidgetitem89 = self.tableWidget_3.item(1, 4)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("Sistema", u"Conta Inter", None));
        ___qtablewidgetitem90 = self.tableWidget_3.item(1, 5)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("Sistema", u"PAGAMENTO SAL\u00c1RIO JOAQUIM REFERENTE AO M\u00caS DE NOVEMBRO", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.label_168.setText(QCoreApplication.translate("Sistema", u"MOVIMENTA\u00c7\u00c3O:     ", None))
        self.fin_novo_mov.setItemText(0, QCoreApplication.translate("Sistema", u"DESPESA", None))
        self.fin_novo_mov.setItemText(1, QCoreApplication.translate("Sistema", u"ENTRADA", None))
        self.fin_novo_mov.setItemText(2, QCoreApplication.translate("Sistema", u"TRANSFER\u00caNCIA", None))

        self.label_160.setText("")
        self.pushButton_13.setText("")
        self.label_161.setText("")
        self.label_162.setText("")
        self.pushButton_14.setText("")
        self.label_163.setText("")
        self.label_156.setText("")
        self.pushButton_11.setText("")
        self.label_157.setText("")
        self.label_158.setText("")
        self.pushButton_12.setText("")
        self.label_159.setText("")
        self.label_166.setText("")
        self.pushButton_16.setText("")
        self.label_167.setText("")
        self.label_114.setText(QCoreApplication.translate("Sistema", u"INSERIR DESPESA", None))
        self.fin_novo_desp_conta.setItemText(0, "")
        self.fin_novo_desp_conta.setItemText(1, QCoreApplication.translate("Sistema", u"Conta Inter", None))
        self.fin_novo_desp_conta.setItemText(2, QCoreApplication.translate("Sistema", u"Caixa Posto", None))

        self.label_80.setText(QCoreApplication.translate("Sistema", u"TIPO:     ", None))
        self.label_100.setText(QCoreApplication.translate("Sistema", u"VALOR:     ", None))
        self.label_57.setText(QCoreApplication.translate("Sistema", u"VENCIMENTO:     ", None))
        self.fin_novo_desp_btn_inserir.setText(QCoreApplication.translate("Sistema", u"INSERIR", None))
        self.fin_novo_desp_tipo.setItemText(0, "")

        self.label_99.setText(QCoreApplication.translate("Sistema", u"DESCRI\u00c7\u00c3O:     ", None))
        self.label_101.setText(QCoreApplication.translate("Sistema", u"CONTA:     ", None))
        self.label_140.setText(QCoreApplication.translate("Sistema", u"STATUS:     ", None))
        self.fin_novo_desp_status.setItemText(0, "")
        self.fin_novo_desp_status.setItemText(1, QCoreApplication.translate("Sistema", u"Em aberto", None))
        self.fin_novo_desp_status.setItemText(2, QCoreApplication.translate("Sistema", u"Pago", None))

        self.fin_novo_transf_de.setItemText(0, "")
        self.fin_novo_transf_de.setItemText(1, QCoreApplication.translate("Sistema", u"Conta Inter", None))
        self.fin_novo_transf_de.setItemText(2, QCoreApplication.translate("Sistema", u"Caixa Posto", None))

        self.label_135.setText(QCoreApplication.translate("Sistema", u"DESCRI\u00c7\u00c3O:     ", None))
        self.fin_novo_transf_btn_inserir.setText(QCoreApplication.translate("Sistema", u"INSERIR", None))
        self.label_115.setText(QCoreApplication.translate("Sistema", u"TRANSFERENCIA", None))
        self.label_133.setText(QCoreApplication.translate("Sistema", u"VALOR:     ", None))
        self.label_132.setText(QCoreApplication.translate("Sistema", u"DE:     ", None))
        self.fin_novo_transf_para.setItemText(0, "")
        self.fin_novo_transf_para.setItemText(1, QCoreApplication.translate("Sistema", u"Conta Inter", None))
        self.fin_novo_transf_para.setItemText(2, QCoreApplication.translate("Sistema", u"Caixa Posto", None))

        self.label_134.setText(QCoreApplication.translate("Sistema", u"DATA :     ", None))
        self.label_155.setText(QCoreApplication.translate("Sistema", u"PARA:     ", None))
        self.label_151.setText(QCoreApplication.translate("Sistema", u"VALOR:     ", None))
        self.label_149.setText(QCoreApplication.translate("Sistema", u"INSERIR ENTRADA", None))
        self.label_153.setText(QCoreApplication.translate("Sistema", u"DESCRI\u00c7\u00c3O:     ", None))
        self.fin_novo_ent_conta.setItemText(0, "")
        self.fin_novo_ent_conta.setItemText(1, QCoreApplication.translate("Sistema", u"Conta Inter", None))
        self.fin_novo_ent_conta.setItemText(2, QCoreApplication.translate("Sistema", u"Caixa Posto", None))

        self.label_154.setText(QCoreApplication.translate("Sistema", u"CONTA:     ", None))
        self.fin_novo_ent_btn_inserir.setText(QCoreApplication.translate("Sistema", u"INSERIR", None))
        self.label_152.setText(QCoreApplication.translate("Sistema", u"DATA:     ", None))
        self.label_175.setText(QCoreApplication.translate("Sistema", u"ULTIMOS LAN\u00c7AMENTOS", None))
        self.fin_btn_home.setText(QCoreApplication.translate("Sistema", u"Home", None))
        self.cons_lb_5.setText(QCoreApplication.translate("Sistema", u"     Financeiro", None))
        self.est_lb_nav_3.setText("")
        self.fin_btn_mov.setText(QCoreApplication.translate("Sistema", u"Movimenta\u00e7\u00f5es", None))
        self.fin_btn_novo.setText(QCoreApplication.translate("Sistema", u"Novo", None))
        self.in_usuario.setPlaceholderText(QCoreApplication.translate("Sistema", u"Usu\u00e1rio", None))
        self.lb_info_2.setText("")
        self.btn_entrar.setText(QCoreApplication.translate("Sistema", u"Entrar", None))
        self.lb_info.setText("")
        self.in_senha.setPlaceholderText(QCoreApplication.translate("Sistema", u"Senha", None))
        self.label_6.setText(QCoreApplication.translate("Sistema", u"Bem Vindo", None))
        self.lb_info_3.setText("")
        self.label_5.setText("")
    # retranslateUi

