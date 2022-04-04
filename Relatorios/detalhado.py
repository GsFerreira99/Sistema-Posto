from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import DataBase.DataBase as db
from Funcoes.genericas import caminho_db

from Relatorios.pdf_branco import Pdf
    
    
class RelatorioDetalhado(Pdf):

    def __init__(self, nome_arquivo, datas):
        super().__init__(nome_arquivo)

        self.y = 770
        self.datas = datas
        self.db = db.DataBase(caminho_db())
        self.consultar_dados()
        self.gerar()

    def consultar_dados(self):
        self.dados = {}

        self.dados_pagamentos()

    def dados_pagamentos(self):
        tipos = self.db.select_generico("SELECT DISTINCT tipo FROM Despesas WHERE status ='Pago' AND data BETWEEN '{}' AND '{}'".format(self.datas[0],self.datas[1]))
        dados = self.db.select_generico("SELECT data, nome, descricao, valor, tipo, categoria FROM Despesas WHERE status ='Pago' AND data BETWEEN '{}' AND '{}'".format(self.datas[0],self.datas[1]))

        for j in tipos:
            self.dados[j[0]] = {}

        for key in self.dados.keys():
            for indice, value in enumerate(dados):
                self.dados[key][value[5]] = {}
                if value[5] == None:
                    self.dados[key]['OUTROS'] = {}
                
        for key in self.dados.keys():
            for indice, value in enumerate(dados): 
                if key == value[4]:
                    if value[5] != None:
                        self.dados[key][value[5]][indice] = {'data': value[0], 'nome': value[1], 'descrição': value[2], 'valor': value[3]} 
                    else:
                        self.dados[key]['OUTROS'][indice] = {'data': value[0], 'nome': value[1], 'descrição': value[2], 'valor': value[3]} 
        return


    def gerar(self):
        self.can = canvas.Canvas(self.packet)
        self.preencher_cabecalho()
        self.pagamentos()

        self.can.save()
        self.gerar_relatorio_mensal()

    
    def preencher_cabecalho(self):
        self.font(20)
        self.can.drawRightString(320, 790, f"RELATÓRIO DETALHADO")
        self.font(10)
        self.can.drawRightString(570, 790, f"Periodo: {self.datas[0]} à {self.datas[1]}")

    def pagamentos(self):
            self.font(10, font='Helvetica-Bold')
            self.campo_despesa_detalhe(['DATA', 'NOME', 'DESCRIÇÃO', 'VALOR'], font=10)
            self.mudarY(-20)
            for key, value in self.dados.items():
                self.titulo(f"{key}", x=40, font=10, y=-15)
                for key2, value2 in value.items():
                    if key2 != None and value2 != {}:
                        self.titulo(f"{key2}", font=9, y=-5)
                        for i in value2.values():
                            if self.y >= 100:
                                self.campo_despesa_detalhe([i['data'],i['nome'],i['descrição'],self.dinheiro(i['valor'])], y=-10, font=8)
                            else:
                                self.can.showPage()
                                self.mudarY(670)
                        self.mudarY(-20)
                self.mudarY(-10)
            self.mudarY(-20)


    def saldo(self):
            self.campo_saldo(self.dinheiro(self.dados['saldo']), font=10)

