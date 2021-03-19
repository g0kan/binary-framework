from colorama import Fore
import requests
from time import sleep
import os

os.system("clear")

logo = Fore.GREEN + """
  ____  _                        
 | __ )(_)_ __   __ _ _ __ _   _ 
 |  _ \| | '_ \ / _` | '__| | | |
 | |_) | | | | | (_| | |  | |_| | ᴮᶦⁿᵃʳʸ ᶠʳᵃᵐᵉʷᵒʳᵏ ⁻ ᴮᵉᵗᵃ
 |____/|_|_| |_|\__,_|_|   \__, |
                           |___/

 [1] Instalação das Ferramentas.
 [2] Ferramentas.
 [3] Fechar Framework.                          
"""

print(logo)
print(Fore.CYAN + "[*]" + Fore.WHITE + " Digite a opção desejada.")
print("")

option = input("binary-framework :: ~ ")

if option == "1":
    print("")
    print(Fore.CYAN + "[*]" + Fore.WHITE + " Menu de Instalação de Ferramentas.")
    print("")
    print("""
    [1] Instale o nmap (Necessita de ROOT).
    [2] Instale o sqlmap (Necessita de ROOT).
    
    A versão beta possui poucas ferramentas.
    """)
    optionF = input("binary-framework :: ~ ")
    if optionF == "1":
        os.system("apt-get install nmap")
    elif optionF == "2":
        os.system("apt-get install sqlmap")    
    else:
        print(Fore.RED + "[*]" + Fore.WHITE + " Digite uma opção válida.")

elif option == "2":
    print("")
    print(Fore.CYAN + "[*]" + Fore.WHITE + " Menu de Ataques.")
    print("")
    print("""
    [1] Faz uma requisição no site desejado.
    [2] Realiza um scan utilizando o NMAP (Necessita de ROOT).
    [3] Realiza um scan de vulnerabilidades em um sistema ou site.
    
    A versão beta possui poucos ataques.
    """)
    optionA = input("binary-framework :: ~ ")
    if optionA == "1":
        print("")
        print(Fore.CYAN + "[*]" + Fore.WHITE + ' Digite utilizando "https://URL" ou se for http - "http://URL" - Logicamente sem as aspas.')
        print("")
        op = input(Fore.CYAN + "[*]" + Fore.WHITE + " URL: ")
        r = requests.get(op)
        print("")
        print(Fore.CYAN + "[*]" + Fore.WHITE + " Site alvo: " + r.url)
        sleep(2)
        print("")
        print(r.text)
        print("")
        print(Fore.CYAN + "[*]" + Fore.WHITE + " Requisição feita.")
    elif optionA == "2":
        print("")
        print(Fore.CYAN + "[*]" + Fore.WHITE + " Digite o IP ou a URL sem http ou https, exemplo: google.com")
        print("")
        opt = input(Fore.CYAN + "[*]" + Fore.WHITE + " IP / Host: ")
        print("")
        os.system("nmap -sS -sV -sC -A " + opt)
    elif optionA == "3":
        print("")
        print(Fore.CYAN + "[*]" + Fore.WHITE + " Digite o IP ou a URL sem http ou https, exemplo: google.com - Necessita do script de vulnerabilidades do nmap.")
        print("")
        optn = input(Fore.CYAN + "[*]" + Fore.WHITE + " IP / Host: ")
        print("")
        os.system("nmap --script vuln " + optn)
elif option == "3":
    os.system("exit")
else:
    print(Fore.RED + "[*]" + Fore.WHITE + " Opção inválida.")           

    
