'''
Exception Handling in Python

1. Ce este o excepție?
    - O excepție este o eroare care apare în timpul execuției unui program
    - Exemple comune: ZeroDivisionError, ValueError, TypeError, FileNotFoundError
'''
'''
2. Blocul try-except
    - Permite gestionarea excepțiilor pentru a preveni oprirea neașteptată a programului
    - Sintaxă:
        try:
            # cod care poate genera o excepție
        except NumeExceptie:
            # cod pentru gestionarea excepției
        except AltaExceptie as e:
            # cod pentru gestionarea alteia, e conține detalii despre excepție
        else:
            # cod care se execută dacă nu a apărut nicio excepție
        finally:
            # cod care se execută întotdeauna, indiferent dacă a apărut o excepție sau nu
'''
'''
3. Ridicarea excepțiilor
    - Se poate ridica o excepție manual folosind cuvântul cheie raise
    - Exemplu:
        raise ValueError("Mesaj de eroare personalizat")
'''
'''
Optional:
4. Crearea de excepții personalizate
    - Se poate crea o clasă care moștenește din clasa Exception
    - Exemplu:
        class MyCustomError(Exception):
            print("Aceasta este o excepție personalizată")

5. Utilizarea excepțiilor personalizate
    - Se poate folosi excepția personalizată în blocuri try-except
    - Exemplu:
        try:
            raise MyCustomError("Eroare personalizată apărută")
        except MyCustomError as e:
            print(e)
'''

# Exemplu de utilizare a blocului try-except
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Eroare: Împărțire la zero!")
        return None
    except TypeError as e:
        print("Eroare: Tipuri de date invalide!")
        return None
    else:
        print("Împărțirea a avut succes.")
        return result
    finally:
        print("Execuția blocului try-except s-a încheiat.")

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Eroare: Împărțire la zero!
print(divide(10, 'a'))  # Output: Eroare: Tipuri de date invalide!

# Exemplu practic try-except
file_path = 'non_existent_file.txt'
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Eroare: Fișierul '{file_path}' nu a fost găsit.")
    print(f"Detalii eroare: {e}")

# Exemplu de ridicare a unei excepții
def verifica_varsta(varsta):
    if varsta < 0:
        raise ValueError("Vârsta nu poate fi negativă!")
    elif varsta < 18:
        print("Minor")
    else:
        print("Adult")

try:
    verifica_varsta(-5) # Va ridica ValueError
except ValueError as e:
    print(f"Eroare: {e}")


# Exemplu de utilizare a blocului else și finally
def citeste_numar():
    try:
        numar = int(input("Introdu un număr întreg: "))
    except ValueError as e:
        print(f"Eroare: Nu ai introdus un număr întreg valid. Detalii: {e}")
    else:
        print(f"Ai introdus numărul: {numar}")
    finally:
        print("Mulțumim pentru utilizarea programului.")

citeste_numar()


# Exemplu de utilizare try-except impreuna cu if
# Exemplu: citirea unui numar dintr-un fisier si impartirea la el
import os

cale_fisier = 'numar.txt'

# IF pentru preventie: verific dacă fișierul există înainte sa incerc sa-l deschid
if os.path.exists(cale_fisier):
    try:
        # TRY-EXCEPT: doar pentru operațiile care pot genera exceptii
        with open(cale_fisier, 'r') as f:
            linie = f.readline()
            numar = int(linie)
    except ValueError:
        print('Fișierul nu conține un număr valid!')
    except Exception as e:
        print(f'A apărut o eroare neașteptată: {e}')
    else:
        # IF pentru preventie: verificare separată după obținerea valorii
        if numar == 0:
            print('Nu se poate împărți la zero!')
        else:
            rezultat = 100 / numar
            print(f'Rezultatul este: {rezultat}')
else:
    print('Fișierul nu există!')

# Explicație:
# - if os.path.exists(...) previne o eroare de tip FileNotFoundError
# - try-except tratează erori care pot apărea la conversia la int sau la deschiderea fișierului
# - else după try-except se execută doar dacă nu a apărut nicio excepție
# - if numar == 0 previne ZeroDivisionError (separat de try-except)

# Exemplu de creare a unei excepții personalizate
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Aceasta este o eroare personalizată!")
except MyCustomError as e:
    print(f'Prinsă excepția personalizată: {e}')

# Exemplu concret: calculator simplu cu gestionarea excepțiilor
print("\n--- Calculator simplu ---")
try:
    num1 = float(input("Introdu primul număr: "))
    num2 = float(input("Introdu al doilea număr: "))
except ValueError:
    print("Eroare: Trebuie să introduci numere valide!")
else:
    print(f"Adunare: {num1} + {num2} = {num1 + num2}")
    print(f"Scădere: {num1} - {num2} = {num1 - num2}")
    print(f"Înmulțire: {num1} * {num2} = {num1 * num2}")
    # Împărțire cu verificare pentru zero
    if num2 != 0:
        print(f"Împărțire: {num1} / {num2} = {num1 / num2}")
    else:
        print("Eroare: Împărțirea la zero nu este permisă!")
