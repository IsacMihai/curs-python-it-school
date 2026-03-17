'''
Fișiere JSON și CSV în Python

1) Lucrul cu JSON
    - Modulul "json" permite prelucrarea datelor JSON.
    - Funcții principale:
        - json.load(file) - încarcă date JSON dintr-un fișier și le convertește în obiecte Python.
        - json.loads(string) - încarcă date JSON dintr-un șir de caractere.
        - json.dump(obj, file) - scrie un obiect Python ca JSON într-un fișier.
        - json.dumps(obj) - convertește un obiect Python în șir JSON.

    Exemplu fișier JSON:
    {
        "nume": "Ion Popescu",
        "varsta": 30,
        "casatorit": true,
        "copii": ["Ana", "Mihai"],
        "adresa": {
            "strada": "Strada Exemplu 123",
            "oras": "Bucuresti",
            "tara": "Romania"
        },
        "telefon": null
    }

    Exemplu fișier JSON obiecte multiple:
    [
        {
            "nume": "Ion Popescu",
            "varsta": 30
        },
        {
            "nume": "Ana Ionescu",
            "varsta": 25
        },
        {
            "nume": "Mihai Georgescu",
            "varsta": 40
        }
    ]


2) Lucrul cu CSV
    - Modulul "csv" permite prelucrarea fișierelor CSV (Comma-Separated Values).
    - Funcții principale:
        - csv.reader(file) - citește datele dintr-un fișier CSV și le returnează ca un iterator de liste.
        - csv.writer(file) - scrie date într-un fișier CSV folosind un obiect writer.
        - csv.DictReader(file) - citește datele dintr-un fișier CSV și le returnează ca un iterator de dicționare.
        - csv.DictWriter(file, fieldnames) - scrie date într-un fișier CSV folosind un obiect DictWriter.

    Exemplu fișier CSV:
    nume,varsta,oras
    Ion Popescu,30,Bucuresti
    Ana Ionescu,25,Cluj
    Mihai Georgescu,40,Iasi
'''

# Exemple de lucru cu JSON și CSV
import json
import csv
# 1. JSON - exemple
# Citire JSON din fișier
with open('exemplu.json', 'r') as f:
    data = json.load(f)
    print('Date JSON din fișier:', data)

# Scriere JSON într-un fișier
persoana = {'nume': 'Maria', 'varsta': 28, 'oras': 'Timisoara'}
with open('persoana.json', 'w') as f:
    json.dump(persoana, f)

# Citire CSV din fișier
with open('exemplu.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print('Rand CSV:', row)

# Scriere CSV într-un fișier
with open('persoane.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nume', 'varsta', 'oras'])
    writer.writerow(['Ion Popescu', 30, 'Bucuresti'])
    writer.writerow(['Ana Ionescu', 25, 'Cluj'])

# Scriere CSV cu mai multe rânduri
with open('persoane_multi.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nume', 'varsta', 'oras'])
    persoane = [
        ['Mihai Georgescu', 40, 'Iasi'],
        ['Maria Popa', 35, 'Brasov'],
        ['Andrei Vasilescu', 29, 'Constanta']
    ]
    writer.writerows(persoane)

# Citire CSV ca dicționare
with open('exemplu.csv', 'r') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print('Rand CSV ca dict:', row)

# Scriere CSV ca dicționare
with open('persoane_dict.csv', 'w', newline='') as f:
    fieldnames = ['nume', 'varsta', 'oras']
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader()
    dict_writer.writerow({'nume': 'Mihai Georgescu', 'varsta': 40, 'oras': 'Iasi'})
    dict_writer.writerow({'nume': 'Maria Popa', 'varsta': 35, 'oras': 'Brasov'})

# Scriere CSV cu mai multe dicționare
with open('persoane_multi_dict.csv', 'w', newline='') as f:
    fieldnames = ['nume', 'varsta', 'oras']
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader()
    persoane_dict = [
        {'nume': 'Andrei Vasilescu', 'varsta': 29, 'oras': 'Constanta'},
        {'nume': 'Elena Marinescu', 'varsta': 32, 'oras': 'Sibiu'},
        {'nume': 'Cristian Dobre', 'varsta': 27, 'oras': 'Oradea'}
    ]
    dict_writer.writerows(persoane_dict)
