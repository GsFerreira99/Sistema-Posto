from DataBase.DataBase import DataBase as Db
from Funcoes.genericas import caminho_db
from Relatorios.mensal import Relatorio


nov = Db(caminho_db()).querry_generica('SELECT * FROM Registro_ponto WHERE data BETWEEN "2021-11-01" AND "2021-11-31"')
dez = Db(caminho_db()).querry_generica('SELECT * FROM Registro_ponto WHERE data BETWEEN "2021-12-01" AND "2021-12-31"')

Relatorio("relatorio_novembro.pdf", nov).gerar_relatorio_mensal()
Relatorio("relatorio_dezembro.pdf", dez).gerar_relatorio_mensal()



