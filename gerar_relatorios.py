from Relatorios import cabecalho, detalhado



class GerarRelatorios:

    def geral(self, datas, nome='relatorio_geral.pdf'):
        cabecalho.RelatorioGeral(nome, datas).gerar_relatorio_mensal()
    
    def detalhado(self, datas, nome='relatorio_detalhado.pdf'):
        detalhado.RelatorioDetalhado(nome, datas)
         


#GerarRelatorios().geral(['2022-03-01', '2022-03-31'])
GerarRelatorios().detalhado(['2022-03-01', '2022-03-31'])

