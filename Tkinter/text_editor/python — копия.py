
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


#===============================================
def openFunc():
	try:
		f1 = open(e.get(), "r")
		text.delete(1.0, END)
		text.insert(0.0, f1.read())
		f1.close()
	except FileNotFoundError:
		text.delete(1.0, END)
		messagebox.showinfo("Сообщение", "! Файл не найден !")
	

# # # # # # # # # # # # # # # # # # # # # # # # 

def saveFunc():
	str = text.get(1.0, END)
	f1 = open(e.get(), "w")
	f1.write(str)
	messagebox.showinfo("Сообщение", "Файл {0}, был удачно сохранён!".format(e.get()))
	f1.close()
#===============================================
try:
	root = Tk()

################################################
	f_top=Frame(root)
	f_bot=Frame(root)

	e = Entry(f_top, width=40)
	#e.insert(0,"text.out")

	but1 = Button(f_top, text="открыть", command=openFunc)
	but2 = Button(f_top, text="сохранить", command=saveFunc)
	text = Text(f_bot, width=77, wrap=WORD)

	#openFunc()

	f_top.pack()
	f_bot.pack()

	e.pack(side=LEFT)
	but1.pack(side=LEFT)
	but2.pack(side=LEFT)
	text.pack(expand=1, fill=X)
################################################

	root.title("Notepad_python3")
	root.mainloop()
except(KeyboardInterrupt): root.quit()








