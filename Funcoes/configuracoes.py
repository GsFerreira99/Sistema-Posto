from PyQt5.QtWidgets import QMessageBox
from GUI.ui_GUI import Ui_Sistema
from Funcoes.genericas import atualizar_cb, caminho_db, converter_string_para_float, limpar_campos, mascara_dinheiro, verificar_vazio, verificar_vazio_dic
from DataBase.DataBase import DataBase
from Funcoes.poupup import Erro, Poup
from PyQt5.QtCore import QDateTime, QDate


class Configuracoes(Ui_Sistema):

    def __init__(self, ui):        
        #inicia as variaveis basicas
        self.ui = ui
        
        self.aba_home()

        #Principal
        self.ui.config_comb_btn.clicked.connect(lambda: Aba_Combustivel(self.ui))
        self.ui.config_user_btn.clicked.connect(lambda: Aba_Usuario(self.ui))

    def aba_home(self):
        self.ui.stackedWidget_12.setCurrentIndex(0)
        self.ui.stackedWidget_10.setCurrentIndex(2)


class Aba_Combustivel(Configuracoes):

    def __init__(self, ui):
        super().__init__(ui)
        self.ui.stackedWidget_10.setCurrentIndex(1)
        self.ui.stackedWidget_11.setCurrentIndex(3)
        self.ui.stackedWidget_12.setCurrentIndex(1)

        #Navegação
        self.ui.config_comb_voltar.clicked.connect(lambda: self.aba_home())
        self.ui.config_comb_editar.clicked.connect(lambda: self.aba_editar())
        self.ui.config_comb_info_2.clicked.connect(lambda: self.aba_informacoes())
        self.ui.config_comb_entrada.clicked.connect(lambda: self.aba_entrada())

        self.ui.config_comb_edit_combustivel.currentIndexChanged.connect(lambda: self.consultar_valor(self.ui.config_comb_edit_combustivel, self.ui.config_comb_edit_antigo))
        self.ui.config_comb_edit_combustivel_2.currentIndexChanged.connect(lambda: self.consultar_valor(self.ui.config_comb_edit_combustivel_2, self.ui.config_comb_edit_novo_2))
        self.ui.config_comb_edit_combustivel_3.currentIndexChanged.connect(lambda: self.consultar_tanque(self.ui.config_comb_edit_combustivel_3, self.ui.config_comb_edit_novo_3))


        self.ui.config_comb_edit_btn.clicked.connect(lambda: self.atualizar_valor_combustivel())
        self.ui.config_comb_edit_btn_2.clicked.connect(lambda: self.inserir_entrada())
    
    def aba_entrada(self):
        self.ui.stackedWidget_11.setCurrentIndex(2)
        self.ui.config_comb_entrada_data.setDateTime(QDateTime.currentDateTime())
        self.ui.config_comb_entrada_vencimento.setDateTime(QDateTime.currentDateTime())
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_entrada_combustivel)

    def aba_informacoes(self):
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_edit_combustivel_2)
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_edit_combustivel_3)
        self.ui.stackedWidget_11.setCurrentIndex(0)

    def aba_editar(self):
        atualizar_cb(DataBase(caminho_db()), "SELECT combustivel FROM Valor_combustivel", self.ui.config_comb_edit_combustivel)
        self.ui.stackedWidget_11.setCurrentIndex(1)
        self.limpar_edicao()
    
    def consultar_valor(self, cb, ln):
        combustivel = cb.currentText()
        if combustivel == "":
            ln.setText("")
            return
        else: 
            valor = DataBase(caminho_db()).valor_combustivel(combustivel)
            ln.setText(str(valor)) 

    def atualizar_valor_combustivel(self):
        combustivel = self.ui.config_comb_edit_combustivel.currentText()
        try:
            novo = converter_string_para_float(self.ui.config_comb_edit_novo.text())
            if novo != "" and combustivel != "":
                DataBase(caminho_db()).querry_generica("UPDATE Valor_combustivel SET valor = {} WHERE combustivel = '{}'".format(novo, combustivel))
                Erro("Preço do combustível editado com sucesso.", QMessageBox.Information)
                self.limpar_edicao()
                self.ui.stackedWidget_11.setCurrentIndex(2)
            else:
                Erro("Preencha todos os campos.", QMessageBox.Warning, "Aviso!")
        except ValueError:
            Erro("Preencha todos os campos.", QMessageBox.Warning, "Aviso!")

    def limpar_edicao(self):
        limpar_campos([self.ui.config_comb_edit_novo])
        self.ui.config_comb_edit_combustivel.setCurrentIndex(0)

    def consultar_tanque(self, cb, ln):
        combustivel = cb.currentText()
        if combustivel == "":
            ln.setText("")
            return
        else: 
            valor = DataBase(caminho_db()).select_generico("SELECT quantidade FROM Valor_combustivel WHERE combustivel = '{}'".format(combustivel))
            ln.setText(str(valor[0][0])) 

    def inserir_entrada(self):
        if Poup.confirma("Deseja salvar a nova entrada de combustivel?", QMessageBox.Question):
            dados = {
                'combustivel': self.ui.config_comb_entrada_combustivel.currentText(),
                'quantidade': self.ui.config_comb_entrada_quantidade.text(),
                'valor': self.ui.config_comb_entrada_valor.text(),
                'data': self.ui.config_comb_entrada_data.date().toString('yyyy-MM-dd'),
                'vencimento': self.ui.config_comb_entrada_vencimento.date().toString('yyyy-MM-dd'),
                'parcelamento': self.ui.config_comb_entrada_parcelamento.currentText(),
            }
            if not verificar_vazio_dic(dados):
                DataBase(caminho_db()).querry_generica(f"INSERT INTO entrada_combustivel (combustivel, quantidade, valor_nota, data, vencimento, parcelamento) VALUES ('{dados['combustivel']}', '{dados['quantidade']}', '{dados['valor']}', '{dados['data']}', '{dados['vencimento']}', '{dados['parcelamento']}')")
                DataBase(caminho_db()).querry_generica(f"UPDATE Valor_combustivel set quantidade = quantidade + {int(dados['quantidade'])} WHERE combustivel = '{dados['combustivel']}'")
                self.inserir_despesa(dados)
                self.ui.stackedWidget_11.setCurrentIndex(3)
                self.limpar_entrada()
                Erro("Entrada adicionada com sucesso.", QMessageBox.Information)
            else:
                Erro("Preencha todos os campos corretamente!", QMessageBox.Warning)

    def inserir_movimentacao(self, tabela):
        data = QDate.currentDate().toString("yyyy-MM-dd")
        codigo = DataBase(caminho_db()).select_generico("SELECT codigo FROM {} ORDER BY codigo DESC LIMIT 1".format(tabela))
        DataBase(caminho_db()).querry_generica("INSERT INTO Movimentacoes (data, tipo, id) VALUES('{}', '{}', '{}')".format(data, tabela, codigo[0][0]))
   
    def inserir_despesa(self, dados):
        info = {
                'status':'Em Aberto',
                'data':dados['vencimento'],
                'tipo':'POSTO',
                'descrição': f"NOTA DE COMBUSTIVEL ENTREGUE DIA {dados['data']}",
                'valor':dados['valor'],
                'conta':'Conta Inter'
            }
        if dados['parcelamento'] == '1':
                self.inserir_db(f"INSERT INTO Despesas (status, data, tipo, descricao, valor, conta) VALUES ('{info['status']}', '{info['data']}', '{info['tipo']}', '{info['descrição']}', '{info['valor']}', '{info['conta']}')")
                self.inserir_movimentacao("Despesas")
        else:
            datas = self.data_parcela(info["data"], dados['parcelamento'])
            valor = int(info["valor"])/ int(dados['parcelamento'])
            for i,j in enumerate(datas):
                info['descrição'] = f"PARCELA {i+1}/{dados['parcelamento']} NOTA DE COMBUSTIVEL ENTREGUE DIA {dados['data']} "
                info['data'] = j
                info["valor"] = "{:.2f}".format(valor)
                DataBase(caminho_db()).querry_generica(f"INSERT INTO Despesas (status, data, tipo, descricao, valor, conta) VALUES ('{info['status']}', '{info['data']}', '{info['tipo']}', '{info['descrição']}', '{info['valor']}', '{info['conta']}')")
                self.inserir_movimentacao("Despesas")

    def data_parcela(self, data, parcela):
        datas = []
        y = int(data[:4])
        m = int(data[5:7])
        d = int(data[8:])
        for i in range(int(parcela)):
            if m > 12:
                y+=1
                datas.append(QDate(y, m, d).toString('yyyy-MM-dd'))
                m+=1
            else:
                datas.append(QDate(y, m, d).toString('yyyy-MM-dd'))
                m+=1
        return datas

    def limpar_entrada(self):
                self.ui.config_comb_entrada_combustivel.setCurrentIndex(0)
                self.ui.config_comb_entrada_quantidade.setText('')
                self.ui.config_comb_entrada_valor.setText('')
                self.ui.config_comb_entrada_data.setDateTime(QDateTime.currentDateTime())
                self.ui.config_comb_entrada_parcelamento.setCurrentIndex(0)

class Aba_Usuario(Configuracoes):

    def __init__(self, ui):
        super().__init__(ui)
        self.ui.stackedWidget_10.setCurrentIndex(0)
        self.ui.stackedWidget_12.setCurrentIndex(2)
        self.ui.stackedWidget_13.setCurrentIndex(0)


        #Navegação
        self.ui.config_user_voltar.clicked.connect(lambda: self.aba_home())
        self.ui.config_user_lista_2.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentIndex(2))
        self.ui.config_user_novo_btn.clicked.connect(lambda: self.ui.stackedWidget_13.setCurrentIndex(1))