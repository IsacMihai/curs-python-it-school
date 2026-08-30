'''
Funcții în Python

Functie = un bloc de cod reutilizabil care efectuează o anumită sarcină

1. Definirea și apelarea funcțiilor
    - Se folosește cuvântul cheie def

    - O funcție poate avea parametri și poate returna o valoare cu "return"
'''

'''
2. Parametri și argumente
    - Parametri: variabilele din definiția funcției

    - Argumente: valorile transmise la apel

    - Parametri cu valoare implicită
'''

'''
3. Returnarea valorilor
    - O funcție poate returna orice tip de valoare (sau nimic)

    - Se poate returna mai multe valori folosind tuple
'''

'''
4. Scope (domeniul de vizibilitate)
    - Variabilele definite în interiorul funcției nu sunt vizibile în afara ei (scope local)

    - Variabilele definite în afara funcției sunt globale
        - Se poate folosi cuvântul cheie "global" pentru a modifica o
          variabilă globală din interiorul unei funcții
'''

'''
5. Funcții fără parametri sau fără return
    - O funcție poate să nu aibă parametri
    - O funcție poate să nu returneze nicio valoare
'''

'''
6. Funcții ca parametri (funcții de ordin înalt)
    - Funcțiile pot fi transmise ca argumente către alte funcții
    - Exemplu: funcția map(), filter(), reduce()
'''

'''
7. Keyword arguments

    - Keyword arguments: argumente transmise explicit după nume, indiferent de poziție.

    Reguli:
        1) Argumentele poziționale (positional arguments) trebuie să apară înaintea celor numite (keyword arguments)
           si sa fie transmise in ordinea parametrilor din definitia functiei.

        2) Un parametru poate sa primeasca o singura valoare (fie pozitionala, fie numita).

        3) Parametrii cu valoare implicita (default parameters) trebuie sa fie ultimii in definitia functiei.
'''

'''
8. Funcții recursive
    - O funcție care se apelează pe ea însăși pentru a rezolva o problemă
    - Trebuie să aibă o condiție de oprire pentru a evita apelurile infinite
'''

'''
9. Argumente variabile ca numar - *args și **kwargs

    - *args: permite transmiterea unui număr variabil de argumente poziționale (accesibile ca tuplu).

    - **kwargs: permite transmiterea unui număr variabil de argumente numite (accesibile ca dicționar).

    Reguli:
        -> *args trebuie sa fie plasat dupa parametrii pozitionali si sa apara inaintea lui **kwargs in definitia functiei.

        -> La apelarea functiei se pot combina argumente pozitionale, keyword arguments, *args si **kwargs respectand ordinea:
              - Argumentele pozitionale
              - Argumentele numite (keyword arguments)
              - Valorile din *args
              - Valorile din **kwargs

            Exemplu apelare functie:
                functie(1, 2, nume='Ana', varsta=30, *alte_valori, **alte_perechi)
'''

# Exemple practice functii:

# Exemplu simplu de funcție fără parametri și fără return
def salut():
    print('Salut!')

salut()

# Exemplu de funcție cu parametri și return
def aduna(a, b):
    return a + b

rezultat = aduna(3, 4)
print(rezultat)

# Exemplu de funcție cu parametri cu valoare implicită
def salut_nume(nume='Anonim'):
    print(f'Salut, {nume}!')

salut_nume('Maria')
salut_nume()

# Exemplu returnarea mai multor valori
def operatii(a, b):
    suma = a + b
    diferenta = a - b
    return suma, diferenta

s, d = operatii(10, 4)
print('Suma:', s)
print('Diferenta:', d)

# Exemplu scope (domeniul de vizibilitate)
def demo_scope():
    mesaj = 'Salut din funcție!'
    print(mesaj)
demo_scope()
# print(mesaj)  # va da eroare

# Exemplu variabila globală
contor = 0
def incrementeaza_contor():
    global contor
    contor += 1

incrementeaza_contor()
print('Contor:', contor)

# Exemplu funcție fără parametri si fără return
def afiseaza_hello():
    print('Hello!')
afiseaza_hello()

# Exemplu funcție ca parametru
def aplica_functie(f, x):
    return f(x)

def dubleaza(n):
    return n * 2

print(aplica_functie(dubleaza, 5))

# Exemplu argumente transmise după nume (keyword arguments)
def descriere_persoana(nume, varsta, oras):
    print(f'{nume} are {varsta} ani și locuiește în {oras}.')

descriere_persoana(varsta=30, nume='Ana', oras='Cluj')  # argumente după nume

# Exemplu functie recursiva
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Exemplu functie recursiva parcurgere lista imbricata
def numara_element(lista, element):
    count = 0
    for item in lista:
        if isinstance(item, list):
            count += numara_element(item, element)
        elif item == element:
            count += 1
    return count

# Exemplu *args (numar variabil de argumente pozitionale)
def suma(*args):
    print('Argumente primite:', args)
    return sum(args)

print('Suma:', suma(1, 2, 3, 4))

# Exemplu **kwargs (numar variabil de argumente numite)
def afiseaza_date(**kwargs):
    print('Date primite:', kwargs)
    for cheie, valoare in kwargs.items():
        print(f'{cheie}: {valoare}')

afiseaza_date(nume='Ion', varsta=40, oras='Oradea')

# Exemplu combinare *args și **kwargs
def logare(*mesaje, **optiuni):
    nivel = optiuni.get('nivel', 'INFO')
    separator = optiuni.get('separator', ' ')
    mesaj_final = separator.join(str(m) for m in mesaje)
    print(f"[{nivel}] {mesaj_final}")

logare("Pornire program", "Utilizator: Ana", nivel="DEBUG")
# Output: [DEBUG] Pornire program Utilizator: Ana

logare("Eroare la conectare!", nivel="ERROR", separator=" | ")
# Output: [ERROR] Eroare la conectare!
