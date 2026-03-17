'''
Exercitii Functii Python:
1) Scrie o funcție care primește un nume și afișează "Salut, <nume>!".
2) Scrie o funcție care primește două numere și returnează suma lor.
3) Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).
4) Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.
5) Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului la patrat.
5) Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.
6) Scrie o funcție care primește un string și returnează stringul inversat.
7) Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.
8) Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.
9) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.
10) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au varsta peste 18 ani.
11) Scrie o functie care primeste o lista de numere si un numar n, si returneaza o lista cu numerele mai mici decat n.
12) Scrie o functie care primeste o lista de numere si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.
13) Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa).
14) Scrie o functie care primeste o lista de numere si returneaza o lista care contine numerele fara duplicate.
15) Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.
'''


#Tema

#1) Scrie o funcție care primește un nume și afișează "Salut, <nume>!".

# def salut(nume):
#     print(f"Salut, {nume}!")

# salut(input("Introdu numele: "))

#sau

# def salut(nume):
#     print(f"Salut, {nume}!")

# nume = input("Introdu numele: ")
 # salut(nume)

#2) Scrie o funcție care primește două numere și returnează suma lor.

# a = 2
# b = 9
# def suma(a,b):
#      return a+b 
# print(suma(a,b))

#3) Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor 
#(returnează un tuple).

# a = 5
# b = 7
# def operatii(a, b):
#      return a + b, a - b, a * b

# print(operatii(a, b))

# sau

# suma, diferenta, produs = operatii(a, b)

# print(suma)
# print(diferenta)
# print(produs)


#4) Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.

# numar = '6'
# def este_par(numar):
#      numar = int(numar)
#      return numar % 2 == 0
# print(este_par(numar))

#5) Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile 
# globale cu valoarea numarului la patrat.

# numar = 6
# rezultat = 0

# def patrat(numar):
#     global rezultat
#     rezultat = numar ** 2
# patrat(numar)
# print(rezultat)

#5) Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.
#  
# lista = ( 1, 2, 3, 4, 5)
# def suma_lista(lista):
#      return sum(lista)
# print(suma_lista(lista))

# def suma_numere(lista):
#     suma = 0
#     for i in lista :
#         suma += 1
#     return suma

# char = input('Introdu sirul')
# numar_char = char.split("")
# lista = [int(i.strip()) for i in numar_char]
# rezultat = suma_numerelor(lista)
# print("Rezultatul est: ", rezultat)

# rezultat = suma_numere(lista)
# print('Rezultatul este:', rezultat)

# def suma_lista(lista):
#     return sum(lista)

# n = int(input('Cate numere vrei sa introduci? '))

# lista = []

# for i in range[n]:
#     numar = int(input(f'Introdu numarul {i=1}: '))
#     lista.append(numar)
# print('Suma numerelor este:', suma_lista(lista))

#6)Scrie o funcție care primește un string și returnează stringul inversat.

# text = 'masa'
# def inversare(text):
#      return text[::-1]
# print(inversare(text))

#7) Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.

# text = {'masa', 'casa', 'film'}
# def lungimea_stringului(lista):
#     return [len(x) for x in lista]
# print(lungimea_stringului(text))

# 8) Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.

# lista1 = (1, 2, 3)
# lista2 = (2, 3, 4)
# def comune(lista1, lista2):
#     return list(set(lista1) & set(lista2))
# print(comune(lista1, lista2))

# 9) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei 
# cu cea mai mica varsta.

# persoane = {'Ana': 22, 'Marius': 17, 'Florin': 19, 'Daniel': 20 }
# def cea_mai_mica_varsta(persoane):
#     return min(persoane, key=persoane.get)
# print((cea_mai_mica_varsta(persoane)))

#10) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar
#  cu persoanele care au varsta peste 18 ani.

# persoane = {'Ana': 22, 'Marius': 17, 'Florin': 19, 'Daniel': 20 }
# def peste_18ani(persoane):
#     return{nume: varsta for nume, varsta in persoane.items() if varsta > 18}
# print(peste_18ani(persoane))

# date = input("Introduceti date: ")
# print(date)

# persoane = {}

# def filtru(persoane):
#     rezultat = {}
#     for nume, varsta in persoane.item():
#         if varsta >= 18:
#            rezultat[nume] = varsta

# while True:
#     date = input("Introdu date: ")
#     print(date)

#     if date == "stop":
#         break 

#     date_separate = date.split()
#     nume = date_separate[2]
#     varsta = date_separate[-1]
#     print(nume)
#     print(varsta)
# #    print(date_separate)
# persoane[nume] = varsta
# print(filtu(persoane))

#varianta de la Paul
# Nume - Ionescu | Varsta - 18
# Nume - Popescu | Varsta - 15
# Nume - Ana | Varsta - 21
# Nume - Paul | Varsta - 31

# persoane = {}
# def filtru (persoane):
#     rezultat = {}
#     for nume, varsta in persoane.items() :
#         if int(varsta) >= 18 :
#             rezultat[nume] = varsta
#     return rezultat
# while True :
#     date = input("Introdu datele : ")
#     if date == 'stop' :
#         break
#     date_separate = date.split()
#     nume = date_separate[2]
#     varsta = date_separate[-1]
#     persoane[nume] = varsta
# print(filtru(persoane))


#11) Scrie o functie care primeste o lista de numere si un numar n,
#  si returneaza o lista cu numerele mai mici decat n.

# numere = [3, 4, 7, 9, 4, 6, 8, 2]
# def mai_mici(lista, n):
#     return [x for x in lista if x < n]
# print(mai_mici(numere, 5))

#12)Scrie o functie care primeste o lista de numere 
#si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.

# numere = [3, 7, 1, 9, 4, 6]
# def statistici(lista):
#     minim = min(lista)
#     maxim = max(lista)
#     media = sum(lista) / len(lista)
#     return minim, maxim, media
# rez = statistici(numere)
# print('Min:', rez[0])
# print('Max:', rez[1])
# print('Media:', rez[2])

#13) Scrie o functie care primeste o lista de numere si returneaza un dictionar 
#cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa).

# lista = [1, 2, 2, 3, 3, 3, 4]
# def frecventa(lista):
#     rezultat = {}
#     for numar in lista:
#         rezultat[numar] = rezultat.get(numar, 0) + 1
#     return rezultat
# print(frecventa(lista))

# creez un ditctionar gol

#alternativa

# def frecv_numere(lista):
#     dictionar = {}

#     for x in lista:
#         if x in dictionar:
#             dictionar[x] = dictionar[x] + 1
#         else:
#             dictionar[x] = 1
#     return dictionar


# numere = [10, 20, 10, 20, 30, 40, 30, 40, 50]

# rezultat = frecv_numere(numere)
# print(rezultat)

#14) Scrie o functie care primeste o lista de numere
# si returneaza o lista care contine numerele fara duplicate.

# lista = [1, 2, 2, 3, 3, 3, 4]
# def fara_duplicate(lista):
#     return list(set(lista))
# print(fara_duplicate(lista))

#15) Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.

# numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# def este_prim(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return  True
# def numere_prime(lista):
#     return(x for x in lista if este_prim(x))
# print(numere_prime(numere))


