'''
Module (modules) și pachete (packages) în Python
'''
'''
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

# import random as rand
# # from random import randint as r
# # from random import randint # , randrange, ...
# import exemplu_modules_import as md
# # import math
# import exemplu_package.exemplu_pkg_mod1 as pkgmd1

# def calcul():
#     a = rand.randint(1,5)
#     b = rand.randint(1,5)
#     return a + b


# def main():
#     print(calcul())
#     # md.my_function()
#     # print(md.my_var)
#     # print(math.pi)
#     # print(md.__name__)
#     # print(__name__)
#     pkgmd1.pkg_mod_1_function()
#     print(pkgmd1.var_mod1)

# import sys

# def afiseaza_nume(nume, prenume):
#     print(f'Nume: {nume}, Prenume: {prenume}')


# def main(lista_argumente):
#     afiseaza_nume(lista_argumente[0], lista_argumente[1])


# if __name__ == '__main__':
#     main(sys.argv[1:])


import argparse

def parse_arguments():
    my_parser = argparse.ArgumentParser(description='Afiseaza nume frumos')

    my_parser.add_argument('--nume', type=str, default='Ionescu', help='Nume de familie')
    my_parser.add_argument('--prenume', type=str, default='Mihai')

    args = my_parser.parse_args()
    return args.nume, args.prenume


def main():
    nume, prenume = parse_arguments()
    print(f'Nume: {nume}, Prenume: {prenume}')


if __name__ == '__main__':
    main()

# ArgumentParser() → creează parser
# add_argument() → adaugă argumente
# required=True → argument obligatoriu
# default= → valoare implicită
# type=str/int/float → tipul datelor
# parse_args() → citește argumentele din terminal