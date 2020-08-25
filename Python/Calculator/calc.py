

def choise(simbol):
	if(simbol=='+'): plus(a,b);
	if(simbol=='-'): razn(a,b);
	if(simbol=='*'): div(a,b);
	if(simbol=='/'): dif(a,b);

def plus(a,b):
	print ("%.2f" % (a+b));

def razn(a,b):
	print ("%.2f" % (a-b));

def div(a,b):
	print ("%.2f" % (a*b));

def dif(a,b):
	if(b!=0): print ("%.2f" % (a/b));
	else: print('!!! деление на 0 !!!')

########################################

#('0','1','2','3','4','5','6','7','8','9')
numbers = (0,1,2,3,4,5,6,7,8,9)

print('\t# CALCULATOR #')
while(True):

	print(' ');
	print('для выхода нажмите q ')
	print(' ');

	simbol = str(input('Enter a simbol: '))
	if (simbol.strip() == 'q' or simbol.strip() == 'Q' or simbol == '0'): break
	if (simbol in ('+','-','*','/')):
		a = float(input('Enter a: '));
		b = float(input('Enter b: '));
		choise(simbol);
	else: print('invalid simbol!')

	
		



# \/ 1) счет
# \/ 2) бескон. цикл
# \/ 3) проверка
# \/ 4) ООП









