"""
1) Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
Exemplu: 10, 50 -> 16, 32


3) Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0


4) Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]


5) Afișează toate elementele de pe poziții impare dintr-o listă dată.
Exemplu: [10,20,30,40,50,60] -> 20,40,60


6) Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]


7) Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1


8) Elimină toate elementele pare dintr-o listă de numere.
Exemplu: [1,2,3,4,5,6] -> [1,3,5]


9) Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']


10) Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False


11) Interclasează două liste de aceeași lungime într-o singură listă.
# Exemplu: [1,2], [3,4] => [1,3,2,4]


12) Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]



13) Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
Fara a folosi set().
# Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]


14) Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

15) Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
Fara a folosi functia sort() sau sorted().

16) Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).


17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.

18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.


21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
in functie de numele de familie.
"""




# 1) Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# Exemplu: 10, 50 -> 16, 32

# start = int(input('Introdu limita minima: '))
# end = int(input('Introdu limita maxima: '))

# numar = 1 

# while numar <= end:
#       if numar >= start:
#          print(numar)
#       numar = numar * 2

# 3) Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza 
# functiile sum() si avg().
# Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

# lista = [1, 2, 3, 4, 5, 6, 7]

# suma = 0

# for numar in lista:
#     suma = suma + numar

# media = suma / len(lista)

# print('Suma = ', suma)
# print('Media = ', media)

#varianta cu input de la user:


# lista = []

# for i in range(7):
#     numar = int(input(f"Introdu numarul {i+1}: "))
#     lista.append(numar)

# suma = 0

# for numar in lista:
#     suma += numar

# media = suma / len(lista)

# print("Lista:", lista)
# print("Suma =", suma)
# print("Media =", media)


# 4) Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
# a. Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

# text = input("Introdu numare separate prin spatiu: ")
# lista = text.split() #transforma stringu in lista
# lista_inversata = lista[::-1] # inversare lista
# print(lista_inversata)

#b. varianta fara shorcut

# text = input("Introdu numere: ")
# lista = text.split()

# lista_inversata = []

# for i in range(len(lista) - 1, -1, -1):
#     lista_inversata.append(lista[i])

# print(lista_inversata)



#c. cu numere reale, nu string

# text = input("Introdu numere: ")
# lista = [int(x) for x in text.split()]

# lista_inversata = lista[::-1]

# print(lista_inversata)


# 5) Afișează toate elementele de pe poziții impare dintr-o listă dată.
# Exemplu: [10,20,30,40,50,60] -> 20,40,60

# lista = [10, 20, 30, 40, 50, 60, 70]

# for i in range(1, len(lista), 2):
#     print(lista[i])

#varianta mai scurta

# lista = [10, 20, 30, 40, 50, 60, 70]
# print(lista[1::2])



# 6) Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
# Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]

# lista = [1, 2, 3, 4]
# vechi = 2
# nou = 5
# for i in range(len(lista)):
#     if lista[i] == vechi:
#         lista[i] = nou

# print(lista)

#varianta clean

# lista = [1, 2, 3, 4]
# lista_noua = [5 if x == 2 else x for x in lista]

# print(lista_noua)

#varianta super simpla

# def inlocuieste(lista, vechi, nou):
#     return [nou if x == vechi else x for x in lista]

# print(inlocuieste([1, 2, 3, 4], 2,5))

# 7) Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
# Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1

# lista = [3, 1, 4, 1, 5, 9, 2]

# maxim = lista[0]
# minim = lista[0]

# for numar in lista:
#     if numar > maxim:
#         maxim = numar
#     if numar < minim:
#         minim = numar

# print("max = ", maxim)
# print("min = ", minim)


#varianta cu index

# lista = [3, 1, 4, 1, 5, 9, 2]

# maxim = lista[0]
# poz_max = 0

# for i in range(len(lista)):
#     if lista[i] > maxim:
#         maxim = lista[i]
#         poz_max = i

# print("max = ", maxim, "pozitia = ", poz_max)

#8) Elimină toate elementele pare dintr-o listă de numere.
# Exemplu: [1,2,3,4,5,6] -> [1,3,5]

# lista =  [1, 2, 3, 4, 5, 6]

# rezultat = []

# for numar in lista:
#     if numar % 2 != 0:
#         rezultat.append(numar)

# print(rezultat)

#varianta cu list coprehension

# lista = [1, 2, 3, 4, 5, 6]

# rezultat = [x for x in lista if x % 2 != 0]

# print(rezultat)

# 9) Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

# lista = ['ana', 'mere', 'casa', 'masina']

# rezultat = []

# for cuvant in lista:
#     if 'a' in cuvant:
#         rezultat.append(cuvant)

# print(rezultat)


#varianta cu list coprehension

# lista = ['ana', 'mere', 'casa', 'masina']

# rezultat = [cuvant for cuvant in lista if 'a' in cuvant]

# print(rezultat)



#varianta cu list coprehension case-sensitive


# lista = ['Ana', 'mere', 'Casa', 'Masina']
# rezultat = [cuvant for cuvant in lista if 'a' in cuvant.lower()]
# print(rezultat)



# 10) Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# # Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False

# lista = [1, 2, 3, 2, 1]

# if lista == lista[::-1]:
#     print(True)
# else:
#     print(False)


#functie reutilizabila


# def este_palindrom(lista):
#     return lista == lista[::-1]

# print(este_palindrom([1, 2, 3, 2, 1]))

# 11) Interclasează două liste de aceeași lungime într-o singură listă.
# # Exemplu: [1,2], [3,4] => [1,3,2,4]

# lista1 = [1, 2]
# lista2 = [3, 4]

# rezultat = []

# for i in range(len(lista1)):
#     rezultat.append(lista1[i])
#     rezultat.append(lista2[i])

# print(rezultat)


#varianta cu zip


# lista1 = [1, 2]
# lista2 = [3, 4]

# rezultat = []

# for a,b in zip(lista1, lista2):
#     rezultat.append(a)
#     rezultat.append(b)

# print(rezultat)


# 12) Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# # Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]


# lista = [10, 20, 30]

# rezultat = []

# for i in range(len(lista)): #→ generează indexuri: 0, 1, 2
#     rezultat.append([i, lista[i]]) #→lista[i] ia valoarea de pe poziția respectivă 
#     #[i, lista[i]] → creează pereche index + valoare

# print(rezultat)


# 13) Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează 
# doar elementele unice).
# Fara a folosi set().
# # Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

# lista = [1, 2, 2, 3, 4, 4, 5]

# rezultat = []

# for numar in lista:
#     if lista.count(numar) == 1:
#         rezultat.append(numar)

# print(rezultat)

#logica manuala fara count:

# lista = [1, 2, 2, 3, 4, 4, 5]

# rezultat = []

# for i in range(len(lista)):
#     apare = False

#     for j in range(len(lista)):
#         if i != j and lista[i] == lista[j]:
#            apare = True
#            break

#     if not apare:
#         rezultat.append(lista[i])

# print(rezultat)


# 14) Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu
#  numere pozitive și zero.
# # Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

# lista = [10, -1, 2, -3, 0, 4, -5]

# negative = []
# pozitive_si_zero = []

# for numar in lista:
#     if numar < 0:
#         negative.append(numar)
#     else:
#         pozitive_si_zero.append(numar)

# print('negative:', negative)
# print('pozitive_si_zero:', pozitive_si_zero)


#varianta cu list coprehension

# lista = [10, -1, 2, -3, 0, 4, -5]
# negative = [x for x in lista if x < 0]
# pozitive_si_zero = [x for x in lista if x >= 0]

# print(negative)
# print(pozitive_si_zero)

# intru-un dictionar 

# lista = [10, -1, 2, -3, 0, 4, -5]

# rezultat = {
#     'negative': [x for x in lista if x < 0],
#     'pozitive_si_zero': [x for x in lista if x >= 0]
# }

# print(rezultat)




# 15) Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
# Fara a folosi functia sort() sau sorted().

# def numara_vocale(cuvant):
#     vocale = 'aeiouAEIOU'
#     count = 0

#     for litera in cuvant:
#         if litera in vocale:
#             count += 1

#     return count

# lista = ["ana", "mere", "casa", "masina"]

# for i in range(len(lista)):
#     for j in range(len(lista) - 1):
#         if numara_vocale(lista[j]) > numara_vocale(lista[j + 1]):
#             # swap
#             lista[j], lista[j + 1] = lista[j + 1], lista[j]

# print(lista)

#varianta simplificata 

# lista = ["ana", "mere", "casa", "masina"]
# vocale = "aeiouAEIOU"

# for i in range(len(lista)):
#     for j in range(len(lista) - 1):
        
#         # număr vocale pentru lista[j]
#         count1 = 0
#         for litera in lista[j]:
#             if litera in vocale:
#                 count1 += 1

#         # număr vocale pentru lista[j+1]
#         count2 = 0
#         for litera in lista[j + 1]:
#             if litera in vocale:
#                 count2 += 1

#         # comparăm
#         if count1 > count2:
#             lista[j], lista[j + 1] = lista[j + 1], lista[j]

# print(lista)


#varianta mai usor de inteles

# lista = ["ana", "mere", "casa", "masina"]
# vocale = "aeiouAEIOU"
# for cuvant in lista:
#     count = 0
#     for litera in cuvant:
#         if litera in vocale:
#             count += 1
#             print(cuvant, count)



# 16) Primește o listă de liste (matrice) și
# calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).

# matrice = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# n = len(matrice)

# este_patratica = True

# for linie in matrice:
#     if len(linie) != n:
#         este_patratica = False

# if este_patratica:
#     suma = 0

#     for i in range(n):
#         suma += matrice[i][i]

#         print('Suma diagonalei:', suma)
#     else:
#         print('Matricea nu este patratica')



# 17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele 
# "Ionut" si sa se afiseze.

# lista = [
#     [10, 5, 29],
#     ["Marian", "Ionut", "Marcel"],
#     [10.2, 7.5, 3.4]
# ]
# print(lista[1][1])



# 18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera 
# "r" din numele "Marcel" si sa se afiseze.

# lista = [
#     [10, 5, 29],
#     ["Marian", "Ionut", "Marcel"],
#     [10.2, 7.5, 3.4]
# ]

# print(lista[1][2][2])


# 19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# # Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori



# def numara_aparitia(lista, cautat):
#     count = 0

#     for element in lista:
#         if isinstance(element, list):
#             count += numara_aparitia(element, cautat)
#         elif element == cautat:
#             count += 1

#     return count
    
# lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]

# print(numara_aparitia(lista, 1))




# 20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
# ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai
# mic decat cel generat.Programul se termina cand utilizatorul ghiceste numarul corect sau daca 
# introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

# import random

# #genereaza numarul random intre 1 si 100
# numar_secret = random.randint(1, 100)

# incercari = 0

# while True:
#     user_input = input("Ghiceste numarul (sau scrie 'exit'): ")
#     #daca vrei sa iasa
#     if user_input.lower() == 'exit':
#         print('Ai iesit din joc')
#         break

#     try:
#         numar = int(user_input)
#         incercari += 1

#         if numar < numar_secret:
#             print('Numarul este mai mare.')
#         elif numar > numar_secret:
#             print('Numarul este mai mic.')
#         else:
#             print('Felicitari ! ai ghicit numarul') 
#             print('Numar incercari:', incercari)
#             break 

#     except ValueError:
#         print('Te rog introdu un numar valid.')  



# 21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand 
# se introduce caracterul . Programul trebuie sa stocheze toate datele citite, iar la final sa le 
# afiseze in ordine alfabetica in functie de numele de familie.

# lista_persoane = []

# while True:
#     text = input('Introduceti date (sau # pentru stop): ')

#     if text == '#':
#         break

#     #extragem numele si prenumele
#     parti = text.split()

#     nume = parti[1] # dupa nume
#     prenume = parti[3] #dupa prenume

#     lista_persoane.append([nume, prenume])

# #sorteaza dupa nume (fara sort())
# for i in range(len(lista_persoane)):
#     for j in range(len(lista_persoane) - 1):
#         if lista_persoane[j][0] > lista_persoane[j + 1][0]:
#             lista_persoane[j], lista_persoane[j + 1] = lista_persoane[j + 1], lista_persoane[j]

# #afisare
# for persoane in lista_persoane:
#     print('Nume:', persoane[0], 'Prenume', persoane[1])


#varianta cu dictionare

# lista = []

# while True:
#     text = input("Introdu date (sau # pentru stop): ")

#     if text == "#":
#         break

#     parti = text.split()

#     # verificare input corect
#     if len(parti) < 4:
#         print("Format gresit! Exemplu: Nume: Ionescu Prenume: Ion")
#         continue

#     persoana = {
#         "nume": parti[1],
#         "prenume": parti[3]
#     }

#     lista.append(persoana)

# # sortare
# lista.sort(key=lambda x: x["nume"])

# for p in lista:
#     print(p["nume"], p["prenume"])