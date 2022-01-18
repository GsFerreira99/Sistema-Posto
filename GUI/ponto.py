# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_pontoKVeJPo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 260)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(173, 173, 173, 255), stop:1 rgba(231, 231, 231, 255));")
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.label_10 = QLabel(MainWindow)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QSize(16777215, 10))
        font = QFont()
        font.setFamily(u"Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)

        self.ponto_ln_entrada = QLabel(MainWindow)
        self.ponto_ln_entrada.setObjectName(u"ponto_ln_entrada")
        sizePolicy.setHeightForWidth(self.ponto_ln_entrada.sizePolicy().hasHeightForWidth())
        self.ponto_ln_entrada.setSizePolicy(sizePolicy)
        self.ponto_ln_entrada.setMaximumSize(QSize(16777215, 40))
        self.ponto_ln_entrada.setFont(font)
        self.ponto_ln_entrada.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.ponto_ln_entrada.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ponto_ln_entrada, 3, 1, 1, 1)

        self.ponto_ln_entrada_2 = QLabel(MainWindow)
        self.ponto_ln_entrada_2.setObjectName(u"ponto_ln_entrada_2")
        sizePolicy.setHeightForWidth(self.ponto_ln_entrada_2.sizePolicy().hasHeightForWidth())
        self.ponto_ln_entrada_2.setSizePolicy(sizePolicy)
        self.ponto_ln_entrada_2.setMaximumSize(QSize(16777215, 30))
        self.ponto_ln_entrada_2.setFont(font)
        self.ponto_ln_entrada_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.ponto_ln_entrada_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ponto_ln_entrada_2, 4, 1, 1, 1)

        self.label_6 = QLabel(MainWindow)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.ponto_ln_saida = QLabel(MainWindow)
        self.ponto_ln_saida.setObjectName(u"ponto_ln_saida")
        sizePolicy.setHeightForWidth(self.ponto_ln_saida.sizePolicy().hasHeightForWidth())
        self.ponto_ln_saida.setSizePolicy(sizePolicy)
        self.ponto_ln_saida.setMaximumSize(QSize(16777215, 40))
        self.ponto_ln_saida.setFont(font)
        self.ponto_ln_saida.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.ponto_ln_saida.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ponto_ln_saida, 3, 2, 1, 1)

        self.label_5 = QLabel(MainWindow)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_7 = QLabel(MainWindow)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Noto Serif")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494318, y1:1, x2:0.477, y2:0, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(75, 75, 75, 255));\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.ponto_btn = QPushButton(MainWindow)
        self.ponto_btn.setObjectName(u"ponto_btn")
        self.ponto_btn.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.ponto_btn.setFont(font2)
        self.ponto_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 209, 22, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 205, 0, 239), stop:1 rgba(255, 237, 162, 255));\n"
"	border: 1px solid rgb(135, 135, 135);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ponto_btn, 5, 0, 1, 3)

        self.label_8 = QLabel(MainWindow)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.ponto_ln_saida_2 = QLabel(MainWindow)
        self.ponto_ln_saida_2.setObjectName(u"ponto_ln_saida_2")
        sizePolicy.setHeightForWidth(self.ponto_ln_saida_2.sizePolicy().hasHeightForWidth())
        self.ponto_ln_saida_2.setSizePolicy(sizePolicy)
        self.ponto_ln_saida_2.setMaximumSize(QSize(16777215, 30))
        self.ponto_ln_saida_2.setFont(font)
        self.ponto_ln_saida_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.ponto_ln_saida_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ponto_ln_saida_2, 4, 2, 1, 1)

        #MainWindow.setCentralWidget(MainWindow)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText("")
        self.ponto_ln_entrada.setText("")
        self.ponto_ln_entrada_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.ponto_ln_saida.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Registro de Ponto", None))
        self.ponto_btn.setText(QCoreApplication.translate("MainWindow", u"Bater Ponto", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ponto_ln_saida_2.setText("")
    # retranslateUi

