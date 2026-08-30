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
- CNP
- Nume
- Prenume
- Nota romana
- Nota matematica
- Nota engleza
- Media (sa se calculeze automat pe baza notelor introduse)

Implementarea programului trebuie sa utilizeze conceptele de programare orientata pe obiect, cum ar fi clase, obiecte, mostenire, polimorfism, incapsulare si abstractizare.
Si o baza de date SQLlite pentru stocarea informatiilor despre elevi impreuna cu o interfata grafica reazilata cu Tkinter.
'''


import sqlite3
import tkinter
import tkinter.ttk
import tkinter.messagebox


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


class SchoolService:
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

    def get_students_sorted_by_avg_grade(self):
        students = self._student_db.get_all_students()
        return sorted(students, key=lambda student: student.get_media())

    def get_students_with_avg_above_8(self):
        students = self._student_db.get_all_students()
        return [student for student in students if student.get_media() > 8]

    def get_students_with_avg_below_5(self):
        students = self._student_db.get_all_students()
        return [student for student in students if student.get_media() < 5]


class SchoolApp:
    def __init__(self, window, school_service):
        self._window = window
        self._school_service = school_service

        self._build_interface()
        self._refresh_treeview(self._school_service.get_all_students())


    def _build_interface(self):
        self._window.title('School App')
        self._window.geometry('500x400')
        self._window.resizable(True, True)

        tkinter.Label(self._window, text='CNP').grid(row=0, column=0)
        self._cnp_entry = tkinter.Entry(self._window)
        self._cnp_entry.grid(row=0, column=1)

        tkinter.Label(self._window, text='Firstname').grid(row=1, column=0)
        self._firstname_entry = tkinter.Entry(self._window)
        self._firstname_entry.grid(row=1, column=1)

        tkinter.Label(self._window, text='Lastname').grid(row=2, column=0)
        self._lastname_entry = tkinter.Entry(self._window)
        self._lastname_entry.grid(row=2, column=1)

        tkinter.Label(self._window, text='Rom').grid(row=3, column=0)
        self._rom_entry = tkinter.Entry(self._window)
        self._rom_entry.grid(row=3, column=1)

        tkinter.Label(self._window, text='Math').grid(row=4, column=0)
        self._math_entry = tkinter.Entry(self._window)
        self._math_entry.grid(row=4, column=1)

        tkinter.Label(self._window, text='Engl').grid(row=5, column=0)
        self._engl_entry = tkinter.Entry(self._window)
        self._engl_entry.grid(row=5, column=1)

        tkinter.Button(self._window, text='Add student', command=self._add_student).grid(row=0, column=2)
        tkinter.Button(self._window, text='Find student', command=self._find_student).grid(row=1, column=2)
        tkinter.Button(self._window, text='Show students', command=self._show_all_students).grid(row=2, column=2)
        tkinter.Button(self._window, text='Update student', command=self._update_student).grid(row=3, column=2)
        tkinter.Button(self._window, text='Delete student', command=self._delete_student).grid(row=4, column=2)

        tkinter.Button(self._window, text='Sort by average', command=self._sort_by_avg).grid(row=0, column=3)
        tkinter.Button(self._window, text='Show students above 8', command=self._show_above_8).grid(row=1, column=3)
        tkinter.Button(self._window, text='Show students below 5', command=self._show_below_5).grid(row=2, column=3)

        tkinter.Button(self._window, text='Clear form', command=self._clear_form).grid(row=4, column=3)

        columns = ('cnp', 'firstname', 'lastname', 'rom', 'math', 'engl', 'avg')
        self._students_tree = tkinter.ttk.Treeview(self._window, columns=columns, show='headings')
        self._students_tree.grid(row=6, column=0, columnspan=4, pady=10)

        self._students_tree.heading('cnp', text='CNP')
        self._students_tree.heading('firstname', text='Firstname')
        self._students_tree.heading('lastname', text='Lastname')
        self._students_tree.heading('rom', text='Rom')
        self._students_tree.heading('math', text='Math')
        self._students_tree.heading('engl', text='Engl')
        self._students_tree.heading('avg', text='Avg')

        self._students_tree.column('cnp', width=100)
        self._students_tree.column('firstname', width=100)
        self._students_tree.column('lastname', width=100)
        self._students_tree.column('rom', width=50)
        self._students_tree.column('math', width=50)
        self._students_tree.column('engl', width=50)
        self._students_tree.column('avg', width=50)

        self._students_tree.bind('<<TreeviewSelect>>', self._on_student_select)


    def _refresh_treeview(self, students):
        for item in self._students_tree.get_children():
            self._students_tree.delete(item)

        for student in students:
            self._students_tree.insert('', tkinter.END, values=(*student.to_row(), student.get_media()))


    def _clear_form(self):
        self._cnp_entry.delete(0, tkinter.END)
        self._firstname_entry.delete(0, tkinter.END)
        self._lastname_entry.delete(0, tkinter.END)
        self._rom_entry.delete(0, tkinter.END)
        self._math_entry.delete(0, tkinter.END)
        self._engl_entry.delete(0, tkinter.END)


    def _add_student(self):
        cnp = int(self._cnp_entry.get())
        firstname = self._firstname_entry.get()
        lastname = self._lastname_entry.get()
        rom = int(self._rom_entry.get())
        math = int(self._math_entry.get())
        engl = int(self._engl_entry.get())

        student = Student(cnp, firstname, lastname, rom, math, engl)
        self._school_service.add_student(student)
        self._refresh_treeview(self._school_service.get_all_students())
        self._clear_form()


    def _find_student(self):
        cnp = int(self._cnp_entry.get())
        if not cnp:
            tkinter.messagebox.showwarning('Warning', 'CNP is required to find a student!')
            return

        student = self._school_service.find_student(cnp)
        if student:
            self._refresh_treeview([student])
        else:
            tkinter.messagebox.showwarning('Warning', 'Student not found!')


    def _show_all_students(self):
        self._refresh_treeview(self._school_service.get_all_students())


    def _on_student_select(self, event):
        selected_item = self._students_tree.selection()
        if selected_item:
            item_values = self._students_tree.item(selected_item)['values']
            cnp, firstname, lastname, rom, math, engl, _ = item_values

            self._clear_form()
            self._cnp_entry.insert(0, cnp)
            self._firstname_entry.insert(0, firstname)
            self._lastname_entry.insert(0, lastname)
            self._rom_entry.insert(0, rom)
            self._math_entry.insert(0, math)
            self._engl_entry.insert(0, engl)


    def _update_student(self):
        cnp = self._cnp_entry.get()
        if not cnp:
            tkinter.messagebox.showwarning('Warning', 'CNP is required to update a student!')
            return

        rom = int(self._rom_entry.get())
        math = int(self._math_entry.get())
        engl = int(self._engl_entry.get())
        if not (rom and math and engl):
            tkinter.messagebox.showwarning('Warning', 'All grades need to be filled!')

        self._school_service.update_student(cnp, rom, math, engl)
        self._refresh_treeview(self._school_service.get_all_students())
        self._clear_form()

        tkinter.messagebox.showinfo('Info', 'Successfully updated the student!')


    def _delete_student(self):
        pass


    def _sort_by_avg(self):
        sorted_students = self._school_service.get_students_sorted_by_avg_grade()
        self._refresh_treeview(sorted_students)


    def _show_above_8(self):
        pass

    def _show_below_5(self):
        pass


def main():
    student_db = StudentDatabase()
    school_service = SchoolService(student_db)

    window = tkinter.Tk()
    SchoolApp(window, school_service)
    window.mainloop()


if __name__ == "__main__":
    main()
