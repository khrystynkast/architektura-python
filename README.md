# Architektura aplikacji w Pythonie 
### Zadania tydzień 1–2

Repozytorium zawiera rozwiązania zadań z przedmiotu Architektura aplikacji w Pythonie.  
W folderze `tyd1-2` znajdują się wszystkie pliki wykonane w ramach pierwszych dwóch tygodni zajęć.

---

### Zawartość folderu `tyd1-2`

Dokumentacja i konfiguracja
- konfiguracja_srodowiska.md - instrukcja tworzenia i aktywacji środowiska wirtualnego (venv)
- python_boost_pack_weeks_1_2.md - materiały i notatki do tygodnia 1–2

---

## Zadania z tygodnia 1 (zad1_x.py)

Pliki:
- zad1_1.py
- zad1_2.py
- zad1_3.py
- zad1_4.py
- zad1_5.py
- zad1_6.py

Każdy plik zawiera osobne zadanie programistyczne z podstaw Pythona:
- operacje na zmiennych
- instrukcje warunkowe
- pętle
- funkcje
- listy, słowniki, krotki
- proste przetwarzanie danych


---

## Zadania z tygodnia 2 (zad2_x.py)

- zad2_1.py
Zadanie dotyczące pracy z modułami, importami lub strukturą programu.

- zad2_2
Folder lub plik zawierający kolejne zadanie z tygodnia 2.

- zad2_3.py
Program „Pogodynka” - aplikacja pobierająca dane pogodowe z API OpenWeather.

Wykorzystuje:
- bibliotekę `requests`
- format JSON
- parsowanie odpowiedzi API
- pętlę wejścia użytkownika

---

Plik testowy
- test2_1.py - plik pomocniczy/testowy do wybranych zadań

--- 

### Zadania tydzień 3-4

Repozytorium zawiera rozwiązania zadań z przedmiotu Architektura aplikacji w Pythonie dotyczących programowania współbieżnego i równoległego.
W folderze`tyd3-4`  znajdują się wszystkie pliki wykonane w ramach tygodnia 3–4.

---

### Zawartość folderu `tyd3-4`

Lab2_Concurrency_Multi_MAIN_FILE.ipynb — notebook z zajęć (wprowadzenie do threading, queue, multiprocessing)

lab2_functions.py — funkcje pomocnicze wykorzystywane w zadaniu 3
(`is_prime`, `find_primes`, `calculate_power_sum`)

---

## Zadanie 1 - Cat Facts API (Threading)

Plik: `zadanie_1.py`

Program pobiera 20 faktów o kotach z publicznego API:
`https://catfact.ninja/fact`

Zadanie obejmuje dwie wersje:
1. Wersja sekwencyjna
* 20 zapytań wykonywanych jedno po drugim
* pomiar czasu wykonania

2. Wersja wielowątkowa (ThreadPoolExecutor)
* 20 zapytań wykonywanych równolegle
* znaczące przyspieszenie działania

Technologie:
* `requests`
* `concurrent.futures.ThreadPoolExecutor`
* pomiar czasu (`time.time()`)

---

## Zadanie 2 — Producent–Konsumenci (Queue + Threads)

Plik: `zadanie_2.py`

Implementacja klasycznego wzorca Producer–Consumer:
* Producent generuje kolejne liczby naturalne i dodaje je do kolejki.
* Konsument 1 przetwarza liczby parzyste.
* Konsument 2 przetwarza liczby nieparzyste.
* Komunikacja odbywa się przez queue.Queue.
* Program kończy się po przetworzeniu określonej liczby liczb.

Technologie:
* `threading.Thread`
* `queue.Queue`
* sygnały STOP (`None`)
* poprawne użycie `q.task_done()` i `q.join()`

---

## Zadanie 3 — Multiprocessing (CPU-bound)

Plik: `zadanie_3.py`

Program porównuje czas wykonania obliczeń:
* wersja sekwencyjna
* wersja równoległa z multiprocessing

Wykorzystuje funkcję:
`calculate_power_sum(n)`
która oblicza sumę potęg liczby n od 1 do 100 — operacja kosztowna obliczeniowo, idealna do multiprocessing.

Technologie:
* `multiprocessing.Pool`
* mapowanie funkcji na wiele procesów
* pomiar czasu

---
### Zadania tydzień 5-6

Folder `tyd5-6` zawiera implementację klasy Product oraz zestaw testów jednostkowych przygotowanych w dwóch technologiach: unittest oraz pytest.

---

### Zawartość folderu `tyd5-6`

`product.py` — implementacja klasy Product wraz z metodami biznesowymi
`__init__.py` — plik inicjalizujący pakiet
`tests/` — katalog zawierający testy jednostkowe
`test_product_unittest.py` — testy w stylu unittest
`test_product_pytest.py` — testy w stylu pytest
`.venv/` — środowisko wirtualne (wykluczone z repozytorium)


---

## Zadanie 1 - Implementacja klasy Product i testy jednostkowe w unittest

Plik: `product.py`
Plik: `tests/test_product_unittest.py`

Klasa reprezentuje produkt w sklepie internetowym i zawiera:
* `add_stock(amount)` — dodawanie ilości produktu
* `remove_stock(amount)` — usuwanie ilości produktu
* `is_available()` — sprawdzanie dostępności
* `total_value()` — obliczanie wartości magazynowej
* `apply_discount(percent)` — obniżanie ceny o podany procent (0–100)

Wszystkie metody zawierają walidację danych i rzucają ValueError w przypadku błędnych wartości.

Testy obejmują:
* poprawne działanie metod (add_stock, remove_stock, total_value)
* testy wyjątków (ValueError)
* wykorzystanie metody setUp() do przygotowania obiektu testowego

Uruchamianie:
```
python -m unittest discover -v
```

---

## Zadanie 2 + dodatkowe zadanie — Testy jednostkowe w pytest

Plik: `tests/test_product_pytest.py`

Testy przygotowane z użyciem biblioteki pytest, zgodnie z dobrymi praktykami:
* `@pytest.fixture` — tworzenie instancji `Product`
* `@pytest.mark.parametrize` — testy parametryzowane
* `pytest.raises(ValueError)` — testowanie wyjątków
* testy metody `apply_discount`
Uruchamianie:
```
pytest -v

pytest tests/test_product_pytest.py -v 
```