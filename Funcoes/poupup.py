from PyQt5.QtWidgets import QMessageBox

class Poup():

    def confirma(mensagem, tipo, titulo="Confirmação",):
        status = False
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(tipo)
        msg.setText(mensagem)
        btn_yes = msg.addButton(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)

        execute = msg.exec_()

        if execute == QMessageBox.Yes:
            status = True

        return status


def Erro(mensagem, tipo, titulo="Confirmação",):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(tipo)
        msg.setText(mensagem)
        msg.addButton(QMessageBox.Ok)

        msg.exec_()