# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadPerson.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadPerson(object):
    def setupUi(self, CadPerson):
        CadPerson.setObjectName("CadPerson")
        CadPerson.resize(739, 471)
        self.centralwidget = QtWidgets.QWidget(CadPerson)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gBInfoUser = QtWidgets.QGroupBox(self.centralwidget)
        self.gBInfoUser.setObjectName("gBInfoUser")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gBInfoUser)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frCampos = QtWidgets.QFrame(self.gBInfoUser)
        self.frCampos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCampos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCampos.setObjectName("frCampos")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frCampos)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hrLyName = QtWidgets.QHBoxLayout()
        self.hrLyName.setObjectName("hrLyName")
        self.lbPersonName = QtWidgets.QLabel(self.frCampos)
        self.lbPersonName.setObjectName("lbPersonName")
        self.hrLyName.addWidget(self.lbPersonName)
        self.txtPersonName = QtWidgets.QLineEdit(self.frCampos)
        self.txtPersonName.setObjectName("txtPersonName")
        self.hrLyName.addWidget(self.txtPersonName)
        self.verticalLayout_3.addLayout(self.hrLyName)
        self.hrLyNascimento = QtWidgets.QHBoxLayout()
        self.hrLyNascimento.setObjectName("hrLyNascimento")
        self.lbNascimento = QtWidgets.QLabel(self.frCampos)
        self.lbNascimento.setObjectName("lbNascimento")
        self.hrLyNascimento.addWidget(self.lbNascimento)
        self.dtNascimento = QtWidgets.QDateEdit(self.frCampos)
        self.dtNascimento.setObjectName("dtNascimento")
        self.hrLyNascimento.addWidget(self.dtNascimento)
        self.verticalLayout_3.addLayout(self.hrLyNascimento)
        self.hrLyRg = QtWidgets.QHBoxLayout()
        self.hrLyRg.setObjectName("hrLyRg")
        self.lbRg = QtWidgets.QLabel(self.frCampos)
        self.lbRg.setObjectName("lbRg")
        self.hrLyRg.addWidget(self.lbRg)
        self.txtRg = QtWidgets.QLineEdit(self.frCampos)
        self.txtRg.setObjectName("txtRg")
        self.hrLyRg.addWidget(self.txtRg)
        self.verticalLayout_3.addLayout(self.hrLyRg)
        self.hrLyCpf = QtWidgets.QHBoxLayout()
        self.hrLyCpf.setObjectName("hrLyCpf")
        self.lbCpf = QtWidgets.QLabel(self.frCampos)
        self.lbCpf.setObjectName("lbCpf")
        self.hrLyCpf.addWidget(self.lbCpf)
        self.txtCpf = QtWidgets.QLineEdit(self.frCampos)
        self.txtCpf.setObjectName("txtCpf")
        self.hrLyCpf.addWidget(self.txtCpf)
        self.verticalLayout_3.addLayout(self.hrLyCpf)
        self.hrLySexo = QtWidgets.QHBoxLayout()
        self.hrLySexo.setObjectName("hrLySexo")
        self.lbSexo = QtWidgets.QLabel(self.frCampos)
        self.lbSexo.setObjectName("lbSexo")
        self.hrLySexo.addWidget(self.lbSexo)
        self.cbSexo = QtWidgets.QComboBox(self.frCampos)
        self.cbSexo.setObjectName("cbSexo")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.hrLySexo.addWidget(self.cbSexo)
        self.verticalLayout_3.addLayout(self.hrLySexo)
        self.hrLyTelefone = QtWidgets.QHBoxLayout()
        self.hrLyTelefone.setObjectName("hrLyTelefone")
        self.lbTelefone = QtWidgets.QLabel(self.frCampos)
        self.lbTelefone.setObjectName("lbTelefone")
        self.hrLyTelefone.addWidget(self.lbTelefone)
        self.txtTelefone = QtWidgets.QLineEdit(self.frCampos)
        self.txtTelefone.setObjectName("txtTelefone")
        self.hrLyTelefone.addWidget(self.txtTelefone)
        self.verticalLayout_3.addLayout(self.hrLyTelefone)
        self.hrLyEmail = QtWidgets.QHBoxLayout()
        self.hrLyEmail.setObjectName("hrLyEmail")
        self.lbEmail = QtWidgets.QLabel(self.frCampos)
        self.lbEmail.setObjectName("lbEmail")
        self.hrLyEmail.addWidget(self.lbEmail)
        self.txtEmail = QtWidgets.QLineEdit(self.frCampos)
        self.txtEmail.setObjectName("txtEmail")
        self.hrLyEmail.addWidget(self.txtEmail)
        self.verticalLayout_3.addLayout(self.hrLyEmail)
        self.hrLyCep = QtWidgets.QHBoxLayout()
        self.hrLyCep.setObjectName("hrLyCep")
        self.lbCep = QtWidgets.QLabel(self.frCampos)
        self.lbCep.setObjectName("lbCep")
        self.hrLyCep.addWidget(self.lbCep)
        self.txtCep = QtWidgets.QLineEdit(self.frCampos)
        self.txtCep.setObjectName("txtCep")
        self.hrLyCep.addWidget(self.txtCep)
        self.lbVerfCep = QtWidgets.QLabel(self.frCampos)
        self.lbVerfCep.setObjectName("lbVerfCep")
        self.hrLyCep.addWidget(self.lbVerfCep)
        self.btnCheckCep = QtWidgets.QPushButton(self.frCampos)
        self.btnCheckCep.setObjectName("btnCheckCep")
        self.hrLyCep.addWidget(self.btnCheckCep)
        self.verticalLayout_3.addLayout(self.hrLyCep)
        self.chBxInfoAtCep = QtWidgets.QCheckBox(self.frCampos)
        self.chBxInfoAtCep.setObjectName("chBxInfoAtCep")
        self.verticalLayout_3.addWidget(self.chBxInfoAtCep)
        self.verticalLayout_5.addWidget(self.frCampos)
        self.horizontalLayout.addWidget(self.gBInfoUser)
        self.gBCpmLoc = QtWidgets.QGroupBox(self.centralwidget)
        self.gBCpmLoc.setObjectName("gBCpmLoc")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gBCpmLoc)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frCpmEnder = QtWidgets.QFrame(self.gBCpmLoc)
        self.frCpmEnder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCpmEnder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCpmEnder.setObjectName("frCpmEnder")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frCpmEnder)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hrLyPais = QtWidgets.QHBoxLayout()
        self.hrLyPais.setObjectName("hrLyPais")
        self.lbPais = QtWidgets.QLabel(self.frCpmEnder)
        self.lbPais.setObjectName("lbPais")
        self.hrLyPais.addWidget(self.lbPais)
        self.txtPais = QtWidgets.QLineEdit(self.frCpmEnder)
        self.txtPais.setObjectName("txtPais")
        self.hrLyPais.addWidget(self.txtPais)
        self.verticalLayout.addLayout(self.hrLyPais)
        self.hrLyEstado = QtWidgets.QHBoxLayout()
        self.hrLyEstado.setObjectName("hrLyEstado")
        self.lbEstado = QtWidgets.QLabel(self.frCpmEnder)
        self.lbEstado.setObjectName("lbEstado")
        self.hrLyEstado.addWidget(self.lbEstado)
        self.txtEstado = QtWidgets.QLineEdit(self.frCpmEnder)
        self.txtEstado.setObjectName("txtEstado")
        self.hrLyEstado.addWidget(self.txtEstado)
        self.verticalLayout.addLayout(self.hrLyEstado)
        self.hrLyCidade = QtWidgets.QHBoxLayout()
        self.hrLyCidade.setObjectName("hrLyCidade")
        self.lbCidade = QtWidgets.QLabel(self.frCpmEnder)
        self.lbCidade.setObjectName("lbCidade")
        self.hrLyCidade.addWidget(self.lbCidade)
        self.txtICidade = QtWidgets.QLineEdit(self.frCpmEnder)
        self.txtICidade.setObjectName("txtICidade")
        self.hrLyCidade.addWidget(self.txtICidade)
        self.verticalLayout.addLayout(self.hrLyCidade)
        self.hrLyCpmEnder_2 = QtWidgets.QHBoxLayout()
        self.hrLyCpmEnder_2.setObjectName("hrLyCpmEnder_2")
        self.lbBairro = QtWidgets.QLabel(self.frCpmEnder)
        self.lbBairro.setObjectName("lbBairro")
        self.hrLyCpmEnder_2.addWidget(self.lbBairro)
        self.txtBairro = QtWidgets.QLineEdit(self.frCpmEnder)
        self.txtBairro.setObjectName("txtBairro")
        self.hrLyCpmEnder_2.addWidget(self.txtBairro)
        self.verticalLayout.addLayout(self.hrLyCpmEnder_2)
        self.hrLyEndereco = QtWidgets.QHBoxLayout()
        self.hrLyEndereco.setObjectName("hrLyEndereco")
        self.lbEndereco = QtWidgets.QLabel(self.frCpmEnder)
        self.lbEndereco.setObjectName("lbEndereco")
        self.hrLyEndereco.addWidget(self.lbEndereco)
        self.txtEndereco = QtWidgets.QLineEdit(self.frCpmEnder)
        self.txtEndereco.setObjectName("txtEndereco")
        self.hrLyEndereco.addWidget(self.txtEndereco)
        self.verticalLayout.addLayout(self.hrLyEndereco)
        self.hrLyCpmEnder = QtWidgets.QHBoxLayout()
        self.hrLyCpmEnder.setObjectName("hrLyCpmEnder")
        self.lbCpmEnder = QtWidgets.QLabel(self.frCpmEnder)
        self.lbCpmEnder.setObjectName("lbCpmEnder")
        self.hrLyCpmEnder.addWidget(self.lbCpmEnder)
        self.txtCpmEnder = QtWidgets.QLineEdit(self.frCpmEnder)
        self.txtCpmEnder.setObjectName("txtCpmEnder")
        self.hrLyCpmEnder.addWidget(self.txtCpmEnder)
        self.verticalLayout.addLayout(self.hrLyCpmEnder)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.frCpmEnder)
        self.horizontalLayout.addWidget(self.gBCpmLoc)
        self.frAcoes = QtWidgets.QFrame(self.centralwidget)
        self.frAcoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frAcoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAcoes.setObjectName("frAcoes")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frAcoes)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 370, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.hrLyComand = QtWidgets.QHBoxLayout()
        self.hrLyComand.setObjectName("hrLyComand")
        self.verticalLayout_2.addLayout(self.hrLyComand)
        self.btnExecutar = QtWidgets.QPushButton(self.frAcoes)
        self.btnExecutar.setObjectName("btnExecutar")
        self.verticalLayout_2.addWidget(self.btnExecutar)
        self.horizontalLayout.addWidget(self.frAcoes)
        CadPerson.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CadPerson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastros = QtWidgets.QMenu(self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        CadPerson.setMenuBar(self.menubar)
        self.actionPessoa = QtWidgets.QAction(CadPerson)
        self.actionPessoa.setObjectName("actionPessoa")
        self.menuCadastros.addAction(self.actionPessoa)
        self.menubar.addAction(self.menuCadastros.menuAction())

        self.retranslateUi(CadPerson)
        QtCore.QMetaObject.connectSlotsByName(CadPerson)

    def retranslateUi(self, CadPerson):
        _translate = QtCore.QCoreApplication.translate
        CadPerson.setWindowTitle(_translate("CadPerson", "CadPerson"))
        self.gBInfoUser.setTitle(_translate("CadPerson", "Informacoes necessarias"))
        self.lbPersonName.setText(_translate("CadPerson", "Nome Completo:"))
        self.lbNascimento.setText(_translate("CadPerson", "Data de nascimento:"))
        self.lbRg.setText(_translate("CadPerson", "RG:"))
        self.lbCpf.setText(_translate("CadPerson", "CPF:"))
        self.lbSexo.setText(_translate("CadPerson", "Sexo:"))
        self.cbSexo.setItemText(0, _translate("CadPerson", "M"))
        self.cbSexo.setItemText(1, _translate("CadPerson", "F"))
        self.lbTelefone.setText(_translate("CadPerson", "Numero Telefone:"))
        self.lbEmail.setText(_translate("CadPerson", "e-mail:"))
        self.lbCep.setText(_translate("CadPerson", "CEP:"))
        self.lbVerfCep.setText(_translate("CadPerson", "Cep nao verificado"))
        self.btnCheckCep.setText(_translate("CadPerson", "check cep"))
        self.chBxInfoAtCep.setText(_translate("CadPerson", "Informações preenchidas atraves do cep"))
        self.gBCpmLoc.setTitle(_translate("CadPerson", "Complementos para localizacao"))
        self.lbPais.setText(_translate("CadPerson", "Pais:"))
        self.lbEstado.setText(_translate("CadPerson", "Estado:"))
        self.lbCidade.setText(_translate("CadPerson", "Cidade:"))
        self.lbBairro.setText(_translate("CadPerson", "Bairro:"))
        self.lbEndereco.setText(_translate("CadPerson", "Rua:"))
        self.lbCpmEnder.setText(_translate("CadPerson", "Complemento de endereco:"))
        self.btnExecutar.setText(_translate("CadPerson", "Cadastrar"))
        self.menuCadastros.setTitle(_translate("CadPerson", "Cadastros"))
        self.actionPessoa.setText(_translate("CadPerson", "Pessoa"))