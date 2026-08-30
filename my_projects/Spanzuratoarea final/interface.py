"""Modul pentru interfata grafica Tkinter."""

import logging
import tkinter
import tkinter.messagebox
import tkinter.ttk
from datetime import datetime

from database import ScorDatabase
from game_logic import JocSpanzuratoarea
from reports import RaportScoruri


class SpanzuratoareaApp:
    """Aplicatia grafica pentru jocul Spanzuratoarea."""

    def __init__(self, window: tkinter.Tk, scor_db: ScorDatabase):
        self._window = window
        self._scor_db = scor_db
        self._joc = None

        self._build_interface()
        self._refresh_treeview(self._scor_db.get_all_scoruri())

    def _build_interface(self) -> None:
        """Construieste interfata grafica."""
        self._window.title("Spanzuratoarea")
        self._window.geometry("1100x800")
        self._window.resizable(True, True)

        tkinter.Label(self._window, text="Nume jucator").grid(row=0, column=0, padx=5, pady=5)
        self._nume_entry = tkinter.Entry(self._window)
        self._nume_entry.grid(row=0, column=1, padx=5, pady=5)

        tkinter.Label(self._window, text="Dificultate").grid(row=1, column=0, padx=5, pady=5)
        self._dificultate_combo = tkinter.ttk.Combobox(self._window, values=["easy", "medium", "hard"])
        self._dificultate_combo.set("easy")
        self._dificultate_combo.grid(row=1, column=1, padx=5, pady=5)

        tkinter.Button(self._window, text="Start joc", command=self._start_joc).grid(row=2, column=0, padx=5, pady=5)

        self._cuvant_label = tkinter.Label(self._window, text="Cuvant: -", font=("Arial", 18))
        self._cuvant_label.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

        tkinter.Label(self._window, text="Litera").grid(row=4, column=0, padx=5, pady=5)
        self._litera_entry = tkinter.Entry(self._window, width=10)
        self._litera_entry.grid(row=4, column=1, padx=5, pady=5)
        tkinter.Button(self._window, text="Incearca", command=self._incearca_litera).grid(row=4, column=2, padx=5, pady=5)

        self._mesaj_label = tkinter.Label(self._window, text="Alege dificultatea si apasa Start joc.")
        self._mesaj_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        self._greseli_label = tkinter.Label(self._window, text="Greseli: 0")
        self._greseli_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        coloane = ("id", "nume", "dificultate", "cuvant", "rezultat", "scor", "greseli", "data")
        self._tree = tkinter.ttk.Treeview(self._window, columns=coloane, show="headings")
        for coloana in coloane:
            self._tree.heading(coloana, text=coloana)
            self._tree.column(coloana, width=100)
        self._tree.grid(row=7, column=0, columnspan=8, padx=5, pady=10)

        tkinter.Label(self._window, text="ID scor").grid(row=8, column=0, padx=5, pady=5)
        self._id_entry = tkinter.Entry(self._window, width=10)
        self._id_entry.grid(row=8, column=1, padx=5, pady=5)

        tkinter.Label(self._window, text="Nume nou").grid(row=9, column=0, padx=5, pady=5)
        self._nume_update_entry = tkinter.Entry(self._window)
        self._nume_update_entry.grid(row=9, column=1, padx=5, pady=5)

        tkinter.Label(self._window, text="Scor nou").grid(row=10, column=0, padx=5, pady=5)
        self._scor_update_entry = tkinter.Entry(self._window)
        self._scor_update_entry.grid(row=10, column=1, padx=5, pady=5)

        tkinter.Label(self._window, text="Dificultate noua").grid(row=11, column=0, padx=5, pady=5)
        self._dificultate_update_combo = tkinter.ttk.Combobox(self._window, values=["easy", "medium", "hard"])
        self._dificultate_update_combo.set("easy")
        self._dificultate_update_combo.grid(row=11, column=1, padx=5, pady=5)

        tkinter.Button(self._window, text="Modifica scor", command=self._modifica_scor).grid(row=12, column=0, padx=5, pady=5)
        tkinter.Button(self._window, text="Sterge scor", command=self._sterge_scor).grid(row=12, column=1, padx=5, pady=5)

        tkinter.Label(self._window, text="Cauta nume").grid(row=8, column=3, padx=5, pady=5)
        self._cauta_entry = tkinter.Entry(self._window)
        self._cauta_entry.grid(row=8, column=4, padx=5, pady=5)
        tkinter.Button(self._window, text="Cauta", command=self._cauta_nume).grid(row=8, column=5, padx=5, pady=5)

        tkinter.Button(self._window, text="Sorteaza dupa nume", command=self._sortare_nume).grid(row=9, column=3, padx=5, pady=5)
        tkinter.Button(self._window, text="Cei mai buni", command=self._cei_mai_buni).grid(row=9, column=4, padx=5, pady=5)
        tkinter.Button(self._window, text="Cei mai slabi", command=self._cei_mai_slabi).grid(row=9, column=5, padx=5, pady=5)

        tkinter.Button(self._window, text="Easy", command=lambda: self._filtru_dificultate("easy")).grid(row=10, column=3, padx=5, pady=5)
        tkinter.Button(self._window, text="Medium", command=lambda: self._filtru_dificultate("medium")).grid(row=10, column=4, padx=5, pady=5)
        tkinter.Button(self._window, text="Hard", command=lambda: self._filtru_dificultate("hard")).grid(row=10, column=5, padx=5, pady=5)

        tkinter.Button(self._window, text="Afiseaza toate", command=self._afiseaza_toate).grid(row=11, column=3, padx=5, pady=5)
        tkinter.Button(self._window, text="Genereaza raport", command=self._genereaza_raport).grid(row=11, column=4, padx=5, pady=5)

        self._raport_text = tkinter.Text(self._window, height=7, width=50)
        self._raport_text.grid(row=12, column=3, columnspan=4, padx=5, pady=5)

    def _start_joc(self) -> None:
        """Porneste un joc nou."""
        nume = self._nume_entry.get().strip()
        dificultate = self._dificultate_combo.get()

        if not nume:
            tkinter.messagebox.showwarning("Atentie", "Introdu numele jucatorului!")
            return

        self._joc = JocSpanzuratoarea(dificultate)
        self._cuvant_label.config(text=f"Cuvant: {self._joc.afiseaza_cuvant()}")
        self._mesaj_label.config(text="Joc pornit. Introdu o litera.")
        self._greseli_label.config(text=f"Greseli: 0 / {self._joc.max_greseli}")
        logging.info("Joc nou pornit pentru %s.", nume)

    def _incearca_litera(self) -> None:
        """Proceseaza litera introdusa."""
        if self._joc is None:
            tkinter.messagebox.showwarning("Atentie", "Trebuie sa pornesti jocul mai intai!")
            return

        litera = self._litera_entry.get()
        mesaj = self._joc.incearca_litera(litera)
        self._litera_entry.delete(0, tkinter.END)

        self._cuvant_label.config(text=f"Cuvant: {self._joc.afiseaza_cuvant()}")
        self._mesaj_label.config(text=mesaj)
        self._greseli_label.config(text=f"Greseli: {self._joc.greseli} / {self._joc.max_greseli}")

        if self._joc.este_castigat():
            self._salveaza_joc("castigat")
            tkinter.messagebox.showinfo("Felicitari", f"Ai castigat! Cuvantul era: {self._joc.cuvant}")
            self._joc = None

        elif self._joc.este_pierdut():
            self._salveaza_joc("pierdut")
            tkinter.messagebox.showinfo("Joc pierdut", f"Ai pierdut! Cuvantul era: {self._joc.cuvant}")
            self._joc = None

    def _salveaza_joc(self, rezultat: str) -> None:
        """Salveaza rezultatul jocului in baza de date."""
        nume = self._nume_entry.get().strip()
        scor = self._joc.calculeaza_scor()
        data_joc = datetime.now().strftime("%Y-%m-%d %H:%M")

        self._scor_db.adauga_scor(
            nume,
            self._joc.dificultate,
            self._joc.cuvant,
            rezultat,
            scor,
            self._joc.greseli,
            data_joc
        )
        self._refresh_treeview(self._scor_db.get_all_scoruri())

    def _refresh_treeview(self, scoruri) -> None:
        """Reincarca tabelul cu scoruri."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for scor in scoruri:
            self._tree.insert("", tkinter.END, values=scor)

    def _modifica_scor(self) -> None:
        """Modifica scorul selectat pe baza ID-ului."""
        try:
            scor_id = int(self._id_entry.get())
            nume = self._nume_update_entry.get().strip()
            scor = int(self._scor_update_entry.get())
            dificultate = self._dificultate_update_combo.get()

            if not nume:
                raise ValueError("Numele este obligatoriu.")

            if self._scor_db.find_scor_by_id(scor_id) is None:
                raise ValueError("Nu exista scor cu acest ID.")

            self._scor_db.update_scor(scor_id, nume, dificultate, scor)
            self._refresh_treeview(self._scor_db.get_all_scoruri())
        except ValueError as error:
            tkinter.messagebox.showerror("Eroare", str(error))

    def _sterge_scor(self) -> None:
        """Sterge scorul selectat pe baza ID-ului."""
        try:
            scor_id = int(self._id_entry.get())
            if self._scor_db.find_scor_by_id(scor_id) is None:
                raise ValueError("Nu exista scor cu acest ID.")
            self._scor_db.delete_scor(scor_id)
            self._refresh_treeview(self._scor_db.get_all_scoruri())
        except ValueError as error:
            tkinter.messagebox.showerror("Eroare", str(error))

    def _cauta_nume(self) -> None:
        """Cauta scorurile dupa nume."""
        nume = self._cauta_entry.get().strip()
        self._refresh_treeview(self._scor_db.cauta_dupa_nume(nume))

    def _sortare_nume(self) -> None:
        """Sorteaza scorurile dupa nume."""
        self._refresh_treeview(self._scor_db.get_scoruri_sortate("nume", "ASC"))

    def _cei_mai_buni(self) -> None:
        """Afiseaza scorurile de la cel mai bun la cel mai slab."""
        self._refresh_treeview(self._scor_db.get_scoruri_sortate("scor", "DESC"))

    def _cei_mai_slabi(self) -> None:
        """Afiseaza scorurile de la cel mai slab la cel mai bun."""
        self._refresh_treeview(self._scor_db.get_scoruri_sortate("scor", "ASC"))

    def _filtru_dificultate(self, dificultate: str) -> None:
        """Filtreaza scorurile dupa dificultate."""
        self._refresh_treeview(self._scor_db.filtreaza_dupa_dificultate(dificultate))

    def _afiseaza_toate(self) -> None:
        """Afiseaza toate scorurile."""
        self._refresh_treeview(self._scor_db.get_all_scoruri())

    def _genereaza_raport(self) -> None:
        """Genereaza raportul si il afiseaza in interfata."""
        raport = RaportScoruri(self._scor_db.get_all_scoruri()).genereaza_raport()
        self._raport_text.delete("1.0", tkinter.END)
        self._raport_text.insert(tkinter.END, raport)
