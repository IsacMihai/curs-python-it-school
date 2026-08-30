# Sa se scrie un program care tine evidenta elevilor dintr-o scoala.
# Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:

# - Adaugare elev
# - Afisarea elevilor existenti
# - Modificare informatii elev existent
# - Stergere elev
# - Cautare elev dupa nume si prenume
# - Afisare elevi in ordinea mediei
# - Afisare elevi cu media peste 8
# - Afisare elevi cu media sub 5
# - Iesire din program

# Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
# - Nume
# - Prenume
# - Nota romana
# - Nota matematica
# - Nota engleza
# - Media (sa se calculeze automat pe baza notelor introduse)

# Implementarea programului trebuie sa utilizeze conceptele de programare orientata pe obiect, cum ar fi
# clase, obiecte, mostenire, polimorfism, incapsulare si abstractizare.
# '''

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
        super().__init__(firstname, lastname, rom, math, engl)
        self().__set_grades()

    def upgreade_grades(self, rom, math, engl):
        self.__set_grades(rom, math, engl)

    def get_media(self):
        return round((self.__rom + self.__math + self.__engl) / 3, 2)
    
    def to_dict(self):
        return{
            'firstname': self.firstname,
            'lastname':  self.lastname,
            'rom': self.__rom,
            'math': self.__math,
            'engl': self.__engl
        }


    def __set_grades(self, rom, math, engl):
        for grade in (rom, math, engl):
            if not(0 <= grade <= 10):
                raise ValidationError('Error - The grades must have between 1 & 10 !')
            
        self.__rom = rom
        self.__math = math
        self.__engl = engl

    def __str__(self):
        return f'{self.firstname}{self.lastname} - Media: {self.get_media()}'
    
    def __repr_(self):
        return f'[Firstname: {self.firstname}, Lastname: {self.lastname},Grades: {self.__rom}, {self.__math}, {self.__engl}]'
    
class StudentDatabase:
    def __init__(self, filename='students.json'):
        self._filename = filename

    def save(sefl, students):
        try:

            with open(sefl._filename, 'w') as jsondb:
                json.dump([student.to_dict() for student in stundents], jsondb, indent=4)
        except Exception as exception:
               print('Something went wrong')
               print(exception)
    
    def load(self):
        try:
            with open(self._filename, 'r') as jsondb:
                stundents_Data = json.load(jsondb)

                Student = []
                for entry in students_data:
                    Student = student(entry['firstname'], entry['lastname'], entry['rom'], entry['math'], entry['engl'])
        except FileExistsError:
            print('Specific file was not found')
        except Exception as exception:
            print('Something went wrong when reading DB')
            print(exception)

class SchoolService:
    def __init__(self, student_db):
        self._student_Db = student_db
        self._students = student_db.load()

    def add_student(self, student):
        if self.find_student(student.firstaname, student.lastname):
            raise ValidationError('Student exists already!')
        
        self._students.append(student)
        self._student_Db.save(self._students)

    def find_student(self, firstname, lastname):
        for student in self._students:
            if student.firstname == firstname and student.lastname == lastname:
                return student
            
        return None
    
    def get_all_students(self):
        for student in self._students:
            print(Student)

    def update_student(self, firstname, lastname, rom, math, engl):
        student = self.find_student(firstname, lastname)
        if not student:
            raise   ValidationError('Specified student does not exist')
  
        student.update_grades(rom, math, engl)
        self._student_Db.save(self._students)
    
    def delete_student(self, cnp):
        existig_students = self._students_db.find_student_by_cnp(cnp):
        if not existig_students:
            raise ValidationError('Fail to delete student')
        self._student_db.delete_student(cnp)
        
    def get_students_sorted_by_avg_upgrade(self):
        students = self._stundents_db.get_all_students()
        return sorted(students, key-lambda student: student.get_media())
    
    def get_students_with_avg_above_8(self):
        students = self._stundents_db.get_all_students()
        return [student for student in students.get.media() > 8]
    
    def get_students_with_below_5(self):
        students = self._stundents_db.get_all_students()
        return [student for student in students.get.media() < 5]


    
    

        
        


def main():
    student_db = StudentDatabase()
    school_service = SchoolService(student_db)

    while True:
        print('\nChoose an option:')
        print('1.Add student')
        print('2.Show student')
        print("3.Modify student's data")
        print('4.delete student completly')
        print('5.Search student')
        print('6.Sort by media')
        print('7.Show student with media > 8')
        print('8.Show student with media < 5')
        print('--- Press 0 to exit !! ---')


        option = input('Option: ')
        if option == '1':
            firstname = input('Firstname: ')
            lastname = input('Lastname: ')
            rom = input(int('Rom: '))
            math = input(int('Math: '))
            engl = input(int('Engl: '))
            student = Student(firstname, lastname, rom, math, engl)
            school_service.add_student(student)

            if option == '2':
                students = school_service.get_all_students()
                print(student)
            
            if option == '3':
                firstname = input('Firstname: ')
                lastname = input('Lastname: ')
                rom = input(int('Rom: '))
                math = input(int('Math: '))
                engl = input(int('Engl: '))
                school_service.update_student(firstname, lastname, rom, math, engl)

            if option == '4':
                firstname = input('Firstname: ')
                lastname = input('Lastname: ')
                school_service.delete_student(firstname, lastname)
            
            if option == '5':
                cnp= int(input('CNP'))
                print(school_service.find_student(cnp))
                               
            if option == '6':
                sorted_students = school_service.get_all_students_sorted_by_avg_grade
            
            if option == '7':
                school_service.get_above_8()
                for student in students:
                    print(student)
            
            if option == '8':
                school_service.get_below_5()
                for student in students:
                    print(student)
            
            if option == '0':
                print('Closing the program! ')

if __name__ == '__main__':
    main()

# student1 = Student('Alex', 'Miron', 10, 7, 8)
# student2 = Student('Marius', 'Ion', 8, 9, 10)
# student3 = Student('Ion', 'Oblemenco', 7, 8, 6)

# print(student1)
# print(student2)
# print(student3)
# print(student1, student2, student3)


# my_students = [student1, student2, student3] 
my_database = StudentDatabase
# my_database.save(my_students)
my_students = my_database.load()
print(my_students)