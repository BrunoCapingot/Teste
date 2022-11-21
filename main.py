import sys
from banco import Banco
from frmCadPerson import Ui_CadPerson
from PyQt5.QtWidgets import QApplication,QMainWindow
import requests
import json

class Warnings():
    def dbError(self):
        print('--banco em manuntenão--')

    def cepError(self):
        print('--mecanismo de pesquisa em manutenção--')

    def preenchError(self):
        print('--mecanismo de preenchimento em manutenção--')

class TelaCd(QMainWindow,Ui_CadPerson):
    def __init__(self,db = Banco(),error = Warnings()):
        super(TelaCd,self).__init__()
        self.db = db
        self.error = error
        self.cep = '75691708'
        self.setupUi(self)


        self.btnExecutar.clicked.connect(self.cadastraNoBanco)
        self.btnCheckCep.clicked.connect(self.bsCep)

    def bsCep(self):
        self.dt = json.loads(requests.get(f'https://viacep.com.br/ws/{self.cep}/json').text)
        self.preencheTxt()

    def preencheTxt(self):
        [self.error.preenchError(), self.txtPais.setText('brasil'), self.txtEstado.setText(self.dt['uf']),
               self.txtICidade.setText(self.dt['localidade']), self.txtEndereco.setText(self.dt['logradouro']),
               self.txtBairro.setText(self.dt['bairro']), self.txtCpmEnder.setText(self.dt['complemento']),
               self.lbVerfCep.setText('Cep verificado com sucesso')]





    def cadastraNoBanco(self):
        self.tuplaDt = (self.txtPersonName.text(), self.txtRg.text(), self.txtCpf.text(), self.txtEndereco.text(),
                        self.txtCpmEnder.text(), self.txtICidade.text(), self.txtEstado.text(), self.txtPais.text(),
                        self.cbSexo.currentText(), self.dtNascimento.text(), self.txtEmail.text(),
                        self.txtTelefone.text(), self.txtCep.text())
        [self.error.dbError(),self.limpaCampos()]
        self.db.insert(self.tuplaDt)

    def limpaCampos(self):
        [self.txtCep.setText(''),self.txtRg.setText(''),self.txtCpf.setText(''),
        self.txtPais.setText(''),self.txtEstado.setText(''),self.txtBairro.setText(''),
        self.txtICidade.setText(''),self.txtEmail.setText(''),self.txtEndereco.setText(''),
        self.txtPersonName.setText(''),self.txtCpmEnder.setText('')]




class System():
    def __init__(self):
        pass
    def openUi(self):
        app = QApplication(sys.argv)
        ui = TelaCd()
        ui.show()
        sys.exit(app.exec_())

if __name__ == '__main__':

    sistema = System()
    sistema.openUi()



