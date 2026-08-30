'''
Sa se scrie un program care tine evidenta elevilor dintr-o scoala.
Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:

- Adaugare elev
- Afisarea elevilor existenti
- Modificare informatii elev existent
- Stergere elev
- Cautare elev dupa nume si prenume
- Afisare elevi in ordinea mediei
- Afisare elevi cu media peste 8
- Afisare elevi cu media sub 5
- Iesire din program

Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
- Nume
- Prenume
- Nota romana
- Nota matematica
- Nota engleza
- Media (sa se calculeze automat pe baza notelor introduse)

Implementarea programului trebuie sa utilizeze conceptele de programare orientata pe obiect, cum ar fi
clase, obiecte, mostenire, polimorfism, incapsulare si abstractizare.
'''


import json


class ValidationError(Exception):
    pass


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def present(self):
        print(f'My name is: {self.firstname} {self.lastname}')


class Student(Person):
    def __init__(self, firstname, lastname, rom, math, engl):
        super().__init__(firstname, lastname)
        self.__set_grades(rom, math, engl)

    def update_grades(self, rom, math, engl):
        self.__set_grades(rom, math, engl)

    def get_media(self):
        return round((self.__rom + self.__math + self.__engl) / 3, 2)

    def to_dict(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'rom': self.__rom,
            'math': self.__math,
            'engl': self.__engl
        }

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
        return f'[Firstname: {self.firstname}, Lastname: {self.lastname}, Grades: {self.__rom}, {self.__math}, {self.__engl}]'


class StudentDatabase:
    def __init__(self, filename='students.json'):
        self._filename = filename

    def save(self, students):
        try:
            with open(self._filename, 'w') as jsondb:
                json.dump([student.to_dict() for student in students], jsondb, indent=4)
        except Exception as exception:
            print('Something went wrong when writing to DB!')
            print(exception)

    def load(self):
        try:
            with open(self._filename, 'r') as jsondb:
                students_data = json.load(jsondb)

                students = []
                for entry in students_data:
                    student = Student(entry['firstname'], entry['lastname'], entry['rom'], entry['math'], entry['engl'])
                    students.append(student)

                return students

        except FileNotFoundError:
            print('Specified DB file was not found!')
        except Exception as exception:
            print('Something went wrong when reading from DB!')
            print(exception)


class SchoolService:
    def __init__(self, student_db):
        self._student_db = student_db
        self._students = student_db.load()

    def add_student(self, student):
        if self.find_student(student.firstname, student.lastname):
            raise ValidationError("Student already exists!")

        self._students.append(student)
        self._student_db.save(self._students)

    def find_student(self, firstname, lastname):
        for student in self._students:
            if student.firstname == firstname and student.lastname == lastname:
                return student

        return None


def main():
    student_db = StudentDatabase()
    school_service = SchoolService(student_db)

    while True:
        print('\nChoose an option:')
        print('1.Add student')

        option = input('Option: ')
        if option == '1':
            firstname = input('Firstname: ')
            lastname = input('Lastname: ')
            rom = int(input('Rom: '))
            math = int(input('Math: '))
            engl = int(input('Engl: '))
            student = Student(firstname, lastname, rom, math, engl)
            school_service.add_student(student)


if __name__ == '__main__':
    main()

# student1 = Student('Alex', 'Miron', 10, 7, 8)
# student2 = Student('Marina', 'Ionescu', 6, 7, 10)
# student3 = Student('Maria', 'Marinescu', 9, 7, 6)
# student4 = Student('Daniel', 'Neamtiu', 11, 10, -1)

# print(student1)
# print(student2)
# print(student3)
# print([student1, student2, student3])
# print(student1.to_dict())

# my_students = [student1, student2, student3]
# my_database = StudentDatabase()
# my_database.save(my_students)
# my_students = my_database.load()
# print(my_students)
