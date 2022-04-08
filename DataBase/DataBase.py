import sqlite3


class DataBase():

    def __init__(self, db_name):
        #Conecta ao banco de dados
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error:
            pass

    def close_db(self):
        #Fecha o banco de dados
        if self.conn:
            self.conn.close()

    def commit_db(self):
        #Faz o communt dos dados
        if self.conn:
            self.conn.commit()
    
    def acesso_login(self, login):
        #Consulta o banco de dados através do login do usuário e retorna uma tupla com nome, senha e codigo do usuario
        dados = self.cursor.execute(
            "SELECT usuario, senha, codigo, nome, tipo FROM Usuarios WHERE usuario = ?", (login,))

        dados = dados.fetchone()
        return dados
    
    def inserir_caixa(self, info):
        #Insere os dados referentes ao fechamento de caixa ao banco de dados
        dados = []
        for valores in info.values():
            dados.append(valores)

        self.cursor.execute(
            """INSERT INTO Caixa (data, bomba, funcionario, digital_anterior, analogico_anterior,
            digital_atual, analogico_atual, litros, valor, dinheiro_caixa, pix, cartao, total, resto, vendas) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, dados,)
        self.commit_db()
        #self.close_db()

    def select_caixa_anterior(self, bomba):
        #Retorna os valores do caixa anterior da referente bomba
        if bomba == "":
            bomba = "1"
        cod = self.cursor.execute("SELECT * FROM Caixa WHERE bomba = ?", (bomba,))
        cod = cod.fetchall()
        cod = cod[-1]
        valores = [cod[5], cod[7]]
        return (valores), (int(cod[0])+1)

    def inserir_retiradas(self, info):
        #Faz a inserção dos dados de retiradas ao banco de dados
        codigo = info['codigo']
        info = info['retiradas']
        for i in info.values():
            dados = []
            for dado in i.values():
                dados.append(dado)
            dados.append(codigo)
            self.cursor.execute("""
                INSERT INTO Retiradas (nome, valor, descricao, caixa)
                VALUES (?, ?, ?, ?)
                """, dados)
            self.commit_db()

    def consulta_bombas(self):
        #Retorna todas as bombas cadastradas no sistema
        dados = self.cursor.execute("""
        SELECT bomba FROM Bombas 
        """)

        return dados.fetchall()

    def consulta_retirada(self):
        #Retorna o nome das pessoas que ja efetuaram uma retirada 
        dados = self.cursor.execute("""
        SELECT DISTINCT nome FROM Retiradas 
        """)

        return dados.fetchall()

    def relatorio_vendas(self, dados):
        #Retorna as datas e valores dos caixas
        datas = dados[1]
        if dados[0] == "Tudo":
            info = self.cursor.execute("""
            SELECT strftime('%d', data), ? 
            FROM Caixa
            WHERE data  BETWEEN ? AND ?
            """, (dados[2], datas[0], datas[1],))
        
        else:
            info = self.cursor.execute("""
            SELECT strftime('%d', data), ?
            FROM Caixa
            Where bomba=? AND data BETWEEN ? AND ?
            """, (dados[2], dados[0], datas[0], datas[1],))

        info = info.fetchall()
        return info

    def dados_tabela_caixa(self, dados):
        datas = dados[1]
        if dados[0] == "Tudo":
            info = self.cursor.execute("""
            SELECT * 
            FROM Caixa
            WHERE data  BETWEEN ? AND ?
            """, (datas[0], datas[1],))
        
        else:
            info = self.cursor.execute("""
            SELECT *
            FROM Caixa 
            WHERE bomba=? AND data  BETWEEN ? AND ?
            """, (dados[0], datas[0], datas[1],))

        info = info.fetchall()
        return info

    def dados_tabela_retiradas(self, dados):
        infos = dados[0]
        datas = dados[1]
        if infos[0] == "Data":
            info = self.cursor.execute("""
            SELECT * 
            FROM Retiradas
            WHERE data  BETWEEN ? AND ?
            """, (datas[0], datas[1],))
        
        elif infos[0] == "Nome":
            nome = '%{}%'.format(infos[1])
            info = self.cursor.execute("""
            SELECT *
            FROM Retiradas 
            WHERE nome LIKE ?
            """, (nome,))
        
        elif infos[0] == "Descrição":
            descricao = '%{}%'.format(infos[1])
            info = self.cursor.execute("""
            SELECT *
            FROM Retiradas 
            WHERE descricao LIKE ?
            """, (descricao,))
        
        elif infos[0] == "Caixa":
            caixa = infos[1]
            info = self.cursor.execute("""
            SELECT *
            FROM Retiradas 
            WHERE caixa = ?
            """, (caixa,))

        info = info.fetchall()
        return info

    def data_retirada(self, dado):
        info = self.cursor.execute("SELECT data FROM Caixa WHERE codigo = ?",(dado,))
        return info.fetchone()

    def cadastrar_novo_produto(self, dados):
        self.cursor.execute("""
        INSERT INTO Estoque (tipo, marca, produto, quantidade, cod_barras, preço_compra, preço_venda)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, dados,)
        self.commit_db()
    
    def inserir_ponto(self, dados):
        self.cursor.execute("""
        INSERT INTO Registro_ponto (data, funcionario, entrada_1, saida_1, entrada_2, saida_2)
        VALUES (?, ?, ?, ?, ?, ?)
        """, dados,)
        self.commit_db()

    def querry_generica(self, querry): 
        dados = self.cursor.execute(querry)
        self.commit_db()
        return dados.fetchall()
    
    def select_generico(self, querry):
        dados = self.cursor.execute(querry)
        return dados.fetchall()
    
    def valor_combustivel(self, combustivel):
        dados = self.cursor.execute("SELECT valor FROM Valor_combustivel WHERE combustivel = ?", (combustivel,))
        dados = dados.fetchone()
        return dados[0]

    def atualizar_produto(self, dados, id_produto):
        dados.append(id_produto)
        self.cursor.execute("""
            UPDATE 
                Estoque
            SET 
                tipo = ?,
                marca = ?,
                produto = ?,
                preço_compra = ?,
                preço_venda = ?,
                quantidade = ?,
                cod_barras = ?
            WHERE 
                codigo = ?
            """, dados,)
        self.commit_db()

    def inserir_nova_entrada(self, dados):
        self.cursor.execute("""
            UPDATE 
                Estoque
            SET 
                quantidade = quantidade + ?
            WHERE 
                produto = ?
            """, dados,)
        self.commit_db()
    
