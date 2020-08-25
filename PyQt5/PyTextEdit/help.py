# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(732, 701)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Help)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 731, 701))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "PyTextEdit Help"))
        self.plainTextEdit.setPlainText(_translate("Help", "        ИНСТРУКЦИЯ\n"
"\n"
"1. Тулбар\n"
"    1.1. Вкладка File\n"
"        1.1.1) Кнопка \"New\" создает новый файл\n"
"        1.1.2) Кнопка \"Open\" открывает файл\n"
"        1.1.3) Кнопка \"Save\" сохраняет текущий файл\n"
"        1.1.4) Кнопка \"Save as ...\" сохраняет текущий файл как новый\n"
"        1.1.5) Кнопка \"Quit\" закрывает приложение\n"
"\n"
"    1.2 Вкладка Edit\n"
"        1.2.1) Кнопка \"Undo\" отменяет последнее действие\n"
"        1.2.2) Кнопка \"Redo\" возвращает последнее действие\n"
"        1.2.3) Кнопка \"Cut\" вырезает выделенный текст\n"
"        1.2.4) Кнопка \"Copy\" копирует выделенный текст\n"
"        1.2.5) Кнопка \"Paste\" вставляет ранее вырезанный (скопированный) текст\n"
"\n"
"    1.3 Вкладка View\n"
"        1.3.1) Кнопка \"Fullscreen\" разворачивает окно приложения в полный экран\n"
"        1.3.2) Кнопка \"Normal\" сворачивает окно приложения к стандартному состоянию\n"
"        1.3.3) Кнопка \"Minimize\" полностью сворачивает окно приложения\n"
"        1.3.4) Кнопка \"Font\" открывет диалоговое окно выбора параметров шрифта\n"
"\n"
"    1.4 Вкладка Help\n"
"        1.4.1) Кнопка \"Text Editor Help\" выводит текущую инструкцию пользования\n"
"        1.4.2) Кнопка \"About\" выводит краткую справку о приложении и разработчике\n"
"\n"
"2. Текстовая область\n"
"    Текстовая область применяется для ввода и вывода текста. Также имеет поддержку выделения \n"
"    отдельных элементов.\n"
"\n"
"3. Прочее\n"
"    - Текстовый редактор имеет возможность чтения как простых текстовых файлов, так и HTML страниц\n"
"    - Кнопки \"Undo\" и \"Redo\" выполняют взаимообратные действия. Каждая из этих кнопок отменяет \n"
"       эффект предыдущей\n"
"    - Диалоговое окно выбора параметров шрифта предоставляет на выбор след. действия:  \n"
"       шрифт,  размер , стиль, эффекты и систему ввода\n"
" "))
