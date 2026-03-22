import csv

kontakty = []

def dodaj_kontakt():
    imie = input("Imie: ").strip()
    nazwisko = input("Nazwisko: ").strip()
    telefon = input("Telefon: ").strip()
    email = input("Email: ").strip()
    
    if not telefon.isdigit():
        print("Telefon musi być liczbą!")
        return
    if "@" not in email:
        print("Email musi zawierać '@'!")
        return

    kontakt = {
        "imie": imie,
        "nazwisko": nazwisko,
        "telefon": telefon,
        "email": email
    }

    kontakty.append(kontakt)
    print("Kontakt dodany")
    
def wyswietl_kontakty():
    if not kontakty:
        print("Brak kontaktów.")
        return

    for i, k in enumerate(kontakty, start=1):
        print(f"{i}. {k['imie']} {k['nazwisko']} — tel: {k['telefon']}, email: {k['email']}")

def szukaj_kontakt():
    fraza = input("Podaj imię lub nazwisko: ").lower()

    znalezione = [
        k for k in kontakty
        if fraza in k["imie"].lower() or fraza in k["nazwisko"].lower()
    ]

    if not znalezione:
        print(" Nie znaleziono kontaktu.")
        return

    for k in znalezione:
        print(f"{k['imie']} {k['nazwisko']} — {k['telefon']} — {k['email']}")

def usun_kontakt():
    wyswietl_kontakty()
    if not kontakty:
        return

    indeks = int(input("Podaj numer kontaktu do usunięcia: ")) - 1

    if 0 <= indeks < len(kontakty):
        usuniety = kontakty.pop(indeks)
        print(f"Usunięto: {usuniety['imie']} {usuniety['nazwisko']}")
    else:
        print("Nieprawidłowy numer.")
        

def zapisz_do_csv():
    with open("kontakty.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["imie", "nazwisko", "telefon", "email"])

        for k in kontakty:
            writer.writerow([k["imie"], k["nazwisko"], k["telefon"], k["email"]])

    print("Zapisano do pliku kontakty.csv")
    
def wczytaj_z_csv():
    try:
        with open("kontakty.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            kontakty.clear()
            for row in reader:
                kontakty.append(row)
        print("✔️ Wczytano kontakty z pliku.")
    except FileNotFoundError:
        print("Plik kontakty.csv nie istnieje.")
        
while True:
    print("""
    --- MENEDŻER KONTAKTÓW ---
    1. Dodaj kontakt
    2. Wyświetl kontakty
    3. Wyszukaj kontakt
    4. Usuń kontakt
    5. Zapisz kontakty do pliku (CSV)
    6. Wczytaj kontakty z pliku (CSV)
    7. Wyjdź
    """)

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        dodaj_kontakt()
    elif wybor == "2":
        wyswietl_kontakty()
    elif wybor == "3":
        szukaj_kontakt()
    elif wybor == "4":
        usun_kontakt()
    elif wybor == "5":
        zapisz_do_csv()
    elif wybor == "6":
        wczytaj_z_csv()
    elif wybor == "7":
        print("Do zobaczenia!")
        break
    else:
        print("Nieprawidłowa opcja.")



