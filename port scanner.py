import socket
from colorama import init, Fore
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER ^-^")
print(ascii_banner)

init()
green = Fore.GREEN
red = Fore.RED
gray =  Fore.LIGHTWHITE_EX

def IsPortOpen (host, port):
    SOCKET = socket.socket

    try:
        SOCKET.connect((host, port))
        # s.settimeout(0.2)

    except:
        return False
        
    else:
        return True
    
host = input("Enter the host: ")

for port in range(1, 1024):
    if IsPortOpen(host, port):
        print(f"{green}[+] {host}:{port} is open      {gray}") 
        
    else: 
        print(f"{red}[-] {host}:{port} is closed      {gray}")
