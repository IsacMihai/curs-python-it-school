'''
Object Oriented Programming - OOP

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
            - Mai usor de inteles si de mentinut
            - Scalabilitate

OOP -> se bazeaza pe organizarea codului in jurul obiectelor si interactiunii dintre ele

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

# Exemplu clasa si obiect
class ClasaMea:
    pass

# Exemplu obiect de tipul clasei mele
obiect1 = ClasaMea()
print(type(obiect1))

# Exemplu concret - clasa si obiect
class Masina:
    pass

masina1 = Masina()
print(type(masina1))

# Exemplu clasa cu atribute
class Elev:
    def __init__(self, nume, prenume, medie):
        self.nume = nume
        self.prenume = prenume
        self.medie = medie

elev1 = Elev("Popescu", "Ion", 8.5)
print(elev1.nume)
print(elev1.prenume)
print(elev1.medie)

# Exemplu clasa cu atribute si metode
class Elev:
    def __init__(self, nume, prenume, medie):
        self.nume = nume
        self.prenume = prenume
        self.medie = medie

    def afiseaza_informatii(self):
        print(f"Nume: {self.nume}, Prenume: {self.prenume}, Medie: {self.medie}")

elev2 = Elev("Ionescu", "Maria", 9.2)
elev2.afiseaza_informatii()

# Exercitii:
# 1) Creați o clasă Book care să aibă atribute: title, author, pages,
# metodă describe() care afișează informațiile si constructor care inițializează atributele
# Instanțiați un obiect al clasei Book și apelați metoda describe() pentru a afișa informațiile despre carte.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")


b = Book("1984", "Orwell", 328)
b.describe()

# 2) Creati o clasa numita "Rectangle" care are atributele "length" si "width".
# Adauga o metoda numita "area" care returneaza aria dreptunghiului, si o metoda numita
# "perimeter" care returneaza perimetrul dreptunghiului.
# Instantiaza un obiect al clasei Rectangle si afiseaza aria si perimetrul acestuia.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(4, 5)
print(r.area())
print(r.perimeter())

# 3) Creati 3 obiecte Student cu atributele nume, nota si adauga o metoda numita "is_passing" care returneaza
# True daca nota este mai mare sau egala cu 5, si False in caz contrar. Adaugati-le intr-o lista si afisati
# numele studentilor care au trecut examenul (nota >= 5).
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 5


students = [
    Student("Ana", 8),
    Student("Ion", 4),
    Student("Maria", 6),
]

for s in students:
    if s.is_passing():
        print(s.name)
