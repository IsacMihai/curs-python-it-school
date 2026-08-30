'''
Module (modules) și pachete (packages) în Python

1. Ce este un modul (module)?
   - Un modul este un fișier Python (.py) care conține cod (funcții, clase, variabile) ce poate fi 
   importat și folosit în alte fișiere.
   - Exemplu: math.py, util.py
'''
'''
2. Ce este un pachet (package)?
   - Un pachet este un director care conține mai multe module și un fișier __init__.py (poate fi gol).
   - Permite organizarea codului pe mai multe fișiere și subdirectoare.
'''
'''
3. Importarea unui modul
   - import nume_modul
   - from nume_modul import nume_functie
   - from nume_modul import *
   - from pachet.modul import nume_functie
'''
'''
4. Instalarea unui modul extern
   - Se folosește pip (Python Package Installer) din terminal:
     pip install nume_modul
   - Exemplu: pip install requests
'''
'''
5. Argparse - modul pentru gestionarea argumentelor din linia de comandă
   - Permite definirea și parsarea argumentelor transmise la rularea scriptului din terminal
'''

# Exemple de import și utilizare

# Import modul standard
# import math
# print(math.sqrt(16))  # sqrt este funcție din modulul math

# # Import doar o funcție din modul
# from math import ceil
# print(ceil(3.2))

# # Import cu alias
# import math as m
# print(m.pi)

# # Import dintr-un pachet (exemplu generic)
# # from pachet.submodul import functie
# # Exemplu: from datetime import datetime
# from datetime import datetime
# print(datetime.now())

# Import toate funcțiile (NU recomandat în practică)
# from math import *

# Instalare modul extern (exemplu, se rulează în terminal, nu în cod):
# pip install requests

# Import modul extern instalat
# import requests
# r = requests.get('https://www.google.com')
# print(r.status_code)

# # Crearea unui modul propriu:
# # 1. Creezi un fișier util.py cu funcții.
# # 2. În alt fișier: import util sau from util import func_name

# # Crearea unui pachet propriu:
# # 1. Creezi un director cu __init__.py și alte module.
# # 2. Import: from pachet.modul import func_name

# # Exemplu parsare argumente din linia de comandă cu argparse
# import argparse
# parser = argparse.ArgumentParser(description='Descrierea scriptului')

# parser.add_argument('--nume', type=str, help='Numele utilizatorului')

# args = parser.parse_args()
# print(f"Salut, {args.nume}!")


lista = [7, 5, 9, 2, 0, 3, 12, 1]

def min_max(lista):
   min = lista[0]
   max = lista[0]

   for numar in lista:
      if numar < min:
            min = numar

      if numar > max:
            max = numar
   # print('Min:', min)
   # print('Max:', max)    
   return min, max
# min_max(lista)
print(min_max(lista))
