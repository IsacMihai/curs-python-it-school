'''
Object Oriented Programming - OOP
'''
'''
Tipuri de programare:
    - Procedurala -> se bazeaza pe executarea secventiala a instructiunilor, folosind functii pentru a organiza codul
        * Programul este o listă de instrucțiuni
        * Se folosesc variabile care se modifică
        * Flux clar, de sus în jos

        - Util pentru programe simple, scripturi, dar devine dificil de gestionat pe măsură ce programul crește în complexitate

    - Orientata pe obiecte (OOP) -> se bazeaza pe organizarea codului in jurul obiectelor si interactiunii dintre ele
        * Programul este o colecție de obiecte care interacționează între ele
        * Flux mai flexibil, bazat pe interacțiunea dintre obiecte

        - Util pentru programe complexe, aplicații mari, dar poate fi excesiv pentru programe simple

        Avantaje OOP (pentru aplicatii mari):
            - Reutilizarea codului
            - Organizare mai buna a codului
            - Mai usor de inteles si de mentinut (in cazul aplicatiilor mari)
            - Scalabilitate

OOP = modelam lucruri din lumea reala in cod, folosind clase si obiecte

* Clasa  - template / blueprint pentru crearea obiectelor
* Obiect - un element de tipul clasei respective (instanta a unei clase)

Analogie:
    Forma de buiscuit -> Clasa
    Buiscuitul propriu-zis -> Obiect

    Proiectul de casa -> Clasa
    Casa construita -> Obiect

class - cuvantul cheie pentru a defini o clasa in Python
numele clasei - incepe cu litera mare, iar daca avem mai multe cuvinte fiecare incepe cu litera mare (CamelCase)

Sintaxa:
# Definirea unei clase
    class NumeClasa:
        cod pentru clasa

# Crearea unui obiect (instanta) al clasei
    obiect = NumeClasa()

Componentele unei clase:
    - Atribute (proprietati) - caracteristici ale clasei / campuri de date

    - Metoda speciala __init__ - constructorul clasei, care initializeaza atributele obiectului
        ! Se apeleaza automat atunci cand se creeaza un obiect al clasei

    - Cuvantul cheie "self" se refera la instanta curenta a clasei si este folosit pentru a accesa
      atributele si metodele clasei

    - Metode (functii) - comportamente ale clasei / actiuni pe care le poate efectua clasa
        ! Se apeleaza folosind obiect.metoda()

Accesarea atributelor si metodelor:
    - Pentru a accesa un atribut sau o metoda a unui obiect, folosim sintaxa:
        obiect.nume_atribut
        obiect.nume_metoda()
'''

# numar = 7
# lista = [1,2,3]
# my_string = 'ceva'

# print(type(numar))
# print(type(lista))
# print(type(my_string))

# class Persoana:
#     pass

# obiect = Persoana()

# print(type(obiect))

# ClasaMea - obj1
# class ClasaMea:
#     pass

# obj1 = ClasaMea()
# print(type(obj1))

# Persoana - Nume Prenume CNP
# {
#     'nume': 'Neamtiu',
#     'prenume': 'Daniel',
#     'cnp': '123345'
# }

# class Persoana:
#     def __init__(self, nume, prenume, cnp):
#         self.nume = nume
#         self.prenume = prenume
#         self.cnp = cnp

# persoana1 = Persoana('Neamtiu', 'Daniel', '123345')
# persoana2 = Persoana('Popescu', 'Marian', '246321')

# print(type(persoana1))
# print(type(persoana2))

# print(persoana1.nume)
# print(persoana2.nume)

# print(persoana1.cnp)
# print(persoana2.cnp)

# persoana2.nume = 'Ionescu'
# print(persoana1.nume)
# print(persoana2.nume)

# print(persoana1.__dict__)
# print(persoana2.__dict__)

# class Masina:
#     def porneste(self):
#         print("I-am dat cheie")

# masina = Masina()
# masina.porneste()

# class Masina:
#     def __init__(self, model):
#         self.model = model

#     def porneste(self):
#         print(f'I-am dat cheie la {self.model}')

# masina = Masina('BMW')
# masin2 = Masina('Trabant')
# masina3 = Masina('Toyota')
# masina.porneste()
# masin2.porneste()
# masina3.porneste()

# Creati o clasa elev - nume, prenume, nota_romana, nota_matemtica, nota_engleza
# Elev - sa se prezinte
#      - isi zice notele
#      - isi zice media notelor


# class Elev:
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
#         self.nume = nume
#         self.prenume = prenume
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate
#         self.nota_engleza = nota_engleza
#         self.medie = self.calcul()

#     def prezentare(self):
#         print(f'Salut! Ma numesc {self.nume} {self.prenume}.')

#     def prezinta_note(self):
#         print(f'Notele mele sunt romana : {self.nota_romana} mate : {self.nota_mate} engleza : {self.nota_engleza}')

#     def prezinta_media(self):
#         media = (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
#         print(f'Media mea este: {media}')

# elev1 = Elev('Ionescu', 'Marius', 8, 9, 10)
# elev2 = Elev('Popescu', 'Marinel', 5, 5, 5)
# elev3 = Elev('Neamtiu', 'Ioana', 7, 8, 8)

# elev1.prezentare()
# elev2.prezinta_note()
# elev3.prezinta_media()

# Sa se citeasca de la tastatura elevi pana se introduce caracterul 'x'
# Pentru fiecare elev trebuie sa il punem sa se prezinte, sa isi zica notele si isi zica media

# class Elev():
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
#         self.nume = nume
#         self.prenume = prenume
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate
#         self.nota_engleza = nota_engleza

#     def prezentare(self):
#         print(f'Salut! Ma numesc {self.nume} {self.prenume}')

#     def note(self):
#         print(f'Notele mele sunt: {self.nota_romana}, {self.nota_mate}, {self.nota_engleza}')

#     def medie(self):
#         media = (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
#         print(f'Media mea este {media}')

# lista_elevi = []

# while True:
#     nume = input("Baga nume: ")
#     if nume == "x":
#         break
#     prenume = input("Baga prenume: ")
#     rom = int(input(" baga nota rom"))
#     mate = int(input(" baga nota mate"))
#     engl = int(input(" baga nota engl"))

#     elev = Elev(nume, prenume, rom, mate, engl)
#     lista_elevi.append(elev)

# for elem in lista_elevi:
#     elem.prezentare()
#     elem.note()
#     elem.medie()


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2*(self.length + self.width)

# dreptunghi = Rectangle(10, 8)
# print(f'Dreptunghiul are aria de {dreptunghi.area()} si perimetrul de {dreptunghi.perimeter()}')


# class Elev:
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
#         self.nume = nume
#         self.prenume = prenume
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate
#         self.nota_engleza = nota_engleza
#         self.medie = self.calcul()

#     def prezentare(self):
#         print(f'Salut! Ma numesc {self.nume} {self.prenume}.')

#     def prezinta_note(self):
#         print(f'Notele mele sunt romana : {self.nota_romana} mate : {self.nota_mate} engleza : {self.nota_engleza}')

#     def prezinta_media(self):
#         media = (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
#         print(f'Media mea este: {media}')

#     def calcul(self):
#         return (self.nota_romana + self.nota_mate + self.nota_engleza) / 3


# elev1 = Elev('Ionescu', 'Marius', 8, 9, 10)
# print(elev1.calcul())
