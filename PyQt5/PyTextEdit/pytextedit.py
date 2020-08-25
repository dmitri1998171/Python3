import sys, os

from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QApplication, QFileDialog, QFontDialog
from PyQt5.QtGui import QWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtWidgets, uic

from gui import Ui_MainWindow
from about import Ui_Form


class MainWindow(QMainWindow):
        
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fname = False
        
########################################################

        New=self.ui.actionNew
        New.triggered.connect(self.newFunc)
        New.setShortcut('Ctrl+N')
        New.setStatusTip('Create new file')
        
        Open=self.ui.actionOpen
        Open.triggered.connect(self.openFunc)
        Open.setShortcut('Ctrl+O')
        Open.setStatusTip('Open file')
        
        Save=self.ui.actionSave
        Save.triggered.connect(self.saveFunc)
        Save.setShortcut('Ctrl+S')
        Save.setStatusTip('Save file')
        
        SaveAs=self.ui.actionSave_as
        SaveAs.triggered.connect(self.saveAsFunc)
        SaveAs.setShortcut('Ctrl+Shift+S')
        SaveAs.setStatusTip('Save file as ...')
        
        Exit=self.ui.actionQuit
        Exit.triggered.connect(self.closeEvent)
        Exit.setShortcut('Ctrl+Q')
        Exit.setStatusTip('Quit a programm')
        
########################################################

        Undo=self.ui.actionUndo
        Undo.triggered.connect(self.undoFunc)
        Undo.setShortcut('Ctrl+Z')
        Undo.setStatusTip('Undo')
        
        Redo=self.ui.actionRedo
        Redo.triggered.connect(self.redoFunc)
        Redo.setShortcut('Ctrl+Shift+Z')
        Redo.setStatusTip('Redo')
        
        Cut=self.ui.actionCut
        Cut.triggered.connect(self.cutFunc)
        Cut.setShortcut('Ctrl+X')
        Cut.setStatusTip('Cut')
        
        Copy=self.ui.actionCOPY
        Copy.triggered.connect(self.copyFunc)
        Copy.setShortcut('Ctrl+C')
        Copy.setStatusTip('Copy')
        
        Paste=self.ui.actionPaste
        Paste.triggered.connect(self.pasteFunc)
        Paste.setShortcut('Ctrl+V')
        Paste.setStatusTip('Paste')
        
########################################################

        Fullscreen=self.ui.actionFullscreen
        Fullscreen.triggered.connect(self.fullscreenFunc)
        Fullscreen.setShortcut('F10')
        Fullscreen.setStatusTip('Fullscreen window')

        Minimize=self.ui.actionMinimalize
        Minimize.triggered.connect(self.minimizeFunc)
        Minimize.setShortcut('F8')
        Minimize.setStatusTip('Minimize window')
        
        Normalize=self.ui.actionNormal
        Normalize.triggered.connect(self.normalFunc)
        Normalize.setShortcut('F9')
        Normalize.setStatusTip('Normal window')
        
        Font=self.ui.actionFont
        Font.triggered.connect(self.fontFunc)
        Font.setShortcut('Ctrl+Shift+T')
        Font.setStatusTip('Font')

########################################################

        Help=self.ui.actionText_Editor_help
        Help.triggered.connect(self.helpFunc)

        About=self.ui.actionAbout
        About.triggered.connect(self.aboutFunc)
        
########################################################
########################################################
########################################################

    def openFunc(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if(self.fname):
            with open(self.fname, 'r') as f:
                #self.ui.textEdit.setText(txt)
                self.ui.textEdit.setHtml(f.read())
        
    def saveAsFunc(self):
        saveName = QFileDialog.getSaveFileName(self)[0]
        if(saveName):
            with open(saveName, 'w') as f:
                f.write(self.ui.textEdit.toHtml())
    
    def saveFunc(self):
        if not (self.fname): 
            self.saveAsFunc()
        else:
            with open(self.fname, 'w') as f:
                f.write(self.ui.textEdit.toHtml())
                #txt = self.ui.textEdit.toPlainText()
                #openedFile.write(txt)
            
    def newFunc(self):        
        self.fname = False
        self.ui.textEdit.setText("")
        
########################################################
    
    def undoFunc(self):
        self.ui.textEdit.undo()
        
    def redoFunc(self):
        self.ui.textEdit.redo()
        
    def cutFunc(self):
        self.ui.textEdit.cut()
        
    def copyFunc(self):
        self.ui.textEdit.copy()
        
    def pasteFunc(self):
        self.ui.textEdit.paste()
        
########################################################

    def fullscreenFunc(self):
        window.showMaximized()
        #sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #self.ui.textEdit.showMaximized()
    
    def normalFunc(self):
        window.showNormal()
        
    def minimizeFunc(self):
        window.showMinimized()

    def fontFunc(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)
            
########################################################

    def aboutFunc(self):   
        global new_window
        new_window = uic.loadUi("about.ui")
        new_window.show()
        
    def helpFunc(self):
        global help_window
        help_window = uic.loadUi("help.ui")
        help_window.show()
    
########################################################
        
    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "close event", 
           "Save new file?", 
           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, 
           QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.saveFunc()
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.accept()
            
########################################################
########################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
    
    
