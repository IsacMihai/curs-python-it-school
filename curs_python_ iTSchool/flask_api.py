'''
Flask API basic - studenti (nume, prenume, note)

Instalare:
	pip install flask

Rulare:
	python flask_api.py

Endpoint-uri:
	GET    /students
	GET    /students/<student_cnp>
	POST   /students
	PUT    /students/<student_cnp>
	DELETE /students/<student_cnp>
'''

import sqlite3

from flask import Flask, jsonify, request


DB_NAME = 'exercitiu_students.db'
app = Flask(__name__)


def row_to_dict(row):
    return {
        'cnp': row[0],
        'firstname': row[1],
        'lastname': row[2],
        'rom': row[3],
        'math': row[4],
        'engl': row[5]
    }


def validate_data(data):
    required_fields = [
        'cnp',
        'firstname',
        'lastname',
        'rom',
        'math',
        'engl'
    ]

    for field in required_fields:
        if field not in data:
            return False, f'Missing field: {field}'

    grades_list = ['rom', 'math', 'engl']
    for field in grades_list:
        print(data[field])
        if not isinstance(data[field], int):
            return False, f'{field} must be of type integer'
        if not 1 <= data[field] <= 10:
            return False, f'{field} must be between 1 and 10'

    return True, 'ok'


@app.get('/')
def home():
    return jsonify({'message': 'Students API is running!'})


@app.get('/students')
def get_stundets():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()

    students_list = []
    for row in rows:
        students_list.append(row_to_dict(row))

    return jsonify(students_list)

@app.get('/students/<int:student_cnp>')
def get_student(student_cnp):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students WHERE cnp = ?', (student_cnp,))
        row = cursor.fetchone()

    if row is None:
        return jsonify({'error': f'Student with CNP: {student_cnp} does not exist!'}), 404

    return jsonify(row_to_dict(row))


@app.post('/students')
def create_student():
    data = request.get_json(silent=True) or {}
    is_valid, message = validate_data(data)

    if not is_valid:
        return jsonify({'error': message}), 400

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
            INSERT INTO students (cnp, firstname, lastname, rom, math, engl)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
               data['cnp'],
               data['firstname'],
               data['lastname'],
               data['rom'],
               data['math'],
               data['engl']
            )
        )
        connection.commit()

    return jsonify({'message': 'Student added!'}), 201


@app.put('/students')
def update_student():
    data = request.get_json(silent=True) or {}
    is_valid, message = validate_data(data)

    if not is_valid:
        return jsonify({'error': message}), 400

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
            UPDATE students
            SET firstname = ?, lastname = ?, rom = ?, math = ?, engl = ?
            WHERE cnp = ?
            ''',
            (
               data['firstname'],
               data['lastname'],
               data['rom'],
               data['math'],
               data['engl'],
               data['cnp']
            )
        )
        connection.commit()

    return jsonify({'message': 'Student updated!'}), 201


@app.delete('/students/<int:student_cnp>')
def delete_student(student_cnp):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT cnp FROM students WHERE cnp = ?', (student_cnp,))
        exists = cursor.fetchone()

        if exists is None:
            return jsonify({'error': 'Students does not exist'}), 404

        cursor.execute('DELETE FROM students WHERE cnp = ?', (student_cnp,))
        connection.commit()

    return jsonify({'message': 'Student deleted'}), 201


if __name__ == '__main__':
    app.run(debug=True)
