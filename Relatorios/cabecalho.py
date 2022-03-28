from tkinter import font
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import DataBase.DataBase as db
from Funcoes.genericas import caminho_db

from Relatorios.pdf_branco import Pdf
    
    
class RelatorioGeral(Pdf):

    def __init__(self, nome_arquivo, datas):
        super().__init__(nome_arquivo)

        self.y = 730
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
                1:{'titulo':'GASOLINA INICIAL', 'valor': 0},
                2:{'titulo':'GASOLINA ATUAL', 'valor': 0},
                },
            'entradas_tanque':{
                0:{'data':'','combustivel':'','quantidade':'','valor_nota':''}
            },
            'entradas_tanque_total':0,
            'vendas':{
                1:{'titulo':'LITROS VENDIDOS', 'valor': 0},
                2:{'titulo':'DINHEIRO', 'valor': 0},
                3:{'titulo':'CARTÃO', 'valor': 0},
                4:{'titulo':'PIX', 'valor': 0},
                5:{'titulo':'TOTAL', 'valor': 0}
            },
            'entrada_total':0,
            'entradas':{
                0:{'data':'', 'descrição': '', 'valor': ''}
            },
            }

        self.dados_tanque()
        self.dados_vendas()
        self.dados_pagamentos()
        self.dados_entradas()
        self.dados_tanque_entrada()

        
    def dados_tanque(self):
        dados = self.db.select_generico("SELECT quantidade FROM Valor_combustivel WHERE codigo=1")
        vendas = self.db.select_generico(f"SELECT litros FROM Caixa WHERE data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}'")
        entrada = self.db.select_generico(f"SELECT data, combustivel, quantidade, valor_nota FROM entrada_combustivel WHERE data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}'")
        tanque = self.dados['tanque']
        total = 0
        for i in vendas:
            total+= i[0]
        for i in entrada:
            total-= i[2]


        tanque[1]['valor'] = self.litro(total + dados[0][0])
        tanque[2]['valor'] = self.litro(dados[0][0])

    def dados_tanque_entrada(self):
        entrada = self.db.select_generico(f"SELECT data, combustivel, quantidade, valor_nota FROM entrada_combustivel WHERE data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}'")
        entrada_tanque = self.dados['entradas_tanque']
        total = 0

        for j, i in enumerate(entrada):
            entrada_tanque[j]['data'] = i[0]
            entrada_tanque[j]['combustivel'] = i[1]
            entrada_tanque[j]['quantidade'] = self.litro(i[2])
            entrada_tanque[j]['valor_nota'] = self.dinheiro(i[3])
            total += i[2]

        self.dados['entradas_tanque_total'] = self.litro(total)

    def dados_entradas(self):
        dados = self.db.select_generico(f"SELECT data, descricao, valor FROM Entrada WHERE data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}'")
        entrada = self.dados['entradas']
        total = 0
        for i, j in enumerate(dados):
            entrada[i]['data'] = j[0]
            entrada[i]['descrição'] = j[1]
            entrada[i]['valor'] = self.dinheiro(j[2])
            total+= j[2]
        self.dados['entrada_total'] = self.dinheiro(total)

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
        self.tanque_entrada()
        self.entradas()
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
        self.mudarY(-40)

    def tanque(self):
            self.titulo('TANQUE')
            for i in self.dados['tanque'].values():
                self.campo(i['titulo'], i['valor'])
            self.mudarY(-20)

    def tanque_entrada(self):
            self.titulo('ENTRADAS COMBUSTIVEL',x=70, font=10)
            self.linhas_tabela_tanque(['DATA', 'COMBUSTIVEL', 'QUANTIDADE', 'VALOR'], font=10)
            for i in self.dados['entradas_tanque'].values():
                self.linhas_tabela_tanque([i['data'], i['combustivel'], i['quantidade'], i['valor_nota']],y=-15, font=10)
            self.total_tabela_tanque(self.dados['entradas_tanque_total'], font=10)
            self.mudarY(-40)

    def entradas(self):
            self.titulo('ENTRADA CAPITAL')
            self.linhas_tabela(['DATA', 'DESCRIÇÃO', 'VALOR'])
            for i in self.dados['entradas'].values():
                self.linhas_tabela([i['data'], i['descrição'], i['valor']], font=10)
            self.total_tabela(self.dados['entrada_total'], font=10)
            self.mudarY(-40)

    def pagamentos(self):
            self.titulo('PAGAMENTOS')
            for i in self.dados['pagamentos'].values():
                self.campo(i['titulo'], i['valor'])
            self.mudarY(-40)


