import os
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtCore, uic

# имя пользователя
log_name = os.getlogin()

# путь
get_path = os.getcwd()
path = "/home/"+log_name+"/"

# список файлов в директории
global dir_list
dir_list = os.listdir(path=path)
print(os.path.split(path))

# текущее кол-во строк
global current_row_count
current_row_count = 0

# подсчет кол-ва новых папок
num_new_folder = 0
current_folder_name = ""

def toolbar_buttons(self):
    create_doc = self.actionCreate_Document
    create_doc.triggered.connect(create_docFunc)
    create_doc.setShortcut('Ctrl+Shift+N')
    create_doc.setStatusTip('Create new file')

    create_folder = self.actionCreate_Folder
    create_folder.triggered.connect(create_folderFunc)
    create_folder.setShortcut('Ctrl+N')
    create_folder.setStatusTip('Create new folder')

    open_with = self.actionOpen_with
    open_with.triggered.connect(open_withFunc)
    open_with.setStatusTip('Open document with ...')
    
    properties = self.actionProperties
    properties.triggered.connect(propertiesFunc)

    Exit=self.actionClose_Window
    Exit.triggered.connect(exitFunc)
    Exit.setShortcut('Ctrl+Q')
    Exit.setStatusTip('Quit a programm')

############################################################

    Cut=self.actionCut
    Cut.triggered.connect(cutFunc)
    Cut.setShortcut('Ctrl+X')
    Cut.setStatusTip('Cut')
    
    Copy=self.actionCopy
    Copy.triggered.connect(copyFunc)
    Copy.setShortcut('Ctrl+C')
    Copy.setStatusTip('Copy')
    
    Paste=self.actionPaste
    Paste.triggered.connect(pasteFunc)
    Paste.setShortcut('Ctrl+V')
    Paste.setStatusTip('Paste')

    dublicate=self.actionDublicate
    dublicate.triggered.connect(dublicateFunc)
    dublicate.setShortcut('Ctrl+B')
    dublicate.setStatusTip('Dublicate')

    MtoTrash=self.actionMove_to_Trash
    MtoTrash.triggered.connect(MtoTrashFunc)
    MtoTrash.setShortcut('Delete')
    MtoTrash.setStatusTip('Delete')
    
    Rename=self.actionRename
    Rename.triggered.connect(RenameFunc)
    Rename.setShortcut('Ctrl+R')
    Rename.setStatusTip('Rename')

    Settings=self.actionSettings
    Settings.triggered.connect(SettingsFunc)

############################################################

    Fullscreen=self.actionFullscreen
    Fullscreen.triggered.connect(fullscreenFunc)
    Fullscreen.setShortcut('F10')
    Fullscreen.setStatusTip('Fullscreen window')

    Minimize=self.actionMinimize
    Minimize.triggered.connect(minimizeFunc)
    Minimize.setShortcut('F8')
    Minimize.setStatusTip('Minimize window')
    
    Normalize=self.actionNormal
    Normalize.triggered.connect(normalFunc)
    Normalize.setShortcut('F9')
    Normalize.setStatusTip('Normal window')

    Reload=self.actionReload
    Reload.triggered.connect(ReloadFunc)
    Reload.setShortcut('F2')
    Reload.setStatusTip('Reload window')

############################################################

    Parent=self.actionParent
    Parent.triggered.connect(ParentFunc)
    Parent.setShortcut('Alt+Up')
    Parent.setStatusTip('Open the parent folder')

    Back=self.actionBack
    Back.triggered.connect(BackFunc)
    Back.setShortcut('Alt+Left')
    Back.setStatusTip('Go to the previous visited folder')
    
    Forward=self.actionForward
    Forward.triggered.connect(ForwardFunc)
    Forward.setShortcut('Alt+Right')
    Forward.setStatusTip('Go to the next visited folder')

############################################################

    About=self.actionAbout
    About.triggered.connect(aboutFunc)

############################################################
############################################################
############################################################

def TableLoadFunc(self, current_row_count):

    # рассчет размеров таблицы
    self.tableWidget.setRowCount(current_row_count)
    if(len(dir_list) > current_row_count): current_row_count = len(dir_list)
    self.tableWidget.setRowCount(current_row_count)

    # Заполнение таблицы
    for i in range(len(dir_list)):
        # имя
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(dir_list[i]))
        
        # размер
        size = os.path.getsize(path+dir_list[i])
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(size)))
        
        # тип
        if(os.path.isfile(path+dir_list[i])):
            file_type = "File"
        if(os.path.isdir(path+dir_list[i])):
            file_type = "Folder"
        self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(file_type))

        # время изменения (+перевод из секунд в дни)
        time = os.path.getmtime(path+dir_list[i]) / (100 * 60 * 60 * 12 * 30)
        self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(str(time)))
        
        print(dir_list[i]," ",size, " ",time)

def create_docFunc(self):
    print("create_docFunc!")

def create_folderFunc(self):
    global num_new_folder
    global current_folder_name
    print("create_folderFunc!")
   
    # проверка наличия новой папки
    if (os.path.exists(path+"New Folder")): 
        current_folder_name = "("+str(num_new_folder)+")"

    result_folder_name = "New Folder"+current_folder_name
    num_new_folder = num_new_folder + 1
    
    # создание папки
    os.mkdir(path+result_folder_name)
    #TableLoadFunc(self, current_row_count)

def open_withFunc(self):
    print("open_withFunc!")

def propertiesFunc(self):
    print("propertiesFunc!")

def exitFunc(self):
    exit(0)

############################################################

def cutFunc(self):
    self.tableWidget.cut()
        
def copyFunc(self):
    self.tableWidget.copy()
    
def pasteFunc(self):
    self.tableWidget.paste()

def dublicateFunc(self):
    print("dublicateFunc!")

def MtoTrashFunc(self):
    print("MtoTrash!")

def RenameFunc(self):
    print("Rename!")

def SettingsFunc(self):
    print("Settings!")

############################################################

def fullscreenFunc(self):
    window.showMaximized()
    #sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    #self.ui.textEdit.showMaximized()
    
def normalFunc(self):
    window.showNormal()
    
def minimizeFunc(self):
    window.showMinimized()

def ReloadFunc(self):
    print("ReloadFunc!")

############################################################

def ParentFunc(self):
    print("ParentFunc!")

def BackFunc(self):
    print("BackFunc!")

def ForwardFunc(self):
    print("ForwardFunc!")

############################################################

def aboutFunc(self):   
    global new_window
    new_window = uic.loadUi("about.ui")
    new_window.show()