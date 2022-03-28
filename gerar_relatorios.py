from Relatorios import cabecalho
from Relatorios.pdf_branco import Pdf



class GerarRelatorios:

    def geral(self, datas, nome='relatorio_geral.pdf'):
        cabecalho.RelatorioGeral(nome, datas).gerar_relatorio_mensal()


         


GerarRelatorios().geral(['2022-03-01', '2022-03-31'])

