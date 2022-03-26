from Relatorios import relatorio_retiradas, vendas_mensal, relatorio_funcionario
from DataBase.DataBase import DataBase as data
from Funcoes.genericas import caminho_db
from datetime import date

Db = data(caminho_db())



def vendas(data, arquivo):
    dados = {
            'total_vendas' : somar(Db.select_generico("SELECT {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format('total', 1, data[0], data[1],)),),
            'dinheiro' : somar(Db.select_generico("SELECT {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format('dinheiro_caixa', 1, data[0], data[1],)),),
            'pix' : somar(Db.select_generico("SELECT {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format('pix', 1, data[0], data[1],)),),
            'cartao' : somar(Db.select_generico("SELECT {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format('cartao', 1, data[0], data[1],)),),
            'litros' : somar(Db.select_generico("SELECT {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format('litros', 1, data[0], data[1],)),),
            'retiradas' : somar(Db.select_generico("SELECT {} FROM Caixa WHERE bomba={} AND data BETWEEN '{}' AND '{}'".format('retiradas', 1, data[0], data[1],)),),
            'tanque' : somar(Db.select_generico("SELECT {} FROM Valor_combustivel WHERE combustivel='{}'".format('quantidade', 'Gasolina Comum')))
        }
    vendas_mensal.Relatorio(arquivo, dados).gerar_relatorio_mensal()


def funcionario(nome, data):
    dados = {
        'nome': nome,
        'data' : data,
        'negativos' : Db.select_generico("SELECT resto FROM Caixa WHERE funcionario LIKE '%{}%' AND data BETWEEN '{}' AND '{}'".format(nome, f"{data}-01", f"{data}-31")),
        'trabalhados' : Db.select_generico("SELECT DISTINCT data FROM Caixa WHERE funcionario LIKE '%{}%' AND data BETWEEN '{}' AND '{}'".format(nome, f"{data}-01", f"{data}-31")),
        'retiradas' : Db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Retiradas.nome LIKE '%{}%' AND Caixa.data BETWEEN '{}' AND '{}'""".format(nome, f"{data}-01", f"{data}-31")),
    }
    relatorio_funcionario.RelatorioFuncionario(f"{nome}_{data}.pdf", dados).gerar_relatorio_mensal()

def somar(dados):
    total = 0
    for valor in dados:
        total+= valor[0]
    return total

def retiradas(arquivo, data):

    pessoas = Db.select_generico("""SELECT DISTINCT Retiradas.nome FROM Retiradas INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE 
                                        Caixa.data BETWEEN '{}' AND '{}' """.format(f"{data}-01", f"{data}-31")),
    retiradas = {}
    for i in pessoas[0]:
        retiradas[i[0]] = []

    dados =  Db.select_generico("""SELECT Retiradas.codigo, Caixa.data, Retiradas.caixa, Retiradas.nome, Retiradas.valor, Retiradas.descricao FROM Retiradas 
                                        INNER JOIN Caixa ON Retiradas.caixa = Caixa.codigo WHERE Caixa.data BETWEEN '{}' AND '{}'
                                        """.format(f"{data}-01", f"{data}-31")),

    for i in dados[0]:
        retiradas[i[3]].append(i)

    info = {
        'data' : data,
        'dados' : retiradas
    }

    relatorio_retiradas.RelatorioRetiradas('relatorio_ret-MAR.pdf', info).gerar_relatorio_mensal()

funcionario('joaquim', '2022-03')