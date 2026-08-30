'''
Stringuri (șiruri de caractere) în Python

    * Un string este o secvență de caractere delimitată de ghilimele simple ('...'), duble ("...") sau triple (\'\'\'...\'\'\', """...""")

    * Stringurile pot conține orice tip de caractere: litere, cifre, simboluri, spații

    * Stringurile sunt imutabile [imutable] (nu pot fi modificate direct)
'''

'''
Definirea stringurilor:
    s1 = 'Ana are mere'
    s2 = "Python este distractiv!"
    s3 = """Acesta este
un string pe mai multe linii."""
'''

'''
Concatenare și repetare:
    * Concatenare: folosim operatorul +
    * Repetare: folosim operatorul *
'''

'''
Indexare și slicing:
    * Putem accesa caractere individuale folosind indexul - incepe de la 0
        - nume_string[index]

    * Indexare negativă pentru a accesa caractere de la sfârșit
        - nume_string[-index]

    * Putem obține subșiruri folosind slicing
        - nume_string[start:end:step]
'''

'''
Metode utile pentru stringuri:
    * len() - lungimea stringului
    * upper(), lower() - conversie la majuscule/minuscule
    * replace() - înlocuire
    * count() - numără aparițiile unui subșir
    * find() - găsește poziția unui subșir

    nume_string.nume_metoda()
'''

'''
Formatarea stringurilor:
    * f-string: f"Salut, {nume}!"
    * metoda format: "Salut, {}!".format(nume)
'''

'''
Eliminarea spațiilor:
    * strip(), lstrip(), rstrip()
'''

'''
Împărțirea și unirea stringurilor:
    * split() - împarte stringul în listă
    * join() - unește elementele unei liste într-un string
'''

'''
Verificări uzuale:
    * startswith(), endswith(), isdigit(), isalpha()
'''

'''
Iterare prin caractere:
    * Putem parcurge fiecare caracter dintr-un string cu bucla for
'''

'''
Caractere speciale (escape):
    * \n - linie nouă
    * \t - tab
    * \\ - backslash
    * \' - ghilimele simple
    * \" - ghilimele duble
'''

'''
Stringuri goale și conversii:
    * Un string gol are lungimea 0
    * Conversie la string: str()
'''

# var = 'Ala are mere'
# var = 'Ana are mere'
# var = 'Ama are mere'
# print(var)

# 'Marius are pere'
# M - index 0
# a - index 1
# u - index 4 (-2)
# s - index 5 (-1)

# var = 'Marius'
# print(var[0])
# print(var[1])
# print(var[2])
# print(var[3])
# print(var[4])
# print(var[5])
# print()
# print(var[-1])
# print(var[-2])
# print(var[-3])
# print(var[-4])
# print(var[-5])
# print(var[-6])

# "Arad Arad Neamtiu Daniel-Pavel 10 9 10 10 Admis"

# nume_string[start:stop:step]
# var = 'Marius are pere'
# print(var[-4:-2:1])
# print(var[0:6:1])

# str1 = "Ana"
# str2 = "are"
# str3 = "mare"
# propozitie = str1 + ' ' + str2 + ' ' + str3
# print(propozitie)

# ana_multipilicata = str1 * 3 # str1 + str1 + str1
# print(ana_multipilicata)

# my_str = "Arad Arad Neamtiu Daniel-Pavel 10 9 10 10 Admis"
# lungime_str = len(my_str)
# print(lungime_str)

# print(my_str.upper())
# print(my_str.lower())
# print(my_str)

# var = 'orice orice'
# print(var)
# var = var.upper()
# print(var)
# print(var.capitalize())

# my_str = 'Arad Arad Neamtiu Daniel-Pavel 10 9 10 10 Admis'
# print(my_str.replace('Arad', 'Timisoara'))
# print(my_str)
# my_str = my_str.replace('Arad', 'Timisoara')
# my_str = my_str.replace('9', '10')
# print(my_str)

# var = my_str.count('A') + my_str.count('a')
# print(var)

# my_str.lower().count('a')
# my_str.lower() -> my_str_lower.count('a') -> 8
# print(my_str.count('a'))
# print(my_str.lower().count('a'))
# print(type(my_str.lower().count('a')))
# print(type(my_str.lower()))

# type('ceva') -> <class 'str'>
# type(9) -> <class 'int'>

# nume = input('Introdu nume: ')
# varsta = input('Introdu varsta: ')
# var1 = 'Salut, {}! {} are {} ani'.format(nume, nume, varsta)
# var2 = f'Salut, {nume}! {nume} are {varsta} ani'
# print(var1)
# print(var2)

# var = '-=-+Daniel-+$-'
# print(var)
# print(var.strip('$-+'))

var = 'tata mama fratele fsora'
# var = 'dafdsjgafjdhfakjhka'
# print(var.find('fratele'))
# print(var.find('tata'))

# my_list = var.split()
# print(my_list)
# print(var.split('fr'))

# new_string = ' '.join(my_list)
# print(new_string)

# print(var.startswith('ta'))
# print(var.endswith('fsor'))

# var = 'test1'
# print(var.isdigit())
# print(var.isalnum())

# print('test'.isalpha())
# print('123'.isdigit())

# python string methods (web3school - python)

# print(var.isalnum) - nu o sa fie apaelata functia, numai daca punem () la final

poezie = "\'ana\' are \tmulte mere,\nionel vine \"si\" cere"
print(poezie)
