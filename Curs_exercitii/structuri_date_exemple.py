'''
Structuri de date în Python

1. Liste (list)
    - O listă este o colecție ordonată, modificabilă(mutable), care permite elemente duplicate, 
    indexabila.

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
            Ex: [x**2 for x in range(10) if x % 2 == 0]  # creeaza o lista cu pătratele numerelor 
            pare de la 0 la 9

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
            Ex: tuple(x**2 for x in range(10) if x % 2 == 0)  # tupla pătratelor numerelor pare de 
            la 0 la 9

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
    - Un dicționar este o colecție de perechi cheie:valoare, ordonată (de la Python 3.7), modificabilă

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
      - dict(iter)    - convertește un iterabil de tupluri (cheie, valoare) într-un dicționar

      - get(k, default) - returnează valoarea pentru cheia k sau default dacă nu există

      - setdefault(k, default) - returnează valoarea pentru cheia k; dacă nu există, adaugă k cu valoarea default

      - iterare - se poate itera prin chei, valori sau perechi folosind bucla for
'''


# 1. Liste - exemple
# fructe = ['mar', 'banana', 'portocala']      # creare listă
# fructe.append('kiwi')                        # adăugare element la final
# fructe.insert(1, 'ananas')                   # inserează pe poziția 1
# fructe.remove('banana')                      # elimină prima apariție a 'banana'
# element = fructe.pop(0)                       # elimină și returnează ultimul element
# index_portocala = fructe.index('portocala')        # indexul lui 'ananas'
# nr_mere = fructe.count('mar')                # de câte ori apare 'mar'
# fructe.sort()                                # sortează lista (in place)
# fructe.reverse()                             # inversează ordinea (in place)
# fructe.extend(['pruna', 'cireasa'])          # adaugă elemente din alt iterabil
# fructe_copie = fructe.copy()                 # copie superficială
# lungime = len(fructe)                        # numărul de elemente
# fructe.clear()                               # elimină toate elementele
# print(fructe)
# list() - conversie
# l = list('abc')  # ['a', 'b', 'c']

# # sorted() - copie sortată
# numere = [3, 1, 2]
# numere_sortate = sorted(numere)  # [1, 2, 3]

# # enumerate()
# for idx, val in enumerate(['a', 'b', 'c']):
  # print(idx, val)

# # zip()
# nume = ['Ana', 'Ion']
# varsta = [20, 30]
# for n, v in zip(nume, varsta):
  # print(n, v)

# # list comprehension
patrate_pare = [x*2 for x in range(10) if x % 2 == 0]
print(patrate_pare)

# # slicing
# lista = [0, 1, 2, 3, 4, 5]
# sublista = lista[1:4]  # [1, 2, 3]
# invers = lista[::-1]   # [5, 4, 3, 2, 1, 0]


# # 2. Tuple - exemple
# zile = ('luni', 'marti', 'miercuri', 'luni') # creare tuple
# print(zile[0])                               # accesare element
# nr_luni = zile.count('luni')                 # de câte ori apare 'luni'
# poz_marti = zile.index('marti')              # indexul lui 'marti'
# subtuple = zile[1:3]                         # slicing
# for zi in zile:                              # iterare
#    print(zi)
# tuple_concat = zile + ('joi',)               # concatenare
# tuple_mult = zile * 2                        # multiplicare

# # tuple() - conversie
# t = tuple([1, 2, 3])
# print(t)

# # tuple comprehension (generator)
# tuple_gen = tuple(x**2 for x in range(6) if x % 2 == 0)
# print(tuple_gen)
# # zile[1] = 'joi'  # va da eroare, tuplele nu pot fi modificate


# # 3. Seturi - exemple
# culori = {'rosu', 'verde', 'albastru'}              # creare set
# culori.add('galben')                                # adăugare element
# culori.remove('verde')                              # eliminare element (eroare dacă nu există)
# culori.discard('negru')                             # eliminare fără eroare dacă nu există
# element = culori.pop()                              # elimină și returnează un element aleator
# culori.update(['negru', 'alb'])                     # adaugă elemente dintr-un iterabil
# reuniune = culori.union({'roz', 'mov'})             # reuniune cu alt set
# intersectie = culori.intersection({'alb', 'rosu'})  # intersecție
# dif = culori.difference({'rosu'})                   # diferență
# este_submultime = {'alb', 'negru'}.issubset(culori) # verificare submulțime
# culori_copie = culori.copy()                        # copie superficială
# culori.clear()                                      # elimină toate elementele

# for culoare in culori:                              # iterare
#   print(culoare)

# # set() - conversie
# s = set([1, 2, 2, 3])  # {1, 2, 3}
# print(s)

# # frozenset
# fs = frozenset(['a', 'b', 'c'])
# print(fs)

# # set comprehension
# patrate_pare_set = {x**2 for x in range(10) if x % 2 == 0}
# print(patrate_pare_set)


# # 4. Dicționare - exemple
# persoana = {'nume': 'Ana', 'varsta': 25}     # creare dicționar
# print(persoana['nume'])                      # accesare valoare
# persoana['varsta'] = 26                      # modificare valoare
# persoana['oras'] = 'Cluj'                    # adăugare pereche
# chei = list(persoana.keys())                 # toate cheile
# valori = list(persoana.values())             # toate valorile
# perechi = list(persoana.items())             # toate perechile (tupluri)
# v = persoana.get('nume', 'necunoscut')       # accesare cu valoare implicită
# persoana.pop('varsta')                       # elimină și returnează valoarea pentru cheia 'varsta'
# persoana.update({'email': 'ana@email.com'})  # actualizează cu alt dicționar
# persoana.update([('telefon', '1234')])       # actualizează cu listă de tupluri
# persoana.setdefault('tara', 'Romania')       # adaugă dacă nu există
# persoana_copie = persoana.copy()             # copie superficială
# persoana.clear()                             # elimină toate elementele

# for cheie in persoana:                       # iterare chei
#   print(cheie)

# for valoare in persoana.values():            # iterare valori
#   print(valoare)

# for cheie, valoare in persoana.items():      # iterare perechi
#   print(cheie, valoare)

# # dict() - conversie
# d = dict([('a', 1), ('b', 2)])
# print(d)

# # dict comprehension
# patrate = {x: x**2 for x in range(5)}
# print(patrate)

