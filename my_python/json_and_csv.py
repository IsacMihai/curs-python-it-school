# import json

# with open('json1.json', 'r') as my_file:
#     date = json.load(my_file)
     
# # print(date)
# # print(type(date))
# print(json.dumps(date, indent=4))

#Vreau sa afisez: <nume> are <x> ani si <y> copii

# nume = date['nume']
# varsta = date.get('varsta')
# numar_copii = len(date['copii'])
# print(f{nume} are {"varsta"} de ani si {numar_copii} copii)

# # <nume> este din <oras>

# oras = date.get('adresa').het('oras')
# print(f'{nume} este din {oras}')

#vreau sa scriu acest dinctionar intru-un fiser numit ion_popescu

# with open('ion_popescu.jsaon', 'w') as my_file:
#     json.dump(my_dict, my_file, indent=4)

#Vreau sa citesc informatia din Ion Poescu si sa i mai adaug un copil si sa adaug nr de telefon

# with open('ion_popescu.json', 'r') as my_file:
#     date = json.load(my_file)
# print(json.dump(date, indent=4))
# date['copii'].append('Mihaela')
# date['telefon'] = '0754254321'

# print(json.dump(date, indent=4))

# with open('ion_popescu', 'w') as my_file:
#     json.dump(date, my_file, indent=4)

# import random

# with open('json2.json', 'r') as my_file:
#     date = json.load(my_file)
# for element in date:
#      date.update['copii']: random.randit(0, 5)
# #    elemente.update({'copii': random.randit})

# with open('json2.json', 'w') as my_file:
#     json.dump(date,my_file, indent=4)



# # print(type(data))

#test daca exist fisierul

# import json

# # Varianta sigura cu tratarea erorilor
# try:
#     with open("fisier.json", "r", encoding="utf-8") as my_file:
#         continut = my_file.read()
        
#         # Verificam daca fisierul este gol
#         if not continut.strip():
#             print("Fisierul JSON este GOL!")
#         else:
#             date = json.loads(continut)
#             print("JSON incarcat cu succes:", date)

# except FileNotFoundError:
#     print("Fisierul nu a fost gasit! Verifica calea.")
    
# except json.JSONDecodeError as e:
#     print(f"JSON invalid! Eroarea: {e}")


#CSV file.
 
# import csv

# with open('test_csv.csv', 'r', newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv = []
#     for row in reader:
#         my_csv.append(row)

# # print(my_csv)
# print(my_csv[2])

# print(type(reader))

# import csv

# with open('test_csv.csv', 'r', newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv = list[reader]
#     for elem in reader:
#         print(elem)

# print(my_csv)

# import csv
# with open('test_csv2.csv', 'w', newline='') as my_file:
#     writer = csv.write(my_file)
#     writer.writerow(['nume', 'prenume', 'varsta', 'oras'])
#     writer.writerow(['Ion Popescu', '30', 'Bucuresti'])
#     writer.writerow(['Ana Ionescu', '25', 'Cluj'])

#varianta cand lucram cu liste
# my_data = [
#     ['Ion Popescu',30,'Bucuresti']
#     ['Ana Ionescu',25,'Cluj']
#     ['Mihai Georgescu',40,'Iasi']
# ]
# with open('test_csv2.csv', 'w', newline='') as my_file:
#     write = csv.write(my_file)
#     write.withrow(['nume', 'varsta', 'oras'])
#     write.withrow(my_data)


# #lista de ddictionare
# import csv
# with open('test_csv.csv', 'r', newline='') as my_file:
#     dict_reader = csv.DictReader(my_file)
#     my_csv = list(dict_reader)

# print(my_csv)
# import csv
# with open('test_csv.csv', 'w', newline='') as my_file:
#     filednames = ['nume', 'varsta', 'oras']
#     dict_write = csv.DictWrite(my_file, fieldnames=fieldnames)
#     dict_write.writeheader()
#     dict_write.writerow({'nume': 'Mihai Georgescu','varsta': 40,'oras': 'Iasi'})

# s = 'python'
# rev = ''
# for i in s:
#     rev = i + rev
#     print(rev)

# print('python'[::-1]) 

# '''
# 5. Se da urmatoarea structura de directoare care contine informatii despre elevii dintr-o scoala:
#    school_files/high_school/classA - contine fisiere CSV cu informatii despre elevii de la filologie
#    school_files/high_school/classB - contine fisiere JSON cu informatii despre elevii de la mate-info 
#     Sa se scrie un program care parcurge recursiv structura de directoare "school_files" si:
#      - Afiseaza toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie
#      - Afiseaza toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80
#      - Calculeaza media generala a tuturor claselor de Filologie
#      - Afiseaza clasele de Mate-info in ordine crescatoare a mediei generale pe clasa
#      - Afiseaza elevii cu cea mai mare medie din fiecare clasa
#      - Convertește fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
#      - Convertește fisierele json in care sunt salvate informatiile despre elevii de la Mate-Info in fisiere csv.
# '''

import csv
import json
import os

