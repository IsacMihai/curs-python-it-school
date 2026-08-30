'''
Controlul fluxului programului în Python

Blocuri de cod și indentare:
    * Un bloc de cod reprezintă o secvență de instrucțiuni care aparțin unei structuri de control (if, for, while, funcții etc.).
    * În Python, blocurile de cod se definesc prin indentare (spații sau tab-uri la începutul liniei).
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

# Exemple: if, elif, else
x = 10
if x > 0:
    print('x este pozitiv')
elif x == 0:
    print('x este zero')
else:
    print('x este negativ')

# Exemple: for
fructe = ['mere', 'pere', 'prune']
for fruct in fructe:
    print(fruct)

for litera in 'Python':
    print(litera)

# Exemple: while
numar = 3
while numar > 0:
    print(numar)
    numar -= 1
print('Stop!')

# Exemple: break, continue, pass
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

for i in range(3):
    pass  # exemplu de pass

# Exemplu: exercițiu interactiv
numar_input = int(input('Introdu un număr: '))
if numar_input % 2 == 0:
    print('Numărul este par')
else:
    print('Numărul este impar')
