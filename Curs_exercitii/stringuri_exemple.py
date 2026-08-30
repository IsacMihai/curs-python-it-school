'''
Stringuri (șiruri de caractere) în Python

    * Un string este o secvență de caractere delimitată de ghilimele simple ('...'), duble ("...")
      sau triple (\'\'\'...\'\'\', """...""")

    * Stringurile pot conține orice tip de caractere: litere, cifre, simboluri, spații

    * Stringurile sunt imutabile [imutable] (nu pot fi modificate direct)
'''

'''
Definirea stringurilor:
    s1 = 'Ana are mere'
    s2 = "Python este distractiv!"
    s3 = """Acesta este
un string pe mai multe linii."""
'''

'''
Concatenare și repetare:
    * Concatenare: folosim operatorul +
    * Repetare: folosim operatorul *
'''

'''
Indexare și slicing:
    * Putem accesa caractere individuale folosind indexul - incepe de la 0
        - nume_string[index]

    * Indexare negativă pentru a accesa caractere de la sfârșit
        - nume_string[-index]

    * Putem obține subșiruri folosind slicing
        - nume_string[start:end:step]
'''

'''
Metode utile pentru stringuri:
    * len() - lungimea stringului
    * upper(), lower() - conversie la majuscule/minuscule
    * replace() - înlocuire
    * count() - numără aparițiile unui subșir
    * find() - găsește poziția unui subșir

    nume_string.nume_metoda()
'''

'''
Formatarea stringurilor:
    * f-string: f"Salut, {nume}!"
    * metoda format: "Salut, {}!".format(nume)
'''

'''
Eliminarea spațiilor:
    * strip(), lstrip(), rstrip()
'''

'''
Împărțirea și unirea stringurilor:
    * split() - împarte stringul în listă
    * join() - unește elementele unei liste într-un string
'''

'''
Verificări uzuale:
    * startswith(), endswith(), isdigit(), isalpha()
'''

'''
Iterare prin caractere:
    * Putem parcurge fiecare caracter dintr-un string cu bucla for
'''

'''
Caractere speciale (escape):
    * \n - linie nouă
    * \t - tab
    * \\ - backslash
    * \' - ghilimele simple
    * \" - ghilimele duble
'''

'''
Stringuri goale și conversii:
    * Un string gol are lungimea 0
    * Conversie la string: str()
'''

# Exemple practice pentru fiecare capitol:

# Definirea stringurilor
s1 = 'Ana are mere'
s2 = "Python este distractiv!"
s3 = '''Acesta este
un string pe mai multe linii.'''
print(s1)
print(s2)
print(s3)

# Concatenare și repetare
nume = "Ana"
mesaj = "Salut, " + nume + "!"
print(mesaj)
repetare = "ha" * 3
print(repetare)

# Indexare și slicing
text = "Python"
primul = text[0]      # primul caracter
ultimul = text[-1]    # ultimul caracter
print(primul, ultimul)
subsir = text[1:4]    # caracterele de la index 1 la 3
print(subsir)

# Metode utile pentru stringuri
lungime = len(text)
print("Lungime:", lungime)
print(text.upper())
print(text.lower())
print(text.replace("P", "J"))
print(text.count("t"))
print(text.find("th"))

# Formatarea stringurilor
varsta = 25
mesaj_formatat = f"Ana are {varsta} ani."
print(mesaj_formatat)
mesaj_formatat2 = "Ana are {} ani.".format(varsta)
print(mesaj_formatat2)

# Eliminarea spațiilor
spatii = "  Python  "
print(spatii.strip())
print(spatii.lstrip())
print(spatii.rstrip())

# Împărțirea și unirea stringurilor
csv = "Ana,25,Bucuresti"
lista = csv.split(",")
print(lista)
print("-".join(lista))

# Verificări uzuale
print(text.startswith("Py"))
print(text.endswith("on"))
print("123".isdigit())
print("abc".isalpha())

# Caractere speciale (escape)
linie_noua = "Salut!\nCe faci?"
tab = "A\tB\tC"
print(linie_noua)
print(tab)

# Stringuri goale și conversii
empty = ""
print("Lungime string gol:", len(empty))
numar = 123
numar_str = str(numar)
print(numar_str, type(numar_str))
