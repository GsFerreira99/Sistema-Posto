from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class Relatorio:

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
        self.can.setFont('Calibri', 14)
        self.can.drawString(395, 750, "RELATÓRIO VENDAS MAR-22")
        self.can.setFont('Calibri', 12)
        self.can.drawString(75, 620, "TOTAL VENDAS   .......................................................................................................   R$ {:.2f}".format(self.dados['total_vendas']))
        self.can.drawString(100, 600, "Dinheiro     ........................................................................................................   R$ {:.2f}".format(self.dados['dinheiro']))
        self.can.drawString(100, 580, "Pix               ........................................................................................................   R$ {:.2f}".format(self.dados['pix']))
        self.can.drawString(100, 560, "Cartão        ........................................................................................................   R$ {:.2f}".format(self.dados['cartao']))
        self.can.drawString(75, 510, "SAÍDAS   ....................................................................................................................   R$ {:.2f}".format(self.dados['retiradas']))
        self.can.drawString(75, 460, "TOTAL LITROS VENDIDOS   .......................................................................................      {:.2f} L".format(self.dados['litros']))
        self.can.drawString(75, 410, "COMBUSTIVEL NO TANQUE   ....................................................................................   {:.2f} L".format(self.dados['tanque']))
        self.can.setFont('Calibri', 10)
        y =  610


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


