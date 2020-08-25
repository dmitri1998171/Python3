# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 213)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 341, 171))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About"))
        self.plainTextEdit.setPlainText(_translate("Form", "PyTextEdit\n"
"\n"
"Приложение для просмотра и редактирования текстовых документов. \n"
"\n"
"Разработчик: Родионов Дмитрий"))
