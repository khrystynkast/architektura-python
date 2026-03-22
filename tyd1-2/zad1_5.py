import csv

with open("studenci.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    dane = list(reader)

srednia = sum(float(s["ocena"]) for s in dane) / len(dane)

naj = max(dane, key=lambda s: float(s["ocena"]))

with open("raport.txt", "w", encoding="utf-8") as f:
    f.write(f"Średnia ocen: {srednia:.2f}\n")
    f.write(f"Najlepszy student: {naj['imię']} {naj['nazwisko']} ({naj['ocena']})\n")


"""
🔹 open() - otwiera plik.

plik = open("dane.txt", "r")
Ale… open() trzeba zamykać ręcznie:

plik.close()
Jeśli zapomnisz → plik może zostać zablokowany.

🔹 with open() — najlepszy sposób

with open("dane.txt", "r") as plik:
    zawartosc = plik.read()
    
🔹 .read() — czyta cały plik jako jeden string

with open("tekst.txt", "r") as f:
    dane = f.read()
print(dane)

🔹 .readlines() — czyta plik linia po linii → lista
with open("tekst.txt", "r") as f:
    linie = f.readlines()
print(linie)

🔹 .write() — zapisuje tekst do pliku
with open("wynik.txt", "w") as f:
    f.write("Hello!")
Uwaga: .write() nie dodaje nowej linii, trzeba dopisać \n.

📂 2. Tryby otwierania plików
Tryb	Znaczenie
"r"	    read — czytanie (plik musi istnieć)
"w" 	write — zapis (nadpisuje plik!)
"a"	    append — dopisywanie na końcu
"r+"	czytanie + pisanie
"w+"	zapis + czytanie (czyści plik)



"""