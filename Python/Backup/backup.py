import sys
import os
import shutil

try:
	argv = sys.argv[1] # получаем аргумент из комманд. строки
	path = os.getcwd() # получаем путь к файлу

	index = argv.find('.',0,len(argv))
	new_name = argv[0:index]
	file_format = argv[index:len(argv)]

	new_name = new_name+' - copy'+file_format # меняем имя(исключаем конфликт одинаковых имен при копир.)
	dst = path +'/'+new_name # копир. переменную
	path = path+'/'+argv # создаем полный путь до файла
	shutil.copyfile(path, dst) # копир. файл
except IndexError:
	print("\nнет имени файла!\n")
except FileNotFoundError:
	print("\nФайл ",argv,"не существует!\n") 


# \/ 1) получить путь файла + аргум. >>> sys.argv()
# \/ 2) переимен. файл 
# \/ 3) копир. файл shutil.copyfile(src, dst)
# \/ 4) исключения
#		\/ 4.1) нет аргумента
#		\/ 4.2) неправильно написано название

# \/5) улучш. переимен. файла(менять имя файла, а не расшир.)
