#!/usr/bin/python3
import re
import subprocess
import sys

def arguments():
    print("\n[!] Use: python3 " + sys.argv[0] + " <IP-address>\n")
    sys.exit(1)

def get_valor(address):
    patron = r"ttl=(\d+)"
    resultado = subprocess.check_output(["ping", "-c", "1", address]).decode("utf-8")
    match = re.search(patron, resultado)
    if match:
       return match.group(1)

if __name__ == '__main__':
    try:
        ip_address = sys.argv[1]
        ttl_value = get_valor(ip_address)
        ttl_value = int(ttl_value)

        if ttl_value >= 0 and ttl_value <= 64:
            print(f"\n {ip_address} -> Linux \n" )
        elif ttl_value >= 65 and ttl_value <= 128:
            print(f"\n {ip_address} -> Windows \n" )
    except:
        arguments()
