zakupy = [
    {"nazwa": "mleko", "cena": 4.50, "ilość": 2},
    {"nazwa": "chleb", "cena": 5.00, "ilość": 1},
    {"nazwa": "masło", "cena": 7.99, "ilość": 1},
    {"nazwa": "jajka", "cena": 12.50, "ilość": 1},
    {"nazwa": "mleko", "cena": 4.50, "ilość": 3},
]

# Laczny koszt zakupow
suma = sum(p["cena"] * p["ilość"] for p in zakupy)
print ("Łączny koszt zakupów:", suma)

# Najdrozszy produkt
najdrozszy = max(zakupy, key=lambda p: p["cena"])
print("Najdroższy produkt:", najdrozszy["nazwa"], najdrozszy["cena"])

# Najtanszy produkt     
najtanszy = min(zakupy, key=lambda p: p["cena"])
print("Najtańszy produkt:", najtanszy["nazwa"], najtanszy["cena"])

# Srednia cena produktu
srednia_cena = sum(p["cena"] for p in zakupy) / len(zakupy)
print("Średnia cena produktu:", srednia_cena)

# Unikalne nazwy
unikalne = {p["nazwa"] for p in zakupy}
print("Unikalne nazwy produktów:", unikalne)

# Drozsze od 5 zl
drozsze_od_5 = [p for p in zakupy if p["cena"] > 5]
print("Produkty droższe od 5 zł:", drozsze_od_5)

"""
🟦 LISTY (list)
lista = [1, 2, 3, 4]

🔹 append() — dodaje 1 element na koniec
lista.append(5)
# [1, 2, 3, 4, 5]

🔹 extend() — dodaje wiele elementów na koniec
lista.extend([6, 7])
# [1, 2, 3, 4, 5, 6, 7]

🔹 insert() — dodaje element na określonej pozycji
lista.insert(2, 10)
# [1, 2, 10, 3, 4, 5, 6, 7]

🔹 remove() — usuwa pierwsze wystąpienie elementu
lista.remove(3)
# [1, 2, 4, 5, 6, 7]

🔹 pop() — usuwa i zwraca element z określonej pozycji
lista.pop()      # usuwa 7
lista.pop(0)     # usuwa pierwszy element
# [2, 4, 5, 6]

🔹 sort() — sortuje listę
lista.sort()
# [2, 4, 5, 6]

🔹 reverse() — odwraca kolejność elementów
lista.reverse()
# [6, 5, 4, 2]  

🔹 Slicing — wycinanie fragmentu listy
lista[1:3]   
[10, 20, 30, 40][1:3]  # [20, 30]

🔹 Iterowanie po liście
for x in lista:
    print(x)
Python bierze każdy element po kolei.


🟩 SŁOWNIKI (dict)
Słownik = dane w formie klucz → wartość.
osoba = {"imie": "Khrystyna", "wiek": 21}

🔹 Dostęp do wartości przez klucz
print(osoba["imie"])  # Khrystyna
print(osaba["wiek"])  # 21

🔹.get() — bezpieczny dostęp
osoba.get("wiek")        # 21
osoba.get("adres")       # None (nie ma błędu)
osoba.get("adres", "brak")  # "brak"

🔹 .keys() — lista kluczy
osoba.keys()
# dict_keys(['imie', 'wiek'])

🔹.values() — lista wartości
osoba.values()
# dict_values(['Khrystyna', 21])

🔹 .items() — lista par (klucz, wartość)
osoba.items()
# dict_items([('imie', 'Khrystyna'), ('wiek', 21)])

🟧 KROTKI (tuple)
Krotka wygląda jak lista, ale jest niezmienna.

krotka = (1, 2, 3)


🟪 ZBIORY (set)
Zbiór = kolekcja unikalnych elementów, bez duplikatów.
zbior = {1, 2, 3, 3, 3}
# {1, 2, 3}

"""

#🔹 Operacje na zbiorach

A = {1, 2, 3}
B = {3, 4, 5}

#👉 Suma zbiorów (union) — |
A | B
# {1, 2, 3, 4, 5}

#👉 Część wspólna (intersection) — &
A & B
# {3}

#👉 Różnica zbiorów — -
A - B
# {1, 2}

B - A
# {4, 5}
