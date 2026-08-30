'''
Mod de lucru cu fișiere în Python

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
Parcurgere structura de foldere:
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
'''

# Exemple de lucru cu fișiere
# Scriere într-un fișier
f = open('exemplu.txt', 'w')
f.write('Salut, lume!\n')
f.write('Aceasta este o altă linie.\n')
f.close()

# Scriere mai multor linii cu writelines()
linii = ['Linia 1\n', 'Linia 2\n', 'Linia 3\n']
f = open('exemplu.txt', 'a')  # 'a' = append
f.writelines(linii)
f.close()

# Citire întreg fișierul cu read()
f = open('exemplu.txt', 'r')
continut = f.read()
print('Continut read():')
print(continut)
f.close()

# Citire linie cu readline()
f = open('exemplu.txt', 'r')
linie1 = f.readline()
linie2 = f.readline()
print('Prima linie:', linie1.strip())
print('A doua linie:', linie2.strip())
f.close()

# Citire toate liniile cu readlines()
f = open('exemplu.txt', 'r')
toate_liniile = f.readlines()
print('Toate liniile:', toate_liniile)
f.close()

# Citire toate liniile cu readlines() și iterare
f = open('exemplu.txt', 'r')
toate_liniile = f.readlines()
for linie in toate_liniile:
    print('Linie din readlines():', linie.strip())
f.close()

# Parcurgerea fișierului linie cu linie folosind un iterator
f = open('exemplu.txt', 'r')
for linie in f:
    print('Linie din iterator:', linie.strip())
f.close()


# Exemple CU context manager (with)
# Scriere cu with + write()
with open('exemplu2.txt', 'w') as f:
    f.write('Exemplu cu context manager.\n')
    f.write('Linie nouă.\n')

# Scriere cu with + writelines()
linii2 = ['A\n', 'B\n', 'C\n']
with open('exemplu2.txt', 'a') as f:
    f.writelines(linii2)

# Citire cu with + read()
with open('exemplu2.txt', 'r') as f:
    continut2 = f.read()
    print('Continut exemplu2.txt:', continut2)

# Citire cu with + readline()
with open('exemplu2.txt', 'r') as f:
    print('Prima linie:', f.readline().strip())
    print('A doua linie:', f.readline().strip())

# Citire cu with + readlines()
with open('exemplu2.txt', 'r') as f:
    linii_citite = f.readlines()
    print('Linii citite:', linii_citite)

# Parcurgere cu with + iterator
with open('exemplu2.txt', 'r') as f:
    for linie in f:
        print('Linie din iterator cu with:', linie.strip())

# Exemplu de parcurgere recursivă a folderului "exemplu_project":
import os
for root, dirs, files in os.walk('exemplu_project'):
    # root = calea curentă, dirs = lista de directoare din root, files = lista de fișiere din root
    # print(f"Root: {root} \n Dirs: {dirs} \n Files: {files}\n\n")
    for file in files:
        print(os.path.join(root, file))
