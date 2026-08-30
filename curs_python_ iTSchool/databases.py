'''
Baze de date în Python folosind SQLite

* Baza de date = un fișier care stochează date structurate într-un mod organizat si ne ofera eficiență în:
    - salvarea datelor
    - accesarea datelor
    - gestionarea datelor

* SQLite = bibliotecă software care oferă o bază de date relațională ușoară, integrată direct în aplicațiile Python
         fără a necesita un server de baze de date separat

* SQL(Structured Query Language) = limbaj standard pentru gestionarea și manipularea bazelor de date relaționale

* DB Browser for SQLite = instrument grafic open-source pentru crearea, proiectarea și editarea bazelor de date SQLite
  (https://sqlitebrowser.org/dl/)

* Comenzi SQL de baza:
    - CREATE TABLE = creează un tabel nou într-o bază de date
    - INSERT INTO = inserează date noi într-un tabel
    - SELECT = interoghează și extrage date dintr-un tabel
    - UPDATE = actualizează datele existente într-un tabel
    - DELETE = șterge date dintr-un tabel

    -- Create table
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        math_grade REAL,
        english_grade REAL,
        cs_grade REAL
    );

    -- Insert data
    INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
    VALUES ('Alice', 'Smith', 85.5, 90.0, 92.5);

    -- Update data
    UPDATE students
    SET math_grade = 95.0
    WHERE id = 1;

    -- Delete data
    DELETE FROM students
    WHERE id = 1;

    -- Query all data
    SELECT * FROM students;

    -- Query specific columns
    SELECT first_name, math_grade FROM students;

    -- Query with condition
    SELECT * FROM students
    WHERE math_grade > 90;

    -- Query with order
    SELECT * FROM students
    ORDER BY math_grade DESC;

* SQLite în Python:
    - modul utilizat -> sqlite3

    Crearea conexiunii cu baza de date:
    connection = sqlite3.connect('students.db')

    Pentru manipularea datelor din baza de date avem nevoie de un cursor:
    cursor = connection.cursor()

    cursor.execute(...) -> folosit pentru a rula actiuni SQL asupra bazei de date

    connection.commit() -> folosit pentru a salva modificarile facute asupra bazei de date

    connection.close() -> folosit pentru a incheia conexiunea cu baza de date

    -> Pentru crearea unei tabele in baza de date:
    Exemplu:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            math_grade INTEGER,
            english_grade INTEGER,
            cs_grade INTEGER
        )
        """)
    connection.commit()

    -> Pentru adaugarea unui element in baza de date:
    Exemplu:
    cursor.execute("""
        INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
        VALUES (?, ?, ?, ?, ?)
        """, ('Alice', 'Smith', 85, 90, 95))
    connection.commit()

    -----
    name = "Alice'; DROP TABLE students; --"
    cursor.execute(f"SELECT * FROM students WHERE first_name = '{name}'")
    # Query-ul devine:
    # SELECT * FROM students WHERE first_name = 'Alice'; DROP TABLE students; --'
    # => tabela students ar fi stearsa!

    name = "Alice'; DROP TABLE students; --"
    cursor.execute("SELECT * FROM students WHERE first_name = ?", (name,))
    # sqlite3 tratează valoarea ca text literal, nu ca cod SQL
    # => niciun pericol de SQL injection!
    -----

    -> Pentru adaugarea mai multor elemente in baza de date simultan:
    students_list = [
        ("Luca", "Bianchi", 90, 85, 88),
        ("Sara", "Rossi", 75, 80, 82),
        ("Marco", "Verdi", 60, 65, 70)
    ]

    cursor.executemany("""
        INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
        VALUES (?, ?, ?, ?, ?)
    """, students_list)
    connection.commit()

    -> Pentru citirea tuturor informatiilor salvate in baza de date:
    cursor.execute("""SELECT * FROM students""")
    rows = cursor.fetchall()

    -> Pentru citirea unui element pe baza unui camp:
    cursor.execute("SELECT * FROM students WHERE first_name = ?", ('Alice',))
    data = cursor.fetchone()

    -> Pentru citirea mai multor elemente pe baza unui camp:
    cursor.execute("SELECT ?, ? FROM students WHERE math_grade > ?", (first_name, math_grade, 80))
    data = cursor.fetchall()

    -> Pentru modificarea unor date existente:
    cursor.execute("""
        UPDATE students
        SET math_grade = ?
        WHERE first_name = ? AND last_name = ?
        """, (95, 'Alice', 'Smith'))
    connection.commit()

    -> Pentru stergerea unui element:
    cursor.execute("DELETE FROM students WHERE first_name = ? AND last_name = ?", ('Alice', 'Smith'))
    connection.commit()

    -> Pentru stergerea tuturor elementelor:
    cursor.execute("DELETE FROM students")
    connection.commit()

    -> Utilizarea unui context manager pentru a gestiona conexiunea cu baza de date:
    with sqlite3.connect('students.db') as connection:
        cursor = connection.cursor()
        # Aici putem rula actiuni SQL asupra bazei de date
        # Modificarile vor fi salvate automat la iesirea din blocul with

    Exemplu creare tabel in baza de date folosind context manager:
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                math_grade INTEGER
            )
        """)
        conn.commit()  # salvează modificările

    Exemplu adaugare date:
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (first_name, last_name, math_grade)
            VALUES (?, ?, ?)
        """, ('Alice', 'Smith', 95))
        conn.commit()

    Exemplu citire date:
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
'''

import sqlite3
# connection = sqlite3.connect('students.db')
# cursor = connection.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT,
#         last_name TEXT,
#         math_grade INTEGER,
#         english_grade INTEGER,
#         cs_grade INTEGER
#     )
#     """)
# connection.commit()
# connection.close()

# cursor.execute("""
#     INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
#     VALUES (?, ?, ?, ?, ?)
#     """, ('Alice', 'Smith', 85, 90, 95))
# connection.commit()
# cursor.execute("""
#     INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
#     VALUES (?, ?, ?, ?, ?)
#     """, ('Daniel', 'Neamtiu', 70, 80, 90))
# connection.commit()

# students_list = [
#     ("Luca", "Bianchi", 90, 85, 88),
#     ("Sara", "Rossi", 75, 80, 82),
#     ("Marco", "Verdi", 60, 65, 70)
# ]

# cursor.executemany("""
#     INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
#     VALUES (?, ?, ?, ?, ?)
# """, students_list)
# connection.commit()

# for student in students_list:
#     cursor.execute("""
#     INSERT INTO students (first_name, last_name, math_grade, english_grade, cs_grade)
#     VALUES (?, ?, ?, ?, ?)
#     """, student)
#     connection.commit()

# cursor.execute("""SELECT * FROM students""")
# rows = cursor.fetchall()

# cursor.execute("SELECT * FROM students WHERE first_name = ?", ('Alice',))
# data = cursor.fetchone()

# cursor.execute("SELECT math_grade, english_grade, cs_grade FROM students WHERE first_name = ?", ('Alice',))
# rows = cursor.fetchall()

# cursor.execute("SELECT first_name, math_grade FROM students WHERE math_grade < ?", (80,))
# data = cursor.fetchall()

# cursor.execute("""
#     UPDATE students
#     SET math_grade = ?
#     WHERE first_name = ? AND last_name = ?
#     """, (95, 'Alice', 'Smith'))
# connection.commit()

# cursor.execute("""SELECT math_grade FROM students WHERE first_name = ? AND last_name = ?""", ('Alice', 'Smith'))
# print(cursor.fetchone())

# cursor.execute("""SELECT * FROM students WHERE first_name = ? AND last_name = ?""", ('Alice', 'Smith'))
# print(cursor.fetchone())

# cursor.execute("DELETE FROM students WHERE first_name = ? AND last_name = ?", ('Alice', 'Smith'))
# connection.commit()

# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()
# print(rows)

# connection.close()

# with sqlite3.connect('students.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#         INSERT INTO students (first_name, last_name, math_grade)
#         VALUES (?, ?, ?)
#     """, ('Alice', 'Smith', 95))
#     connection.commit()

# with sqlite3.connect('students.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#         UPDATE students
#         SET english_grade = ?, cs_grade = ?
#         WHERE first_name = ? AND last_name = ?
#         """, (70, 50, 'Alice', 'Smith'))
#     connection.commit()

# with sqlite3.connect('students.db') as connection:
#     cursor = connection.cursor()
#     ids = [(7,), (8,)]
#     cursor.executemany('DELETE FROM students WHERE id = ?', ids)
#     connection.commit()
