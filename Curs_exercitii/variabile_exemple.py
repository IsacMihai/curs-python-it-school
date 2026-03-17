'''
Variabila - container pentru stocarea datelor / obiectelor

    * Orice element in Python este considerat un obiect

    * Python nu are o comanda specifica pentru a declara o
      variabila

    * O variabila este creeata in momentul in care ii asignam
      o valoare
'''
'''
Denumirea variabilelor:
    * Un nume de variabila poate sa contina doar caractere alfa numerice si bara-jos (A-Z, a-z, 0-9, _ )

    * Trebuie sa inceapa cu o litera sau cu caracterul “_” (bara-jos)

    * NU poate sa inceapa cu un numar

    * Nu poate contine spatii

    * Numele de variabile sunt “case-sensitive”
        - obiect, Obiect, OBIECT - sunt 3 variabile diferite

    * Un nume de “keyword” din Python NU poate fi folosit ca nume de variabila (def, class, if, else, import, etc)

    * Se recomanda folosirea literelor mici si _ pentru a separa cuvintele (Sanke Case)
      (nume_familie_daniel_neamtiu)

    * Alte conventii de denumire:
        - Camel Case (numeFamilieDanielNeamtiu)
        - Pascal Case (NumeFamilieDanielNeamtiu)
        - Upper Case (NEAMTIU_DANIEL)
'''
'''
Tipuri de variabile / obiecte uzuale in Python:
    * String - sir de caractere (text) - ex: 'Ana are mere', "Ana are mere"

    * Integer - numar intreg - ex: 3, 299, -45

    * Float - numar zecimal - ex: 2.5, 3.14, -0.99

    * Boolean - valoare logica - ex: True, False

    * NoneType - tip special care reprezinta absenta unei valori - ex: None



    - In Python NU este necesar sa declaram tipul variabilei

    - Tipul unei variabile se poate schimba in timp

    - Python este un limbaj case sensitive (var / Var - sunt doua variabile diferite)

    - Putem determina tipul unei variabile utilizand functia type()

    - Putem face conversie intre tipuri ("casting") de variabile utilizand functiile:
        str()   - conversie la string
        int()   - conversie la integer
        float() - conversie la float
        bool()  - conversie la boolean
'''

'''
Operatorul "=" - asignare valoare unei variabile

Functia print() - afisare pe ecran

Funtia input() - citire de la tastatura
'''

# Exemple practice pentru fiecare concept teoretic:

# 1. Crearea unei variabile (nu există o comandă specială, doar asignare):
nume = "Ana"
varsta = 25

# 2. Denumirea variabilelor:
nume_familie = "Popescu"  # corect
_nume = "Ion"             # corect
# 1nume = "Maria"         # incorect, începe cu cifră
# nume familie = "Vasile" # incorect, conține spațiu
OBIECT = "carte"
obiect = "pix"
Obiect = "stilou"
# def = "ceva"            # incorect, def e keyword

# 3. Tipuri de variabile:
text = "Ana are mere"      # String
numar_intreg = 10          # Integer
numar_zecimal = 3.14       # Float
valoare_logica = True      # Boolean
valoare_absenta = None     # NoneType

# 4. Tipul variabilei se poate schimba:
valoare = 5                # int
valoare = "cinci"         # devine string

# 5. Determinarea tipului variabilei:
print(type(text))          # <class 'str'>
print(type(numar_intreg))  # <class 'int'>

# 6. Conversii între tipuri (casting):
numar = "123"
numar_int = int(numar)     # conversie la int
numar_float = float(numar) # conversie la float
numar_str = str(numar_intreg) # conversie la string
valoare_bool = bool(0)     # False
valoare_bool2 = bool(1)    # True
