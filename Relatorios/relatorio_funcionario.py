from datetime import date
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class RelatorioFuncionario:

    def __init__(self, nome_arquivo, dados):
        self.nome_arquivo = nome_arquivo
        self.dados = dados
        self.packet = io.BytesIO()

        pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))

    def gerar_relatorio_mensal(self):
        self.criar_novo_pdf()
        self.mover_cursor_inicio()
        self.abrir_pdf_modelo()
        self.adiciona_dados_ao_modelo()
        self.salvar_pdf()


    def criar_novo_pdf(self):
        self.can = canvas.Canvas(self.packet, pagesize=letter)
        y = 625
        x = 50
        #TITULO
        self.can.setFont('Calibri', 14)
        self.can.drawRightString(555, 750, f"RELATÓRIO {self.dados['nome']} {self.dados['data']}")

        #DIAS TRABALHADOS
        self.can.setFont('Calibri', 14)
        self.can.drawString(x, y, f"DIAS TRABALHADOS:")
        y-= 20

        self.can.setFont('Calibri', 12)
        self.can.drawString(x+50, y, f"Total Dias:  {len(self.dados['trabalhados'])}")
        y-=15

        total = 0
        for valor in self.dados['negativos']:
            total+= valor[0]
        self.can.drawString(x+50, y, "Negativos Caixa:  R$ {:.2f}".format(float(total)))

        y-= 50

        #RETIRADAS
        self.can.setFont('Calibri', 14)
        self.can.drawString(x, y, f"RETIRADAS:")
        y-= 30
        self.can.setFont('Calibri', 12)
        self.can.drawCentredString(x+100, y, f"DATA")
        self.can.drawCentredString(x+200, y, f"VALOR")
        self.can.drawCentredString(x+400, y, f"DESCRIÇÃO")
        y-= 30

        self.can.setFont('Calibri', 10)

        total = 0
        for retirada in self.dados['retiradas']:
            self.can.drawCentredString(x+100, y, f"{retirada[1]}")
            self.can.drawCentredString(x+200, y, f"R$ {float(retirada[4])}")
            self.can.drawCentredString(x+400, y, f"{retirada[5]}")
            y-= 20
            total+= retirada[4]

        y-= 15
        self.can.setFont('Calibri', 12)
        self.can.drawRightString(x+480, y, f"TOTAL:   R$ {float(total)}")

        self.can.save()

    def mover_cursor_inicio(self):
        self.packet.seek(0)
        self.new_pdf = PdfFileReader(self.packet)

    def abrir_pdf_modelo(self):
        self.existing_pdf = PdfFileReader(open("Relatorios\MODELO_POSTO.pdf", "rb"))
        self.output = PdfFileWriter()

    def adiciona_dados_ao_modelo(self):
        self.page = self.existing_pdf.getPage(0)
        self.page.mergePage(self.new_pdf.getPage(0))
        self.output.addPage(self.page)
    
    def salvar_pdf(self):
        self.outputStream = open(self.nome_arquivo, "wb")
        self.output.write(self.outputStream)
        self.outputStream.close()


