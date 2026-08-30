#TEMA CU WHILE 14.01.2026

# Ca sa ne jucam putin si cu bucla while, am urmatorul exercitiu pt voi. 
#Idee de baza din spatele lui o sa o folosim si pe viitor la un mini proiect pe care urmeaza 
#sa il facem dupa ce trecem de structuri de date.

# Enuntul suna cam asa:
# Trebuie implementat un meniu interactiv in consola care pune la dispozitie utilizatorului urmatoarele
#  optiuni:

# Adunare
# Scadere
# Inmultire
# Impartire
# Iesire din program

# Utilizatorul trebuie sa introduca optiunea, iar apoi:
# Pentru optiunile 1->4, utilizatorul trebuie sa introduca doua numere, iar programul va afisa 
# rezultatul operatiei.
# In cazul in care introduce 5, atunci iesim din program. 

#Varianta simpla:

# while True:
#     print('\nAlege optiunea:')
#     print('1. Adunare')
#     print('2. Scadere')
#     print('3. Inmultire')
#     print('4. Impartire')
#     print('5. Iesire din program')

#     choice = input('Optiunea ta: ')

#     if choice == '5':
#         print('La Revedere!')
#         break

#     if choice not in ['1', '2', '3', '4']:
#         print('Optiunea invalida!')
#         continue

#     try:
#         a = float(input('Primul numar: '))
#         b = float(input('Al doilea numar: '))

#         if choice == '1':
#             print('Resultat:', a + b)
#         elif choice == '2':
#             print('Rezultat:', a - b)
#         elif choice == '3':
#             print('Rezultat:', a * b)
#         elif choice == '4':
#             if b == 0:
#                 print('Nu se imparte la 0!')
#             else:
#                 print('Rezultatul:', a / b)
    
#     except ValueError:
#         print('Introdu numere valide!')


#Varianta complexa:

# def check_entrydata(value1, value2):
#     try:
#         val1 = float(value1)
#         val2 = float(value2)
#         return val1, val2
#     except  ValueError:
#         raise ValueError('Valorile introduse trebuie sa fie numerale.')
    
# def add(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     return val1 + val2

# def subtract(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     return val1 - val2

# def multiply(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     return val1 * val2

# def divide(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     if val2 == 0:
#         raise ValueError('Impartirea la zero nu este permisa.')
#     return val1 / val2

# def main():
#     while True:
#         print('\nAlege optiunea: ')
#         print('1. Adunare')
#         print('2. Scadere')
#         print('3. Inmultire')
#         print('4. Impartire')
#         print('5. Iesire din program')
#         choice = input('Introduceti optiunea (1/2/3/4/5): ')
#         if choice == '5':
#             print('Iesire din program.')
#             break
#         if choice in ['1','2','3','4']:
#             value1 = input('Introduceti primul numar: ')
#             value2 = input('Introduceti al doilea numar: ')
#             try:
#                 if choice == '1':
#                     result = add(value1, value2)
#                     print(f'Rezultat: {result}')
#                 elif choice == '2':
#                     result = subtract(value1, value2)
#                     print(f'Rezultat: {result}')
#                 elif choice == '3':
#                     result = multiply(value1, value2)
#                     print(f'Rezultat: {result}')
#                 elif choice == '4':
#                     result = divide(value1, value2)
#                     print(f'Rezultat: {result}')
#             except ValueError as e:
#                 print(e)
#         else:
#             print('Optiune invalida.Incercati din nou.')

# main()




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
