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
'''
'''
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

# import json

# with open('exemplu_json1.json', 'r') as my_file:
#     date = json.load(my_file)

# print(date)
# print(type(date))
# print(json.dumps(date, indent=4))

# Vreau sa afisez: <nume> are <x> ani si <y> copii
# nume = date['nume']
# varsta = date.get('varsta')
# numar_copii = len(date['copii'])
# print(f'{nume} are {varsta} de ani si {numar_copii} copii')

# <nume> este din <oras>
# oras = date['adresa']['oras']
# oras = date.get('adresa').get('oras')
# print(f'{nume} este din {oras}')

# my_dict = {
#     "nume": "Ion Popescu",
#     "varsta": 30,
#     "casatorit": True,
#     "copii": ["Ana", "Mihai"],
#     "adresa": {
#         "strada": "Strada Exemplu 123",
#         "oras": "Bucuresti",
#         "tara": "Romania"
#     },
#     "telefon": None
# }

# vreau sa scriu acest dictionar intr-un fisier numit ion_popescu.json
# with open('ion_popescu.json', 'w') as my_file:
#     json.dump(my_dict, my_file, indent=4)

# Vreau sa citesc informatia din Ion Popescu si sa
# ii mai adaug un copil si sa ii completez numarul de telefon

# with open('ion_popescu.json', 'r') as my_file:
#     date = json.load(my_file)

# print(json.dumps(date, indent=4))

# date['copii'].append('Mihaela')
# date['telefon'] = '075254321'

# print(json.dumps(date, indent=4))

# with open('ion_popescu.json', 'w') as my_file:
#     json.dump(date, my_file, indent=4)

# import random

# with open('exemplu_json2.json', 'r') as my_file:
#     date = json.load(my_file)

# for element in date:
#     element['copii'] = random.randint(0, 5)
#     # element.update({'copii': random.randint(0, 5)})

# with open('exemplu_json2.json', 'w') as my_file:
#     json.dump(date, my_file, indent=4)

# [
#     {
#         "nume": "Ion Popescu",
#         "varsta": 30
#     },
#     {
#         "nume": "Ana Ionescu",
#         "varsta": 25
#     },
#     {
#         "nume": "Mihai Georgescu",
#         "varsta": 40
#     }
# ]

# import csv

# with open('exemplu_csv.csv', 'r', newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv = []
#     for row in reader:
#         my_csv.append(row)

# print(my_csv)
# print(my_csv[2])


# with open('exemplu_csv.csv', 'r', newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv = list(reader)
#     for elem in reader:
#         print(elem)

# print(my_csv)

# with open('exemplu_csv2.csv', 'w', newline='') as my_file:
#     writer = csv.writer(my_file)
#     writer.writerow(['nume', 'varsta', 'oras'])
#     writer.writerow(['Ion Popescu', '30', 'Bucuresti'])


# my_data = [
#     ['Mihai Georgescu', 40, 'Iasi'],
#     ['Maria Popa', 35, 'Brasov'],
#     ['Andrei Vasilescu', 29, 'Constanta']
# ]
# with open('exemplu_csv2.csv', 'w', newline='') as my_file:
#     writer = csv.writer(my_file)
#     writer.writerow(['nume', 'varsta', 'oras'])
#     writer.writerows(my_data)


# with open('exemplu_csv2.csv', 'r', newline='') as my_file:
#     dict_read = csv.DictReader(my_file)
#     for row in dict_read:
#         print(row)

# with open('exemplu_csv2.csv', 'r', newline='') as my_file:
#     dict_read = csv.DictReader(my_file)
#     my_csv = list(dict_read)

# print(my_csv)

# with open('exemplu_csv2.csv', 'w', newline='') as my_file:
#     antent = ['nume', 'varsta', 'oras']
#     dict_write = csv.DictWriter(my_file, fieldnames=antent)
#     dict_write.writeheader()
#     dict_write.writerow({'nume': 'Mihai Georgescu', 'oras': 'Iasi'})
#     dict_write.writerow({'nume': 'Andrei Vasilescu', 'varsta': '29', 'oras': 'Constanta'})

# persoane_dict = [
#         {'nume': 'Andrei Vasilescu', 'varsta': 29, 'oras': 'Constanta'},
#         {'nume': 'Elena Marinescu', 'varsta': 32, 'oras': 'Sibiu'},
#         {'nume': 'Cristian Dobre', 'varsta': 27, 'oras': 'Oradea'}
#     ]

# with open('exemplu_csv2.csv', 'w', newline='') as my_file:
#     fieldnames = ['nume', 'varsta', 'oras']
#     dict_write = csv.DictWriter(my_file, fieldnames=fieldnames)
#     dict_write.writeheader()
#     dict_write.writerows(persoane_dict)

# with open('exemplu_csv2.csv', 'a', newline='') as my_file:
#     fieldnames = ['nume', 'varsta', 'oras']
#     dict_write = csv.DictWriter(my_file, fieldnames=fieldnames)
#     dict_write.writerows(persoane_dict)
