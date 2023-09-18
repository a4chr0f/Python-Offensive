#!/usr/bin/python3

import random
import string


def generate_password(length):
    # Definir los caracteres posibles para la contraseña
    pwd = ""
    characters = string.ascii_letters + string.digits + "&%$#@,;.!¡?¿*/-+"
    for i in range(length):
        pwd += ''.join(random.choice(characters))
    
    return pwd

long = int(input("Ingrese la longitud de contraseña: "))
print(generate_password(long))
