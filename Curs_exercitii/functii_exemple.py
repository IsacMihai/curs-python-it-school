'''
Funcții în Python

Functie = un bloc de cod reutilizabil care efectuează o anumită sarcină

1. Definirea și apelarea funcțiilor
    - Se folosește cuvântul cheie def

    - O funcție poate avea parametri și poate returna o valoare cu "return"
'''

'''
2. Parametri și argumente
    - Parametri: variabilele din definiția funcției

    - Argumente: valorile transmise la apel

    - Parametri cu valoare implicită
'''

'''
3. Returnarea valorilor
    - O funcție poate returna orice tip de valoare (sau nimic)

    - Se poate returna mai multe valori folosind tuple
'''

'''
4. Scope (domeniul de vizibilitate)
    - Variabilele definite în interiorul funcției nu sunt vizibile în afara ei (scope local)

    - Variabilele definite în afara funcției sunt globale
        - Se poate folosi cuvântul cheie "global" pentru a modifica o
          variabilă globală din interiorul unei funcții
'''

'''
5. Funcții fără parametri sau fără return
    - O funcție poate să nu aibă parametri
    - O funcție poate să nu returneze nicio valoare
'''

'''
6. Funcții ca parametri (funcții de ordin înalt)
    - Funcțiile pot fi transmise ca argumente către alte funcții
    - Exemplu: funcția map(), filter(), reduce()
'''

'''
7. Keyword arguments

    - Keyword arguments: argumente transmise explicit după nume, indiferent de poziție.

    Reguli:
        1) Argumentele poziționale (positional arguments) trebuie să apară înaintea celor numite 
        (keyword arguments)
           si sa fie transmise in ordinea parametrilor din definitia functiei.

        2) Un parametru poate sa primeasca o singura valoare (fie pozitionala, fie numita).

        3) Parametrii cu valoare implicita (default parameters) trebuie sa fie ultimii in definitia
          functiei.
'''

'''
8. Funcții recursive
    - O funcție care se apelează pe ea însăși pentru a rezolva o problemă
    - Trebuie să aibă o condiție de oprire pentru a evita apelurile infinite
'''

'''
9. Argumente variabile ca numar - *args și **kwargs

    - *args: permite transmiterea unui număr variabil de argumente poziționale (accesibile ca tuplu).

    - **kwargs: permite transmiterea unui număr variabil de argumente numite (accesibile ca dicționar).

    Reguli:
        -> *args trebuie sa fie plasat dupa parametrii pozitionali si sa apara inaintea lui **kwargs in definitia functiei.

        -> La apelarea functiei se pot combina argumente pozitionale, keyword arguments, *args si **kwargs respectand ordinea:
              - Argumentele pozitionale
              - Argumentele numite (keyword arguments)
              - Valorile din *args
              - Valorile din **kwargs

            Exemplu apelare functie:
                functie(1, 2, nume='Ana', varsta=30, *alte_valori, **alte_perechi)
'''

# # Exemple practice functii:

# # Exemplu simplu de funcție fără parametri și fără return
# def salut():
#     print('Salut!')

# salut()

# # Exemplu de funcție cu parametri și return
# def aduna(a, b):
#     return a + b

# rezultat = aduna(3, 4)
# print(rezultat)

# # Exemplu de funcție cu parametri cu valoare implicită
# def salut_nume(nume='Anonim'):
#     print(f'Salut, {nume}!')

# salut_nume('Maria')
# salut_nume()

# # Exemplu returnarea mai multor valori
# def operatii(a, b):
#     suma = a + b
#     diferenta = a - b
#     return suma, diferenta

# s, d = operatii(10, 4)
# print('Suma:', s)
# print('Diferenta:', d)

# # Exemplu scope (domeniul de vizibilitate)
# def demo_scope():
#     mesaj = 'Salut din funcție!'
#     print(mesaj)
# demo_scope()
# # print(mesaj)  # va da eroare

# # Exemplu variabila globală
# contor = 0
# def incrementeaza_contor():
#     global contor
#     contor += 1

# incrementeaza_contor()
# print('Contor:', contor)

# # Exemplu funcție fără parametri si fără return
# def afiseaza_hello():
#     print('Hello!')
# afiseaza_hello()

# # Exemplu funcție ca parametru
# def aplica_functie(f, x):
#     return f(x)

# def dubleaza(n):
#     return n * 2

# print(aplica_functie(dubleaza, 5))

# # Exemplu argumente transmise după nume (keyword arguments)
# def descriere_persoana(nume, varsta, oras):
#     print(f'{nume} are {varsta} ani și locuiește în {oras}.')

# descriere_persoana(varsta=30, nume='Ana', oras='Cluj')  # argumente după nume

# # Exemplu functie recursiva
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))

# # Exemplu functie recursiva parcurgere lista imbricata
# def numara_element(lista, element):
#     count = 0
#     for item in lista:
#         if isinstance(item, list):
#             count += numara_element(item, element)
#         elif item == element:
#             count += 1
#     return count

# # Exemplu *args (numar variabil de argumente pozitionale)
# def suma(*args):
#     print('Argumente primite:', args)
#     return sum(args)

# print('Suma:', suma(1, 2, 3, 4))

# # Exemplu **kwargs (numar variabil de argumente numite)
# def afiseaza_date(**kwargs):
#     print('Date primite:', kwargs)
#     for cheie, valoare in kwargs.items():
#         print(f'{cheie}: {valoare}')

# afiseaza_date(nume='Ion', varsta=40, oras='Oradea')

# # Exemplu combinare *args și **kwargs
# def logare(*mesaje, **optiuni):
#     nivel = optiuni.get('nivel', 'INFO')
#     separator = optiuni.get('separator', ' ')
#     mesaj_final = separator.join(str(m) for m in mesaje)
#     print(f"[{nivel}] {mesaj_final}")

# logare("Pornire program", "Utilizator: Ana", nivel="DEBUG")
# # Output: [DEBUG] Pornire program Utilizator: Ana

# logare("Eroare la conectare!", nivel="ERROR", separator=" | ")
# # Output: [ERROR] Eroare la conectare!







# def verifica_numar(x):
#     if x % 2 == 0:
#         return 'numarul este par'
#     else:
#         return 'numarul este impar'

# rezultat = verifica_numar(6)
# print(rezultat)

# def verifica_numar(x):
#     if x % 2 == 0:
#         return 'par'
#     return 'impar'

# rezultat = verifica_numar(7)
# print(rezultat)

# def putere(x, exponent=2):
#     return x ** exponent

# print(putere(3))
# print(putere(3, 3))

# def salut(nume='Anonim'):
#     print('Salut', nume)

# salut('Mihai')

# args:

# def aduna(*numere):
#     total = 0
#     for x in numere:
#         total += x
#     return total

# print(aduna(1,2,3))
# print(aduna(5,10,15,20))

# def test(*args):
#     print(args)

# test(1,2,3)

#**kwargs (cheie = valoare)

# def afiseaza(**date):
#     print(date)

# afiseaza(nume='Mihai', varsta=25)

# def profil(**info):
#     for cheie, valoare in info.items():
#         print(cheie, '=', valoare)
    
# profil(nume='Mihai', oras='Timisoara')

#combinatie utila

# def functie(nume, *args, **kwargs):
#     print('Nume:', nume)
#     print('Args', args)
#     print('Kwargs:', kwargs)

# functie('Mihai', 1,2,3, oras='TM', job='IT')

# def adauga_angajat(nume, salariu=4050):
#     print(nume, salariu)

# def creeaza_angajat(**date):
#     return date

# angajat = creeaza_angajat(nume='Mihai', salariu=5000, departament='IT')
# print(angajat)

# 1exemplu

# def statistica(*numere): # * - "ia toate valorile date și pune-le într-un singur loc",mai multe valori → devin un tuple
#     if not numere:
#         return 'Nu ai dat numere'
#     total = 0
#     minim = numere[0]
#     maxim = numere[0]

#     for x in numere:
#         total += x
#         if x < minim:
#             minim = x
#         if x > maxim:
#             maxim = x

#     media = total / len(numere)

#     return {
#         'suma': total,
#         'media': media,
#         'minim': minim,
#         'maxim': maxim
#     }

# rez = statistica(10, 5, 8, 20)
# print(rez)

# def creeaza_angajat(**date): # ** - "ia perechi de tip cheie=valoare și pune-le într-un dicționar"
#     angajat = {}

# #valori default
#     angajat['salariu'] = date.get('salariu', 4050) # get = „ia valoarea fără să dea eroare”
#     angajat['departament'] = date.get('departament', 'Necunoscut')

# #valori obligatorii
#     angajat['nume'] = date.get('nume', 'Anonim')

#     return angajat

# a1 = creeaza_angajat(nume='Mihai', salariu=6000)
# a2 = creeaza_angajat(nume='Ana')

# print(a1)
# print(a2)

# Mini exemplu final (totul împreună)

# def test(*numere, **date):
#     print('Numere:', numere)
#     print('Date:', date)

#     nume = date.get('nume', 'Anonim')

#     print('Salut', nume)

# test(1,2,3, nume='Mihai')



## 2.exemplu

# def creeaza_angajat(**date):
#     angajat = {}

#     #valori defalut
#     angajat['salariu'] = date.get('salariu', 4050)
#     angajat['departament'] = date.get('departament', 'necunoscut')

#     #valori obligatorii
#     angajat['nume'] = date.get('nume', 'Anonim')

#     return angajat

# a1 = creeaza_angajat(nume='Mihai', salariu=6000)
# a2 = creeaza_angajat(nume='Ana', departament='IT')

# print(a1)
# print(a2)


# 3.exemplu ,,Funcție combinată (args + kwargs)

# def comanda(client, *produse, **detalii):
#     print('Client:', client)

#     print('Produse')
#     for p in produse:
#         print('-', p)

#     print('Detalii:')
#     for cheie, valoare in detalii.items():
#         print(cheie, '=', valoare)

# comanda(
#     'Mihai',
#     'Laptop',
#     'Mouse',
#     'Tastatura',
#     adresa='Timisoara',
#     plata='card'
# )


# Exemplu tip joc (perfect pentru tine 🎮)

# def joc(player, *scoruri, **setari):
#     total = sum(scoruri)

#     dificultate = setari.get('nivel', 'easy')
#     bonus = setari.get('bonus', 0)

#     scor_final = total + bonus

#     return f'{player} a jucat pe {dificultate} si are scor {scor_final}'

# rez = joc('Mihai', 40,20,30, nivel='hard', bonus=50)
# print(rez)


# def filtreaza_angajati(lista, **criterii):
#     rezultat = []

#     for angajati in lista:
#         ok = True

#         for cheie, valoare in criterii.items():
#             if angajati.get(cheie) != valoare:
#                 ok = False
#                 break

#         if ok:
#             rezultat.append(angajati)

#     return rezultat

# angajati = [
#     {'nume': 'Mihai', 'departament': 'IT'},
#     {'nume': 'Ana', 'departament': 'HR'},
#     {'nume': 'Ion', 'departament': 'IT'},   
# ]

# rez = filtreaza_angajati(angajati, departament='IT')
# print(rez)