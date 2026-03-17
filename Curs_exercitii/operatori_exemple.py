'''
Operatorii in Python

    * Operatorii sunt simboluri speciale care permit efectuarea de operatii asupra valorilor si variabilelor

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

# Operatorii aritmetici
a = 10
b = 3
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a // b =', a // b)
print('a % b =', a % b)
print('a ** b =', a ** b)

# Operatorii de atribuire
x = 5
x += 2
print('x dupa x += 2:', x)
x *= 3
print('x dupa x *= 3:', x)

# Operatorii de comparatie
print('a == b:', a == b)
print('a != b:', a != b)
print('a > b:', a > b)
print('a < b:', a < b)
print('a >= b:', a >= b)
print('a <= b:', a <= b)

# Operatorii logici
print('True and False:', True and False)
print('True or False:', True or False)
print('not True:', not True)

# Operatorii de apartenenta
lista = [1, 2, 3]
print('2 in lista:', 2 in lista)
print('5 not in lista:', 5 not in lista)

# Operatorii de identitate
c = a
print('c is a:', c is a)
print('c is not b:', c is not b)
