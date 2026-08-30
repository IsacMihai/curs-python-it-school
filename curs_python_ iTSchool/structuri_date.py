'''
Structuri de date în Python

1. Liste (list)
    - O listă este o colecție ordonată, modificabilă(mutable), care permite elemente duplicate, indexabila.

    - Se definește cu paranteze pătrate: [ ] sau folosind funcția list().

    - Metode uzuale:
      * append(x)    - adaugă un element la finalul listei
      * insert(i, x) - inserează un element pe poziția i
      * remove(x)    - elimină prima apariție a elementului x
      * pop(i)       - elimină și returnează elementul de pe poziția i (sau ultimul dacă nu se dă index)
      * index(x)     - returnează indexul primei apariții a lui x
      * count(x)     - numără de câte ori apare x în listă
      * extend(iter) - adaugă la listă toate elementele dintr-un alt iterabil
      * len()        - returnează numărul de elemente din listă
      * clear()      - elimină toate elementele din listă
      * sort()       - sortează lista (in place = modifică lista originală)
      * reverse()    - inversează ordinea elementelor (in place = modifică lista originală)

    Funcții utile:
      - sorted(iter) - returnează o copie sortată a iterabilului (nu modifică originalul)

      - list(iter) - convertește un iterabil într-o listă

      - enumerate(iter) - returnează un obiect enumerat (index, valoare) din iterabil

      - zip(iter1, iter2, ...) - combină mai multe iterabile într-un singur iterabil de tupluri

      - list comprehension - sintaxă pentru a crea liste noi din iterabile existente
            Ex: [x**2 for x in range(10) if x % 2 == 0]  # creeaza o lista cu pătratele numerelor pare de la 0 la 9

      - list slicing - extrage subliste folosind sintaxa list[start:stop:step]

      - any() - returnează True dacă cel puțin un element din listă este adevărat

      - all() - returnează True dacă toate elementele din listă sunt adevărate
'''

'''
2. Tuple (tuple)
    - O tuple este o colecție ordonată, nemodificabilă (immutable), permite duplicate, indexabilă.

    - Se definește cu paranteze rotunde: ( ) sau funcția tuple().

    - Metode uzuale:
      * count(x)    - numără de câte ori apare x în tuple
      * index(x)    - returnează indexul primei apariții a lui x

    Funcții utile:
      - tuple(iter) - convertește un iterabil într-o tuple

      - unpacking - atribuirea valorilor dintr-o tuple în variabile separate
            Ex: a, b, c = (1, 2, 3)

      - tuple slicing - extrage sub-tupluri folosind sintaxa tuple[start:stop:step]

      - iterare - se poate itera prin elementele unei tuple folosind bucla for

      - tuple comprehension (generatoare) - sintaxă pentru a crea tupluri noi din iterabile existente
            Ex: tuple(x**2 for x in range(10) if x % 2 == 0)  # tupla pătratelor numerelor pare de la 0 la 9

'''

'''
3. Seturi (set)
    - Un set este o colecție neordonată, fără duplicate.

    - Se definește cu acolade: { } sau funcția set().

    - Metode uzuale:
      * add(x)         - adaugă elementul x în set
      * remove(x)      - elimină x din set (dă eroare dacă nu există)
      * discard(x)     - elimină x dacă există, fără eroare
      * pop()          - elimină și returnează un element aleator
      * clear()        - elimină toate elementele
      * update(iter)   - adaugă toate elementele dintr-un iterabil
      * union(s)       - returnează reuniunea cu setul s
      * intersection(s)- returnează intersecția cu setul s
      * difference(s)  - returnează diferența față de setul s
      * issubset(s)    - verifică dacă setul este sub-mulțime a lui s

    - Funcții utile:
      - set(iter)     - convertește un iterabil într-un set

      - frozenset(iter) - creează un set neschimbabil (immutable)

      - iterare - se poate itera prin elementele unui set folosind bucla for

      - set comprehension - sintaxă concisă pentru a crea seturi noi din iterabile existente
            Ex: {x**2 for x in range(10) if x % 2 == 0}  # setul pătratelor numerelor pare de la 0 la 9
'''

'''
4. Dicționare (dict)
    - Un dicționar este o colecție de perechi cheie:valoare, ordonată (de la Python 3.7), modificabilă (mutable)

    - Se definește cu acolade: { } sau funcția dict()

    - Metode uzuale:
      * keys()         - returnează o listă cu toate cheile
      * values()       - returnează o listă cu toate valorile
      * items()        - returnează o listă de tupluri (cheie, valoare)
      * pop(k)         - elimină și returnează valoarea pentru cheia k
      * popitem()      - elimină și returnează ultima pereche adăugată
      * update(d)      - actualizează dicționarul cu perechi din d (d poate fi alt dicționar sau o listă de tupluri (cheie, valoare)); dacă o cheie există deja, valoarea va fi suprascrisă; dacă nu există, va fi adăugată. Exemplu: d1.update({'a': 10, 'b': 20}), d1.update([('c', 30), ('d', 40)])
      * clear()        - elimină toate elementele

    - Funcții utile:
      - dict(iter) - convertește un iterabil de tupluri (cheie, valoare) într-un dicționar

      - get(k, default) - returnează valoarea pentru cheia k sau default dacă nu există

      - setdefault(k, default) - returnează valoarea pentru cheia k; dacă nu există, adaugă k cu valoarea default

      - iterare - se poate itera prin chei, valori sau perechi folosind bucla for
'''

# fructe = ['banane', 'mere', 'pere', 'kiwi']
# print(fructe)
# print(fructe[1])
# fructe[0] = 'capsuni'
# print(fructe)
# print(fructe[1][-1])
# print(fructe[0][0:4])

# elementul = fructe[0]
# caractere = elementul[0:4]
# print(caractere)

# print(fructe[-1].upper())

# scos 'i' din lista
# numarat de cate ori se afla un element intr-o lista incluzand subliste

# lista_smechera = [1, 2, 3, 'kiwi', 'bere', ['Mariana', ['Ionela'], ['Marius', 3]]] # ela din Ionela
# print(lista_smechera[-1][-1][0][-3:])
# print(len(lista_smechera))

# lista_smechera.append(4.6)
# print(lista_smechera)
# lista_smechera.insert(3, 3.5)
# print(lista_smechera)
# lista_smechera.append(3.5)
# print(lista_smechera)
# print(lista_smechera.index(3.5))
# lista_smechera.remove(3.5)
# print(lista_smechera)

# while 3.5 in lista_smechera:
#     print(lista_smechera.remove(3.5))

# print(lista_smechera)

# print(lista_smechera.pop(-2))
# print(lista_smechera)

# for element in lista_smechera:
#     print(type(element))

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]

# lista1.append(lista2)
# print(lista1)

# lista1.extend(lista2)
# print(lista1)

# lista1.clear()
# print(lista1)

# exemplu = [5, 7, 3, 1, 9, 4]
# exemplu.sort()
# print(exemplu)


# exemplu = ['1', '3', '2', 'asa', 'se' , 'face', 'un' , 'sort', True] # 'a' = 103 '1' = 72 '2' = 73
# exemplu.sort()
# print(exemplu)
# exemplu.sort()
# print(exemplu)

# ex_sorted = sorted(exemplu, reverse=True)
# print(exemplu)
# print(ex_sorted)

# lista_mea = list()
# print(lista_mea)

# for index, valoare in enumerate(exemplu):
#     if valoare == 'face':
#         print(f'{index} -> {valoare}')

# print(exemplu[-3:])

# x = [1, 2, 3, 9]
# y = [4, 5, 6, 10]
# (1, 4)

# for a, b in zip(x, y):
#     print(f'elementele inpachetate sunt {a} - {b}')

# nume = ["ana", "maria", "marcel"]
# varsta = [32, 54, 18]

# for elem_nume, elem_varsta in zip(nume, varsta):
#     print(f'{elem_nume} are {elem_varsta} ani')

# lista1 = [0, 99, 0, 0]
# lista2 = [1, 2, 3, 4]

# print(any(lista1))
# print(any(lista2))

# print(all(lista1))
# print(all(lista2))

# []

# lista_karina = range(1,11)
# # lista_pare = [2, 4, 6, 8, 10]
# lista_pare = []
# for x in lista_karina:
#     if x % 2 == 0:
#         lista_pare.append(x)
#     else:
#         continue

# print(lista_pare)

# # lista_mea -> [element ** 2]

# lista_mea = [x ** 2 for x in lista_karina if x % 2 == 0]
# print(lista_mea)

# lista_initiala = [3, 5, 7, 15, 21, 72, 56, 99]
# lista_speciala = [15, 30] # numerele divizibile cu 3 si cu 5
# lista_speciala = [x for x in lista_initiala if x % 3 == 0 and x % 5 == 0]
# print(lista_speciala)

# verificati cel putin un element din lista_initiala e divizivil si cu 3 si cu 5
# print(any([x % 3 == 0 and x % 5 == 0 for x in lista_initiala]))
# print(flag)

# print(any([lista_initiala] % 15 == 0))

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


# zile = ('luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica')
# print(zile)
# print(zile[3])
# print(zile.count('luni'))
# print(zile.index('vineri'))
# zile_lucratoare = zile[0:5]
# print(zile_lucratoare)
# # zile_lucratoare[0] = 'Luni' # eroare

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
# prenume, varsta = tuple_ceva
# print(prenume)
# print(varsta)

# my_set = {1,2,3,4,5}
# print(my_set)
# my_set.add('5')
# print(my_set)

# lista_mea = [1,2,2,3,3,3,4,5,6,6,7,7,7]
# print(lista_mea)
# lista_mea = set(lista_mea)
# lista_mea = list(lista_mea)
# # lista_mea = list(set(lista_mea))
# print(lista_mea)

# my_set = {1,2,3,4,5,6,7,8}
# print(my_set)
# print(my_set.pop())
# print(my_set)

set1 = {1, 2, 3, 4, 5}
# print(set1)
set2 = {3, 4, 7, 8, 9}
# print(set2)
# set1.update(set2)
# print(set1)

# print(set1.union(set2))
# print(set1)
# print(set2)

# print(set1.difference(set2))
# print(set2.difference(set1))

# print(set1.intersection(set2))
# print(set1.issubset(set2))

# set2 = {3, 4, 7, 8, 9}
# set3 = {3, 4, 7, 8, 9, 10}
# print(set2.issubset(set3))
# print(set3.issuperset(set2))

# set1.clear()
# print(set1)
# ex = {}
# print(type({}))
# print(type(ex))
# print(ex)


# print({x**2 for x in range(10) if x % 2 == 0})

# lista = [1,2,3,3,3,4]
# frz_set = frozenset(lista)
# print(frz_set)
# l = list(frz_set)
# print(l)

# lis = [1, 2, 3, 4]
# var = {'Ana':18, 'Maria': 18, 'Marian':45}
# # print(type(dictionarul_danutului))

# print(var['Ana'])
# var['Ana'] = 19

# print(var)

# buletine = {1: {'Nume': 'Ana', 'CNP':123, 'Varsta':18}, 2: {'Nume': 'Marius', 'CNP':125, 'Varsta':22}}

# for persoana in buletine:
#     if persoana['Nume'] == 'Ana' and persoana['CNP'] == 123:
#         persoana['Nume'] = 'Rodica'
#         break

# lista_keys = list(buletine[0].keys())
# print(lista_keys)
bul1 = {'Nume': 'Ana', 'CNP':123, 'Varsta':18}
# bul2 = {'Nume': 'Marius', 'CNP':125, 'Varsta':22}

# for element in bul1.keys():
#     print(element)
# print()
# for element in bul1.values():
#     print(element)
# print()
# for key, value in bul1.items():
#     print(key, value)

# bul1 = {'Nume': 'Ana', 'CNP':123, 'Varsta':18}
# bul1['Nume Familie'] = 'Ionescu'

# print(bul1)
# print(bul1.pop('Nume'))
# print(bul1)

# print(bul1.popitem())
# print(bul1)

# # print(bul1['Nume'])
# print(bul1.get('Nume'))

# # nume_dict['key_noua'] = 'val_noua'
# bul1.update({'Nume': 'Ana'})
# print(bul1)
# bul1.update([('Nume Familie', 'Ionescu'), ('Salar', 150)])
# print(bul1)

# bul1.update({'Nume': 'Marcela'})
# print(bul1)

# '''
# CNP - Key Unica
#     {* nume
#      * prenume
#      * varsta
#      * masina { * marca
#                 * vin
#                 * tip_combustibil
#               }
#     }
# '''


# dict_mare = {
#     1234: {
#         'nume': 'popescu',
#         'prenume': 'ionut',
#         'varsta': 20,
#         'masina': {
#             'marca': 'bmw',
#             'vin': 1235,
#             'tip_c': 'benzol'
#         }
#     },
#     1235: {
#         'nume': 'ionescu',
#         'prenume': 'codrut',
#         'varsta': 99,
#         'masina': {
#             'marca': 'dacie',
#             'vin': 9901,
#             'tip_c': 'benzol'
#         }
#     }
# }

# lis = [1,2,[3,4]]
# lis[2][0]

# dict_mare[1234] = dict_mare.get(1234)

# print(dict_mare[1235]['masina']['tip_c'])
# dict_mare[1235]['masina']['tip_c'] = 'gpl'
# print(dict_mare[1235]['masina']['tip_c'])

# print(dict_mare.get(1235).get('masina').update({'tip_c': 'electric'}))
# print(dict_mare.get(1235).get('masina').get('tip_c'))
# print(dict_mare)

# import json
# print(json.dumps(dict_mare, indent=4))

# bul1 = {'Nume': 'Ana', 'CNP':123, 'Varsta':18, 'Note': [1,2,3,4]}
# print(bul1.get('masina', 'negasit'))

# print(bul1.setdefault('masina', 'Nu are masina'))
# print(bul1)

d = {}
print(d)
# d.setdefault('fructe', [])
# print(d)
# d.setdefault('fructe', []).append('mar')
# print(d)
# d.setdefault('fructe', []).append('banana')
# print(d)

# d['fructe'] = ['mar', 'banana', 'portocala']

# for fruct in ['mar', 'banana', 'portocala']:
#     d.setdefault('fructe', []).append(fruct)

# print(d)

patr = [x**2 for x in range(5)]
print(patr)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

patrate = {x:x**2 for x in range(5)}
print(patrate)
