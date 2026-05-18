"""Modul cu logica jocului Spanzuratoarea."""

import random
from typing import List

CUVINTE = {
    "easy": ["mere", "casa", "apa", "soare", "masa", "pisica"],
    "medium": ["calculator", "telefon", "masina", "program", "student"],
    "hard": ["virtualizare", "administrator", "spanzuratoare", "dezvoltator", "infrastructura"]
}

MAX_GRESELI = {
    "easy": 8,
    "medium": 6,
    "hard": 5
}


class JocSpanzuratoarea:
    """Clasa care tine starea unui joc de Spanzuratoarea."""

    def __init__(self, dificultate: str):
        self.dificultate = dificultate
        self.cuvant = random.choice(CUVINTE[dificultate])
        self.litere_incercate: List[str] = []
        self.greseli = 0
        self.max_greseli = MAX_GRESELI[dificultate]

    def afiseaza_cuvant(self) -> str:
        """Returneaza cuvantul ascuns, cu literele ghicite afisate."""
        rezultat = []
        for litera in self.cuvant:
            if litera in self.litere_incercate:
                rezultat.append(litera)
            else:
                rezultat.append("_")
        return " ".join(rezultat)

    def incearca_litera(self, litera: str) -> str:
        """Verifica litera introdusa de utilizator."""
        litera = litera.lower().strip()

        if len(litera) != 1 or not litera.isalpha():
            return "Introdu o singura litera!"

        if litera in self.litere_incercate:
            return "Litera a fost deja incercata!"

        self.litere_incercate.append(litera)

        if litera not in self.cuvant:
            self.greseli += 1
            return "Litera gresita!"

        return "Litera corecta!"

    def este_castigat(self) -> bool:
        """Verifica daca jocul este castigat."""
        for litera in self.cuvant:
            if litera not in self.litere_incercate:
                return False
        return True

    def este_pierdut(self) -> bool:
        """Verifica daca jocul este pierdut."""
        return self.greseli >= self.max_greseli

    def calculeaza_scor(self) -> int:
        """Calculeaza scorul in functie de dificultate si numarul de greseli."""
        puncte_dificultate = {
            "easy": 100,
            "medium": 200,
            "hard": 300
        }
        scor = puncte_dificultate[self.dificultate] - self.greseli * 20
        if scor < 0:
            return 0
        return scor
