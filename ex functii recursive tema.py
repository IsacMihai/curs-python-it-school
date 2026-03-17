             
#              Exercitii Functii recursive:

# 1) Scrie o funcție recursivă care calculează factorialul unui număr.
# Ex: pentru n = 5, 5 x 4 x 3 x 2 x 1 = 120
# 2) Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.
# Ex: pentru n=5, returnează 15 (1+2+3+4+5)
# 3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
# Ex: pentru 1234 returneaza 4
# 4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3
# 5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28



# 1) Scrie o funcție recursivă care calculează factorialul unui număr.

# Ex: pentru n = 5, 5 x 4 x 3 x 2 x 1 = 120

# def factorial(n):
#     if n == 0 or n == 1: # Cazul de bază: factorialul lui 0 sau 1 este 1
#         return 1
#     else:
#         return n * factorial(n - 1) # Cazul recursiv: n * factorial(n-1)
# # Testăm funcția
# numar = 7
# rezultat = factorial(numar)
# print(f"Factorialul lui {numar} este {rezultat}")


#sau

# def factorial(n):
#     print(f"Calculez factorial({n})")
    
#     if n == 0 or n == 1:
#         print(f"Cazul de bază: factorial({n}) = 1")
#         return 1
#     else:
#         rezultat = n * factorial(n - 1)
#         print(f"factorial({n}) = {n} × factorial({n-1}) = {rezultat}")
#         return rezultat

# # Testăm
# factorial(6)


# 2) Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.
# Ex: pentru n=5, returnează 15 (1+2+3+4+5)

# def suma(n):
#     if n == 1:
#         return 1
#     else:
#         return n + suma(n - 1)

# numar = 8
# rezultat = suma(numar)
# print(f'Suma numerelor de la 1 la {numar} este {rezultat}')

#sau

# def suma(n):
#     print(f"Calculez suma({n})")
    
#     if n == 1:
#         print(f"Cazul de bază: suma(1) = 1")
#         return 1
#     else:
#         rezultat = n + suma(n - 1)
#         print(f"suma({n}) = {n} + suma({n-1}) = {rezultat}")
#         return rezultat
# suma(5)

#sau
#Comparație cu varianta iterativă (cu for):

# def suma_iterativa(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#     return total

# print(suma_iterativa(5))


# 3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
# Ex: pentru 1234 returneaza 4

# def numar_cifre(n):
#     if n < 10:
#         return 1
#     else:
#         return 1 + numar_cifre(n // 10)
    
# numar = 123456
# rezultat = numar_cifre(numar)
# print(f"Numarul {numar} are {rezultat} cifre")

# def numar_cifre(n):
#     print(f"Verific numărul {n}")
    
#     if n < 10:
#         print(f"Cazul de bază: {n} are o singură cifră")
#         return 1
#     else:
#         rezultat = 1 + numar_cifre(n // 10)
#         print(f"numar_cifre({n}) = 1 + numar_cifre({n // 10}) = {rezultat}")
#         return rezultat
# numar_cifre(1234)



# 4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3

# def adancime_lista(lista):
#     # Cazul de bază: dacă nu este listă, adâncimea este 0
#     if not isinstance(lista, list):
#         return 0
    
#     # Dacă lista este goală, adâncimea este 1
#     if len(lista) == 0:
#         return 1
    
#     # Cazul recursiv: găsim adâncimea maximă a elementelor
#     adancime_maxima = 0
#     for element in lista:
#         adancime_element = adancime_lista(element)
#         if adancime_element > adancime_maxima:
#             adancime_maxima = adancime_element
    
#     return 1 + adancime_maxima

# # Testăm funcția
# lista = [1, 2, [3, 4, [5, 6]], 7]
# rezultat = adancime_lista(lista)
# print(f"Adâncimea listei {lista} este {rezultat}")

#sau

# def adancime_lista(lista, nivel=0):
#     indentare = "  " * nivel  # Pentru afișare mai clară
    
#     if not isinstance(lista, list):
#         print(f"{indentare}{lista} nu este listă → adâncime 0")
#         return 0
    
#     if len(lista) == 0:
#         print(f"{indentare}[] listă goală → adâncime 1")
#         return 1
    
#     print(f"{indentare}Verific lista: {lista}")
    
#     adancime_maxima = 0
#     for element in lista:
#         adancime_element = adancime_lista(element, nivel + 1)
#         if adancime_element > adancime_maxima:
#             adancime_maxima = adancime_element
    
#     rezultat = 1 + adancime_maxima
#     print(f"{indentare}Adâncime pentru {lista} = 1 + {adancime_maxima} = {rezultat}")
#     return rezultat

# # Testăm
# lista = [1, 2, [3, 4, [5, 6]], 7]
# adancime_lista(lista)

# 5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28

# def suma_lista(lista):
#     # Cazul de bază: dacă nu este listă, returnăm numărul
#     if not isinstance(lista, list):
#         return lista
    
#     # Cazul recursiv: calculăm suma tuturor elementelor
#     suma_totala = 0
#     for element in lista:
#         suma_totala = suma_totala + suma_lista(element)
    
#     return suma_totala

# # Testăm funcția
# lista = [1, 2, [3, 4, [5, 6]], 7]
# rezultat = suma_lista(lista)
# print(f"Suma elementelor din {lista} este {rezultat}")

#sau
# def suma_lista(lista, nivel=0):
#     indentare = "  " * nivel  # Pentru afișare mai clară
    
#     if not isinstance(lista, list):
#         print(f"{indentare}{lista} este număr → returnez {lista}")
#         return lista
    
#     print(f"{indentare}Calculez suma pentru: {lista}")
    
#     suma_totala = 0
#     for element in lista:
#         rezultat_element = suma_lista(element, nivel + 1)
#         suma_totala = suma_totala + rezultat_element
#         print(f"{indentare}  suma parțială = {suma_totala}")
    
#     print(f"{indentare}Suma finală pentru {lista} = {suma_totala}")
#     return suma_totala

# # Testăm
# lista = [1, 2, [3, 4, [5, 6]], 7]
# suma_lista(lista)









# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media
# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

# print(
#     """
# # 		1. Adaugare elev
# # 		2. Afisarea elevilor existenti
# # 		3. Modificare informatii elev existent
# # 		4. Stergere elev
# # 		5. Cautare elev dupa nume si prenume
# # 		6. Afisare elevi in ordinea mediilor
# # 		7. Afisare elevi cu media peste 8
# # 		8. Afisare elevi in ordine alfabetica (dupa nume)

# """
# )

# elevi = [{'nume': 'popescu', 'prenume': 'ana', 'nota romana': 6.0, 'nota mate': 7.0, 'nota engleza': 8.0, 'media': 7.0}, 
#          {'nume': 'abesei', 'prenume': 'paul', 'nota romana': 7.0, 'nota mate': 8.0, 'nota engleza': 9.0, 'media': 8.0},
#          {'nume': 'popescu', 'prenume': 'andrei', 'nota romana': 3.0, 'nota mate': 4.0, 'nota engleza': 5.0, 'media': 4.0}
#          ]

# def adauga_elev ():
#     nume = input("Nume : ")
#     prenume = input("Prenume : ")
#     nota_romana = float(input("Nota romana :"))
#     nota_mate = float(input("Nota mate :"))
#     nota_engl = float(input("Nota engleza :"))
#     elev = {
#         "nume": nume,
#         "prenume": prenume,
#         "nota romana" : nota_romana,
#         "nota mate" : nota_mate,
#         "nota engleza" : nota_engl,
#         "media" : calculeaza_media(nota_romana, nota_mate, nota_engl)
#     }
#     elevi.append(elev)

# def calculeaza_media(nota_romana, nota_mate, nota_engl):
#     x = round((nota_romana + nota_mate + nota_engl)/3,2)
#     return x

# def ia_media(elev):
#     return elev['media']

# def ia_nume(elev):
#     return elev['nume']

# def afiseaza_elevi():
#     for elev in elevi :
#         print(f"{elev['nume']} {elev['prenume']} | "
#             f"Romana: {elev['nota romana']} | "
#             f"Matematica: {elev['nota mate']} | "
#             f"Engleza: {elev['nota engleza']} | "
#             f"Media: {elev['media']}")
        
# def afisare_alfabetic():
#     elevi_sortati = sorted(elevi, key=ia_nume)
#     for elev in elevi_sortati:
#         print(f"{elev['nume']} {elev['prenume']}")
        
# def sterge_elevi():
#     nume = input("Ce nume vrei elimini ? ")
#     prenume = input("Ce prenume vrei sa elimini ?")
#     for elev in elevi :
#         if elev["nume"] == nume and elev["prenume"] == prenume:
#             elevi.remove(elev)
#             print("Am sters")
#             return
#     print("Elevul nu a fost gasit")

# def modificare ():
#     nume = input("Ce nume sa modific : ")
#     prenume = input("Ce prenume sa modific : ")
#     for elev in elevi: 
#         if elev['nume'] == nume and elev['prenume'] == prenume:
#             elev['nota romana'] = float(input("Nota roamana noua: "))
#             elev['nota mate'] = float(input("Nota mate noua: "))
#             elev['nota engleza'] = float(input("Nota engleza noua: "))
#             elev['media'] = calculeaza_media(elev['nota romana'], elev['nota mate'], elev['nota engleza'])
#             print("Date modificate success!")
#             return
#     print("Elev negasit!")

# def cauta_elevi():
#     nume = input("Ce nume vrei ? ")
#     prenume = input("Ce prenume vrei ?")
#     for elev in elevi :
#         if elev["nume"] == nume and elev["prenume"] == prenume:
#             print(f"{elev['nume']} {elev['prenume']} | "
#             f"Romana: {elev['nota romana']} | "
#             f"Matematica: {elev['nota mate']} | "
#             f"Engleza: {elev['nota engleza']} | "
#             f"Media: {elev['media']}")
#             return
#     print("Elevul nu a fost gasit")

# def afiseaza_media_crescator():
#     elevi_sortati = sorted(elevi, key=ia_media)
#     for elev in elevi_sortati:
#         print(f"{elev['nume']} {elev['prenume']} | Media: {elev['media']}")

# def medie_5 ():
#     for elev in elevi :
#         if elev['media'] >= 5:
#             print(f"{elev['nume']} {elev['prenume']} | Media: {elev['media']}")
            
# while True :
#     optiune = input("Alege optiune : ")
#     if optiune == '0' :
#         print("Ai iesit din sistem")
#         break
#     if optiune == "1" :
#         adauga_elev()
#     if optiune == "2" :
#         afiseaza_elevi()
#     if optiune == "3" :
#         modificare()
#     if optiune == "4":
#         sterge_elevi()
#     if optiune == "5":
#         cauta_elevi()
#     if optiune == "6":
#         afiseaza_media_crescator()
#     if optiune == "7":
#         medie_5()
#     if optiune == "8":
#         afisare_alfabetic()









#09.02.2026

# import random

# def calcul():
#     a = random.randint(1,5)
#     b = random.randint(1,5)
#     return a + b
# print(calcul())

# from random import randint

# def calcul():
#     a = randint(1,5)
#     b = randint(1,5)
#     return a + b

# print(calcul())



# import SystemError
# def afiseaza nume(nume, prenume):
#     print(f'Nume: {nume}, Prenume: {prenume}')

# def main():
#     print(sys.argv)
#     afiseaza_nume(sys.argv[1], sys.argv[2])

# if __name__ == '__main__':
#     main()


# import argparse
# def par_arguments():
#      my_parser = argparse.ArgumentParser(description='Afiseaza nume frumos')
#      my_parser.add_argument('--name', type=str, help='Nume de familie')
#      my_parser.add_argument('--prenume', type=str, help='Prenumele omului')

# args = my_parser.parse_args()
# return args.name, args.prenume

# def main():
#      nume, prenume = parse.arguments()
#      print(f'print: {args.nume}, Prenume: {args.prenume}')


# if __name__ == '__main__':
#      main()