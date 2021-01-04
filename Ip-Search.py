import socket
import os
import time
os.system("cls || clear")
print("""

 ____  _____    _    ____   ____ _   _
/ ___|| ____|  / \  |  _ \ / ___| | | |
\___ \|  _|   / _ \ | |_) | |   | |_| |
 ___) | |___ / ___ \|  _ <| |___|  _  |
|____/|_____/_/   \_\_| \_\\____|_| |_|


	""")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(2)
url = str(input("Digite o host, www.exemplo.com: "))
time.sleep(2)
resultado = socket.gethostbyname(url)
print("")
print("")

print("Criado por   :         T4OM")
print("URL da Vitima:         {}".format(url))
print("IP da Vitima :         {}".format(resultado))