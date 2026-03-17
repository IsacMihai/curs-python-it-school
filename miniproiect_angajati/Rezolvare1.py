

import json 
import os 
from typing import Any, Optional  


#Aici creezi o constantă sau o variabilă globală
MIN_SALARY = 4050.0
VALID_SENIORITY = {"junior", "mid", "senior"} 



# CALE Fisier 

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
JSON_PATH = os.path.join(BASE_DIR, "info_angajati1.json")
TXT_PATH = os.path.join(BASE_DIR, "rezultate.txt")



# UTILITARE: TXT OUTPUT


def write_txt(text: str) -> None:#funcția primește un parametru numit text, care trebuie să fie string
    """
    Scrie textul in rezultate.txt (append) si il afiseaza pe ecran.
    Daca fisierul nu exista, va fi creat automat.
    """
    print(text)
    try:
        with open(TXT_PATH, "a", encoding="utf-8") as my_file:
            my_file.write(text + "\n")
    except OSError:
        # daca, rar, nu poate scrie in fisier
        print("Eroare: nu pot scrie in rezultate.txt")


def reset_txt() -> None:
    """
    (Optional) Goleste rezultatele.txt la pornirea programului.
    Daca nu vrei asta, sterge apelul din main().
    """
    try:
        with open(TXT_PATH, "w", encoding="utf-8") as my_file:
            my_file.write("=== REZULTATE PROGRAM ANGAJATI ===\n")
    except OSError:
        pass



# UTILITARE: JSON STORAGE


def ensure_json_exists() -> None:
    """Creeaza info_angajati1.json cu [] daca nu exista."""
    if not os.path.exists(JSON_PATH):
        try:
            with open(JSON_PATH, "w", encoding="utf-8") as my_file:
                json.dump([], my_file, ensure_ascii=False, indent=4)
        except OSError:
            write_txt("Eroare: nu pot crea fisierul JSON.")


def load_employees() -> list[dict[str, Any]]:
    """
    Incarca lista de angajati din JSON.
    Daca fisierul e gol/corupt, returneaza [].
    """
    ensure_json_exists()
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as my_file:
            data = json.load(my_file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        write_txt("Eroare: JSON invalid. Pune in fisier macar []")
        return []
    except OSError:
        write_txt("Eroare: nu pot citi fisierul JSON.")
        return []


def save_employees(employees: list[dict[str, Any]]) -> None:
    """Salveaza lista de angajati in JSON."""
    try:
        with open(JSON_PATH, "w", encoding="utf-8") as my_file:
            json.dump(employees, my_file, ensure_ascii=False, indent=4)
    except OSError:
        write_txt("Eroare: nu pot salva fisierul JSON.")



# UTILITARE: CAMPURI (fix pentru chei cu litere mari/mici)


def get_field(d: dict[str, Any], key: str, default: Any = "") -> Any:
    """
    Ia campul key din dict, indiferent daca e scris:
      - 'cnp' / 'CNP'
      - 'nume' / 'Nume'
    """
    return d.get(key, d.get(key.upper(), d.get(key.capitalize(), default)))


def set_field(d: dict[str, Any], key: str, value: Any) -> None:
    """
    Seteaza campul in formatul standard (lowercase in JSON).
    """
    d[key] = value



# VALIDARI (integritate date)


def valid_cnp(cnp: str) -> bool:
    """CNP: 13 cifre."""
    return cnp.isdigit() and len(cnp) == 13


def valid_age(age: int) -> bool:
    """Varsta >= 18."""
    return age >= 18


def valid_salary(salary: float) -> bool:
    """Salar >= minim."""
    return salary >= MIN_SALARY


def valid_seniority(s: str) -> bool:
    """Senioritate: junior/mid/senior."""
    return s.lower() in VALID_SENIORITY



# CAUTARE (dupa CNP)


def find_by_cnp(employees: list[dict[str, Any]], cnp: str) -> Optional[dict[str, Any]]:
    """Returneaza angajatul dupa CNP sau None."""
    for emp in employees:
        if str(get_field(emp, "cnp", "")).strip() == cnp.strip():
            return emp
    return None



# ACTIUNI MENIU


def add_employee() -> None:
    """1) Adaugare angajat."""
    employees = load_employees()

    cnp = input("CNP (13 cifre): ").strip()
    if not valid_cnp(cnp):
        write_txt("CNP invalid (trebuie 13 cifre).")
        return

    if find_by_cnp(employees, cnp) is not None:
        write_txt("Exista deja un angajat cu acest CNP.")
        return

    nume = input("Nume: ").strip()
    prenume = input("Prenume: ").strip()

    try:
        varsta = int(input("Varsta (>=18): ").strip())
    except ValueError:
        write_txt("Varsta invalida (nu e numar).")
        return
    if not valid_age(varsta):
        write_txt("Varsta invalida (trebuie >= 18).")
        return

    try:
        salar = float(input(f"Salar brut (>= {MIN_SALARY}): ").strip())
    except ValueError:
        write_txt("Salar invalid (nu e numar).")
        return
    if not valid_salary(salar):
        write_txt(f"Salar invalid (trebuie >= {MIN_SALARY}).")
        return

    departament = input("Departament: ").strip()
    senioritate = input("Senioritate (junior/mid/senior): ").strip().lower()
    if not valid_seniority(senioritate):
        write_txt("Senioritate invalida.")
        return

    new_emp = {
        "cnp": cnp,
        "nume": nume,
        "prenume": prenume,
        "varsta": varsta,
        "salar": salar,
        "departament": departament,
        "senioritate": senioritate
    }

    employees.append(new_emp)
    save_employees(employees)
    write_txt(f"Angajat adaugat  {nume} {prenume} (CNP {cnp})")


def search_employee() -> None:
    """2) Cautare angajat dupa CNP."""
    employees = load_employees()
    cnp = input("CNP: ").strip()

    emp = find_by_cnp(employees, cnp)
    if emp is None:
        write_txt("Angajat negasit ")
        return

    write_txt("Angajat gasit ")
    write_txt(f"{get_field(emp,'cnp')} | {get_field(emp,'nume')} {get_field(emp,'prenume')} | "
              f"{get_field(emp,'varsta')} ani | {get_field(emp,'salar')} RON | "
              f"{get_field(emp,'departament')} | {get_field(emp,'senioritate')}")


def update_employee() -> None:
    """3) Modificare date angajat dupa CNP (simplu: reintroduci toate datele)."""
    employees = load_employees()
    cnp = input("CNP de modificat: ").strip()

    emp = find_by_cnp(employees, cnp)
    if emp is None:
        write_txt("Angajat negasit ")
        return

    nume = input("Nume nou: ").strip()
    prenume = input("Prenume nou: ").strip()

    try:
        varsta = int(input("Varsta noua (>=18): ").strip())
    except ValueError:
        write_txt("Varsta invalida.")
        return
    if not valid_age(varsta):
        write_txt("Varsta invalida (trebuie >= 18).")
        return

    try:
        salar = float(input(f"Salar nou (>= {MIN_SALARY}): ").strip())
    except ValueError:
        write_txt("Salar invalid.")
        return
    if not valid_salary(salar):
        write_txt(f"Salar invalid (trebuie >= {MIN_SALARY}).")
        return

    departament = input("Departament nou: ").strip()
    senioritate = input("Senioritate noua (junior/mid/senior): ").strip().lower()
    if not valid_seniority(senioritate):
        write_txt("Senioritate invalida.")
        return

    # setam in format standard (lowercase keys)


    set_field(emp, "nume", nume)
    set_field(emp, "prenume", prenume)
    set_field(emp, "varsta", varsta)
    set_field(emp, "salar", salar)
    set_field(emp, "departament", departament)
    set_field(emp, "senioritate", senioritate)

    save_employees(employees)
    write_txt(f"Angajat modificat  (CNP {cnp})")


def delete_employee() -> None:
    """4) Stergere angajat dupa CNP."""
    employees = load_employees()
    cnp = input("CNP de sters: ").strip()

    emp = find_by_cnp(employees, cnp)
    if emp is None:
        write_txt("Angajat negasit ")
        return

    employees.remove(emp)
    save_employees(employees)
    write_txt(f"Angajat sters  (CNP {cnp})")


def list_employees() -> None:
    """5) Afisare angajati."""
    employees = load_employees()
    if not employees:
        write_txt("Nu exista angajati.")
        return

    write_txt("=== LISTA ANGAJATI ===")
    for emp in employees:
        write_txt(f"{get_field(emp,'cnp')} | {get_field(emp,'nume')} {get_field(emp,'prenume')} | "
                  f"{get_field(emp,'varsta')} | {get_field(emp,'salar')} | "
                  f"{get_field(emp,'departament')} | {get_field(emp,'senioritate')}")


def total_salary_company() -> None:
    """6) Calcul cost total salarii companie."""
    employees = load_employees()
    total = 0.0
    for emp in employees:
        total += float(get_field(emp, "salar", 0.0))
    write_txt(f"Cost total salarii companie: {total:.2f} RON")


def total_salary_department() -> None:
    """7) Calcul cost total salarii departament."""
    employees = load_employees()
    dept = input("Departament: ").strip()

    total = 0.0
    for emp in employees:
        if str(get_field(emp, "departament", "")).strip() == dept:
            total += float(get_field(emp, "salar", 0.0))

    write_txt(f"Cost total salarii departament '{dept}': {total:.2f} RON")


def salary_slip() -> None:
    """8) Calcul fluturas salar angajat (dupa CNP)."""
    employees = load_employees()
    cnp = input("CNP: ").strip()

    emp = find_by_cnp(employees, cnp)
    if emp is None:
        write_txt("Angajat negasit ")
        return

    brut = float(get_field(emp, "salar", 0.0))
    cas = 0.10 * brut
    cass = 0.25 * brut
    ramas = brut - cas - cass
    impozit = 0.10 * ramas
    net = brut - cas - cass - impozit

    write_txt("=== FLUTURAS SALARIAL ===")
    write_txt(f"Nume: {get_field(emp,'nume')} {get_field(emp,'prenume')} (CNP {cnp})")
    write_txt(f"Brut: {brut:.2f} RON")
    write_txt(f"CAS (10%): {cas:.2f} RON")
    write_txt(f"CASS (25%): {cass:.2f} RON")
    write_txt(f"Impozit (10% din ce a ramas): {impozit:.2f} RON")
    write_txt(f"NET: {net:.2f} RON")


def list_by_seniority() -> None:
    """9) Afisarea angajatilor pe baza senioritatii (scrie in rezultate.txt)."""
    employees = load_employees()
    s = input("Senioritate (junior/mid/senior): ").strip().lower()

    if not valid_seniority(s):
        write_txt("Senioritate invalida.")
        return

    write_txt(f"=== Angajati cu senioritate: {s} ===")
    found = False
    for emp in employees:
        if str(get_field(emp, "senioritate", "")).strip().lower() == s:
            write_txt(f"{get_field(emp,'nume')} {get_field(emp,'prenume')}")
            found = True

    if not found:
        write_txt("Nu exista angajati cu aceasta senioritate.")


def list_by_department() -> None:
    """10) Afisarea angajatilor pe baza departamentului (scrie in rezultate.txt)."""
    employees = load_employees()
    dept = input("Departament: ").strip()

    write_txt(f"=== Angajati din departament: {dept} ===")
    found = False
    for emp in employees:
        if str(get_field(emp, "departament", "")).strip() == dept:
            write_txt(f"{get_field(emp,'nume')} {get_field(emp,'prenume')}")
            found = True

    if not found:
        write_txt("Nu exista angajati in acest departament.")



# MENIU


def print_menu() -> None:
    """Afiseaza meniul principal."""
    print("""
1) Adaugare angajat
2) Cautare angajat (dupa CNP)
3) Modificare date angajat (dupa CNP)
4) Stergere angajat (dupa CNP)
5) Afisare angajati
6) Calcul cost total salarii companie
7) Calcul cost total salarii departament
8) Calcul fluturas salar angajat (dupa CNP)
9) Afisarea angajatilor pe baza senioritatii
10) Afisarea angajatilor pe baza departamentului
11) Iesire
""")


def main() -> None:
    """
    Program principal:
    - pregateste fisierul JSON daca lipseste
    - scrie rezultate in rezultate.txt
    - ruleaza meniul
    """
    ensure_json_exists()
    reset_txt()

    write_txt(f"JSON folosit: {JSON_PATH}")
    write_txt(f"TXT folosit:  {TXT_PATH}")
    write_txt(f"Angajati incarcati initial: {len(load_employees())}")

    while True:
        print_menu()
        opt = input("Alege optiune: ").strip()

        if opt == "1":
            add_employee()
        elif opt == "2":
            search_employee()
        elif opt == "3":
            update_employee()
        elif opt == "4":
            delete_employee()
        elif opt == "5":
            list_employees()
        elif opt == "6":
            total_salary_company()
        elif opt == "7":
            total_salary_department()
        elif opt == "8":
            salary_slip()
        elif opt == "9":
            list_by_seniority()
        elif opt == "10":
            list_by_department()
        elif opt == "11":
            write_txt("Iesire... ")
            break
        else:
            print("Optiune invalida.")


if __name__ == "__main__":
    main()