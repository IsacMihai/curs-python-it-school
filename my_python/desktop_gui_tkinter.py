'''
Interfata grafica (GUI)
    - modul utilizat -> tkinter (face parte din pachetul de baza, nu necesita instalare)

    - Pentru crearea ferestrei principale folosim -> tkinter.Tk()
        Exemplu: window = tkinter.Tk()

        - Pentru a afisa un titlu pentru aplicatie/fereastra creata -> window.title()
            Exemplu: window.title("Titlul aplicatiei")

        - Pentru a defini dimensiunea ferestrei -> window.geometry()
            Exemplu: window.geometry("400x300") # latime x inaltime

        - Pentru a nu da posibilitatea schimbarii dimensiunii -> window.resizable()
            Exemplu: window.resizable(False, False)

        - Pentru a mentine interfata activa -> window.mainloop()

    - Pentru adaugare de widgets (text, user input, button)
        1) Text - afiseaza text -> tkinter.Label().pack()
            Exemplu: tkinter.Label(window, text='Exemplu text')

        2) User input - locatie unde utilizatorul poate introduce valori -> tkinter.Entry()
            Exemplu: user_input = tkinter.Entry(window).pack()

        3) Button - buton care da trigger la o functionalitate -> tkinter.Button()
            Exemplu:
            def greet():
                tkinter.Label(window, text=f'Hello from app!').pack()

            tkinter.Button(window, text='Greet', command=greet).pack()

    - Pentru organizarea widget-urilor in interfata (pack, grid, place)
        1) pack() - pozitioneaza automat widget-urile pe verticala, de sus in jos sau orizontal
            * util pentru dezvoltare de UI simple, dar are control limitat legat de pozitionare

        2) grid() - pozitioneaza elementele pe baza de linii si coloane (precum un spreadsheet)
            * util pentru dezvoltare de UI pentru completare de formulare si pentru aliniere de widgets
            ! NU poate fi folosit in acelasi context cu pack()

        3) place() - pozitioneaza elementele pe baza coordonatelor exacte (x si y)
            * permite pozitionarea widgeturilor la pozitii exacte
            - nu este foarte responsive si e greu de intretinut

    - Pentru afisare de informatii (Label, Text, Listbox)
        1) Label() - pentru a afisa rezultate si in general mesaje scurte

        2) Text() - pentru a afisa rezultate pe mai multe linii, blocuri mai mari de text

        3) Label() + StringVar() - pentru update dinamic al mesajului

        4) Listbox() - pentru a afisa o lista da elemente (nume, note etc.)

    - Pentru afisarea de pop-up messages (messagebox)
        1) messagebox.showinfo()

        2) messagebox.showwarning()

        3) messagebox.showerror()

    - Pentru a afisa lista de optiuni (Combobox)
        * avem nevoie de ttk din tkinter -> tkinter.ttk.Combobox()

    - Pentru afisare tabelara (Treeview)
        * avem nevoie de ttk din tkinter -> tkinter.ttk.Treeview()
'''

import tkinter

window = tkinter.Tk()
window.title('Prima mea interfata bengoasa')
window.geometry('400x300')
window.resizable(True, True)


# tkinter.Label(window, text='Paul a venit cu ideea').pack()

# user_input = tkinter.Entry(window)

# def greet():
#     tkinter.Label(window, text=f'Hello from app!').pack()

# tkinter.Button(window, text='Greet', command=greet).pack()

# tkinter.Label(window, text='Nume:').pack()
# name_entry = tkinter.Entry(window)
# name_entry.pack()

# def greet():
#     name = name_entry.get()
#     tkinter.Label(window, text=f'Hello {name}!').pack()

# def greet_internal():
#     name = name_entry.get()
#     print(name)

# tkinter.Button(window, text='Greet', command=greet).pack()
# tkinter.Button(window, text='Print in terminal', command=greet_internal).pack()


# tkinter.Label(window, text='Nume:').grid(row=0, column=0)
# name_entry = tkinter.Entry(window)
# name_entry.grid(row=0, column=1)

# output_label = tkinter.Label(window, text='')
# output_label.grid(row=0, column=2)

# def greet():
#     name = name_entry.get()
#     output_label.config(text=f'Hello {name}!')

# tkinter.Button(window, text='Greet', command=greet).grid(row=1, column=2)


# text_output = tkinter.Text(window, height=5, width=30)
# text_output.pack()

# person = tkinter.Entry(window)
# person.pack()

# my_list = ['Ionel', 'Dorel', 'Cosmin']

# def display_message():
#     text_output.delete('1.0', tkinter.END)
#     text_output.insert(tkinter.END, 'This is the list of persons:\n')
#     for element in my_list:
#         text_output.insert(tkinter.END, f'{element}\n')

# def add_person():
#     person_name = person.get()
#     my_list.append(person_name)
#     text_output.insert(tkinter.END, f'{person_name}\n')

# tkinter.Button(window, text='Display', command=display_message).pack()
# tkinter.Button(window, text='Add person', command=add_person).pack()



# output_var = tkinter.StringVar()

# tkinter.Label(window, textvariable=output_var).pack()
# tkinter.Entry(window, textvariable=output_var).pack()



# output_var = tkinter.IntVar()
# tkinter.Label(window, textvariable=output_var).pack()

# text_output = tkinter.Text(window, height=5, width=30)
# text_output.pack()

# person = tkinter.Entry(window)
# person.pack()

# my_list = ['Ionel', 'Dorel', 'Cosmin']

# def display_message():
#     text_output.delete('1.0', tkinter.END)
#     text_output.insert(tkinter.END, 'This is the list of persons:\n')
#     for element in my_list:
#         text_output.insert(tkinter.END, f'{element}\n')

# def add_person():
#     person_name = person.get()
#     my_list.append(person_name)
#     output_var.set(len(my_list))
#     text_output.insert(tkinter.END, f'{person_name}\n')

# tkinter.Button(window, text='Display', command=display_message).pack()
# tkinter.Button(window, text='Add person', command=add_person).pack()

#  output_var.get() output_var.set()



# entry = tkinter.Entry(window)
# entry.pack()

# listbox = tkinter.Listbox(window)
# listbox.pack()

# def add_person():
#     name = entry.get()
#     if name:
#         listbox.insert(tkinter.END, name)
#         entry.delete(0, tkinter.END)

# def show_selected():
#     selection = listbox.curselection()
#     if selection:
#         selected_value = listbox.get(selection[0])
#         print(selected_value)

# tkinter.Button(window, text='Add person', command=add_person).pack()
# tkinter.Button(window, text='Delete selected item', command=show_selected).pack()



# entry = tkinter.Entry(window)
# entry.pack()

# listbox = tkinter.Listbox(window)
# listbox.pack()

# persons = []

# def add_person():
#     name = entry.get()
#     if name:
#         persons.append(name)
#         listbox.insert(tkinter.END, name)
#         entry.delete(0, tkinter.END)

# def delete_selected():
#     selection = listbox.curselection()
#     if selection:
#         selected = listbox.get(selection[0])
#         print(f'List before: {persons}')
#         persons.remove(selected)
#         print(f'List after: {persons}')
#         listbox.delete(selection[0])

# tkinter.Button(window, text='Add person', command=add_person).pack()
# tkinter.Button(window, text='Delete selected item', command=delete_selected).pack()


# import tkinter.messagebox

# entry = tkinter.Entry(window)
# entry.pack()

# listbox = tkinter.Listbox(window)
# listbox.pack()

# persons = []

# def add_person():
#     name = entry.get()
#     if name:
#         persons.append(name)
#         listbox.insert(tkinter.END, name)
#         entry.delete(0, tkinter.END)
#         tkinter.messagebox.showinfo('Succes', f'{name} has been added!')
#     else:
#         tkinter.messagebox.showwarning('Warning', 'Please complete the name field!')

# def delete_selected():
#     selection = listbox.curselection()
#     if selection:
#         selected = listbox.get(selection[0])
#         print(f'List before: {persons}')
#         persons.remove(selected)
#         print(f'List after: {persons}')
#         listbox.delete(selection[0])
#         tkinter.messagebox.showinfo('Success', f'{selected} deleted successfully!')
#     else:
#         tkinter.messagebox.showerror('Error', 'No selected name!')

# tkinter.Button(window, text='Add person', command=add_person).pack()
# tkinter.Button(window, text='Delete selected item', command=delete_selected).pack()

import tkinter.ttk

# options = ['Python', 'C++', 'C#']
# dropdown = tkinter.ttk.Combobox(window, values=options)
# dropdown.pack()

# def show_selected():
#     selected = dropdown.get()
#     print(f'Selected language: {selected}')

# tkinter.Button(window, text='Show selected', command=show_selected).pack()



# cap_tabel = ('Name', 'Math', 'English')
# tree = tkinter.ttk.Treeview(window, columns=cap_tabel, show='headings')
# tree.pack()

# # for element in cap_tabel:
# #     tree.heading(element, text=element)

# tree.heading('Name', text='Nume')
# tree.heading('Math', text='Math grade')
# tree.heading('English', text='English grade')

# tree.insert('', tkinter.END, values=('Maria', 10, 9))
# tree.insert('', tkinter.END, values=('Ionela', 8, 10))


# cap_tabel = ('Name', 'Math', 'English')
# tree = tkinter.ttk.Treeview(window, columns=cap_tabel, show='tree headings')
# tree.pack()

# tree.heading('#0', text='Clasa')
# tree.heading('Name', text='Nume')
# tree.heading('Math', text='Math grade')
# tree.heading('English', text='English grade')

# class_a = tree.insert('', tkinter.END, text='Class A', open=True)
# class_b = tree.insert('', tkinter.END, text='Class B', open=True)

# tree.insert(class_a, tkinter.END, text='', values=('Maria', 10, 9))
# tree.insert(class_a, tkinter.END, text='', values=('Mihai', 8, 9))
# tree.insert(class_b, tkinter.END, text='', values=('Dani', 7, 9))
# tree.insert(class_b, tkinter.END, text='', values=('Laurentiu', 8, 5))


cap_tabel = ('Name', 'Math', 'English')
tree = tkinter.ttk.Treeview(window, columns=cap_tabel, show='headings')
tree.pack()

# for element in cap_tabel:
#     tree.heading(element, text=element)

# tree.heading('Name', text='Nume')
# tree.heading('Math', text='Math grade')
# tree.heading('English', text='English grade')

# tree.insert('', tkinter.END, values=('Maria', 10, 9))
# tree.insert('', tkinter.END, values=('Ionela', 8, 10))


# def load_student_data(event):
#     selected = tree.focus()
#     print(selected)
#     print(event)
#     values = tree.item(selected, 'values')
#     print('Row: ', values)

# tree.bind('<ButtonRelease-1>', load_student_data)

# window.mainloop()
