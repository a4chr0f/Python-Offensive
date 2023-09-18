#!/usr/bin/python3

import socket
def scan_Port(target, ini_port, fin_port):
    for port in range(ini_port, fin_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        resultado = sock.connect_ex((target, port))
        if resultado == 0:
            print(f"Puerto {port}: Abierto")
        
        sock.close()
if __name__ == '__main__':
    print("Bienvenido al Escáner de Puertos\n")
    target = input("Ingrese la dirección IP del objetivo: ")
    start_port = int(input("Ingrese el puerto de inicio: "))
    end_port = int(input("Ingrese el puerto final: "))

    scan_Port(target, start_port, end_port)

