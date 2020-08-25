import sys, os, shutil  
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, uic

from functions import *
import gui                           # Это наш конвертированный файл 
      

class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# Работа с таблицей ################################################

        self.tableWidget.setColumnWidth(0,575)
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.resizeColumnToContents(2)
        self.tableWidget.resizeColumnToContents(3)
        TableLoadFunc(self, current_row_count)

# Кнопки ############################################################

        self.prev.clicked.connect(self.prevFunc)
        self.next.clicked.connect(self.nextFunc)
        self.up.clicked.connect(self.upFunc)
        self.lineEdit.setText(path)

            # Тулбар
        toolbar_buttons(self)

#####################################################################
#####################################################################
# Функции ###########################################################

    def prevFunc(self):
        print("prevFunc!")
        os.chdir()

    def nextFunc(self):
        print("nextFunc!")
        os.chdir()

    def upFunc(self):
        print("upFunc!")

#####################################################################

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        if e.key() == QtCore.Qt.Key_Enter:
            # openFile_FolderFunc()
            pass

#####################################################################
#####################################################################
#####################################################################

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()                   # Создаём объект класса ExampleApp
    window.show()                           # Показываем окно
    app.exec_()                             # и запускаем приложение

if __name__ == '__main__':                  # Если мы запускаем файл напрямую, а не импортируем
    main()                                  # то запускаем функцию main()

#       TODO
#
# \/ 1) заполнить таблицу
# 2) переход
# 3) тулбар
#   \/ 3.1) кнопки
#   3.2) функции
# 4) контекст. меню
#   4.1) открыть файл   !!!
# 5) доп.
#   5.1) скрыть файлы
#   5.2) 
#