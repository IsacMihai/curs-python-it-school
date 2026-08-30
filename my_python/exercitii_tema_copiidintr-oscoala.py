# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

#implementarea programului trebuie sa utilizeze concepte de proramare orientate pe obiecte, cum ar fi  clase, obiecte,

# import sqlite3

# class Person:
#     def __init__(self, firstname, lastname):
#         self.cnp = cnp
#         self.firstname = firstname
#         self.lastname = lastname

#     def present(self):
#         print(f'My name is:L {self.firstname}{self.lastname}')

# class student(Person):
#     def __init__(self, cnp, firstname, lastname, rom, math, engl):
#         super().__init__(firstname, lastname)
#         self.__set_grades(rom, math, engl)

#     def update_grades(self, rom, math, engl):
#         self.__set_grades(rom, math, engl)

#     def get_media(self):
#         return round((self.__rom + self.__math + self.__engl) / 3, 2)
    
    
#     def to_row(self):
#         return (    
#             self.cnp,
#             self.firstname,
#             self.lastname,
#             self.__rom,
#             self.__math,
#             self.__engl
#         )
        
#     def __set_grades(self, rom, math, engl):
#         for grade in (rom, math, engl):
#             if not (1 <= grade <= 10):
#                 raise ValidationError('Error - Grades must have value.')
            
#         self.__rom = rom
#         self.__math = math
#         self.__engl = engl

#     def __str__(self):
#         return f'{self.firstname} {self.lastname} - Media: {self.get_media}'
    
#     def __repr_(self):
#         return f'(CNP: {self.cnp}, Firstname: {self.firstname}, Lastname: {self.lastname})'
    
#     class StudentDatabase:
#          def __init__(self, db_name='stundents.db'):
#              self._db_name = db_name
#              self._create_table()

#          def _create_table(self):
#              with sqlite3.connect(self._db_name) as connection:
#                  cursor = connection.cursor()
#                  cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS STUDENTS (
#                                 cnp INTEGER PRIMARY KEY,
#                                 firstname TEXT NOT NULL,
#                                 lastname TEXT NOT NULL,
#                                 rom INTEGER NOT NULL,
#                                 math INTEGER NOT NULL,
#                                 engl INTEGER NOT NULL
#                                 ) 
#                  ''')
#                  connection.commit()
         
#          def find_student_by_cnp(self, cnp):
#              with sqlite3.connect(self._db_name) as connection:
#                  cursor = connection.cursor()
#                  cursor.execute('''
#                                 SELECT * FROM students WHERE cnp = ?
#                                 ''', (cnp))
#                  row = cursor.fetchone()
#                  if row:
#                      cnp, firstname, lastname, rom, math, engl = row
#                      return Student(cnp, firstname, lastname, rom, math, engl)
                 
#                  return None
             
#          def add_student(self, student):
#              with sqlite3.connect(self._db_name) as connection:
#                  cursor = connection.cursor()
#                  cursor.execute('''
#                                 INSERT INTO students (cnp, firstname, lastname, rom, math, engl)
#                                 VALUES (?, ?, ?, ?, ?, ?)
#                                 ''', student.ro_row())
#                  connection.commit()

#          def get_all_students(self):
#              with sqlite3.connect(self._db_name) as connection:
#                  cursor = connection.cursor()
#                  cursor.execute('SELECT * FROM students')
#                  rows = cursor.fetchall
                 
#                  students = []
#                  for row in rows:
#                      cnp, firstname, lastname, rom, math, engl = row
#                      student = Student(cnp, firstname, lastname, rom, math, engl)
#                      students.append()

#                      return students
#                      #return [Student(*row) for row in row

# my_db = StudentDatabase()
# my_db.add_student(Student(123456, 'Mihai', 'Isac', 10, 9, 8))
# print(my_db.get_all_students())
# student = my_db.find_student_by_cnp(123456)
# if student:
#     print(student)
# else:
#     print("Nu exista.")

#varianta copiata


import sqlite3

class ValidationError(Exception):
    pass


class Person:
    def __init__(self, cnp, firstname, lastname):
        self.cnp = cnp
        self.firstname = firstname
        self.lastname = lastname

    def present(self):
        print(f'My name is: {self.firstname} {self.lastname}')


class Student(Person):
    def __init__(self, cnp, firstname, lastname, rom, math, engl):
        super().__init__(cnp, firstname, lastname)
        self.__set_grades(rom, math, engl)

    def update_grades(self, rom, math, engl):
        self.__set_grades(rom, math, engl)

    def get_media(self):
        return round((self.__rom + self.__math + self.__engl) / 3, 2)

    def to_row(self):
        return (
            self.cnp,
            self.firstname,
            self.lastname,
            self.__rom,
            self.__math,
            self.__engl
        )

    def __set_grades(self, rom, math, engl):
        for grade in (rom, math, engl):
            if not (1 <= grade <= 10):
                raise ValidationError('Error - Grades must have values between 1 and 10!')

        self.__rom = rom
        self.__math = math
        self.__engl = engl

    def __str__(self):
        return f'{self.firstname} {self.lastname} - Media: {self.get_media()}'

    def __repr__(self):
        return f'(CNP: {self.cnp}, Firstname: {self.firstname}, Lastname: {self.lastname}, Grades: {self.__rom}, {self.__math}, {self.__engl})'


class StudentDatabase:
    def __init__(self, db_name='exercitiu_students.db'):
        self._db_name = db_name
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    cnp INTEGER PRIMARY KEY,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    rom INTEGER NOT NULL,
                    math INTEGER NOT NULL,
                    engl INTEGER NOT NULL
                )
            ''')
            connection.commit()

    def find_student_by_cnp(self, cnp):
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM students WHERE cnp = ?
            ''', (cnp,))
            row = cursor.fetchone()
            if row:
                cnp, firstname, lastname, rom, math, engl = row
                return Student(cnp, firstname, lastname, rom, math, engl)
                #return  Student(*row)

            return None

    def add_student(self, student):
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO students (cnp, firstname, lastname, rom, math, engl)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', student.to_row())
            connection.commit()

    def get_all_students(self):
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM students')
            rows = cursor.fetchall()

            students = []
            for row in rows:
                cnp, firstname, lastname, rom, math, engl = row
                student = Student(cnp, firstname, lastname, rom, math, engl)
                students.append(student)

            return students
            # return [Student(*row) for row in rows]

    def update_student(self, cnp, rom, math, engl):
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE students
                SET rom = ?, math = ?, engl = ?
                WHERE cnp = ?
                ''', (rom, math, engl, cnp))
            connection.commit()

    def delete_student(self, cnp):
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM students WHERE cnp = ?', (cnp,))
            connection.commit()


class SchoolSerice:
    def __init__(self, student_db):
        self._student_db = student_db

    def add_student(self, student):
        existing_student = self._student_db.find_student_by_cnp(student.cnp)
        if existing_student:
            raise ValueError('Failed to add student as he/she already exists!')
        self._student_db.add_student(student)

    def find_student(self, cnp):
        return self._student_db.find_student_by_cnp(cnp)

    def get_all_students(self):
        return self._student_db.get_all_students()

    def update_student(self, cnp, rom, math, engl):
        existing_student = self._student_db.find_student_by_cnp(cnp)
        if not existing_student:
            raise ValueError('Failed to update student as he/she does not exist!')
        self._student_db.update_student(cnp, rom, math, engl)

    def delete_student(self, cnp):
        existing_student = self._student_db.find_student_by_cnp(cnp)
        if not existing_student:
            raise ValueError('Failed to delete student as he/she does not exist!')
        self._student_db.delete_student(cnp)


def main():
    student_db = StudentDatabase()
    school_service = SchoolSerice(student_db)

    while True:
        print("\nChoose an option : ")
        print('1. Add student')
        print('2. Show students')
        print("3. Modify student's data")
        print('4. Delete student completly')
        print('5. Search student')
        print('6. Sort by media')
        print('7. Show students with media > 8')
        print('---- Press 0 to exit !!! ----')

        option = input('Option: ')
        try:
            if option == '1':
                cnp = int(input('CNP:'))
                firstname = input('Firstname: ')
                lastname = input('Lastname: ')
                rom = int(input('Rom: '))
                math = int(input('Math: '))
                engl = int(input('Engl: '))
                student = Student(cnp, firstname, lastname, rom, math, engl)
                school_service.add_student(student)

            if option == '2':
                school_service.get_all_students()

            if option == '3':
                cnp = int(input('CNP:'))
                rom = int(input('Rom: '))
                math = int(input('Math: '))
                engl = int(input('Engl: '))
                school_service.update_student(cnp, rom, math, engl)

            if option == '4':
                cnp = int(input('CNP:'))
                school_service.delete_student(cnp)

            if option == '5':
                cnp = int(input('CNP:'))
                print(school_service.find_student(cnp))

            if option == '6':
                school_service.sort_by_avg_grade()

            if option == '7':
                school_service.get_above_8()

            if option == '8':
                school_service.get_below_5()

            if option == '0':
                print('Closing the program!')
                break

        except ValidationError as exception:
            print('System error', exception)


if __name__ == '__main__':
    main()



