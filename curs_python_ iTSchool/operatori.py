'''
Operatorii in Python

    * Operatorii sunt simboluri speciale care permit efectuarea de operatii asupra
      valorilor si variabilelor

    * Python are mai multe tipuri de operatori:
      - Aritmetici
      - De atribuire
      - De comparatie
      - Logici
      - De apartenenta
      - De identitate
      - Bitwise (pe biti)
'''

'''
Operatorii aritmetici:
    +    Adunare              ex: a + b
    -    Scadere              ex: a - b
    *    Inmultire            ex: a * b
    /    Impartire            ex: a / b
    //   Impartire intreaga   ex: a // b
    %    Restul impartirii    ex: a % b
    **   Ridicare la putere   ex: a ** b
'''

'''
Operatorii de atribuire:
    =     Asignare                           ex: a = 5
    +=    Adunare si asignare                ex: a += 2   (echivalent cu a = a + 2)
    -=    Scadere si asignare                ex: a -= 2
    *=    Inmultire si asignare              ex: a *= 2
    /=    Impartire si asignare              ex: a /= 2
    //=   Impartire intreaga si asignare     ex: a //= 2
    %=    Rest si asignare                   ex: a %= 2
    **=   Putere si asignare                 ex: a **= 2
'''

'''
Operatorii de comparatie:
    ==    Egalitate              ex: a == b
    !=    Diferit                ex: a != b
    >     Mai mare               ex: a > b
    <     Mai mic                ex: a < b
    >=    Mai mare sau egal      ex: a >= b
    <=    Mai mic sau egal       ex: a <= b
'''

'''
Operatorii logici:
    and    Si logic              ex: a and b (ambele trebuie sa fie adevarate)
    or     Sau logic             ex: a or b  (cel putin una trebuie sa fie adevarata)
    not    Negatie logica        ex: not a   (neaga valoarea curenta)
'''

'''
Operatorii de apartenenta:
    in      ex: 'a' in 'ana'
    not in  ex: 5 not in [1,2,3]
'''

'''
Operatorii de identitate:
    is      ex: a is b
    is not  ex: a is not b
'''

'''
funtia round() - rotunjeste la cate zecimale ii specifici
    ex: x = 3.12345678
        x = round(x, 3) -> x = 3.123
'''
# Exemple practice pentru fiecare tip de operator:
# x = int(input("Valoare x: "))
# y = int(input("Valoare y: "))

# print(x, y)
# print(x + y)
# print(x - y)
# print(x / y)
# print(x * y)
# print(x // y)
# print(x % y)
# print(x ** y)

# print(x + y, x - y, x / y)
# var1 = x + y
# var2 = x - y
# var3 = x / y
# suma = var1 + var2 + var3
# print(suma)
# suma = (x + y) + ((int(x) - y) + (x / y))
# print(round(suma, 2))

# x = 10
# y = input("y: ")
# x += int(y) # x = x + y
# z = input("z: ")
# x += int(z) # x = x + z
# print(x)

# y += x # y = y + x
# x **= y # x = x ** y

# var1 = 5
# var2 = 7

# rezultat = var1 < var2

# print(rezultat)
# print(var1 < var2)
# print(var1 == var2)
# print(var1 > var2)
# print(var1 != var2)
# print(var1 >= var2)

# a = 5
# b = 7
# c = 9

# print((a < b) and (a < c)) # -> True
# print((a < b) and (a > c)) # -> False
# print((a < b) or (a < c))  # -> True
# print((a < b) and not (a > c)) # -> True

# print('a' in 'ana')
# print('an' in 'ana')
# print('10' in '101')
# print(10 not in [7,8,9,'10'])

# a = None
# b = None
# a = 139123193819283918743814
# b = 139123193819283918743814
# print(a is b)

a = 7 # binar -> 111
b = 6 # binar -> 110
