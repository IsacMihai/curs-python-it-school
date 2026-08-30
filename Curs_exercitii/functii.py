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
        -> *args trebuie sa fie plasat dupa parametrii pozitionali si sa apara inaintea lui **kwargs in
          definitia functiei.

        -> La apelarea functiei se pot combina argumente pozitionale, keyword arguments, *args si
          **kwargs respectand ordinea:
              - Argumentele pozitionale
              - Argumentele numite (keyword arguments)
              - Valorile din *args
              - Valorile din **kwargs

            Exemplu apelare functie:
                functie(1, 2, nume='Ana', varsta=30, *alte_valori, **alte_perechi)
'''


# def func_basic():
#     print("Salut din funcite!")
#     return [1,2,3]

# var = func_basic()
# print(var)
# print(func_basic())

# print(func_basic(3))

# def afiseaza_nume(nume, prenume):
#     print(f'Salut {nume} {prenume}!')

# afiseaza_nume()


# def afiseaza_nume(prenume, nume='Popescu'):
#     print(f'Salut {nume} {prenume}!')

# afiseaza_nume('Ana')

# def func(par1, par2, par3=True):
#     pass

# # func(val1, val2)
# var1 = 1
# var2 = 2
# var3 = 3

# def func(par1, par2, par3=True):
#     print(par1, par2, par3)

# func(var2, par3=var1, par2=var2)

# def operatii(val1, val2):
#     return val1 + val2, val1 - val2, val1 * val2

# arg1 = 10
# arg2 = 20

# print(type(operatii(10, 20)))
# print(operatii(10, 20))
# adunare, scadere, inmultire = operatii(10, 20)

# print(adunare, scadere, inmultire) # -> adunarea, scaderea, inmultire

#-----------------------------------------------------------------
# VARIABILA_GLOBALA = "Ceva"

# def functie_extra(param1, param2):
#     global var
#     var = param1 + param2
#     print(var) # 300

# functie_extra(100, 200)
# print(var)

# var = var + 1000
# print(var)

# lista_simpla = [1, 2, 3, 4, 5, 1, 7 , 1]


# lista = [1, 2, 3, [1, 3, 5], 6, [1, [1, 2], 3]]

# def fr_nr(lista_in_care_caut, nr_cautat):
#     counter = 0
#     for elem in lista_in_care_caut:
#         if elem == nr_cautat:
#             counter += 1
#         else:
#             pass

#     return counter

# def frecventa_nr(lista_in_care_caut, nr_cautat):
#     counter = 0
#     for elem in lista_in_care_caut:
#         if isinstance(elem, list): # type(elem) == list
#             counter += frecventa_nr(elem, nr_cautat)
#         elif elem == nr_cautat:
#             counter += 1
#         else:
#             pass

#     return counter

# print(frecventa_nr(lista, 1))
# print(fr_nr(lista, 1))

#Exercitii Gpt


# #1.Scrie o funcție care primește un nume și afișează:

# def func_basic(nume):
#     print(f"Salut, {nume}")
#     return

# func_basic('Mihai')

#2.Scrie o funcție care primește două numere și returnează suma lor.

# def suma_numere(a, b):
#     return a + b


# rezultat = suma_numere(5, 3)
# print(rezultat)

# def inmultire_numere(a, b):
#     return a * b

# rezultat = inmultire_numere(4 ,6)
# print(rezultat)

#3.Scrie o funcție care primește un număr și returnează:

# def restul_impartirii(x):
#     if x % 2 == 0:
#         return 'Par'
#     if x % 2 == 1:
#         return 'Impar'

# print(restul_impartirii(5))

#4. Scrie o funcție care primește lungimea și lățimea și returnează aria.

# def aria_dreptunghi(lungime, latime):
#     return lungime * latime

# rezultat = aria_dreptunghi(5, 3)
# print(rezultat)

# x = 15

# if x % 3 == 0  and x % 5 == 0:
#     print('fizzBuzz')
 
# elif x % 5 == 0:
#     print('buzz')

# elif x % 3 == 0:
#     print('fizz')

# else:
#     print('Lets try something else! ')

def aduna(lista_elemente):
    suma = 0
    for elem in lista_elemente:
        suma += elem

    return suma

def produs(lista_elemente):
    produsul = 1
    for elem in lista_elemente:
        produsul *= elem

    return produsul

def suma_liste(func, lista_cu_liste):
    suma_totala = 0
    for lista in lista_cu_liste:
        print(lista)
        print(func(lista))
        suma_totala += func(lista)

    return suma_totala
    
lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("Suma sumelor elementelor din lista este: ",suma_liste(aduna, lista))
print("Suma produselor elementelor din lista este: ",suma_liste(produs, lista))