from Relatorios import cabecalho, detalhado
from Relatorios.funcionario import RelatorioFuncionario



class GerarRelatorios:

    def geral(self, datas, nome='relatorio_geral.pdf'):
        cabecalho.RelatorioGeral(nome, datas).gerar_relatorio_mensal()
    
    def detalhado(self, datas, nome='relatorio_detalhado.pdf'):
        detalhado.RelatorioDetalhado(nome, datas)

    def funcionario_mensal(self, funcionario, datas, nome='relatorio_funcionario.pdf'):
        RelatorioFuncionario(funcionario, nome, datas)
         


#GerarRelatorios().geral(['2022-03-01', '2022-03-31'])
#GerarRelatorios().detalhado(['2022-03-01', '2022-03-31'])
GerarRelatorios().funcionario_mensal('junior', ['2022-02-20', '2022-02-28'])

