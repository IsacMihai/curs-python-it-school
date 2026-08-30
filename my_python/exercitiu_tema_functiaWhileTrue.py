# Enuntul suna cam asa:
# Trebuie implementat un meniu interactiv in consola care pune la dispozitie 
# utilizatorului urmatoarele optiuni:
# 1.Adunare
# 2.Scadere
# 3.Inmultire
# 4.Impartire
# 5.Iesire din program

# Utilizatorul trebuie sa introduca optiunea, iar apoi:
# Pentru optiunile 1->4, utilizatorul trebuie sa introduca doua numere, iar 
# programul va afisa rezultatul operatiei.
# In cazul in care introduce 5, atunci iesim din program. 
# Incercati sa rezolvati pana la cursul de maine daca aveti timp. La finalul 
# cursului am sa aloc niste timp ca sa ne uitam peste exercitiu.

# def check_entrydata(value1,value2):
#     try:
#         val1 = float(value1)
#         val2 = float(value2)
#         return val1, val2
#     except ValueError:
#         raise ValueError("Valorile introduse trebuie sa fie numere.")
    
# def add(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     return val1 + val2

# def subtract(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     return val1 - val2

# def multiply(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     return val1 * val2

# def devide(value1, value2):
#     val1, val2 = check_entrydata(value1, value2)
#     if val2 == 0:
#         raise ValueError("Impartirea la '0' nu e permisa.")
#     return val1 / val2

# def main():
#     while True:
#         print("Alege optiunea:")
#         print("1. Adunare")
#         print("2. Scadere")
#         print("3. Inmultire")
#         print("4. Impartire")
#         print("5. Iesire din program")
#         choice = input("Introduceti optiunea (1/2/3/4/5): ")
#         if choice == '5':
#             print("Iesire din program.")
#             break
#         if choice in "1234":
#             value1 = input("Introduceti primul numar: ")
#             value2 = input("Introduceti al doilea numar: ")
#             try:
#                 if choice == '1':
#                     result = add(value1, value2)
#                     print(f"Rezultat: {result}")
#                 elif choice == '2':
#                     result = subtract(value1, value2)
#                     print(f"Rezultat: {result}")
#                 elif choice == '3':
#                     result = multiply(value1, value2)
#                     print(f"Result: {result}")
#                 elif choice == '4':
#                     result = devide(value1, value2)
#                     print(f"Result: {result}")
#             except ValueError as e:
#                 print(e)
#         else:
#             print("Optiune invalida. Va rugam incercati din nou.")

# if __name__ == "__main__":
#     main()

#o alta versiune

def adunare():
    """Docstring for adunare"""
    a = int(input("Introdu primul numar: "))
    b = int(input("Introdu al doilea numar: "))
    print("Rezultatul adunarii este: ", a + b)
    return True

def  scadere():
    """Docstring for scadere"""
    a = int(input("Introdu primul numar: "))
    b = int(input("Introdu al doilea numar: "))
    print("Rezultatul scaderii este: ", a - b)
    return True

def inmultire():
    """Docstring for inmultire"""
    a = int(input("Introdu primul numar: "))
    b = int(input("Introdu al doilea numar: "))
    print("Rezultatul inmultire este: ", a * b)
    return True

def impartire():
    """Docstring for impartire"""
    a = int(input("Introdu primul numar: "))
    b = int(input("Introdu al doilea numar: "))
    if a == 0 and b == 0:
        print("Impartirea la zero este neperminsa.")
    else:
        print("Rezultatul impartire este: ", a / b)
        return True

def main():
    """Docstring for main"""
    while True:
        alege = click.prompt("1.Adunare \n2. Scadere \n3. Inmultire \n4. Impartire \n5. Iesire din program")
        if alege == 1:
            adunare()
        elif alege == 2:
            scadere()
        elif alege == 3:
            inmultire()
        elif alege == 4:
            impartire()
        elif alege == 5:
            click.echo("Ciau! ")
        else:
            print("Optiunea nu exista, incearca din nou.")

if __name__ == "__main__":
    main()


    

