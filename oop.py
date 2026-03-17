# Creati o clasa numita "Rectangle" care are atributele "length" si "width".
# # Adauga o metoda numita "area" care returneaza aria dreptunghiului, si o metoda numita
# # "perimeter" care returneaza perimetrul dreptunghiului.
# # Instantiaza un obiect al clasei Rectangle si afiseaza aria si perimetrul acestuia.




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




#Numele elev, notele romana mate eng
#toat smecheria asta se numeste 'name mangle'


# class Elev: 
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
#         self.nume = nume
#         self.prenume = prenume
#         self.nota_romana = nota_romana 
#         self.nota_mate = nota_mate
#         self.nota_engleza = nota_engleza
#         self.media = self.calcul_medie()

#     def prezinta_te(self):
#         print(f"Salut! Numele meu este {self.nume} {self.prenume}")

#     def spune_notele(self):
#         print(f"Notele mele sunt: roman: {self.nota_romana}, mate: {self.nota_mate}, engleza: {self.nota_engleza}")

#     def spune_media(self):
#         self.media = (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
#         print(f"Media mea generala este {self.media:.2f}")


#     def calcul_medie(self):
#         return (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
    
# elev1 = Elev("Ionescu", "Andrei", 8, 10, 9)



# elev1.prezinta_te()
# elev1.spune_notele()
# print(elev1.media)
# elev1.spune_media()
# print(elev1.media)

# #sau 

# print(elev1.calcul_medie)

# elev1 = elev{'Dan', 'Nicovala', 32, 10}
# elev2 = elev{'Bibi', 'Stan', 36, 7}
# #Peoblema cu profesoru

# class Profesor (Persoana):
#     def __init__(self, nume, prenume, varsta, materie ):
#         super().__init__(nume, prenume, varsta)
#         self.materie = materie
#     def prezentare(self):
#         print(f'Eu sunt profesorul {self.nume} {self.prenume}, am varsta {self.varsta} si predau {self.materie} ! ')

# profesor1 = Profesor('Marinescu', 'Ionel', 55, 'spaniola')
# profesor2 = Profesor('Andreescu', 'Angelo', 45, 'etichal')

# lista_scoala = [elev1, elev2, profesor1, profesor2]

# for elem in lista_scoala :
#     elem.prezentare()

# class Profesor (Persoana):
#     def __init__(self, nume, prenume, varsta, materie ):
#         super().__init__(nume, prenume, varsta)
#         self.materie = materie
#     def prezentare(self):
#         print(f'Eu sunt profesorul {self.nume} {self.prenume}, am varsta {self.varsta} si predau {self.materie} ! ')

# profesor1 = Profesor('Marinescu', 'Ionel', 55, 'spaniola')
# profesor2 = Profesor('Andreescu', 'Angelo', 45, 'etichal')

# lista_scoala = [elev1, elev2, profesor1, profesor2]

# for elem in lista_scoala :
#     elem.prezentare()




#programul final cu toate modificările :
#'''# Mostenire si polimorfism ----------------------------------------'''

class Persoana :
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
    def prezentare (self):
        print(f'Numele meu este {self.nume} {self.prenume} si am {self.varsta} ani !')

persoana1 = Persoana('Abesei', 'Paul', 72)
persoana2 = Persoana('Popescu','Ana', 27)

persoana1.prezentare()
persoana2.prezentare()

# Elev - nume, prenume, varsta, nota_rom, nota_mate
class Elev(Persoana):
    def __init__ (self, nume, prenume, varsta, nota_rom, nota_mate):
        super().__init__(nume, prenume, varsta)
        self.nota_rom = nota_rom
        self.nota_mate = nota_mate

    def prezentare(self): # daca vreau sa suprascriu prezentarea din clasa Persoana
        super().prezentare()
        print(f'Am urmatoarele note: \n Romana : {self.nota_rom} \n Matematica : {self.nota_mate}')

    def afiseaza_note (self):
        print(f'Notele mele sunt : romana : {self.nota_rom} si mate : {self.nota_mate}')
    
    def media (self):
        return sum([self.nota_rom, self.nota_mate]) /2

class ElevLiceu(Elev):
    def __init__(self, nume, prenume, varsta, nota_rom, nota_mate, diriginte ):
        super().__init__(nume, prenume,varsta, nota_rom, nota_mate)
        self.diriginte = diriginte
    def get_diriginte(self):
        print ( f'Dirigintele meu este {self.diriginte}' )
    def __str__(self):
        return f'{self.nume} {self.prenume}'

elev1 = Elev('Neamtiu', 'Daniel', 27, 10, 10)
elev2 = Elev('Abesei', 'Paul', 31, 8, 9)
elev1.prezentare() # apelez prezentarea din clasa 'mama' - Persoana
elev1.afiseaza_note()

lista_oameni = [persoana1, persoana2, elev1]

for om in lista_oameni :
    om.prezentare()

class Profesor (Persoana):
    def __init__(self, nume, prenume, varsta, materie ):
        super().__init__(nume, prenume, varsta)
        self._materie = materie
    def prezentare(self):
        print(f'Eu sunt profesorul {self.nume} {self.prenume}, am varsta {self.varsta} si predau {self.materie} ! ')
    def __str__(self):
        return f'{self.nume} {self.prenume}'
    def get_materie(self):
        return self._materie

profesor1 = Profesor('Marinescu', 'Ionel', 55, 'spaniola')
profesor2 = Profesor('Andreescu', 'Angelo', 45, 'etichal')

elev_liceu1 = ElevLiceu('Antonescu', 'Maria',15, 7,8,profesor1)
elev_liceu2 = ElevLiceu('Parvulescu', 'Alexandru', 16, 9,9,profesor2)

lista_scoala = [elev1, elev2, profesor1, profesor2, elev_liceu1, elev_liceu2]

for elem in lista_scoala :
    elem.prezentare()

elev_liceu1.get_diriginte()

# Ce materie prezinta profesorul ce le este diriginte la : elev_liveu1 si 2
print(f'Digigintele lui {elev_liceu1} preda {elev_liceu1.diriginte.get_materie()}')

elev_liceu1.diriginte.materie = "Germana"

print(f'Digigintele lui {elev_liceu1} preda {elev_liceu1.diriginte.get_materie()}')

print(profesor1.materie)
print(profesor1._materie)