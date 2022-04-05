from reportlab.pdfgen import canvas
import DataBase.DataBase as db
from Funcoes.genericas import caminho_db

from Relatorios.pdf_branco import Pdf
    
    
class RelatorioFuncionario(Pdf):

    def __init__(self, nome, nome_arquivo, datas):
        super().__init__(nome_arquivo)

        self.y = 720
        self.datas = datas
        self.nome = nome
        self.db = db.DataBase(caminho_db())
        self.consultar_dados()
        self.gerar()


    def consultar_dados(self):
        self.dados = {}
        self.dados_pagamentos()

    def dados_pagamentos(self):
        dias = self.db.select_generico(f"SELECT DISTINCT data FROM Caixa WHERE funcionario LIKE '%{self.nome}%' AND data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}' ORDER BY data")
        resto = self.db.select_generico(f"SELECT resto FROM Caixa WHERE funcionario LIKE '%{self.nome}%' AND data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}'")
        pagamentos = self.db.select_generico(f"SELECT data, descricao, valor FROM Despesas WHERE nome LIKE '%{self.nome}%' AND tipo = 'POSTO' AND data BETWEEN '{self.datas[0]}' AND '{self.datas[1]}' ORDER BY data")

        resto_total = 0
        for i in resto:
            resto_total+= float(i[0])

        pagamentos_total = 0
        for i in pagamentos:
            pagamentos_total+= float(i[2])

        self.dados = {
            'dias' : dias,
            'resto' : resto_total,
            'pagamentos' : pagamentos,
            'total_pagamentos' : pagamentos_total,
        }


    def gerar(self):
        self.can = canvas.Canvas(self.packet)
        self.preencher_cabecalho()
        self.dias()
        self.pagamentos()
        self.resto()

        self.can.save()
        self.gerar_relatorio_mensal()

    def preencher_cabecalho(self):
        self.font(20)
        self.can.drawString(100, 790, f"RELATÓRIO MENSAL   {self.nome.upper()}")
        self.font(10)
        self.can.drawString(435, 790, f"Periodo: {self.datas[0]} à {self.datas[1]}")

    def dias(self):
            self.font(10)
            self.titulo('DIAS TRABALHADOS', font=12, y=0)
            self.mudarY(-25)
            self.font(10)

            x=80
            for i in self.dados['dias']:
                self.dias_trabalhados(f"{i[0]}, ", x=x, font=10)
                x+=55
                if x >= 430:
                    x=80
                    self.mudarY(-15)
            self.mudarY(-15)
            self.campo('Total', f"{len(self.dados['dias'])} dias", font=10)
            self.mudarY(-50)
        
    def pagamentos(self):
            self.font(10)
            self.titulo('PAGAMENTOS', font=12, y=0)
            self.mudarY(-10)

            self.campo_pagamentos_titulo(['Data', 'Descrição', 'Valor'], font=11)
            for i in self.dados['pagamentos']:
                self.campo_pagamentos(i, font=10)
            self.mudarY(-20)
            self.campo('Total', f"{self.dinheiro(self.dados['total_pagamentos'])}", font=10)
            self.mudarY(-50)

    def resto(self):
            self.font(10)
            self.titulo('NEGATIVOS CAIXA', font=12, y=0)
            self.mudarY(-15)
            self.campo('Total', self.dinheiro(float(self.dados['resto'])), font=10)


    def saldo(self):
            self.campo_saldo(self.dinheiro(self.dados['saldo']), font=10)

