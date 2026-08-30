'''
Logging, assertions and tracebacks in Python
'''
'''
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
'''
'''
2. Assertions
    - Un assertion este o declarație care verifică dacă o condiție este adevărată
    - Dacă condiția este falsă, se ridică o excepție AssertionError
    - Se folosește pentru a detecta erori în timpul dezvoltării

    Sintaxă:
        assert conditie, "Mesaj de eroare optional"

    Exemplu:
        assert x > 0, "x trebuie să fie pozitiv"
'''
'''
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


import logging
# name = 'Ionut'
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')
# logging.debug(f'Acesta este un mesaj de debug generat de {name}')
# logging.info('Acesta este un mesaj de tip INFO')
# logging.critical('Acesta este un mesaj critic')
# logging.warning('Acesta esta un warning')
# logging.error('error message')

# logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug(f'Acesta este un mesaj de debug generat de {name}')
# logging.info('Acesta este un mesaj de tip INFO')
# logging.critical('Acesta este un mesaj critic')
# logging.warning('Acesta esta un warning')
# logging.error('error message')

# Se citesc 2 numere de la tastatura si calculeaza suma lor.
# Programul ruleaza pana la introducerea tastei x


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def aduna(nr1, nr2):
#     try:
#         suma = int(nr1) + int(nr2)
#     except ValueError:
#         logging.error('Unul dintre numere nu este integer! Introduceti doua numere valide')
#     else:
#         return suma


# logging.info('Application started')
# while True:
#     nr1 = input('Baga nr1: ')
#     nr2 = input('Baga nr2: ')
#     logging.debug(f'Numerele introduse sunt: {nr1} si {nr2}')
#     if nr1 == 'x' or nr2 == 'x':
#         break

#     print(aduna(nr1, nr2))

# logging.info('Application closed')
# name = 'Maria'
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug(f'Acesta este un mesaj de debug generat de {name}')
# logging.info('Acesta este un mesaj de tip INFO')
# logging.critical('Acesta este un mesaj critic')
# logging.warning('Acesta esta un warning')
# logging.error('error message')

# Avem o lista cu elemente [10, -5, 5, 12, 20, 30, -6]

# logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def data_processor(lista):
#     logging.info('Incepere procesare')
#     for index, value in enumerate(lista):
#         if value < 0:
#             logging.warning(f'Valoare negativa {value} la pozitia {index}')
#         else:
#             logging.debug(f'Valoare citita: {value} la pozitia {index}')
#             processing_result = value / 2
#             print(f'Processed result: {processing_result}')
#             logging.debug(f'Processing result: {processing_result}')

#     logging.info('Procesare finalizata')

# date = [10, -5, 5, 12, 20, 30, -6]
# data_processor(date)


# logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def data_processor(lista):
#     logging.info('Incepere procesare')
#     for index, value in enumerate(lista):
#         if value < 0:
#             logging.warning(f'Valoare negativa {value} la pozitia {index}')

#         assert value > 0, f'Frate, s-au citit ceva valori eronate {index} - {value}'
#         logging.debug(f'Valoare citita: {value} la pozitia {index}')
#         processing_result = value / 2
#         print(f'Processed result: {processing_result}')
#         logging.debug(f'Processing result: {processing_result}')

#     logging.info('Procesare finalizata')

# date = [10, -5, 5, 12, 20, 30, -6]
# data_processor(date)

# import math

# def calcul_logaritm(x):
#     assert x > 0, f'Numarul introdus trebuie sa fie pozitiv (valoarea introdusa: {x})'
#     logaritm = math.log(x)
#     return logaritm

# print(calcul_logaritm(10))
# print(calcul_logaritm(-1))

# print(10 / 0)

# try:
#     print(10 / 0)
# except Exception as exceptie:
#     print(exceptie)

import traceback

# while True:
#     x = input('Baga numar: ')
#     if x == 'x':
#         break

#     try:
#         print(10 / int(x))
#     except Exception as exceptie:
#         print('A aparut o eraore la impartire!')
#         traceback.print_exc()
#         print(f'Exceptia aparuta este: {exceptie}')

# def functia_a(x):
#     return functie_b(x)

# def functie_b(y):
#     return functie_c(y)

# def functie_c(z):
#     return 10 / z


# while True:
#     x = input('Baga numar: ')
#     if x == 'x':
#         break

#     try:
#         rezultat = functia_a(int(x))
#     except Exception as exceptie:
#         print('A aparut o eraore la apelarea functiei a!')
#         traceback.print_exc()
#         print(f'Exceptia aparuta este: {exceptie}')
#     else:
#         print(rezultat)
