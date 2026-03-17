'''
Exercitii pentru dictionare:
1) Creeaza un dictionar care sa contina numele si varsta a 5 persoane.
2) Afiseaza varsta unei persoane specifificate de utilizator.
3) Afiseaza cea mai mare si cea mai mica varsta din dictionar.
4) Adauga 3 noi persoane in dictionar.
5) Afiseaza varsta medie a persoanelor din dictionar.
6) Sterge o persoana specificata de utilizator din dictionar.
7) Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.
8) Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".
9) Verifica daca o persoana specificata de utilizator exista in dictionar.
10) Actualizeaza varsta unei persoane specificate de utilizator.
11) Afiseaza numarul total de persoane din dictionar.
12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.
13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.
14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.
15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.
16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.).
17) Afiseaza persoanele sortate alfabetic dupa nume. (Utilizati functia sorted pentru a rezolva acest exercitiu).
18) Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
   (Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).
19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
    Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.
20) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
    Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.
'''

#1. 2.

#dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
#print(type(dicrionarul_meu))
#print(dicrionarul_meu['Barbu'])

#3.
# persoane = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}

# varste = persoane.values()
# min_varsta = min(varste)
# max_varsta = max(varste)

# print("Cea mai mica varsta:", min_varsta)
# print("Cea mai mare varsta:", max_varsta)

# #4.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# dicrionarul_meu.update({'Voinea': 21, 'Flavius': 16, 'Bogdan':25})
# print(dicrionarul_meu)

#5
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}

# media = sum(dicrionarul_meu.values()) / len(dicrionarul_meu)
# print("Varsta medie este:", round(media))

#6.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}

# nume = input("Introdu numele persoanei de sters: ")
# if nume in dicrionarul_meu:
#     del dicrionarul_meu[nume]
#     print(f"{nume} a fost sters din dictionar.")
# else:
#     print("Persoana nu exista in dictionar.")

#7

# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}

# limita = int(input("Introdu varsta minima: "))
# rezultat = {nume: varsta for nume, varsta in dicrionarul_meu.items() if varsta > limita}
# print(rezultat)

#8.

# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# for nume in dicrionarul_meu:
#     print("Nume:", nume + ", Varsta:", dicrionarul_meu[nume])

#9.

# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}

# nume = input("Introdu numele persoanei: ")
# if nume in dicrionarul_meu:
#     print("Persoana exista in dictionar.")
# else:
#     print("Persoana NU exista in dictionar.")

#10.

# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# nume = input("Introdu numele persoanei: ")

# if nume in dicrionarul_meu:
#     varsta_noua = int(input("Introdu noua varsta: "))
#     dicrionarul_meu[nume] = varsta_noua
#     print(f"Varsta lui {nume} a fost actualizata la {varsta_noua}.")

#11.

# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# numar_persoane = len(dicrionarul_meu)
# print("Numarul total de persoane este:", numar_persoane)

#12.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# nume_persoane = list(dicrionarul_meu.keys())
# print(nume_persoane)

#13.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# adulti = {}
# for nume, varsta in dicrionarul_meu.items():
#     if varsta > 18:
#         adulti[nume] = varsta
# print(adulti)

#14.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# varsta_fara_duplicate = []
# for varsta in dicrionarul_meu.values():
#     if varsta not in varsta_fara_duplicate:
#         varsta_fara_duplicate.append(varsta)
# print(varsta_fara_duplicate)

#15.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# valoare = int(input("Introdu varsta: "))
# persoana_apropiata = min(
#     dicrionarul_meu,
#     key=lambda nume: abs(dicrionarul_meu[nume] - valoare)
# )
# print(
#     f"Persoana cu varsta cea mai apropiata este: "
#     f"{persoana_apropiata}({dicrionarul_meu[persoana_apropiata]} ani)"
# )

#16.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# grupare = {}

# for nume, varsta in dicrionarul_meu.items():
#     decada = (varsta // 10) * 10
#     cheie = f"{decada}-{decada + 9}"

#     if cheie not in grupare:
#         grupare[cheie] = []

#     grupare[cheie].append(nume)

#sau

# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# from collections import defaultdict

# grupare = defaultdict(list)

# for nume, varsta in dicrionarul_meu.items():
#     decada = f"{(varsta // 10) * 10}-{(varsta // 10) * 10 + 9}"
#     grupare[decada].append(nume)

# for decada, persoane in grupare.items():
#     print(decada, ":", persoane)


#17.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}
# for nume in sorted(dicrionarul_meu):
#     print(f"Nume: {nume}, Varsta: {dicrionarul_meu[nume]}")


#18.
# dicrionarul_meu = {'Ion':20, 'Barbu':44, 'Narcis':33, 'Andra':27, 'Lore':18}

# dicrionarul_meu_sortate = sorted(dicrionarul_meu.items(), key=lambda item: item[1])

# for nume, varsta in dicrionarul_meu_sortate:
#     print(f"Nume: {nume}, Varsta: {varsta}")

#19.
# text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"

# persoane = {}

# propozitii = text.split(", ")

# for p in propozitii:
#     parti = p.split()
#     nume = parti[0]
#     varsta = int(parti[2])
#     persoane[nume] = varsta

# print(persoane)

#20.
text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"

from collections import Counter

frecventa = Counter(c for c in text.lower() if c.isalpha())
print(dict(frecventa))

