'''
OOP - Composition

Composition - o relatie "has-a" intre clase, unde o clasa contine obiecte altor clase ca parte a sa
    Analogie:
        - O masina are un motor, un volan, roti, etc. (Masina "has-a" Motor, Volan, Roti)
        - Un telefon mobil are un ecran, o baterie, un procesor, etc. (Telefon "has-a" Ecran, Baterie, Procesor)

    Sintaxa:
        class ClasaPrincipala:
            def __init__(self, componenta):
                self.componenta = componenta

        class Componenta:
            def __init__(self, atribut):
                self.atribut = atribut

Composition VS Inheritance
    - Composition este preferata cand relatia este "has-a" (ex: Masina are Motor)
    - Inheritance este folosita cand relatia este "is-a" (ex: Caine este Animal)
'''

# Exemplu de composition:
class Engine:
    def __init__(self, horsepower, type = "gasoline"):
        self.horsepower = horsepower
        self.type = type

    def start(self):
        print(f"{self.type} engine with {self.horsepower} HP is starting.")

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  # Car "has-a" Engine

    def start_car(self):
        print(f"Starting the {self.brand} {self.model}.")
        self.engine.start()  # Delegating the start action to the Engine class

engine1 = Engine(150, "gasoline")
car1 = Car("Toyota", "Camry", engine1)
car1.start_car()

engine2 = Engine(200, "electric")
car2 = Car("Tesla", "Model 3", engine2)
car2.start_car()

# Exercitii:
# 1) Creati o clasa Engine care are metoda start() care afiseaza un mesaj de pornire a motorului.
# Creati o clasa Car care are atributele brand, model si engine (obiect de tip Engine). Adaugati o metoda
# start_car() care porneste masina folosind metoda start() a clasei Engine.
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is moving")


c = Car()
c.start()

# 2) Creati o clasa ElectricEngine si modificati tipul motorului detinut de clasa car pentru a fi un ElectricEngine.
# Apoi apelati metoda start() pentru a porni motorul electric.
class ElectricEngine:
    def start(self):
        print("Electric engine started")


c.engine = ElectricEngine()
c.start()

# 3) Creati o clasa Product cu atributele name si price. Creati o clasa Order care contine o lista de produse.
# Adaugati metode pentru a adauga produse si a calcula pretul total al comenzii.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)


p1 = Product("Laptop", 3000)
p2 = Product("Mouse", 100)

order = Order()
order.add_product(p1)
order.add_product(p2)

print(order.total_price())

# Exercitiu Final:
# Creati un sistem pentru gestionarea studentilor si cursurilor.
# Aveti o clasa Person cu atributele nume, varsta si gen.
# Avem o clasa Student care mosteneste Person si adauga atributele student_id si cursuri (o lista de cursuri).
# Avem o clasa Course cu atributele course_name si grade. Fiecare curs are metoda get_grade() care returneaza nota cursului.
# Studentul are o metoda add_course() pentru a adauga un curs la lista sa de cursuri, si o metoda calculate_average() care calculeaza media notelor pentru toate cursurile studentului.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Course:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_final_grade(self):
        return self.grade


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def average(self):
        return sum(c.get_final_grade() for c in self.courses) / len(self.courses)


s = Student("Ana", 20, "Female", "S12345")
s.add_course(Course("Math", 9))
s.add_course(Course("Physics", 7))

print(s.average())
