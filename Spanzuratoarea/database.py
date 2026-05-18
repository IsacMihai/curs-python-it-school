"""Modul pentru lucrul cu baza de date SQLite."""

import logging
import sqlite3
from typing import List, Optional, Tuple

DB_NAME = "spanzuratoarea.db"


class ScorDatabase:
    """Clasa care gestioneaza tabela scoruri din baza de date."""

    def __init__(self, db_name: str = DB_NAME):
        self._db_name = db_name
        self._create_table()

    def _create_table(self) -> None:
        """Creeaza tabela scoruri daca aceasta nu exista."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scoruri (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nume TEXT NOT NULL,
                    dificultate TEXT NOT NULL,
                    cuvant TEXT NOT NULL,
                    rezultat TEXT NOT NULL,
                    scor INTEGER NOT NULL,
                    greseli INTEGER NOT NULL,
                    data_joc TEXT NOT NULL
                )
            """)
            connection.commit()
        logging.info("Tabela scoruri a fost verificata/creata.")

    def adauga_scor(self, nume: str, dificultate: str, cuvant: str, rezultat: str,
                    scor: int, greseli: int, data_joc: str) -> None:
        """Adauga un scor nou in baza de date."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO scoruri (nume, dificultate, cuvant, rezultat, scor, greseli, data_joc)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nume, dificultate, cuvant, rezultat, scor, greseli, data_joc))
            connection.commit()
        logging.info("Scor adaugat pentru jucatorul %s.", nume)

    def get_all_scoruri(self) -> List[Tuple]:
        """Returneaza toate scorurile din baza de date."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM scoruri")
            return cursor.fetchall()

    def find_scor_by_id(self, scor_id: int) -> Optional[Tuple]:
        """Cauta un scor dupa id."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM scoruri WHERE id = ?", (scor_id,))
            return cursor.fetchone()

    def update_scor(self, scor_id: int, nume: str, dificultate: str, scor: int) -> None:
        """Modifica numele, dificultatea si scorul unei inregistrari."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE scoruri
                SET nume = ?, dificultate = ?, scor = ?
                WHERE id = ?
            """, (nume, dificultate, scor, scor_id))
            connection.commit()
        logging.info("Scorul cu id %s a fost modificat.", scor_id)

    def delete_scor(self, scor_id: int) -> None:
        """Sterge un scor dupa id."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM scoruri WHERE id = ?", (scor_id,))
            connection.commit()
        logging.info("Scorul cu id %s a fost sters.", scor_id)

    def get_scoruri_sortate(self, camp: str = "scor", ordine: str = "DESC") -> List[Tuple]:
        """Returneaza scorurile sortate dupa nume, scor, dificultate sau data."""
        campuri_acceptate = ["nume", "dificultate", "scor", "data_joc"]
        if camp not in campuri_acceptate:
            camp = "scor"

        if ordine not in ["ASC", "DESC"]:
            ordine = "DESC"

        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM scoruri ORDER BY {camp} {ordine}")
            return cursor.fetchall()

    def filtreaza_dupa_dificultate(self, dificultate: str) -> List[Tuple]:
        """Returneaza scorurile pentru o anumita dificultate."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM scoruri WHERE dificultate = ?", (dificultate,))
            return cursor.fetchall()

    def cauta_dupa_nume(self, nume: str) -> List[Tuple]:
        """Returneaza scorurile unde numele contine textul cautat."""
        with sqlite3.connect(self._db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM scoruri WHERE nume LIKE ?", (f"%{nume}%",))
            return cursor.fetchall()
