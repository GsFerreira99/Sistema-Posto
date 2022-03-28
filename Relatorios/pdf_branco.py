from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class Pdf:

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.packet = io.BytesIO()
        pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))

    def gerar_relatorio_mensal(self):
        self.mover_cursor_inicio()
        self.abrir_pdf_modelo()
        self.adiciona_dados_ao_modelo()
        self.salvar_pdf()

    def mover_cursor_inicio(self):
        self.packet.seek(0)
        self.new_pdf = PdfFileReader(self.packet)

    def abrir_pdf_modelo(self):
        self.existing_pdf = PdfFileReader(open("Relatorios\MODELO.pdf", "rb"))
        self.output = PdfFileWriter()

    def adiciona_dados_ao_modelo(self):
        self.page = self.existing_pdf.getPage(0)
        self.page.mergePage(self.new_pdf.getPage(0))
        self.output.addPage(self.page)
    
    def salvar_pdf(self):
        self.outputStream = open(self.nome_arquivo, "wb")
        self.output.write(self.outputStream)
        self.outputStream.close()
        
    def campo(self, titulo, valor, y=-25, font=12):
        self.font(font)
        self.can.drawString(60+20, self.mudarY(-15), titulo)
        self.can.drawString(60+150, self.y, f".........................................................................     {valor}")

    def linhas_tabela(self, dados, y=-25, font=12):
        self.font(font)
        self.mudarY(-20)
        self.can.drawString(60, self.y, f'{dados[0]}')
        self.can.drawString(130, self.y, f'{dados[1]}')
        self.can.drawString(500, self.y, f'{dados[2]}')

    def linhas_tabela_tanque(self, dados, y=-10, font=12):
        self.font(font)
        self.mudarY(y)
        self.can.drawString(80, self.y, f'{dados[0]}')
        self.can.drawString(220, self.y, f'{dados[1]}')
        self.can.drawString(360, self.y, f'{dados[2]}')
        self.can.drawString(448, self.y, f'{dados[3]}')

    def total_tabela(self, valor,x=60, y=-20, font=12):
        self.font(font)
        self.can.drawString(x+20, self.mudarY(y), "TOTAL")
        self.can.drawString(x+80, self.y, f"..........................................................................................................................................     {valor}")
    
    def total_tabela_tanque(self, valor,x=60, y=-20, font=12):
        self.font(font)
        self.can.drawString(x+20, self.mudarY(y), "TOTAL")
        self.can.drawString(x+80, self.y, f"...................................................................................     {valor}")
            
    def titulo(self, titulo, x=60, font=14, y=-10):
        self.font(font)
        self.can.drawString(x, self.y, titulo)
        self.mudarY(y)

    def font(self, size, font='Calibri'):
        self.can.setFont(font, size)

    def mudarY(self, y=-25):
        self.y+= y
        return self.y

    def dinheiro(self, valor):
        return "R$ {:.2f}".format(valor)
    
    def litro(self, valor):
        return "{:.2f} L".format(valor)


