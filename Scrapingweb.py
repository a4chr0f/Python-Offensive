#!/usr/bin/python3
#author: achraf
import re
import requests
from bs4 import BeautifulSoup
import socket
import ssl


def web_scraping_url(url):
  
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print('Error al realizar la solicitud HTTP.')

def web_scraping_email(url):
    
    response = requests.get(url)

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        # Buscar patrones de correo electrónico en el contenido HTML
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(pattern, response.text)

        # Imprimir las direcciones de correo encontradas
        for email in emails:
            print(email)
    else:
        print('Error al realizar la solicitud HTTP.')

def web_scraping_ssl_info(url):
    # Obtener el nombre de host y el puerto de la URL
    host = url.split("//")[-1].split("/")[0]
    port = 443
    
    # Crear una conexión segura SSL
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            # Obtener el certificado SSL
            cert = ssock.getpeercert()
            
            # Extraer los detalles del certificado
            subject = dict(x[0] for x in cert['subject'])
            issuer = dict(x[0] for x in cert['issuer'])
            common_name = subject['commonName']
            not_before = cert['notBefore']
            not_after = cert['notAfter']
            
            # Imprimir los detalles del certificado
            print("\nDetalles del Certificado SSL:")
            print("Sujeto:", subject)
            print("Emisor:", issuer)
            print("Nombre Común (Common Name):", common_name)
            print("Válido desde:", not_before)
            print("Válido hasta:", not_after)
def main():
    while True:
        
        print(" ___   ___  ____    __    ____  ____  _    _  ____ ")
        print('/ __) / __)(  _ \  /__\  (  _ \( ___)( \/\/ )(  _ \`')
        print("\__ \( (__  )   / /(__)\  )___/ )__)  )    (  ) _ <")
        print("(___/ \___)(_)\_)(__)(__)(__)  (____)(__/\__)(____/\n")
        

        print("1. Extraer URLs de una página web")
        print("2. Extraer certificado de una página web")
        print("3. Extraer correos electrónicos de una página web\n")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            url = input("Ingrese la URL: ")
            
            web_scraping_url(url)

        elif opcion == "2":
            url = input("Ingrese la URL: ")
            web_scraping_ssl_info(url)
        elif opcion == "3":
            url = input("Ingrese la URL: ")
            web_scraping_email(url)            
        else:
            break
if __name__ == '__main__':
    main()
