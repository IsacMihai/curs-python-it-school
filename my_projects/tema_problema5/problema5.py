
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
# ''' -->

import csv
import json
import os

# ClasaA = 'tema_problema5/ClasaA' #definim calea folderului printr o variabila

# for file_name in os.listdir(ClasaA):
#     cale_fisier = os.path.join(ClasaA, file_name) # lipeste dous stringuri, adauga nume de fisier,doar le pune impreuna

#     print(cale_fisier)

#     with open(cale_fisier, 'r', newline='') as my_file:
#        reader = csv.DictReader(my_file)
#        for row in reader:
#           #print(row)
#           if int(row['History']) >= 90: 
#             print(row)


# ClasaB = 'tema_problema5/ClasaB'

# for file_name in os.listdir(ClasaB):
#    cale_fisier = os.path.join(ClasaB, file_name)

#    print(cale_fisier)

#    with open(cale_fisier, 'r') as my_file:
#       date = json.load(my_file)
#       for element in date:
#          nume = element['name']
#          nota = element['grades']
#          media = int(nota['math'] + nota['english'] + nota['science'])/3
#          if media <= 80:
#             print(f'{nume} are media {media}')
            



# for file_name in os.listdir(ClasaA):
#     cale_fisier = os.path.join(ClasaA, file_name)
#     with open(cale_fisier, 'r', newline='') as my_file:
#         reader = csv.DictReader(my_file)
#         print(cale_fisier)
#         lista_medii = []
#         for row in reader:
#                media_elev = int(row['Geography']) + int(row['English']) + int(row['History'])/3
#                lista_medii.append(media_elev)
#         media_clasei = sum(lista_medii)/ len(lista_medii)
#         print(f'Media clasei {file_name} este {media_clasei}')
               




