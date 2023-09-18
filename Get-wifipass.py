#!/usr/bin/python3

import os
import sys
import subprocess

def get_wifi_linux_passwords():
    passwords = []
    wifi_dir = "/etc/NetworkManager/system-connections/"
    
    if os.geteuid() != 0:
        print("This script requires root privileges to access WiFi passwords.")
        return
    
    for filename in os.listdir(wifi_dir):
        if filename.endswith(".nmconnection"):
            file_path = os.path.join(wifi_dir, filename)
            with open(file_path, "r") as f:
                content = f.read()
                if "psk=" in content:
                    password = content.split("psk=")[1].splitlines()[0].strip()
                    passwords.append((filename, password))
    
    return passwords

def get_wifi_windows_passwords():
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = result.stdout.split("\n")
    wifi_networks = []

    for line in profiles:
        if "Perfil de todos los usuarios" in line:
            parts = line.split(":")
            network_name = parts[1].strip()
            wifi_networks.append(network_name)

    passwords = []
    for network in wifi_networks:
        result = subprocess.run(["netsh", "wlan", "show", "profile", "name=" + network, "key=clear"], capture_output=True, text=True)
        output_lines = result.stdout.split("\n")
        for line in output_lines:
            if "Clave de seguridad" in line:
                password = line.split(":")[1].strip()
                passwords.append((network, password))
    
    return passwords


if __name__ == "__main__":
    print("\n1. Visualizar la contraseña de la red WiFi en Linux")
    print("2. Visualizar la contraseña de la red WiFi en Windows\n")
    option = input("Ingresa la option: ")
    if option == '1':
        wifi_passwords = get_wifi_linux_passwords()
        if wifi_passwords:
            print("WiFi Passwords:")
            for filename, password in wifi_passwords:
                print(f"Network: {filename}, Password: {password}")
        else:
             print("No WiFi passwords found.")
    elif option == '2':
        wifi_passwords = get_wifi_windows_passwords()
        if wifi_passwords:
            print("WiFi Passwords:")
            for filename, password in wifi_passwords:
                print(f"Network: {filename}, Password: {password}")
        else:
             print("No WiFi passwords found.")

