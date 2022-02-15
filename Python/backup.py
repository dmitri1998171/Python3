import sys, os, shutil

try:
	# Получаем аргументы
	argv = sys.argv[1] 
	path = os.getcwd()

	# Переименовывем скопированный файл
	index = argv.find('.', 0, len(argv))
	new_name = argv[0:index]
	file_format = argv[index:len(argv)]

	new_name = new_name + ' - copy' + file_format # меняем имя (исключаем конфликт одинаковых имен при копир.)
	dst = path + '/' + new_name # копир. переменную
	path = path + '/' + argv # создаем полный путь до файла

	# копир. файл
	shutil.copyfile(path, dst) 

except IndexError:
	print("Invalid filename!")

except FileNotFoundError:
	print("Invalid filename!")
