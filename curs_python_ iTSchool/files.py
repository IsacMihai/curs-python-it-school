'''
Mod de lucru cu fișiere în Python
'''
'''
Moduri de deschidere a fișierelor:
    - 'r' - read - citire (implicit)
    - 'w' - write - scriere (creează fișierul dacă nu există, suprascrie dacă există)
    - 'a' - append - adăugare (creează fișierul dacă nu există, adaugă la sfârșit dacă există)
    - 'b' - binary - mod binar (utilizat împreună cu celelalte moduri, ex: 'rb', 'wb')
    - 't' - text - mod text (implicit, ex: 'rt', 'wt')
'''
'''
Funcții:
    - open() - deschide un fișier și returnează un obiect de fișier
    - read() - citește conținutul unui fișier
    - readline() - citește o linie dintr-un fișier
    - readlines() - citește toate liniile dintr-un fișier și le returnează ca o listă
    - write() - scrie date într-un fișier
    - writelines() - scrie o listă de linii într-un fișier
    - close() - închide fișierul
'''
'''
Context manager:
    - with open('nume_fisier', 'mod') as f:
          # lucrul cu fișierul f
    - Asigură închiderea automată a fișierului după terminarea blocului with
'''
'''
Parcurgere structura de foldere
    - "os" module:
        * os.listdir(path) - listează fișierele și directoarele din path
        * os.path.join(path, name) - construiește un path complet
        * os.path.isfile(path) - verifică dacă path este fișier
        * os.path.isdir(path) - verifică dacă path este director
        * os.walk(path) - generează fișierele dintr-un director recursiv

    Exemplu structura folder:
    exemplu_project/
    ├── data/
    │   ├── file1.py
    │   └── file2.py
    ├── logs/
    │   └── log1.txt
    └── script.py

    - Exemplu de parcurgere recursivă a folderului "exemplu_project":
    import os
    for root, dirs, files in os.walk('exemplu_project'):
        for file in files:
            print(os.path.join(root, file))
'''

mesaj = "Bai, frate! In sfrasit ne-o invatat Danutu despre fisiere!"
nume_fisier = "danutu_thau.txt"

# my_file = open("danutu_thau.txt", 'w')
# my_file.write("Bai, frate! In sfrasit ne-o invatat Danutu despre fisiere!")
# my_file.write(mesaj)
# my_file.close()

# my_file = open(nume_fisier, 'r')
# data = my_file.readlines()
# print(data[0])
# my_file.close()

# Ana are mere
# Ionut e mare baiat pe cartier
# Cand cresc mare vreau sa fiu politist

# mesaj1 = 'Ana are mere\n'
# mesaj2 = 'Ionut e mare baiat pe cartier\n'
# mesaj3 = 'Cand cresc mare vreau sa fiu politist\n'

# my_file = open(nume_fisier, 'a')
# my_file.writelines([mesaj1, mesaj2, mesaj3])
# # my_file.append(mesaj1)
# # my_file.append(mesaj2)
# # my_file.append(mesaj3)
# my_file.close()

# Bai, frate! In sfrasit ne-o invatat Danutu despre fisiere!
# Ionela are mere
# Ionut e mare baiat pe cartier
# Cand cresc mare vreau sa fiu politist

# my_file = open(nume_fisier, 'r')
# linii_fisier = my_file.readlines()
# my_file.close()

# # Varianta 1
# for i in range(len(linii_fisier)):
#     if 'Ana' in linii_fisier[i]:
#         linii_fisier[i] = linii_fisier[i].replace('Ana', 'Ionela')
#         break

# my_file = open(nume_fisier, 'w')
# my_file.writelines(linii_fisier)
# my_file.close()

# Varianta 2
# result = []
# print(linii_fisier)
# for linie in linii_fisier:
#     print(result)
#     if 'Ana' in linie:
#         result.append(linie.replace('Ana', 'Ionela'))
#     else:
#         result.append(linie)

# my_file = open(nume_fisier, 'w')
# my_file.writelines(result)
# my_file.close()

# Not working - modificam exact pe lsita pe care iteram
# for  linie in linii_fisier:
#     if 'Ana' in linie:
#         linie = linie.replace('Ana', 'Ionela')
#         print('am fost aici')

# my_file = open(nume_fisier, 'r')
# my_file.close()


# Deschidere si inchidere fisier cu context manager
# with open(nume_fisier, 'r') as my_file:
#     linii_fisier = my_file.readlines()

# # Varianta 1
# for i in range(len(linii_fisier)):
#     if 'Ana' in linii_fisier[i]:
#         linii_fisier[i] = linii_fisier[i].replace('Ana', 'Ionela')
#         break

# with open(nume_fisier, 'w') as my_file:
#     my_file.writelines(linii_fisier)

# with open("danutu_thau.txt", 'r') as my_file:
#     text = my_file.read()

# text = text.replace('Ana', 'Ionela')

# with open("danutu_thau.txt", 'w') as my_file:
#     my_file.write(text)
#     print("Modificarea a fost facuta!")

# with open("danutu_thau.txt", 'r') as my_file:
#     for line in my_file:
#         print(line)

# with open('danutu_thau.txt', 'r', ecoding='utf-8') as input_file, open('temp_file.txt', 'w') as output_file:
#     for line in input_file:
#         output_file.write(line[::-1])
#     print('Resscriere fisier reusita!')

import os

# * os.listdir(path) - listează fișierele și directoarele din path
# * os.path.join(path, name) - construiește un path complet
# * os.path.isfile(path) - verifică dacă path este fișier
# * os.path.isdir(path) - verifică dacă path este director

# * os.walk(path) - generează fișierele dintr-un director recursiv

# print(os.listdir("C:\Work\Personal\ITSchool\Curs\exemplu_project"))
# my_path = os.path.join("C:\Work\Personal\ITSchool\Curs\exemplu_project\ceva")
# print(my_path)
# print(os.path.isdir(my_path))
# print(os.path.isfile(my_path))

# sa verificam daca in exemplu_project -> data -> file1.py
# continut_proiect = os.listdir("C:\Work\Personal\ITSchool\Curs\exemplu_project")
# print(continut_proiect)
# continut_proiect = os.path.join("C:\Work\Personal\ITSchool\Curs\exemplu_project","data")
# print(continut_proiect)
# continut_data = os.listdir(continut_proiect)
# if 'file1.py' in continut_data:
#     print('Gasit')
# else:
#     print('NU gasit')

# gasiti in folderul ceva daca exista un fisier txt, iar daca exista,
# cititi continutul si afisati-l

# * os.listdir(path) - listează fișierele și directoarele din path
# * os.path.join(path, name) - construiește un path complet
# * os.path.isfile(path) - verifică dacă path este fișier
# * os.path.isdir(path) - verifică dacă path este director

# path_proiect = "C:\Work\Personal\ITSchool\Curs\exemplu_project"
# continut_proiect = os.listdir(path_proiect)
# if 'ceva' in continut_proiect:
#     print('Folderul ceva gasit!')
#     path_ceva = os.path.join(path_proiect, 'ceva')
#     continut_ceva = os.listdir(path_ceva)
#     print(continut_ceva)

# else:
#     print('Folderul ceva nu exista, deci nu avem fisier txt pe care sa il citim')

# path_ceva = os.path.join(path_proiect, 'ceva')
# elemente = os.listdir(path_ceva)
# print(elemente)
# for nume in elemente:
#     if nume.endswith('.txt'):
#         new_path = os.path.join(path_ceva, nume)
#         if os.path.isfile(new_path):
#             with open(new_path, 'r') as my_file:
#                 print(my_file.read())

# path_proiect = "C:\Work\Personal\ITSchool\Curs\exemplu_project"
# for root, dirs, files in os.walk(path_proiect):
#     # print(root, dirs, files)
#     for file in files:
#         if file.endswith('.txt') and os.path.join(path_proiect, 'ceva') in root:
#             my_file_path = os.path.join(root, file)
#             with open(my_file_path, 'r') as my_file:
#                 print(my_file.read())
