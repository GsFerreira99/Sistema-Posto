from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
import datetime

def inserir_dados_cb(combo_box, dados):
    combo_box.clear()
    combo_box.addItem("")
    for i in dados:
        combo_box.addItem(str(i[0]))

def limpar_campos(campos):
    for campo in campos:
        campo.setText("")

def preencher_ln(campos, dados):
    for i, campo in enumerate(campos):
        campo.setText(str(dados[i]))
    
def preencher_cb(campos, dados):
    for i, campo in enumerate(campos):
        campo.setCurrentText(str(dados[i]))

def limpar_tabela(tabela):
    while (tabela.rowCount() > 0):
        tabela.removeRow(0)

def preencher_tabela(dados, tabela):
    for i, j in enumerate(dados):
        rowPosition = tabela.rowCount()
        tabela.insertRow(rowPosition)
        for i, s in enumerate(j):
            dado = QTableWidgetItem(str(s))
            dado.setTextAlignment(Qt.AlignCenter)
            tabela.setItem(rowPosition, i, dado)

def receber_dados_campos(campos):
    return campos

def converter_string_para_float(n):
    try:
        n = n.replace(",", ".")
        return float(n)
    except AttributeError:
        return float(n)

def mascara_dinheiro(num):
    try:
        n = f"{num:.2f}"
        n.replace(".", ",")
        return "R$ " + n
    except AttributeError:
        return num

def remover_masc_dinheiro(num):
    try:
        n = num.replace("R$ ", "")
        return float(n)
    except AttributeError:
        return num

def atualizar_cb(db, querry, widget):
        dados = db.querry_generica(querry)
        inserir_dados_cb(widget, dados)

def caminho_db():
    #file = resource_filename(__name__, 'DataBase/caminho_db.txt')
    with open('DataBase/caminho_db.txt', "r") as db:
        caminho = db.readline()
        #caminho.replace("/", '\')
        return caminho

def calculo_horas(dados):
    teste = dados
    horarios = []
    for i in teste:
        
        if i == "":
            i = "00:00:00"
        hora = i.split(':')
        horario = datetime.datetime(1, 1, 1, int(hora[0]), int(hora[1]), int(hora[2]))
        horarios.append(horario)
    
    if horarios[0] > horarios[1]:
        total = datetime(1, 1, 1, 0, 0, 0)
    elif horarios[2] > horarios[3]:
        total = (horarios[1] - horarios[0])
    else:
        total = (horarios[1] - horarios[0]) + (horarios[3] - horarios[2])

    return total

def verificar_vazio(dados):
    for i in dados:
        if i == "":
            return True
    return False