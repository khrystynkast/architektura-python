class Ksiazka:
    def __init__(self, tytul, autor, rok, isbn):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.isbn = isbn

    def __str__(self):
        return f"'{self.tytul}' — {self.autor} ({self.rok})"

    def __repr__(self):
        return f"Ksiazka(tytul={self.tytul!r}, autor={self.autor!r}, rok={self.rok}, isbn={self.isbn!r})"

    def __eq__(self, other):
        if isinstance(other, Ksiazka):
            return self.isbn == other.isbn
        return False


class Biblioteka:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.ksiazki = []

    def dodaj(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def usun(self, isbn):
        self.ksiazki = [k for k in self.ksiazki if k.isbn != isbn]

    def szukaj(self, fraza):
        fraza = fraza.lower()
        return [
            k for k in self.ksiazki
            if fraza in k.tytul.lower() or fraza in k.autor.lower()
        ]

    def __len__(self):
        return len(self.ksiazki)

    def __str__(self):
        return f"Biblioteka '{self.nazwa}' — {len(self)} książek"


"""
 Klasa vs instancja
Klasa = przepis
Instancja = gotowy obiekt

 __init__ — konstruktor
Tworzy obiekt i ustawia jego dane.

 Atrybuty instancji vs klasy
instancji → różne dla każdego obiektu
klasy → wspólne dla wszystkich

 Metody:
zwykłe (self)
@classmethod
@staticmethod

 Dziedziczenie
Tworzenie podklas.

 Metody specjalne (dunder):
__str__ — ładny opis
__repr__ — techniczny opis
__eq__ — porównanie obiektów
__len__ — długość obiektu
"""