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

# Da eroare pt ca nu exista fisierul
# with open('macarena.txt', 'r') as my_file:
#         print(my_file.read())


# try:
#     with open('macarena.txt', 'r') as my_file:
#         print(my_file.read())
# except FileNotFoundError:
#     print('Fisierul macarena.txt nu exista!')
# else:
#     print('Fisierul deschis cu succes!')


# try:
#     with open('macarena.txt', 'r') as my_file:
#         print(my_file.read())
# except Exception as my_exception:
#     print('Fisierul macarena.txt nu exista!')
#     print(my_exception)
# else:
#     print('Fisierul deschis cu succes!')


# try:
#     with open('temp_file.txt', 'r') as my_file:
#         print(my_file.read())
# except Exception as my_exception:
#     print('Fisierul macarena.txt nu exista!')
#     print(my_exception)
# else:
#     print('Fisierul deschis cu succes!')


# try:
#     with open('macarena.txt', 'r') as my_file:
#         print(my_file.read())
# except Exception as my_exception:
#     print('Fisierul macarena.txt nu exista!')
#     print(my_exception)
# else:
#     print('Fisierul deschis cu succes!')
# finally:
#     print('Codul asta se executa tot timpul')


# try:
#     with open('macarena.txt', 'r') as my_file:
#         print(my_file.read())
# except FileNotFoundError:
#     print('Nu am gasit fisierul')
# except Exception as my_exception:
#     print('Fisierul macarena.txt nu exista!')
#     print(my_exception)
# else:
#     print('Fisierul deschis cu succes!')
# finally:
#     print('Codul asta se executa tot timpul')

# while True:
#     try:
#         numar = int(input("introduceti nr: "))
#     except Exception as ex:
#         print(ex)
#     else:
#         print(f'felicitari ati introdus nuamrul {numar}')
#         if numar == 0:
#             break

# while True:
#     numar = int(input("introduceti nr: "))
#     print(f'felicitari ati introdus nuamrul {numar}')
#     if numar == 0:
#         break
