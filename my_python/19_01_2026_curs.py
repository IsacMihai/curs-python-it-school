#zip lister de tuple iterabile

# x = [1, 2, 3, 9]
# y = [4, 5, 6, 10]

# for a, b in zip(x, y):
#     print(f'element impachetate sunt {a} - {b}')


# nume = ["ana", "maria", "marcel"]
# varsta = [32, 54, 18]

# for elem_nume, elem_varsta in zip(nume, varsta):
#     print(f'{elem_nume} are {elem_varsta} ani')





#any() - returneaza True daca cel putin un element din lista este adevarat
#all() -  returneaza True daca toate elementele din lista sunt adevarate

# #lista1 = [1, 2, 3, 4, 5]
# lista1 = [75, 0, 0, 0]  # -> True
# #lista1 = [ False, False, False, False] # -> False
# lista2 = [0, 2, 3, 4] # -> True

# # print(any(lista1))

# # print(any(lista2))
# print(all(lista1))
# # print(all(lista2))





# []

# Sa se scrie un program care genereaza numere pare si afiseaza.
# # lista_pare = [2, 4, 6, 8, 10]

# lista_karina = range(1,11)

# lista_mea = [x for x in range(1,11) if x % 2 == 0]
# print(lista_mea)

# lista_mea = [x ** 2 for x in range(1,11) if x % 2 == 0]  #element la **2
# print(lista_mea)



# lista_pare = []
# for x in range(1,11):
#     if x % 2 == 0:   # %(lasuta) verifica restul impartirii , daca restul e 0 se indep conditia

#         print(x)




# lista_mihai = range(1,200)

# lista_pare = [] # lista_pare care stocheaza o lista care momentan e goala
# for x in range(1,200):
#     if x % 2 == 0:      # punem o conditie folosind "if"
#         lista_pare.append(x)# folosind .append ca sa putem adauga elemente, x - nr.
#     else:
#         continue 
# print(lista_pare) # afisam 





#sa se caute numerele divizibile cu 3 si 5 din lista:

# lista_initiala = [3, 5, 7, 15, 30]

# lista_divizibila = [x for x in lista_initiala if x % 3 == 0 and x % 5 ==0]
# print(lista_divizibila)


#lista initiala ,sa se verefice daca cel putin un element din lista initiala e divizibil cu 3 si cu 5

# lista_initiala = [3, 5, 7, 15, 21, 72, 56, 99]
# lista = any(x % 3 == 0 and x % 5 == 0 for x in lista_initiala)
# print(lista)




# ------Exemple probleme liste----

#1.Sa se afiseze toate puterile lui 2 aflate intre interva;e dat de utilizator.
# Exemplu: 10, 50 -> 16, 32

# lim_min = int(input('Introdu limita inferioara: '))
# lim_max = int(input('Introdu limita superioara: '))
# val = 2
# for i in range(1, int(lim_max/2) + 1):  # un for care incepe de la range pana la jumatatea numarului
#     val = 2 ** i #numarul la puterea 2 daca se afla intre puterea min si max il printeaza
#     if lim_min < val & val < lim_max :
#         print(val)



#2.Creeaza o lista cu 7 numere intregi, apoi afiseaza suma si media elementelor fara a utiliza functiile sum()si avg().
#Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

# lista = [1,2,3,4,5,6,7]
# sum = 0
# for i in lista:
#     sum += i
# print('Suma elementelor este: ', sum)
# print('Media elementelor este: ', sum/len(lista))


#3.Primeste o lista de la tastatura (elem. separate prin spatiu) si afiseaza lista inversata.
#Ex.: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

# lista = input('Introdu lista de elemente separate prin spatiu: ').split()
# lista_inversata = lista[::-1]
# print(lista_inversata)


#4.Primesti o lista cu stringuri si construiesti o noua lista cu stringuri care contin litera 'a':
#Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

# lista = ['ana', 'mere', 'casa', 'masina']
# lista_noua = []
# for i in lista :
#     for x in i :
#         if x == 'a' :
#             lista_noua.append(i)
#             break
# print("Lista ce contine cuvinte cu litera 'a' este: ", lista_noua)

#sau

# lista = ['ana', 'mere', 'casa', 'masina']
# lista_noua = []

# for word in lista:
#     if 'a' in word:
#         lista_noua.append(word)
# print(lista_noua)





#5.Verifica daca o lista este palindrom (se citeste de la stanga la dreapta si invers)
# ex: [1,2,3,2,1] -> True, [1,2,3,4] -> False

# lista = [1, 2, 3, 2, 1]
# flag = True
# for i in range(len(lista) // 2): # am luat prima valuare si am incercat sa vdm daca se imparte la 2
#     if lista[i] != lista[-(i + 1)]: #daca mai ramane o valoare la mijloc
#         flag=False # daca ramane palindrom
#         break
# if flag:
#     print('Lista este palindrom')
# else:
#     print('Lista nu este palindrom') 

#varianta cu slice

# lista = [1, 2, 3, 2, 1]

# if lista == lista[::-1]:
#     print('Lista este palindrom')
# else:
#     print('Lista nu este palindrom.')

#varianta cu reversed()

# lista = [1, 2, 3, 2, 1]
# if lista == list(reversed(lista)):
#     print('Lista este palindrom')
# else:
#     print('Lista nu este palindrom')




#6.Interclaseaza doua liste de aceeasi lungime intr-o singura lista.
#ex: [1,2], [3,4] -> [1,3,2,4]

#Varianta [1,2,3,4]

# list1 = [1,2]
# print(list1)
# list2 = [3,4]
# print(list2)
# list1.extend(list2)
# print(list1)

#varianta [1,3,2,4]

# list1 = [1,2]
# list2 = [3,4]

# rezultat = [] #creezi o lista goala unde vei pune

# for i in range(len(list1)):
#     rezultat.append(list1[i])
#     rezultat.append(list2[i])

# print(rezultat)

# varianta cu zip

# list1 = [1,2]
# list2 = [3,4]

# rezultat = []

# for a, b in zip(list1, list2):
#     rezultat.append(a)
#     rezultat.append(b)

# print(rezultat)

#varianta cea mai avansata

# list1 = [1,2]
# list2 = [3,4]
# rezultat = [x for pereche in zip(list1, list2) for x in pereche]

# print(rezultat)



#7.Primeste o lista de numere si grupeaza elementele in doua liste: una cu 
# numere negative alta cu numere pozitrive 
# ex: [10, -1, 2, -3, 0, 4, -5] -> negative: [-1, -3 -5], pozitive: [10, 2, 0, 4]

# lista = [10, -1, 2, -3, 0, 4, -5]
# negative = []
# pozitive = []

# for i in lista :
#     if i < 0 :
#         negative.append(i)
#     else:
#         pozitive.append(i)
# print('Numere negative: ', negative)
# print('Numere pozitive: ',pozitive)

#varianta cu list comprehension

# lista = [10, -1, 2, -3, 0, 4, -5]

# negative = [x for x in lista in x < 0]
# pozitive = [x for x in lista if x >= 0]

# print('Negative: ', negative)
# print('Pozitive:', pozitive)

#8.Primeste o lista de stringuri si sort crecator dupa numar de vocale din fiecare string, 
# fara a folosi sort() sau sorted()
#ex: ['ana', 'masina', 'casa', 'mere']

#lista = ['ana', 'masina', 'casa', 'mere']

# x = 4

# if x > 0:
#     print('pozitiv')

#     if x % 2 == 0:
#         print('par')
#     else:
#         print('impar')
    
# else:
#     print('negativ sau zero')

# lista = [4, 3, -2, 0, 7]

# for x in lista:
#     if x > 0:
#        if x % 2 == 0:
#             print('numar par')
#        else:
#             print('numar impar')

# else:
#     print(x, 'negativ sau zero')



# lista = [5, -1, 0, 8]

# for x in lista:
#     if x > 0:
#         print('pozitiv')
#     else:
#         print(x, 'negativ sau zero')

# lista = [5, -1, 0, 8]

# for x in lista:
#     if x > 0:
#         if x > 10:
#             print(x, 'mai mare')
#         else:
#             print(x, 'mai mic')
#     else:
#         print(x, 'negativ sau 0')

# t = (1, 2, 2, 3, 2)
# count = 0
# for x in t:
#     if x == 2:
#         count += 1
# print(count)


# import random as rand
# from random import randint as r
# from random import randint # , randrange, ...
# import exemplu_modules_import as md
# import math
# import exemplu_package.exemplu_pkg_mod1 as pkgmd1

# def calcul():
#     a = rand.randint(1,5)
#     b = rand.randint(1,5)
#     return a + b





import random as rand
# from random import randint as r
# from random import randint # , randrange, ...
import exemplu_modules_import as md
# import math
import exemplu_package.exemplu_pkg_mod1 as pkgmd1

def calcul():
    a = rand.randint(1,5)
    b = rand.randint(1,5)
    return a + b


def main():
    print(calcul())
    # md.my_function()
    # print(md.my_var)
    # print(math.pi)
    # print(md.__name__)
    # print(__name__)
    pkgmd1.pkg_mod_1_function()
    print(pkgmd1.var_mod1)


# def main():
#     nume, prenume = parse_arguments()
#     print(f'Nume: {nume}, Prenume: {prenume}')


# if __name__ == '__main__':
#     main()