'''
Controlul fluxului programului în Python

Blocuri de cod și indentare:
    * Un bloc de cod reprezintă o secvență
      de instrucțiuni care aparțin unei structuri de control (if, for, while, funcții etc.).
    * În Python, blocurile de cod se definesc prin indentare
      (spații sau tab-uri la începutul liniei).
    * Toate instructiunile care aparțin aceluiași bloc trebuie să fie indentate la același nivel.
    * Exemplu:

[bloc1]
instructiune1
instructiune2
instructiune3

codnditie1
    [bloc2]
    instructiune4
    instructiune5
    [sfarsit_bloc2]

instructiune6

codnditie2
    [bloc3]
    instructiune7
    instructiune8

    conditie3
        [bloc4]
        instructiune9
        instructiune10
        [sfarsit_bloc4]

    instructiune11
    [sfarsit_bloc3]

[sfarsit_bloc1]


1. Instrucțiunea if
    * Permite executarea condiționată a unor blocuri de cod
    * Sintaxă:
        if condiție:
            # cod dacă condiția e adevărată
        elif altă_condiție:
            # cod dacă altă condiție e adevărată
        else:
            # cod dacă niciuna nu e adevărată

2. Instrucțiunea for
    * Permite parcurgerea elementelor dintr-o secvență (listă, string, etc.)
    * Sintaxă:
        for element in secvență:
            # cod pentru fiecare element

3. Instrucțiunea while
    * Execută un bloc de cod cât timp o condiție este adevărată
    * Sintaxă:
        while condiție:
            # cod repetat

TODO
Instrucțiuni suplimentare:
    * break - oprește bucla
    * continue - sare peste restul iterației curente
    * pass - nu face nimic (placeholder)


Functii:
    - range() - generează o secvență de numere de la un start până la un stop [exclusiv], cu un step specificat (implicit 1)
        exemple:
            range(5) generează 0, 1, 2, 3, 4 (nu e obligatoriu sa contina start si step)
            range(2, 10, 2) generează 2, 4, 6, 8
                2 - start
                10 - stop (exclusiv)
                2 - step
'''

# a = 10
# b = 12

# if a < b:
#     print("a este mai mare decat b")
# elif a > b:
#     print("a este mai mare decat b")
# else:
#     print("a este egal cu b")

# if a > b:
#     print("a > b")
# else:
#     print("a este mai mai mic sau egal cu b")

# if a < b and a % 2 == 0:
#     print("a e mai mic decat b si a este par")
# a = 14
# if a < b:
#     print("a este mai mic decat b")
#     print("ce faci frate?")

# if a % 2 == 0:
#     print("a este si numar par")


my_str = 'mama are 10 pere'
# for char in my_str:
#     print(char)

# mama -> x litere

# for cuvant in my_str.split():
#     # print(cuvant)
#     lungime = len(cuvant)
#     # print(lungime)
#     print(f'{cuvant} -> {lungime} litere')

# for char in my_str:
#     if char.isdigit():
#         var = ''.join()
#         print(char)

# my_str = 'mama are 10 pere'
# text = ''
# for char in my_str:
#     if char.isdigit():
#         text += char

# print(f"Cifrele din string sunt: {text}")

# print(f"Cifrele din string sunt: {text}")
# print(f"Cifrele din string sunt: " + text)

# for numar in range(2,4,2):
#     print(numar)

# numar = 1
# limita = 5
# while numar <= limita:
#     print(numar)
#     numar += 1

# x = 15

# if x % 3 == 0:
#     print('fizz')

# if x % 5 == 0:
#     print('buzz')

# if x % 3 == 0 and x % 5 == 0:
#     print('fizzbuzz')

# n = 15

# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# elif n % 5 == 0:
#     print("Buzz")
# elif n % 3 == 0:
#     print("Fizz")
# else:
#     print("Let's try something else! ")

# x = -4
# if x > 0:
#     print("mai mare ca 0")
# else:
#     pass


# print("ultima comanda")

# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)
#     else:
#         continue

#     y = x + 20
#     z = y - 5

# for x in range(10): # x = 5
#     # comenzi1
#     # comenzi1
#     # comenzi1
#     if ceva:
#         continue

#     for y in range(5): # y = 2 -> 3
#         if conditie:
#             continue
#         # comanda1.1
#         # cpmanda1.2



# linia 1
# linia 2
# linia 3
# linia 4
# date 1
# date 2
# date 3
# .
# .
# date 500000

# for linie in fisier:
#     if not "date" in linie:
#         continue
#     else:
#         # prelucram date

# for linie in fisier:
#     if "date 3" in linie:
#         # prelucreaza informatie
#         break


# while inputul != 0:
#     # if inputul == 0:
#     #     break
#     pass
