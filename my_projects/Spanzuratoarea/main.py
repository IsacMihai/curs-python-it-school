"""Fisierul principal al aplicatiei Spanzuratoarea."""

import logging
import tkinter

from database import ScorDatabase
from interface import SpanzuratoareaApp


def main() -> None:
    """Porneste aplicatia."""
    logging.basicConfig(
        filename="spanzuratoarea.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    scor_db = ScorDatabase()
    window = tkinter.Tk()
    SpanzuratoareaApp(window, scor_db)
    window.mainloop()


if __name__ == "__main__":
    main()
