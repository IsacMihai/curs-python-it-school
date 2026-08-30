'''
Exercitii pentru tuples:
1) Creează un tuplu care conține numele a trei fructe și afișează-le pe ecran.
    Exemplu: ('măr', 'banană', 'cireașă') -> măr, banană, cireașă

Se da tuplul: fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi').

2) Afișează al doilea și al patrulea fruct din tuplu.

3) Afișează tuplul inversat.

4) Verifică dacă 'kiwi' este în tuplu și afișează un mesaj corespunzător.

5) Creează un tuplu nou care conține doar fructele de la pozițiile(index) pare din tuplul original.

6) Afișează lungimea fiecarui element din tuplu.

7) Concatenează tuplul cu un alt tuplu care conține alte două fructe și afișează rezultatul.

8) Adauga un fruct nou 'ananas' in tuplu.

9) Se da tuplul: ('măr', 'banană', 'cireașă'). Faceti unpacking pentru a extrage fiecare element in variabile separate
   si afisati-le.

Exerciții pentru seturi:
1) Creează un set care conține numele a cinci culori și afișează-le pe ecran.

2) Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat.

3) Elimină o culoare din set și afișează setul actualizat.

4) Verifică dacă o anumită culoare (de exemplu, 'albastru') este în set și afișează un mesaj corespunzător.

5) Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi.

6) Afișează toate culorile din primul set care nu sunt în al doilea set.

7) Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista,
   astfel incat fiecare element sa apara o singura data.

'''
#lista = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]
#lista = []




#Exercitiu extra:Se dau urmatoarele expresii matematice:
# ((a + b) * (c - d) + e) / f - (g * (h + i)) -> corect deschise si inchise
# ((a + b) * (c - d) + e) / f - )g * (h + i)( -> incorect deschise si inchise
# Sa se verifice daca parantezele sunt corect deschise si inchise. 

# exp1 = "((a + b) * (c - d) + e) / f-(g * (h + i))"
# exp2 = "((a + b) * (c - d) + e) / f-(g * (h + i)("

# lista = []

# for char in exp2:
#     if char == "(":
#         lista.append(char)
#     elif char == ")":
#         lista.append(char)

# lista2 = []
# flag = False

# for char in lista:
#     if char == "(":
#         lista2.append(char)
#     elif char == ")":
#         if len(lista2) > 0:
#             lista2.pop()
#     elif len(lista2) == 0:
#         print("Incorrect")
#         flag = True
#         break

# if len(lista2) != 0:
#     print("Ai prea multe paranteze deschise! ")
# elif flag is False:
#     print("Corect!")





#tema:
#Exercitii pentru tuples:

#1.Creează un tuplu care conține numele a trei fructe și afișează-le pe ecran. Exemplu: ('măr', 'banană', 'cireașă') -> măr, banană, cireașă

# fructe = ('mar', 'banana', 'cireasa')
# print(fructe)

#sau

# fructe = ('măr', 'banană', 'cireașă')
# print(", ".join(fructe)) #.join - uneste elementele cu , intre ele

#2.Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# print(fructe[1], fructe[3]) #indexu incepe de la 0

#3.Afișează tuplul inversat.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# print(fructe[::-1]) # [::-1] - intoarce tuplul invers

#4.Verifică dacă 'kiwi' este în tuplu și afișează un mesaj corespunzător.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# if "kiwi" in fructe:
#     print("Kivi este in tuplu")
# else:
#     print("Kivi nu este in tuplu")

#5.Creează un tuplu nou care conține doar fructele de la pozițiile(index) pare din tuplul original.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# print(fructe[::2]) # [::2] - pozitii pare

#6.Afișează lungimea fiecarui element din tuplu.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# for fruct in fructe:
#     print(fruct, "are", len(fruct), "litere") # len - numarul de elemente lungimea dintr-un obict

#7. Concatenează tuplul cu un alt tuplu care conține alte două fructe și afișează rezultatul.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# alte_fructe = ('mango', 'pere')
# tuplu_nou = fructe + alte_fructe
# print(tuplu_nou)

#8.Adauga un fruct nou 'ananas' in tuplu.

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# fructe = fructe + ('ananas',)
# print(fructe)

#9.Se da tuplul: ('măr', 'banană', 'cireașă'). Faceti unpacking pentru a extrage fiecare element in variabile separate
#   si afisati-le.

# fructe = ('mar', 'banana', 'cireasa')
# f1, f2, f3 = fructe
# print(f1)
# print(f2)
# print(f3)




#Exerciții pentru seturi:

#1) Creează un set care conține numele a cinci culori și afișează-le pe ecran.

# culori = {'roșu', 'verde', 'albastru', 'galben', 'negru'}
# print(culori)

#2) Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat.

# culori = {'roșu', 'verde', 'albastru', 'galben', 'negru'}
# culori.add('mov')   # add daca veri sa adaugi culori
# print(culori)

#3) Elimină o culoare din set și afișează setul actualizat..

# culori = {'roșu', 'verde', 'albastru', 'galben', 'negru'}
# culori.remove('verde')
# print(culori)

#4) Verifică dacă o anumită culoare (de exemplu, 'albastru') este în set și afișează un mesaj corespunzător.

# culori = {'roșu', 'verde', 'albastru', 'galben', 'negru'}
# if 'albastru' in culori:
#     print('Albastru este in set')
# else:
#     print('Albastru nu este in set')

#5) Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi.

# culori = {'roșu', 'verde', 'albastru', 'galben', 'negru'}
# alte_culori = {'albastru', 'roz', 'verde'}
# comun = culori & alte_culori  # & - intersectie
# print(comun)

#6) Afișează toate culorile din primul set care nu sunt în al doilea set.

# culori = {'roșu', 'verde', 'albastru', 'galben', 'negru'}
# alte_culori = {'albastru', 'roz', 'verde'}
# diferenta = culori - alte_culori
# print(diferenta)

#7) Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista,
#   astfel incat fiecare element sa apara o singura data.

# lista = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]
# # fara_duplicate = set(lista)
# # print(fara_duplicate)

# #sau
# lista_unica = list(set(lista))
# print(lista_unica)