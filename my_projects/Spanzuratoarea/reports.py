"""Modul pentru generarea raportului jocului."""

from typing import List, Tuple


class RaportScoruri:
    """Clasa care genereaza un raport text pe baza scorurilor."""

    def __init__(self, scoruri: List[Tuple]):
        self.scoruri = scoruri

    def genereaza_raport(self) -> str:
        """Genereaza raport cu informatii despre scoruri."""
        if not self.scoruri:
            return "Nu exista scoruri salvate."

        total_jocuri = len(self.scoruri)
        scoruri_numere = [scor[5] for scor in self.scoruri]
        cel_mai_bun = max(scoruri_numere)
        cel_mai_slab = min(scoruri_numere)

        easy = 0
        medium = 0
        hard = 0

        for scor in self.scoruri:
            if scor[2] == "easy":
                easy += 1
            elif scor[2] == "medium":
                medium += 1
            elif scor[2] == "hard":
                hard += 1

        raport = f"""
RAPORT SPANZURATOAREA
---------------------
Total jocuri: {total_jocuri}
Cel mai bun scor: {cel_mai_bun}
Cel mai slab scor: {cel_mai_slab}
Jocuri easy: {easy}
Jocuri medium: {medium}
Jocuri hard: {hard}
"""
        return raport.strip()
