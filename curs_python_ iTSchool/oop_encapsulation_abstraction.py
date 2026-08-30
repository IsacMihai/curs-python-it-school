'''
OOP - Encapsulation si Abstraction + Special Methods
'''
'''
Encapsulation - ascunderea datelor interne ale unui obiect și accesarea lor controlată prin metode publice
    Analogie:
        - Stim ce face o capsula de medicamente, dar nu si ce contine sau cum functioneaza in interior
        - Putem sa conducem o masina fara sa stim toate componentele interne

    Tipuri de atribute in encapsulation:
        - Atribute publice - pot fi accesate si modificate direct din exteriorul clasei
        - Atribute protejate - pot fi accesate si modificate doar in interiorul clasei si in clasele derivate, sunt prefixate cu _ (un underscore)
        - Atribute private - nu pot fi accesate sau modificate direct din exteriorul clasei, sunt prefixate cu __ (doua underscore-uri)
'''
'''
Abstraction - ascunde complexitatea (detaliile de implementare) si expune doar functionalitatea esentiala a unei clase
    Analogie:
        - Folosim un telefon mobil pentru a face apeluri, trimite mesaje, naviga pe internet, etc., fara sa stim cum functioneaza in interior
        - Folosim un televizor pentru a viziona programe, fara sa stim cum functioneaza electronica din interior


Special Methods - metode predefinite in Python care au un comportament special si care pot fi suprascrise pentru a personaliza comportamentul
    - Exemple de metode speciale: __init__, __str__, __repr__, __len__, etc.
    - Aceste metode sunt apelate automat in anumite situatii, cum ar fi atunci cand se creeaza un obiect, cand se converteste un obiect la string, cand se afiseaza un obiect etc.

'''

# class Elev:
#     def __init__(self, nume, prenume, mate, romana, engleza):
#         self.nume = nume
#         self.prenume = prenume
#         self._mate = mate
#         self._romana = romana
#         self._engleza = engleza
#         self.__media = self._update_media()

#     def get_mate(self):
#         return self._mate

#     def set_mate(self, new_mate):
#         if self._validare_nota(new_mate):
#             self._mate = new_mate
#             self.__media = self._update_media()
#         else:
#             print('Nota trebuie sa fie cuprinsa intre 1 si 10')

#     def get_media(self):
#         return self.__media

#     def _update_media(self):
#         return round((self._mate + self._romana + self._engleza) / 3, 2)

#     def _validare_nota(self, new_nota):
#         if 0 < new_nota <= 10:
#             return True
#         else:
#             return False

# elev1 = Elev('Neamtiu', 'Daniel', 8, 9, 10, 9)
# print(elev1._mate)
# elev1._mate = 20
# print(elev1._mate)

# elev1 = Elev('Neamtiu', 'Daniel', 8, 9, 10)
# print(elev1.get_media())
# print(elev1.get_mate())
# elev1.set_mate(22)
# print(elev1.get_mate())
# elev1.set_mate(10)
# print(elev1.get_mate())
# print(elev1.get_media())

# class Ghiozdan:
#     def __init__(self, obiecte):
#         self.obiecte = obiecte

#     def __len__(self):
#         return len(self.obiecte)

#     def __str__(self):
#         return f"Ghiozdanul are urmatoarele obiecte {self.obiecte}"

#     def __repr__(self):
#         return f"Ghiozdan(obiecte='{self.obiecte}')"

# lista = [1, 2, 3, 4]
# print(len(lista))

# ghiozdan = Ghiozdan(lista)
# print(len(ghiozdan))
# x = str(ghiozdan)
# print(x)
# print(ghiozdan)

# lista_ghiozdane = [1, 2, {1:1, 2:2, 3:3}, Ghiozdan(lista), Ghiozdan([6, 5, 7, 6]), Ghiozdan([8, 9, 10, 6])]
# print(lista_ghiozdane)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person1 = Person("Alice", 30)
print(repr(person1))  # Person(name='Alice', age=30)
