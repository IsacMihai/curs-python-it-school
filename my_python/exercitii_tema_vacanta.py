# Exerciții de vacanță – recapitulare Python (variabile, operatori, stringuri, control flow)
# Perioada: 23 decembrie – 11 ianuarie

# Încălzire (1-10):
# 1. Creează două variabile cu valori numerice și afișează suma lor.
# 2. Afișează produsul a două numere introduse de la tastatură.
# 3. Primește un nume de la tastatură și afișează-l cu litere mari.
# 4. Afișează lungimea unui string introdus de la tastatură.
# 5. Verifică dacă un număr este par sau impar.
# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text.
# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.
# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero.
# 9. Afișează toate caracterele unui string, câte unul pe linie.
# 10. Primește două numere și afișează cel mai mare dintre ele.

# Exerciții pentru oameni incalziti (11-30):
# 11. Primește trei numere și afișează cel mai mic dintre ele.
# 12. Primește un text și verifică dacă este palindrom.
# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.
# 14. Primește un text și construiește un nou string numai cu vocalele din el.
# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).
# 16. Primește un text și afișează doar literele mici din el.
# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.
# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.
# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).
# 20. Primește un text și verifică dacă toate caracterele sunt litere mici.
# 21. Primește un text și afișează-l inversat.
# 22. Primește o propoziție și numără câte cuvinte conține.
# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_".
# 24. Primește un număr și afișează suma cifrelor sale.
# 25. Primește un text și afișează doar caracterele care sunt cifre.
# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.
# 27. Primește un text și afișează toate caracterele distincte din el.
# 28. Primește un text și afișează literele care apar de exact două ori.
# 29. Primește un număr n și afișează toți divizorii săi.
# 30. Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră.

# Exercitii pentru oameni supraincalziti (31-33):
# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".
# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")
# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666)

# Spor la exersat și sărbători fericite!


# 1. Creează două variabile cu valori numerice și afișează suma lor.

# a = 5
# b = 8

# print(a + b)

# # numere de la tastatura

# a = int(input('Introdu primul numar: '))
# b = int(input('Introdu al doilea numar: '))

# print(a + b)

#  2. Afișează produsul a două numere introduse de la tastatură.

# a = int(input('Primul numar: '))
# b = int(input('Al doilea numar: '))

# print( a * b)

# 3. Primește un nume de la tastatură și afișează-l cu litere mari.

# nume = input('Introdu nume: ')

# print(nume.upper())

# 4. Afișează lungimea unui string introdus de la tastatură

# text = input("Introdu un text: ")

# print(len(text))

# 5. Verifică dacă un număr este par sau impar

# numar = int(input('Introdu un numar :'))
# if numar % 2 == 0:
#     print('Par')
# else:
#     print('Impar')

# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text

# text = input('Introduceti textul: ')
# caracter = input('Introduceti caracterul: ')

# print(text.count(caracter))

# sau varianta cu for

# text = input('Intrroduceti textul: ')
# caracter = input('Introduceti caracterul: ')
# contor = 0

# for litera in text:
#     if litera == caracter:
#         contor += 1
# print(contor)

# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.

# text = input('Introduceti textul: ')
# print(text[-1])

# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero

# numar = int(input('Introduceti numarul: '))

# if numar > 0:
#     print('Pozitiv')
# elif numar < 0:
#     print('Negativ')
# else:
#     print('Zero')    

# 9. Afișează toate caracterele unui string, câte unul pe linie

# text = input('Introduceti textul: ')
# for caracter in text:
#     print(caracter)


#varianta 2 folosind index

# text = input('Introduceti textul: ')

# for i in range(len(text)):
#     print(text[i])


#varianta 3 folosind while

# text = input('Introduceti un text: ')
# i = 0

# while i < len(text):
#     print(text[i])
#     i += 1

#varianta 4 cu bucla

# text = input('Intordu un text: ')
# print(*text, sep='\n')

# 10. Primește două numere și afișează cel mai mare dintre ele.

# a = int(input('Primul numar: '))
# b = int(input('Al doilea numar: '))

# if a > b:
#     print(a)
# else:
#     print(b)

# 11. Primește trei numere și afișează cel mai mic dintre ele.

# a = int(input('Primul numar:'))
# b = int(input('Al doilea numar:'))
# c = int(input('Al treilea numar:'))

# if a <= b and a <= c:
#     print(a)
# elif a => b and b <= c:
#     print(b)
# else:
#     print(c)

# varianta cu if:

# a = int(input('Primul numar:'))
# b = int(input('Al doilea numar:'))
# c = int(input('Al treilea numar:'))

# minim = a

# if b < minim:
#     minim = b
# if c < minim:
#     minim = c

# print(minim)

# 12. Primește un text și verifică dacă este palindrom.

# text = input('Verifica daca este polindrom: ')

# if text == text[::-1]:
#     print('Is polindrom')
# else:
#     print('Is not polindrom')
