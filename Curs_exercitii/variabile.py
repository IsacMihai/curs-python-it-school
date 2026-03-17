'''
Variabila - container pentru stocarea datelor / obiectelor

    * Orice element in Python este considerat un obiect

    * Python nu are o comanda specifica pentru a declara o
      variabila

    * O variabila este creeata in momentul in care ii asignam
      o valoare
'''

'''
Denumirea variabilelor:
    * Un nume de variabila poate sa contina doar caractere alfa numerice si bara-jos (A-Z, a-z, 0-9, _ )

    * Trebuie sa inceapa cu o litera sau cu caracterul “_” (bara-jos)

    * NU poate sa inceapa cu un numar

    * Nu poate contine spatii

    * Numele de variabile sunt “case-sensitive”
        - obiect, Obiect, OBIECT - sunt 3 variabile diferite

    * Un nume de “keyword” din Python NU poate fi folosit ca nume de variabila (def, class, if, else, import, etc)

    * Se recomanda folosirea literelor mici si _ pentru a separa cuvintele (Sanke Case)
      (nume_familie_daniel_neamtiu)

    * Alte conventii de denumire:
        - Camel Case (numeFamilieDanielNeamtiu)
        - Pascal Case (NumeFamilieDanielNeamtiu)
        - Upper Case (NEAMTIU_DANIEL)
'''

'''
Tipuri de variabile / obiecte uzuale in Python:
    * String - sir de caractere (text) - ex: 'Ana are mere', "Ana are mere"

    * Integer - numar intreg - ex: 3, 299, -45

    * Float - numar zecimal - ex: 2.5, 3.14, -0.99

    * Boolean - valoare logica - ex: True, False

    * NoneType - tip special care reprezinta absenta unei valori - ex: None



    - In Python NU este necesar sa declaram tipul variabilei

    - Tipul unei variabile se poate schimba in timp

    - Python este un limbaj case sensitive (var / Var - sunt doua variabile diferite)

    - Putem determina tipul unei variabile utilizand functia type()

    - Putem face conversie intre tipuri ("casting") de variabile utilizand functiile:
        str()   - conversie la string
        int()   - conversie la integer
        float() - conversie la float
        bool()  - conversie la boolean
'''

'''
Operatorul "=" - asignare valoare unei variabile

Functia print() - afisare pe ecran

Funtia input() - citire de la tastatura
'''

# Exemple practice pentru fiecare concept teoretic:
# Exemple corecte pentru denumire variabila:
# variabila
# var_iabila
# var1
# Var1
# VaR_ceva_112
# _var
# _Var
# _1Var
# variabila_mea_este_incredibila

# Exemplu incorect
# 1var
# variabila mea este incredibila
# def
# import
# for
# if

# Aici vreau sa imi declar o variabila
# variabila_mea = "text"
# def = 1

# nume_familie = "Neamtiu"

# nota_maxima = 10

# variabila_string = '' # ""
# variabila_string = ""

# variabila_string = 'a'
# variabila_string = 'Ana are mere'
# variabila_string = "Ana are mere"
# variabila_string = "10" # '10'
# variabila_int = 10
# variabila_float = 10.5

# var_str = '''Ana
# are
# multe
# mere
# '''

# var_str = """Soara
# lu
# ana
# are
# mere
# """

# var_str = "don't"
# var_str = 'Citat Cioran "Citat din Cioran"'

# var_int = -10

# var_bool = True
# var_bool = False

# var_meah = None

# var = "10"
# var = 10
# var = 10.0

# _var1 = 1
# _vaR1 = 2

# string1 = 'ceva'
# string2 = 'Ceva'

# var1 = 10
# var2 = "test"
# var3 = 7.3
# var4 = True

# var_type = type(var1)
# print(var_type)
# var_type = type(var2)
# print(var_type)
# var_type = type(var3)
# print(var_type)
# var_type = type(var4)
# print(var_type)

# var = "10"
# print(var)
# print(type(var))

# var = int(10)
# print(var)
# print(type(var))

# var = "10"
# var = 10
# print(var)
# print(type(var))
# var = float(var)
# print(var)
# print(type(var))
# print(var)

# var = "ceva"
# print(var)
# print(type(var))

maraciuca = input("Introdu un nume: ")
print("Numele introdus este:", maraciuca)

#print(type(var))
# var1 = "ana are"
# var2 = "10"
# var3 = "mere"

# var4 = "ana are 10 mere"

# print(var1, var2, var3)
# print(var4)

# print(type(var1), type(var2), type(var3))
# print(type(var4))

# var1 = "10"
# var2 = "10"
# rezultat = var1 + var2
# print(rezultat)
# 1010
# 20
# eroare

# var3 = 10
# var4 = 10
# rezultat = var3 + var4
# print(rezultat)

# var5 = 10
# var6 = "10"
# # rezultat = str(var5) + var6
# print(str(var5) + var6)

# var7 = 10
# var8 = 10.999
# rezultat = var7 + int(var8)
# print(rezultat)
# print(type(rezultat))

# Bool = True \ False
# var1 = ''
# var2 = 'mama ce schema'
# var3 = 0
# var4 = 0.0

# var1 = bool(var1)
# var2 = bool(var2)
# var3 = bool(var3)
# var4 = bool(var4)

# print(var1)
# print(var2)
# print(var3)
# print(var4)
