
from tkinter import *

win = Tk()
win.title("Решение примеров")

PlusMinus = False

##############################################
def test(s):
	try:
		l1["text"] = eval(ent.get())
		#ent.insert(0,eval(ent.get()))
	except:
		l1["text"] = "! ошибка !"

def calc():
	l1["text"] = eval(ent.get())
###############################################

def commandOne():
	ent.insert(END,'1')

def commandTwo():
	ent.insert(END,'2')

def commandThree():
	ent.insert(END,'3')

def commandFour():
	ent.insert(END,'4')

def commandFive():
	ent.insert(END,'5')

def commandSix():
	ent.insert(END,'6')

def commandSeven():
	ent.insert(END,'7')

def commandEight():
	ent.insert(END,'8')

def commandNine():
	ent.insert(END,'9')

def commandZero():
	ent.insert(END,'0')

def commandPlus():
	ent.insert(END,'+')

def commandDot():
	ent.insert(END,'.')

def commandMinus():
	ent.insert(END,'-')

def commandDiv():
	ent.insert(END,'*')

def commandDel():
	ent.insert(END,'/')

def commandAC():
	ent.delete(0,END)

def commandPlusMinus():
	if(PlusMinus==True): 
		ent.insert(0,'-');
		PlusMinus=False;




ent = Entry(width=20,bg="white")
ent.grid(row=0,column=0, columnspan=4)
ent.bind('<Return>', test)
ent.bind('<Escape>', win.quit())
s = ent.get()

l1 = Label()
l1.grid(row=6, column=0, columnspan=4)


################################################################
b0 = Button(text="0", width=1, command=commandZero).grid(row=5, column=0)
bDot = Button(text=".", width=1, command=commandDot).grid(row=5, column=1)
bvoid = Button(text=" ", width=1).grid(row=5, column=2)

b1 = Button(text="1", width=1, command=commandOne).grid(row=4, column=0)
b2 = Button(text="2", width=1, command=commandTwo).grid(row=4, column=1)
b3 = Button(text="3", width=1, command=commandThree).grid(row=4, column=2)

b4 = Button(text="4",width=1, command=commandFour).grid(row=3,column=0)
b5 = Button(text="5",width=1, command=commandFive).grid(row=3,column=1)
b6 = Button(text="6",width=1, command=commandSix).grid(row=3,column=2)

b7 = Button(text="7",width=1, command=commandSeven).grid(row=2,column=0)
b8 = Button(text="8",width=1, command=commandEight).grid(row=2,column=1)
b9 = Button(text="9",width=1, command=commandNine).grid(row=2,column=2)

AC = Button(text="AC",width=1, command=commandAC).grid(row=1,column=0)
plmin = Button(text="+/-",width=1, command=commandPlusMinus).grid(row=1,column=1)
percents = Button(text="%",width=1).grid(row=1,column=2)

div = Button(text="/",width=1, command=commandDel).grid(row=1,column=3)
proizv = Button(text="*",width=1, command=commandDiv).grid(row=2,column=3)
minus = Button(text="-",width=1, command=commandMinus).grid(row=3,column=3)
plus = Button(text="+",width=1, command=commandPlus).grid(row=4,column=3)
equ = Button(text="=",width=1, command=calc).grid(row=5,column=3)
################################################################


win.geometry('193x195+500+300')
win.mainloop()












