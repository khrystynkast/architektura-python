pelne = input("Podaj pelne imie i nazwisko: ")

imie, nazwisko = pelne.split()
inicjaly = f"{imie[0].upper()}.{nazwisko[0].upper()}."
print("Inicjaly:", inicjaly)

od_tylu = imie[::-1]
print("Imie od tylu:", od_tylu)

bez_spacji = pelne.replace(" ", "")
print("Pelne imie i nazwisko bez spacji:", bez_spacji)


"""
Slicing — wycinanie fragmentów tekstu
tekst = "Python"
print(tekst[0:3])   # Pyt


.upper() — zamiana na wielkie litery
"hello".upper()   # "HELLO"


.lower() — zamiana na małe litery
"HELLO".lower()   # "hello"


.strip() — usuwa spacje z początku i końca
"   hello   ".strip()   # "hello"


.split() — dzieli tekst na listę słów
"hello world".split()   # ["hello", "world"]

.replace() — zamienia fragment tekstu na inny
"Hello world".replace("world", "Khrystyna")
# "Hello Khrystyna"

"""