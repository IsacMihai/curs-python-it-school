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

class Motor:
    def __init__(self, cai_putere, tip_combustibil, capacitate_cilindrica):
        self.cai_putere = cai_putere
        self.tip_combustibil = tip_combustibil
        self.capacitate_cilindrica = capacitate_cilindrica

    def start_engine(self):
        print('Engine started!')
        return True

    def detalii_motor(self):
        print(f'Motor pe {self.tip_combustibil}, cu capacitate cilindrica {self.capacitate_cilindrica} cm cubi, cu {self.cai_putere} cai putere.')


class Volan:
    def __init__(self, diametru, tip_material):
        self.diametru = diametru
        self.tip_material = tip_material

    def viraj_stanga(self):
        print('Vireaza stanga')

    def viraj_dreapta(self):
        print('Vireaza dreapta')


class Roti:
    def __init__(self, tip_material_jante, presiune):
        self.tip_material_jante = tip_material_jante
        self.presiune = presiune

    def check_presiune(self):
        if self.presiune > 2.2:
            print('Roata prea umflata')
            return False
        elif self.presiune < 1.8:
            print('Roata dezumflata')
            return False
        else:
            print('Presiune roata ok')
            return True


class Masina:
    def __init__(self, culoare, marca, motor, volan, roti):
        self.culoare = culoare
        self.marca = marca
        self.motor = motor
        self.volan = volan
        self.roti = roti

    def porneste_masina(self):
        if self.motor.start_engine() and self.roti.check_presiune():
            print('Masina e gata de drum!')
        else:
            print('Momentan deplasarea este imposibila: verificati motorul sau rotile')

    def deplasare_drapta(self):
        self.volan.viraj_dreapta()

    def deplasare_stanga(self):
        self.volan.viraj_stanga()


roata_model_1 = Roti('tabla', 2.0)
roata_model_2 = Roti('aliaj', 1.7)

volan_model_1 = Volan(20, 'piele')
volan_model_2 = Volan(18, 'textil')

motor_model_1 = Motor(135, 'benzina', 1.5)
motor_model_2 = Motor(160, 'diesel', 0.99)
motor_model_3 = Motor(90, 'benzina', 1.3)

masina_angelo = Masina('visinie', 'ford', motor_model_3, volan_model_2, roata_model_2)
masina_angelo.porneste_masina()
masina_angelo.roti = roata_model_1
masina_angelo.porneste_masina()
masina_angelo.deplasare_drapta()
masina_angelo.deplasare_stanga()

masina_angelo.motor.detalii_motor()

"Avem o clasa produs si o clasa comanda(cos cumparaturi), trb sa avem posibilitatea sa adaugam produse "
"in acea comanda si sa calculam costul total al comenzii"

class Produs :
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret
    def prezentare(self):
        print(f'Produsul este {self.nume} si are pretul de {self.pret} lei')

class Comanda :
    def __init__ (self):
        self.cos = []
    def adauga_produs (self, produs, cantitate):
        self.cos.extend([produs] * cantitate)
    def total (self):
        total = 0
        for produs in self.cos :
            total += produs.pret
        return f'Comanda are total : {total} lei'

produs1 = Produs('baterie', 6)
produs2 = Produs('ciocolata', 12)
produs3 = Produs('bere',9)
produs4 = Produs('tigari', 33)
produs5 = Produs('chips', 10)

comanda1 = Comanda()
comanda1.adauga_produs(produs1,2)
comanda1.adauga_produs(produs2,1)
comanda1.adauga_produs(produs3,3)
comanda1.adauga_produs(produs4,1)
comanda1.adauga_produs(produs5,2)

print(comanda1.total())
