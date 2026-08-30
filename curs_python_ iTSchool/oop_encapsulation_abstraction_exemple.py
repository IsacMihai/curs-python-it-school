'''
OOP - Encapsulation si Abstraction + Special Methods

Encapsulation - ascunderea datelor interne ale unui obiect și accesarea lor controlată prin metode publice
    Analogie:
        - Stim ce face o capsula de medicamente, dar nu si ce contine sau cum functioneaza in interior
        - Putem sa conducem o masina fara sa stim toate componentele interne

    Tipuri de atribute in encapsulation:
        - Atribute publice - pot fi accesate si modificate direct din exteriorul clasei
        - Atribute protejate - pot fi accesate si modificate doar in interiorul clasei si in clasele derivate, sunt prefixate cu _ (un underscore)
        - Atribute private - nu pot fi accesate sau modificate direct din exteriorul clasei, sunt prefixate cu __ (doua underscore-uri)


Abstraction - ascunde complexitatea (detaliile de implementare) si expune doar functionalitatea esentiala a unei clase
    Analogie:
        - Folosim un telefon mobil pentru a face apeluri, trimite mesaje, naviga pe internet, etc., fara sa stim cum functioneaza in interior
        - Folosim un televizor pentru a viziona programe, fara sa stim cum functioneaza electronica din interior


Special Methods - metode predefinite in Python care au un comportament special si care pot fi suprascrise pentru a personaliza comportamentul
    - Exemple de metode speciale: __init__, __str__, __repr__, __len__, etc.
    - Aceste metode sunt apelate automat in anumite situatii, cum ar fi atunci cand se creeaza un obiect, cand se converteste un obiect la string, cand se afiseaza un obiect etc.

'''

# Exemplu de encapsulation:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public (ok de citit)
        self._currency = "RON"      # protected (intern)
        self.__balance = balance    # private (critic)

    def display_balance(self):
        print(f"Sold: {self.__balance} {self._currency}")

    def deposit(self, amount):
        if amount <= 0:
            print("Suma invalida!")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Fonduri insuficiente!")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Exemplu de abstraction:
class CoffeeMachine:
    def __init__(self):
        self.__water_level = 100
        self.__coffee_level = 100

    def make_coffee(self):
        if self.__water_level >= 10 and self.__coffee_level >= 10:
            self.__water_level -= 10
            self.__coffee_level -= 10
            print("Coffee made!")
        else:
            print("Not enough water or coffee!")


# Exemplu de metode speciale - __str__:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person1 = Person("Alice", 30)
print(person1)  # Alice, 30 years old


# Exemplu de metode speciale - __repr__:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person1 = Person("Alice", 30)
print(repr(person1))  # Person(name='Alice', age=30)


# Exemplu de metode speciale - __len__:
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))  # 3

# Exercitii:
# Creati o clasa User care are atributele username, _age(protected).
# Adauga un setter pentru a seta varsta utilizatorului, care sa verifice daca varsta este un numar pozitiv.
class User:
    def __init__(self, username, age):
        self.username = username
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


u = User("ana", 20)
u.set_age(25)
print(u.get_age())

# Creati o clasa Car cu metoda publica start() si metodata protected _check_engine() care verifica daca motorul este in stare buna.
# Metoda start() ar trebui sa apeleze metoda _check_engine() inainte de a porni masina.
class Car:
    def start(self):
        self._check_engine()
        print("Car started")

    def _check_engine(self):
        print("Engine OK")


c = Car()
c.start()
