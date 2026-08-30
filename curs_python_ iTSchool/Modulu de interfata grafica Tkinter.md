**În acest modul am construit interfața grafică folosind Tkinter. Clasa SpanzuratoareaApp face legătura între utilizator, logica jocului și baza de date. Am folosit Entry pentru input, Button pentru acțiuni, Combobox pentru dificultate, Treeview pentru tabelul de scoruri și Text pentru raport. Tot aici sunt apelate funcțiile de CRUD, sortare, filtrare și generare raport.”**



**"""Modul pentru interfata grafica Tkinter."""**



**import logging**   -> Am folosit Tkinter pentru interfața grafică, iar ttk pentru elemente mai avansate precum Combobox și Treeview.”

**import tkinter**

**import tkinter.messagebox**

**import tkinter.ttk**

**from datetime import datetime ->** Îl folosești ca să salvezi data și ora când s-a terminat jocul.



**from database import ScorDatabase  ->** Aici imporți clase din celelalte fișiere.

**from game\_logic import JocSpanzuratoarea**

**from reports import RaportScoruri**

“Aici se vede modularizarea: interfața nu conține direct codul bazei de date sau logica jocului, ci le folosește din module separate.



**class SpanzuratoareaApp: ->** clasa aplic grafice , se ocupa cu: construirea ferestrei, porneste jocul, citeste litere introduce, afiseaza scoruri, modifica/sterge scor, sorteaza/filtreaza, genereaza raport

&#x20;   **"""Aplicatia grafica pentru jocul Spanzuratoarea."""**



&#x20;   **def \_\_init\_\_(self, window: tkinter.Tk, scor\_db: ScorDatabase): constructorul,** window= fereastra principala Tkinter, score\_db=obiectul care lucreaza cu baze de date

&#x20;       **self.\_window = window     ->**

&#x20;       **self.\_scor\_db = scor\_db   ->**  salvezi in clasa:Aici salvezi în clasă: fereastra, baza de date, jocul curent

&#x20;       **self.\_joc = None          ->**  înseamnă că la început nu există joc pornit.



&#x20;       **self.\_build\_interface()  ->** Construiește interfața grafică.

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.get\_all\_scoruri())  -** Încarcă scorurile existente din baza de date în tabel.



&#x20;   **def \_build\_interface(self) -> None: ->** Aici creezi toate elementele vizuale: Label, Entry,Button, Combobox, Treeview, Text

&#x20;       **"""Construieste interfata grafica."""**

&#x20;       **self.\_window.title("Spanzuratoarea") ->** Setează titlul ferestrei.

&#x20;       **self.\_window.geometry("950x650")     ->** Setează dimensiunea ferestrei.

&#x20;       **self.\_window.resizable(True, True)**

În metoda \_build\_interface am construit toate widget-urile Tkinter: câmpuri de introducere, butoane, combobox pentru dificultate, tabel pentru scoruri și zonă pentru raport.”





&#x20;       **tkinter.Label(self.\_window, text="Nume jucator").grid(row=0, column=0, padx=5, pady=5) ->** Așază elementele în interfață pe rânduri și coloane.

&#x20;       **self.\_nume\_entry = tkinter.Entry(self.\_window)**

&#x20;       **self.\_nume\_entry.grid(row=0, column=1, padx=5, pady=5)**

“Am folosit grid pentru organizarea elementelor în interfață.”





&#x20;       **tkinter.Label(self.\_window, text="Dificultate").grid(row=1, column=0, padx=5, pady=5)**

&#x20;       **self.\_dificultate\_combo = tkinter.ttk.Combobox(self.\_window, values=\["easy", "medium", "hard"])** ->Este lista din care utilizatorul alege dificultatea.

&#x20;       **self.\_dificultate\_combo.set("easy")**

&#x20;       **self.\_dificultate\_combo.grid(row=1, column=1, padx=5, pady=5)**



&#x20;       **tkinter.Button(self.\_window, text="Start joc", command=self.\_start\_joc).grid(row=2, column=0, padx=5, pady=5) ->**command spune ce funcție se execută când apeși butonul.



&#x20;       **self.\_cuvant\_label = tkinter.Label(self.\_window, text="Cuvant: -", font=("Arial", 18))**

&#x20;       **self.\_cuvant\_label.grid(row=3, column=0, columnspan=3, padx=5, pady=10)**



&#x20;       **tkinter.Label(self.\_window, text="Litera").grid(row=4, column=0, padx=5, pady=5)**

&#x20;       **self.\_litera\_entry = tkinter.Entry(self.\_window, width=10)**

&#x20;       **self.\_litera\_entry.grid(row=4, column=1, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Incearca", command=self.\_incearca\_litera).grid(row=4, column=2, padx=5, pady=5)**



&#x20;       **self.\_mesaj\_label = tkinter.Label(self.\_window, text="Alege dificultatea si apasa Start joc.")**

&#x20;       **self.\_mesaj\_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)**



&#x20;       **self.\_greseli\_label = tkinter.Label(self.\_window, text="Greseli: 0")**

&#x20;       **self.\_greseli\_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)**



&#x20;       **coloane = ("id", "nume", "dificultate", "cuvant", "rezultat", "scor", "greseli", "data")**

&#x20;       **self.\_tree = tkinter.ttk.Treeview(self.\_window, columns=coloane, show="headings") ->** Acesta este tabelul cu scoruri**.**Afișează:id, nume, dificultate, cuvânt, rezultat, scor,greșeli, data

“Am folosit Treeview pentru afișarea tabelară a scorurilor salvate în baza de date.”

&#x20;       **for coloana in coloane:**

&#x20;           **self.\_tree.heading(coloana, text=coloana)**

&#x20;           **self.\_tree.column(coloana, width=100)**

&#x20;       **self.\_tree.grid(row=7, column=0, columnspan=8, padx=5, pady=10)**



&#x20;       **tkinter.Label(self.\_window, text="ID scor").grid(row=8, column=0, padx=5, pady=5)**

&#x20;       **self.\_id\_entry = tkinter.Entry(self.\_window, width=10)**

&#x20;       **self.\_id\_entry.grid(row=8, column=1, padx=5, pady=5)**



&#x20;       **tkinter.Label(self.\_window, text="Nume nou").grid(row=9, column=0, padx=5, pady=5)**

&#x20;       **self.\_nume\_update\_entry = tkinter.Entry(self.\_window)**

&#x20;       **self.\_nume\_update\_entry.grid(row=9, column=1, padx=5, pady=5)**



&#x20;       **tkinter.Label(self.\_window, text="Scor nou").grid(row=10, column=0, padx=5, pady=5)**

&#x20;       **self.\_scor\_update\_entry = tkinter.Entry(self.\_window)**

&#x20;       **self.\_scor\_update\_entry.grid(row=10, column=1, padx=5, pady=5)**



&#x20;       **tkinter.Label(self.\_window, text="Dificultate noua").grid(row=11, column=0, padx=5, pady=5)**

&#x20;       **self.\_dificultate\_update\_combo = tkinter.ttk.Combobox(self.\_window, values=\["easy", "medium", "hard"])**

&#x20;       **self.\_dificultate\_update\_combo.set("easy")**

&#x20;       **self.\_dificultate\_update\_combo.grid(row=11, column=1, padx=5, pady=5)**



&#x20;       **tkinter.Button(self.\_window, text="Modifica scor", command=self.\_modifica\_scor).grid(row=12, column=0, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Sterge scor", command=self.\_sterge\_scor).grid(row=12, column=1, padx=5, pady=5)**



&#x20;       **tkinter.Label(self.\_window, text="Cauta nume").grid(row=8, column=3, padx=5, pady=5)**

&#x20;       **self.\_cauta\_entry = tkinter.Entry(self.\_window)**

&#x20;       **self.\_cauta\_entry.grid(row=8, column=4, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Cauta", command=self.\_cauta\_nume).grid(row=8, column=5, padx=5, pady=5)**



&#x20;       **tkinter.Button(self.\_window, text="Sorteaza dupa nume", command=self.\_sortare\_nume).grid(row=9, column=3, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Cei mai buni", command=self.\_cei\_mai\_buni).grid(row=9, column=4, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Cei mai slabi", command=self.\_cei\_mai\_slabi).grid(row=9, column=5, padx=5, pady=5)**



&#x20;       **tkinter.Button(self.\_window, text="Easy", command=lambda: self.\_filtru\_dificultate("easy")).grid(row=10, column=3, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Medium", command=lambda: self.\_filtru\_dificultate("medium")).grid(row=10, column=4, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Hard", command=lambda: self.\_filtru\_dificultate("hard")).grid(row=10, column=5, padx=5, pady=5)**



&#x20;       **tkinter.Button(self.\_window, text="Afiseaza toate", command=self.\_afiseaza\_toate).grid(row=11, column=3, padx=5, pady=5)**

&#x20;       **tkinter.Button(self.\_window, text="Genereaza raport", command=self.\_genereaza\_raport).grid(row=11, column=4, padx=5, pady=5)**



&#x20;       **self.\_raport\_text = tkinter.Text(self.\_window, height=7, width=50)**

&#x20;       **self.\_raport\_text.grid(row=12, column=3, columnspan=4, padx=5, pady=5)**



&#x20;   **def \_start\_joc(self) -> None: ->** ia numele din Entry, ia dificultatea din Combobox, verifică dacă numele este completat, creează un obiect JocSpanzuratoarea, afișează cuvântul ascuns

&#x20;       **"""Porneste un joc nou."""**

&#x20;       **nume = self.\_nume\_entry.get().strip()**

&#x20;       **dificultate = self.\_dificultate\_combo.get()**



&#x20;       **if not nume: ->**Verifică dacă utilizatorul nu a introdus nume.

&#x20;           **tkinter.messagebox.showwarning("Atentie", "Introdu numele jucatorului!")**

&#x20;           **return**



&#x20;       **self.\_joc = JocSpanzuratoarea(dificultate)**

&#x20;       **self.\_cuvant\_label.config(text=f"Cuvant: {self.\_joc.afiseaza\_cuvant()}")**

&#x20;       **self.\_mesaj\_label.config(text="Joc pornit. Introdu o litera.")**

&#x20;       **self.\_greseli\_label.config(text=f"Greseli: 0 / {self.\_joc.max\_greseli}")**

&#x20;       **logging.info("Joc nou pornit pentru %s.", nume)**



&#x20;   **def \_incearca\_litera(self) -> None: ->** verifică dacă jocul a fost pornit,ia litera din Entry,actualizează cuvântul afișat,verifică dacă jocul e câștigat sau pierdut -> Aici interfața comunică direct cu game\_logic.py.

&#x20;       **"""Proceseaza litera introdusa."""**

&#x20;       **if self.\_joc is None:**

&#x20;           **tkinter.messagebox.showwarning("Atentie", "Trebuie sa pornesti jocul mai intai!")**

&#x20;           **return**



&#x20;       **litera = self.\_litera\_entry.get()**

&#x20;       **mesaj = self.\_joc.incearca\_litera(litera)**

&#x20;       **self.\_litera\_entry.delete(0, tkinter.END)**



&#x20;       **self.\_cuvant\_label.config(text=f"Cuvant: {self.\_joc.afiseaza\_cuvant()}")**

&#x20;       **self.\_mesaj\_label.config(text=mesaj)**

&#x20;       **self.\_greseli\_label.config(text=f"Greseli: {self.\_joc.greseli} / {self.\_joc.max\_greseli}")**



&#x20;       **if self.\_joc.este\_castigat():**

&#x20;           **self.\_salveaza\_joc("castigat")**

&#x20;           **tkinter.messagebox.showinfo("Felicitari", f"Ai castigat! Cuvantul era: {self.\_joc.cuvant}")**

&#x20;           **self.\_joc = None**



&#x20;       **elif self.\_joc.este\_pierdut():**

&#x20;           **self.\_salveaza\_joc("pierdut")**

&#x20;           **tkinter.messagebox.showinfo("Joc pierdut", f"Ai pierdut! Cuvantul era: {self.\_joc.cuvant}")**

&#x20;           **self.\_joc = None**



&#x20;   **def \_salveaza\_joc(self, rezultat: str) -> None: ->**Salvează jocul în baza de date după câștig sau pierdere

&#x20;       **"""Salveaza rezultatul jocului in baza de date."""**

&#x20;       **nume = self.\_nume\_entry.get().strip()**

&#x20;       **scor = self.\_joc.calculeaza\_scor()**

&#x20;       **data\_joc = datetime.now().strftime("%Y-%m-%d %H:%M") ->** pentru data jocului.



&#x20;       **self.\_scor\_db.adauga\_scor( ->** Adică trimite datele către baza de date.

&#x20;           **nume,**

&#x20;           **self.\_joc.dificultate,**

&#x20;           **self.\_joc.cuvant,**

&#x20;           **rezultat,**

&#x20;           **scor,**

&#x20;           **self.\_joc.greseli,**

&#x20;           **data\_joc**

&#x20;       **)**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.get\_all\_scoruri())**



&#x20;   **def \_refresh\_treeview(self, scoruri) -> None: ->** Reîncarcă tabelul., Prima dată șterge ce era afișat:, Apoi introduce scorurile noi:

&#x20;       **"""Reincarca tabelul cu scoruri."""**

&#x20;       **for item in self.\_tree.get\_children():**

&#x20;           **self.\_tree.delete(item)**



&#x20;       **for scor in scoruri:**

&#x20;           **self.\_tree.insert("", tkinter.END, values=scor)**

“Această funcție actualizează tabelul după fiecare operație: adăugare, modificare, ștergere, căutare sau sortare.”





&#x20;   **def \_modifica\_scor(self) -> None: ->** Asta este partea de UPDATE din CRUD.

&#x20;       **"""Modifica scorul selectat pe baza ID-ului."""**

&#x20;       **try:**

&#x20;           **scor\_id = int(self.\_id\_entry.get())**

&#x20;           **nume = self.\_nume\_update\_entry.get().strip()**

&#x20;           **scor = int(self.\_scor\_update\_entry.get())**

&#x20;           **dificultate = self.\_dificultate\_update\_combo.get()**



&#x20;           **if not nume:**

&#x20;               **raise ValueError("Numele este obligatoriu.")**



&#x20;           **if self.\_scor\_db.find\_scor\_by\_id(scor\_id) is None:**

&#x20;               **raise ValueError("Nu exista scor cu acest ID.")**



&#x20;           **self.\_scor\_db.update\_scor(scor\_id, nume, dificultate, scor)**

&#x20;           **self.\_refresh\_treeview(self.\_scor\_db.get\_all\_scoruri())**

&#x20;       **except ValueError as error:**

&#x20;           **tkinter.messagebox.showerror("Eroare", str(error))**



&#x20;   **def \_sterge\_scor(self) -> None: ->** Asta este partea de DELETE din CRUD.

&#x20;       **"""Sterge scorul selectat pe baza ID-ului."""**

&#x20;       **try:**

&#x20;           **scor\_id = int(self.\_id\_entry.get())**

&#x20;           **if self.\_scor\_db.find\_scor\_by\_id(scor\_id) is None:**

&#x20;               **raise ValueError("Nu exista scor cu acest ID.")**

&#x20;           **self.\_scor\_db.delete\_scor(scor\_id)**

&#x20;           **self.\_refresh\_treeview(self.\_scor\_db.get\_all\_scoruri())**

&#x20;       **except ValueError as error:**

&#x20;           **tkinter.messagebox.showerror("Eroare", str(error))**



&#x20;   **def \_cauta\_nume(self) -> None:**

&#x20;       **"""Cauta scorurile dupa nume."""**

&#x20;       **nume = self.\_cauta\_entry.get().strip()**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.cauta\_dupa\_nume(nume))**



&#x20;   **def \_sortare\_nume(self) -> None:**

&#x20;       **"""Sorteaza scorurile dupa nume."""**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.get\_scoruri\_sortate("nume", "ASC"))**



&#x20;   **def \_cei\_mai\_buni(self) -> None:**

&#x20;       **"""Afiseaza scorurile de la cel mai bun la cel mai slab."""**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.get\_scoruri\_sortate("scor", "DESC"))**



&#x20;   **def \_cei\_mai\_slabi(self) -> None:**

&#x20;       **"""Afiseaza scorurile de la cel mai slab la cel mai bun."""**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.get\_scoruri\_sortate("scor", "ASC"))**



&#x20;   **def \_filtru\_dificultate(self, dificultate: str) -> None:**

&#x20;       **"""Filtreaza scorurile dupa dificultate."""**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.filtreaza\_dupa\_dificultate(dificultate))**



&#x20;   **def \_afiseaza\_toate(self) -> None:**

&#x20;       **"""Afiseaza toate scorurile."""**

&#x20;       **self.\_refresh\_treeview(self.\_scor\_db.get\_all\_scoruri())**

\-> opțiuni de filtrare și sortare date.





&#x20;   **def \_genereaza\_raport(self) -> None:**

&#x20;       **"""Genereaza raportul si il afiseaza in interfata."""**

&#x20;       **raport = RaportScoruri(self.\_scor\_db.get\_all\_scoruri()).genereaza\_raport()**

&#x20;       **self.\_raport\_text.delete("1.0", tkinter.END)**

&#x20;       **self.\_raport\_text.insert(tkinter.END, raport)**

Ia toate scorurile și generează raportul. Apoi îl afișează în zona Text.









