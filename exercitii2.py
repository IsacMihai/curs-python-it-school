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
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

16) Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9)

17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.

18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

Pentru generarea numarului aleator:
import random
numar_aleator = random.randint(1, 100)

21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
in functie de numele de familie.
"""
#1.
# lim_min = int(input("Introdu limita inferioara: "))
# lim_max = int(input("Introdu limita superioara: "))
# val= 2
# for i in range(1, int(lim_max/2) + 1):
#     val = 2 ** i if lim_min < val $ val < lim_max :
#                 print(val)
    
#2.
# lista = [1,2,3,4,5,6,7]
# sum = 0
# for i in lista:
#      sum += i 
# print("Suma elementelor este: ", sum)
# print("Media elementelor este: ", sum/len(lista))

#3.
# lista = input("introdu o lista de elemente separate prin spatiu: ").split()
# lista_inversata = lista[::-1]
# print("Lista inversata este:", lista_inversata)


# #4.
# lista = [10,20,30,40,50,60]
# for i in range(1, len(lista), 2):
#     print(lista[i])


#5
# lista = [1,2,3,2,4]
# lista2 = []
# for i in lista :
#     if i == 2:
#         lista2.append(5)
#     else:
#         lista2.append(i)
# print(lista2)

#6
# lista = [3,1,4,1,5,9,2]
# maxim = lista[0]
# minim = lista[0]
# for i in lista:
#     if i > maxim:
#         maxim = i
#     if i < minim :
#         minim = i
# print("Maximul este: ", maxim)
# print("Minimul este: ", minim)

#7
# lista = [1,2,3,4,5,6]
# for i in lista :
#     if i % 2 == 0 :
#         lista.remove(i)
# print(lista)

# #8
# lista = ['ana', 'mere, 'casa', 'masina']
# lista_noua= []
# for i in lista:
# for x in i:
# if x == 'a' :
# lista_noua.append(i)
# break
# print("Lista ce contine cuvinte cu litera 'a' este: ",lista_noua )

#9
# lista = [1,2,3,2,1]
# flag = True
# for i in range(len(lista) // 2):
#     if lista[i] != lista[-(i + 1)]:
#         flag = False
#         break
#     if flag:
#         print("Lista este palindrom.")
#     else:
#         print("Lista nu este palindrom.")


#10.
# lista1 =[1,2]
# print(lista1)
# lista2 = [3,4]
# print(lista2)
# lista1.extend(lista2)
# print(lista1)

# #11

# lista = [10,20,30]
# lista2= 

#12

# lista = [1,2,2,3,4,4,5]
# lista_unica = []
# for i in lista:
#     if lista.count(item) == 1:
#         lista_unica.append(intem)
# print(lista_unica)

#13
# lista = [10,-1,2,-3,0,4,-5]
# negative = []
# restul = []
# for i in lista:
#     if i< 0 :
#         negative.append(i)
#     else: 
#         restul.append(i)
# print("Numerele negative: ", negative)
# print("Pozitive si zero: ", restul)        


#15.not sure
# lista = [ 'ana', 'masina', 'casa', 'mere']
# vocale = 'aeiou'
# for i in range(len(lista)):
#     for j in range(i + 1, len(lista)):
#         count_i = 0
#         for char in lista[i]:
#           if char in vocale:
#             count_i += 1
#         count_j = 0
#         for char in lista[j]:
#           if char in vocale:
#             count_j += 1
#           if count_i > count_j:
#             lista[i],lista[j] = lista[j], lista[i]
# print(lista)


#16.
# lista = [[1,2,3],[4,5,6,],[7,8,9]]
# lista = [[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]]
# lista = [[1,2,3,4,5]]
# count_i = 0
# sum_diag = 0
# for i in lista :
#     if len(i) == len(lista)
    
#19.
   # Eercitiu: lista = [1, 2, [3, 1, 4], 7,[1, 2, [1, 5]]]
# lista = [1, 2, 3, [3, 1, 4], 7, [1, 2,[1, 5]]]

# def count(l):
#     total = 0
#     for x in l:
#         if isinstance(x, list):
#             total += count(x)
#         elif x== l:
#             total += l
#     return total

# resultat = count(lista)
# print(f"Elementul 1 apare in lista de ", resultat, "ori.")

# lista_elemente = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# element = 1

# count = 0
# index = 0
# while index < len(lista_elemente):
#     if isinstance(lista_elemente[index], list):
#         lista_elemente.extend(lista_elemente[index])
#     else:
#         if lista_elemente[index] == element:
#             count += 1

#     index += 1


#20.

# import random
# numar_ales = random.radint(1,100)
# nr_g = ""
# count = 1
# flag = True
# while flag :
#        nr_g = int(input("Ghiceste numar : "))
#        if numar_ales == nr_g :
#           print("ai gasit numarul")
#           flag = False
#        elif nr_g > numar_ales : 
#           print("Numarul ghicit e mai mare ")
#           count += 1
#        else :
#            print("Numarul ghicit e mai mic")
#            count += 1
#        if nr_g = "exit" :
#            flag = False
# print("Ti-ai luat" + str(count) + "incearca sa ghicesti")


#21
# lista_nume = []
# familie = ''
# prenume = ''
# while True:
#     familie = input('introdu numa de familie: ')
#     if familie != '#':
#         prenume = input('Introdu numele: ')
#         lista_nume.append(['Nume:', familie, 'Prenume:', prenume])
#     else:
#         break
# print(lista_nume)
# for i in range(len(lista_nume)):
#     for j in range(len(lista_nume)-1):
#         if lista_nume[j][1] > lista_nume[j+1][1]:
#                       temp = lista_nume[j+1]
#                       lista_nume[j+1] = lista_nume[j]
#                       lista_nume[j] = temp
# print("Lista sortata alfabetic este:", lista_nume)

#teste:

# zile = ('Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica')
# print(zile)
# print(zile[3])
# print(zile.count('luni'))
# #print(zile.index('vineri'))
# zile_lucratoare = zile[0:5]
# print(zile_lucratoare)
# zile_i = tuple(zi for zi in zile if 'i' in zi)
# print(zile_i)


# tuple_numere = (1,2,3,4)
# print(tuple_numere)
# tuple_numere = list(tuple_numere)
# print(tuple_numere)
# tuple_numere.append(5)
# print(tuple_numere)
# tuple_numere = tuple(tuple_numere)
# print(tuple_numere)


# tuple_ceva = ('Ana', 'Ionescu', '25')
# prenume, nume, varsta = tuple_ceva
# print(prenume)
# print(nume)
# print(varsta)



# my_set = {1,2,3,4,5}
# print(my_set)
# my_set.add('5')
# print(my_set)

#Remove duplicate
# lista_mea = [1,2,2,3,3,3,4,5,6,6,7,7,7]
# print(lista_mea)
# lista_mea = set(lista_mea)
# lista_mea = list(lista_mea)
# #lista_mea = list(set(lista_mea))
# print(lista_mea)

# my_set = {1,2,3,4,5,6,7,8}
# print(my_set)
# print(my_set.pop())
# print(my_set)

#cum sa legi impreuna fara duplicate
# set1 = {1,2,3,4,5}
# print(set1)
# set2 = {3,4,7,8,9}
# print(set2)
# set1.update(set2)
# print(set1)
# print(se1.union(set2))
# print(set1)
# print(set2)
# print(set1.differentce(set2))
# print(set2.difference(set1))
# print(set1.intersection(set2))
# print(set1.issubset(set2))

set2 = {3, 4, 7, 8, 9}
set3 = {3, 4, 7, 8, 9, 10}
print(set2.issubset(set3))
print(set3.issuperset(set2))

set1.clear()
print(set1)
ex = {}
print(type({}))
print(type(ex))
print(ex)




# Folositi list comprehension pentru a rezolva urmatoarele exercitii:
# 1) Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 2) Creeaza o lista cu toate numerele pare intre divizibile cu 3 dintre 1 si 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48]
# 3) Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7]
# 4) Dintr-o lista cu numere de la 1 la 25, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304]
# 5) Creeaza o lista cu toate vocalele dintr-un text dat. Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e']

# Folositi any pentru rezolvarea urmatoarelor exercitii:
# 1) Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True
# 2) Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True
# 3) Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True
# 4) Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True
# 5) Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True

