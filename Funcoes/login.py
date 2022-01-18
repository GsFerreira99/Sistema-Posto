from DataBase.DataBase import DataBase
from Funcoes.genericas import caminho_db


class Login():      
    
    def __init__(self, usuario, senha):
        self.dados_login = {'usuario': usuario, 'senha': senha}
        self.db = DataBase(caminho_db())
        self.dados = {'usuario': '', 'senha': '', 'codigo': '', 'nome': '', 'tipo': ''}
        
    def validar_dados(self):
        try:
            self.acessar_db()
            if self.dados_login['senha'] == self.dados['senha'] and self.dados_login['usuario'] == self.dados['usuario']:
                return True, self.dados
            else:
                return [False]
        except TypeError:
            return [False]
    
    def acessar_db(self):
        dados_db = self.db.acesso_login(self.dados_login['usuario'])
        self.db.close_db()
        self.formatar_dados(dados_db)

    def formatar_dados(self, informacoes):
        for num, keys in enumerate(self.dados.keys()):
            self.dados[keys] = informacoes[num]
        return self.dados