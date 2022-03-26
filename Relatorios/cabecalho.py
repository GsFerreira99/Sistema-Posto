from tkinter import font
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import DataBase.DataBase as db
from Funcoes.genericas import caminho_db

from Relatorios.pdf_branco import Pdf
    
    
class RelatorioGeral(Pdf):

    def __init__(self, nome_arquivo, datas):
        super().__init__(nome_arquivo)

        self.y = 720
        self.datas = datas
        self.db = db.DataBase(caminho_db())
        self.consultar_dados()
        self.gerar()

    def consultar_dados(self):
        self.dados = {
            'titulo':'GERAL',
            'data_ini':self.datas[0],
            'data_fim':self.datas[1],
            'pagamentos':{
                },
            'tanque':{
                1:{'titulo':'GASOLINA COMUM', 'valor': 0}
                },
            'vendas':{
                1:{'titulo':'LITROS VENDIDOS', 'valor': 0},
                2:{'titulo':'DINHEIRO', 'valor': 0},
                3:{'titulo':'CARTÃO', 'valor': 0},
                4:{'titulo':'PIX', 'valor': 0},
                5:{'titulo':'TOTAL', 'valor': 0}
            },
            }

        self.dados_tanque()
        self.dados_vendas()
        self.dados_pagamentos()

        
    def dados_tanque(self):
        dados = self.db.select_generico("SELECT quantidade FROM Valor_combustivel WHERE codigo=1")
        tanque = self.dados['tanque']
        for i in dados:
            tanque[1]['valor'] = self.litro(i[0])

    def dados_pagamentos(self):
        tipos = self.db.select_generico("SELECT DISTINCT tipo FROM Despesas")
        dados = self.db.select_generico("SELECT tipo, valor FROM Despesas WHERE data BETWEEN '{}' AND '{}'".format(self.datas[0],self.datas[1]))
        pagamentos = self.dados['pagamentos']
        for j in tipos:
            pagamentos[j[0]] = {'titulo': j[0], 'valor': 0}
        for i in dados:
            pagamentos[i[0]]['valor'] += i[1]

        total = {'titulo': 'TOTAL', 'valor': 0}
        for i in pagamentos.values():
            total['valor'] += i['valor']

        pagamentos['TOTAL'] = total
        
        for i in pagamentos.values():
            i['valor'] = self.dinheiro(i['valor'])

    def dados_vendas(self):
        dados = self.db.select_generico("SELECT litros, dinheiro_caixa, cartao, pix, total FROM Caixa WHERE data BETWEEN '{}' AND '{}'".format(self.datas[0],self.datas[1]))
        vendas = self.dados['vendas']
        for i in dados:
            vendas[1]['valor'] += i[0]
            vendas[2]['valor'] += i[1]
            vendas[3]['valor'] += i[2]
            vendas[4]['valor'] += i[3]
            vendas[5]['valor'] += i[4]

        vendas[1]['valor'] = self.litro(vendas[1]['valor'])
        vendas[2]['valor'] = self.dinheiro(vendas[2]['valor'])
        vendas[3]['valor'] = self.dinheiro(vendas[3]['valor'])
        vendas[4]['valor'] = self.dinheiro(vendas[4]['valor'])
        vendas[5]['valor'] = self.dinheiro(vendas[5]['valor'])

    def gerar(self):
        self.can = canvas.Canvas(self.packet, pagesize=letter)
        self.preencher_cabecalho()
        self.vendas()
        self.tanque()
        self.pagamentos()
        self.can.save()
        self.gerar_relatorio_mensal()

    
    def preencher_cabecalho(self):
        self.font(26)
        self.can.drawRightString(320, 790, f"RELATÓRIO {self.dados['titulo']}")
        self.font(10)
        self.can.drawRightString(570, 790, f"Periodo: {self.dados['data_ini']} à {self.dados['data_fim']}")

    def vendas(self):
        self.titulo('VENDAS')
        for i in self.dados['vendas'].values():
            self.campo(i['titulo'], i['valor'])

        self.mudarY(-50)

    def tanque(self):
            self.titulo('TANQUE')
            for i in self.dados['tanque'].values():
                self.campo(i['titulo'], i['valor'])
            self.mudarY(-50)

    def pagamentos(self):
            self.titulo('PAGAMENTOS')
            for i in self.dados['pagamentos'].values():
                self.campo(i['titulo'], i['valor'])
            self.mudarY(-50)


