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
        self.can.drawString(480, 750, "RELATÓRIO")
        self.can.setFont('Calibri', 12)
        self.can.drawString(75, 640, "DATA")
        self.can.drawString(150, 640, "ENTRADA")
        self.can.drawString(225, 640, "SAIDA")
        self.can.drawString(280, 640, "--- ALMOÇO ---")
        self.can.drawString(375, 640, "ENTRADA")
        self.can.drawString(450, 640, "SAIDA")
        self.can.setFont('Calibri', 10)
        y =  610
        for i in self.dados:
            self.can.drawString(75, y, str(i[1]))
            self.can.drawString(150, y, str(i[3]))
            self.can.drawString(225, y, str(i[4]))
            self.can.drawString(295, y, "--------------")
            self.can.drawString(375, y, str(i[5]))
            self.can.drawString(450, y, str(i[6]))
            y-= 20
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

Relatorio("relatorio.pdf", []).gerar_relatorio_mensal()
