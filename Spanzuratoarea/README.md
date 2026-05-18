# Spanzuratoarea

## Descriere proiect
Spanzuratoarea este o aplicatie desktop realizata in Python. Aplicatia permite jucatorului sa joace jocul Spanzuratoarea pe trei nivele de dificultate: easy, medium si hard.

Rezultatele jocurilor sunt salvate intr-o baza de date SQLite si pot fi afisate, modificate, sterse, sortate si filtrate din interfata grafica.

## Tehnologii utilizate
- Python
- Tkinter pentru interfata grafica
- SQLite / sqlite3 pentru baza de date
- logging pentru salvarea evenimentelor aplicatiei

## Functionalitati
- Joc Spanzuratoarea pe nivele: easy, medium, hard
- Salvare scor in baza de date
- Afisare scoruri in tabel
- CRUD:
  - Create: adaugare scor dupa finalizarea jocului
  - Read: afisare scoruri
  - Update: modificare nume, dificultate si scor
  - Delete: stergere scor
- Sortare si filtrare:
  - sortare dupa nume
  - sortare dupa scor, cei mai buni
  - sortare dupa scor, cei mai slabi
  - filtrare dupa dificultate
  - cautare dupa nume
- Generare raport cu total jocuri, cel mai bun scor, cel mai slab scor si numar jocuri pe dificultate

## Instalare
Aplicatia foloseste doar module din biblioteca standard Python, deci nu necesita instalarea unor dependinte externe.

## Rulare aplicatie
Din folderul proiectului se ruleaza comanda:

```bash
python main.py
```

## Structura proiectului
```text
Spanzuratoarea/
├── main.py
├── database.py
├── game_logic.py
├── interface.py
├── reports.py
├── README.md
├── spanzuratoarea.db
└── spanzuratoarea.log
```

## Observatii
Fisierul `spanzuratoarea.db` este creat automat la prima rulare a aplicatiei.
Fisierul `spanzuratoarea.log` este creat automat si salveaza informatii despre actiunile aplicatiei.
