'''
Logging, assertions and tracebacks in Python

1. Logging
    -> modul logging
    - Logging-ul este procesul de înregistrare a evenimentelor care apar în timpul execuției unui program
    - Permite monitorizarea și depanarea aplicațiilor

    Sunt 5 nivele de logging:
        1) DEBUG    - Informatii detaliate pentru debug (util in timpu developmentului)
        2) INFO     - Informatii generale legate de evenimentele din timpul rularii (confirma ca lucrurile functioneaza corespunzator)
        3) WARNING  - Ceva neasteptat s-a intamplat, insa programul inca ruleaza
        4) ERROR    - O problema serioasa impiedica rularea unei bucati de cod
        5) CRITICAL - O eroare critica a aparut, iar programul nu mai poate sa isi continue executia

    Configurarea logging-ului:
    - Se poate configura logging-ul folosind funcția basicConfig()
    - Exemplu:  logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    Pentru afisarea mesajelor de logging:
    - logging.debug("Mesaj de debug")
    - logging.info("Mesaj informativ")
    - logging.warning("Mesaj de warning")
    - logging.error("Mesaj de eroare")
    - logging.critical("Mesaj critic")

    Placeholdere comune in format:
    - %(asctime)s - Timpul la care a fost inregistrat mesajul
    - %(levelname)s - Numele nivelului de logging (DEBUG, INFO, etc.)
    - %(message)s - Mesajul de logging propriu-zis
    - %(filename)s - Numele fisierului din care provine mesajul
    - %(lineno)d - Numarul liniei din cod unde a fost generat mesajul

    Pentru scrierea mesajelor de logging intr-un fisier:
    - logging.basicConfig(filename='app.log', level=logging.INFO)

2. Assertions
    - Un assertion este o declarație care verifică dacă o condiție este adevărată
    - Dacă condiția este falsă, se ridică o excepție AssertionError
    - Se folosește pentru a detecta erori în timpul dezvoltării

    Sintaxă:
        assert conditie, "Mesaj de eroare optional"

    Exemplu:
        assert x > 0, "x trebuie să fie pozitiv"

3. Tracebacks
    - Un traceback este o listă a apelurilor de funcții care au dus la o excepție
    - Este util pentru depanare, deoarece arată unde a apărut eroarea în cod
    - Traceback-urile sunt afișate automat când apare o excepție negestionată

    Modul traceback:
    - Permite manipularea și afișarea tracebacks
    - Exemplu:
        import traceback

        try:
            # cod care poate genera o excepție
        except Exception as e:
            traceback.print_exc()  # Afișează traceback-ul complet
'''

# Exemplu de utilizare a modulului logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("Acesta este un mesaj de debug")
logging.info("Acesta este un mesaj informativ")
logging.warning("Acesta este un mesaj de warning")
logging.error("Acesta este un mesaj de eroare")
logging.critical("Acesta este un mesaj critic")

# Exemplu practic utilizare logging in o functie
def imparte(a, b):
    logging.info(f'Împărțirea {a} la {b}')
    try:
        rezultat = a / b
    except ZeroDivisionError:
        logging.error("Împărțire la zero!")
        return None
    else:
        logging.info(f'Rezultatul este {rezultat}')
        return rezultat

imparte(10, 2)
imparte(10, 0)

# Exemplu practic utilizare logging intr-un program mai complex
def procesare_date(date):
    logging.info("Încep procesarea datelor")
    for i, valoare in enumerate(date):
        logging.debug(f'Procesarea valorii {valoare} la indexul {i}')
        if valoare < 0:
            logging.warning(f'Valoare negativă detectată: {valoare}')
        # Simulare procesare
        rezultat = valoare * 2
        logging.debug(f'Rezultatul procesării: {rezultat}')
    logging.info("Procesarea datelor s-a încheiat")

date_exemplu = [10, -5, 3, 0, 7]
procesare_date(date_exemplu)

# Exemplu practic logging intr-un fisier intr-o aplicatie cu functii multiple
logging.basicConfig(filename='aplicatie.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def citeste_date():
    logging.info("Citirea datelor")
    # Simulare citire date
    date = [1, 2, 3, 4, 5]
    logging.debug(f'Date citite: {date}')
    return date

def prelucreaza_date(date):
    logging.info("Prelucrarea datelor")
    prelucrate = [x * 10 for x in date]
    logging.debug(f'Date prelucrate: {prelucrate}')
    return prelucrate

def salveaza_date(date):
    logging.info("Salvarea datelor")
    # Simulare salvare date
    logging.debug(f'Date salvate: {date}')
    return True

date = citeste_date()
date_prelucrate = prelucreaza_date(date)
salveaza_date(date_prelucrate)

# Exemplu practic sistem de autentificare cu logging in fisier
import logging
logging.basicConfig(filename='autentificare.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Predefined user database (username: password)
users = {
    "alice": "password123",
    "bob": "qwerty",
    "charlie": "letmein"
}

# Track failed attempts per user
failed_attempts = {}
while True:
    username = input("Enter your username: ")
    if username not in users:
        logging.warning(f"Attempted login with non-existent username: {username}")
        print("User not found. Try again.\n")
        continue
    if failed_attempts.get(username, 0) >= 3:
        logging.error(f"User {username} is blocked due to multiple failed attempts.")
        print("Your account is blocked due to too many failed login attempts.\n")
        continue
    password = input("Enter your password: ")
    if users[username] == password:
        logging.info(f"User {username} successfully logged in.")
        print("Login successful!\n")
        break
    else:
        logging.error(f"Failed login attempt for user {username}")
        failed_attempts[username] = failed_attempts.get(username, 0) + 1
        print("Incorrect password. Try again.\n")
print("Exiting authentication system.")


# Exemplu de utilizare a assertions
def calculeaza_radical(x):
    assert x >= 0, "x trebuie să fie pozitiv"
    return x ** 0.5

print(calculeaza_radical(9))  # Output: 3.0
# print(calculeaza_radical(-4))  # Va ridica AssertionError

import math
def calculeaza_logaritm(x):
    assert x > 0, "x trebuie să fie mai mare decât zero"
    return math.log(x)
print(calculeaza_logaritm(10))  # Output: 2.302585092994046
# print(calculeaza_logaritm(0))  # Va ridica AssertionError

# Exemplu de utilizare a tracebacks
import traceback

def imparte(a, b):
    return a / b

try:
    rezultat = imparte(10, 0) # Va ridica ZeroDivisionError
except Exception as e:
    print("A apărut o eroare:")
    traceback.print_exc()
    print(f"Eroare detaliată: {e}") # Afișează mesajul erorii

# Exemplu practic traceback intr-un program cu mai multe functii
import traceback
def functie_a(x):
    return functie_b(x)
def functie_b(y):
    return functie_c(y)
def functie_c(z):
    return 10 / z

try:
    rezultat = functie_a(0)  # Va ridica ZeroDivisionError
except Exception as e:
    print("A apărut o eroare în lanțul de funcții:")
    traceback.print_exc()
    print(f"Eroare detaliată: {e}")  # Afișează mesajul erorii
