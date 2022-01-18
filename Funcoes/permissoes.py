class Permissoes:

    def __init__(self, main, acesso) -> None:
        self.main = main
        self.acesso = acesso
        self.controle()

    def controle(self):
        if self.acesso == 1:
            self.admin()
        elif self.acesso == 2:
            self.funcionario()
        elif self.acesso == 3:
            self.desenvolvedor()
        elif self.acesso == 4:
            self.gerente()

    def admin(self):
        #Desabilita
        self.main.ini_btn_ponto.setMaximumWidth(0)
        #Habilita
        self.main.btn_consulta.setMaximumHeight(60)
        self.main.btn_vendas.setMaximumHeight(60)
        self.main.btn_financeiro.setMaximumHeight(60)
        self.main.btn_estoque.setMaximumHeight(60)

    def funcionario(self):
        #Desabilita
        self.main.btn_consulta.setMaximumHeight(0)
        self.main.btn_vendas.setMaximumHeight(0)
        self.main.btn_financeiro.setMaximumHeight(0)
        self.main.btn_estoque.setMaximumHeight(0)
        #Habilita
        self.main.ini_btn_ponto.setMaximumWidth(200)

    def gerente(self):
        #Desabilita
        self.main.btn_vendas.setMaximumHeight(0)
        self.main.btn_financeiro.setMaximumHeight(0)
        self.main.btn_estoque.setMaximumHeight(0)
        #Habilita
        self.main.btn_consulta.setMaximumHeight(60)

    def desenvolvedor(self):
        pass

