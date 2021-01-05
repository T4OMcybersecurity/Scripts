import socket
import time
import os
os.system("cls")
print("""

 ____ _____ ____   ____    _    _   _ _   _
|  _ \_   _/ ___| / ___|  / \  | \ | | \ | |
| |_) || | \___ \| |     / _ \ |  \| |  \| |
|  __/ | |  ___) | |___ / ___ \| |\  | |\  |
|_|    |_| |____/ \____/_/   \_\_| \_|_| \_|

""")
print("[1]Verificar Portas")
print("[2]Scannear Portas")
print("")
op = int(input("Digite a sua opçao: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if op == 1:
	ip = str(input("Digite o endereço IP: "))
	porta = int(input("Digite a porta: "))
	
	if s.connect_ex((ip,porta)):
		print("[+]Porta {}: Close".format(porta))
	else:
		print("[+]Porta {}: Open".format(porta))
		
elif op == 2:
	ip2 = str(input("Digite o endereço IP: "))
	print("Este processo pode demorar um pouco")
	print("IP: {}".format(ip2))
	for portas in range(1,65335):
		s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s2.connect_ex((ip2,portas)) == 0:
			print("Porta: {}".format(portas))
elif op == "":
	print("Falha de escolha")
	time.sleep(2)
	print(">>>>>>>>>>>>>T4OM<<<<<<<<<<<<<")
	time.sleep(2)
	os.system("exit")	
