# Architektura aplikacji w Pythonie 
## Zadania tydzień 1–2

Repozytorium zawiera rozwiązania zadań z przedmiotu Architektura aplikacji w Pythonie.  
W folderze `tyd1-2` znajdują się wszystkie pliki wykonane w ramach pierwszych dwóch tygodni zajęć.

---

### Zawartość folderu `tyd1-2`

Dokumentacja i konfiguracja
- konfiguracja_srodowiska.md - instrukcja tworzenia i aktywacji środowiska wirtualnego (venv)
- python_boost_pack_weeks_1_2.md - materiały i notatki do tygodnia 1–2
- zadanie 1.1 z pliku AAA_Zestaw_Zaliczeniowy 

---

### Zadania z tygodnia 1 (zad1_x.py)

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

### Zadania z tygodnia 2 (zad2_x.py)

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

### Dodane zadanie z AAP_Zestaw_Zaliczeniowy (Lab 1 — Dekoratory)
Do folderu tyd1-2 został dodany nowy folder:
`zad1.1_`

W nim znajduje się plik:
`lab1_dekoratory.py`

Plik zawiera kompletne rozwiązanie zadania 1.1 — Dekoratory z zestawu zaliczeniowego:
- implementację dekoratora @retry
- implementację dekoratora @cache_to_disk
- funkcję testową flaky_fetch z 50% szansą błędu
- eksperyment 100 wywołań
- porównanie wyniku z teorią
- zapis cache do folderu flaky_cache/

python lab1_dekoratory.py
Wynik eksperymentu:
```
Sukcesy: 97/100
```
---

## Zadania tydzień 3-4

Repozytorium zawiera rozwiązania zadań z przedmiotu Architektura aplikacji w Pythonie dotyczących programowania współbieżnego i równoległego.
W folderze`tyd3-4`  znajdują się wszystkie pliki wykonane w ramach tygodnia 3–4.

---

### Zawartość folderu `tyd3-4`

- Lab2_Concurrency_Multi_MAIN_FILE.ipynb — notebook z zajęć (wprowadzenie do threading, queue, multiprocessing)

- lab2_functions.py — funkcje pomocnicze wykorzystywane w zadaniu 3
(`is_prime`, `find_primes`, `calculate_power_sum`)

- lab2_multiprocessing_sentiment.py  - Współbieżność i równoległość

---

### Zadanie 1 - Cat Facts API (Threading)

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

### Zadanie 2 — Producent–Konsumenci (Queue + Threads)

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

### Zadanie 3 — Multiprocessing (CPU-bound)

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
### Dodane zadanie z AAP_Zestaw_Zaliczeniowy (Lab 2 — Współbieżność)
Do folderu tyd3-4 został dodany nowy folder:
`zad2.1_`
W nim znajduje się plik:
`lab2_multiprocessing_sentiment.py`
Plik zawiera kompletne rozwiązanie zadania 2.1 — Multiprocessing dla CPU-bound z zestawu zaliczeniowego:
- implementację funkcji sentiment_score(text)
- porównanie trzech wariantów:
- sekwencyjny
- ThreadPool
- multiprocessing.Pool
- pobranie 5000 recenzji IMDB
- pomiar czasu wykonania
- wykres słupkowy (matplotlib)

Kod zaczynał się od szkicu:
```
def sentiment_score(text: str) -> int:
    """CPU-bound: tokenizuj, policz pozytywne minus negatywne."""
    raise NotImplementedError
```
i został w pełni zaimplementowany w pliku lab2_multiprocessing_sentiment.py.

Na macOS multiprocessing działa wolniej niż wersja sekwencyjna, ponieważ system używa trybu spawn, który uruchamia każdy proces od nowa i ponownie ładuje wszystkie biblioteki.
Na Linux/Windows multiprocessing jest znacznie szybszy (4–6×), ponieważ używa fork, który kopiuje pamięć procesu natychmiast, bez ponownego ładowania środowiska.

---
## Zadania tydzień 5-6

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

### Zadanie 1 - Implementacja klasy Product i testy jednostkowe w unittest

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

### Zadanie 2 + dodatkowe zadanie — Testy jednostkowe w pytest

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
---

### Dodatkowe zadanie — Tokenizer + pytest (Lab 3 — Testowanie)
W folderze _workspace/ znajduje się pełna implementacja zadania 3.1 z zestawu zaliczeniowego.
Pliki:
- tokenizer.py — implementacja klasy Tokenizer
- test_tokenizer.py — zestaw testów pytest

Zakres implementacji
- usuwanie HTML (strip_html=True)
- konwersję do lowercase (lower=True)
- tokenizację regexem \w+ (obsługa polskich znaków)
- filtrowanie tokenów krótszych niż min_length
- budowanie słownika (vocab) z wielu tekstów

Testy pytest
- fixturę tokenizer
- fixturę imdb_sample (20 recenzji IMDB)
- parametryzację 6 przypadków brzegowych
- test deduplikacji słownika
- test filtra długości
- test integracyjny (słownik > 500 tokenów)
- test oznaczony xfail

Wynik uruchomienia:
``` 
9 passed, 1 xfailed
```

---
## Zadania tydzień 7-8

Folder `tyd7-8` zawiera rozwiązania zadań dotyczących pracy z bazami danych SQL oraz NoSQL (MongoDB), a także symulację wyszukiwania wektorowego (vector search) z użyciem numpy.

---

### Zawartość folderu `tyd7-8`

`zadanie1.py` — pobieranie danych z Random User API i zapis do bazy SQL
`zadanie2.py` — pobieranie danych z API GeckoTerminal i zapis do MongoDB
`zadanie3.py` — symulacja wyszukiwania wektorowego (pgvector) w czystym Pythonie


---

### Zadanie 1 - Random User API + SQL (PostgreSQL lub SQLite)

Plik: `zadanie1.py`

Program pobiera 30 użytkowników z publicznego API:
```
https://randomuser.me/api/?results=30
```
Następnie:
1. Tworzy tabelę users w bazie SQL (SQLite lub PostgreSQL)
2. Zapisuje dane każdego użytkownika:
* imię
* nazwisko
* email
* adres (miasto + kraj)
* wiek
* płeć
3.Wykonuje zapytania analityczne SQL:
* Ile jest mężczyzn, a ile kobiet?
* Jaki jest średni wiek użytkowników?
* W ilu różnych krajach mieszkają?
```
SELECT gender, COUNT(*) FROM users GROUP BY gender;

SELECT AVG(age) FROM users;

SELECT COUNT(DISTINCT country) FROM users;

```

Technologie:
* requests
* sqlite3 
* SQL (CREATE TABLE, INSERT, SELECT, GROUP BY)

Uruchamianie:
```
python zadanie1.py
```

---

### Zadanie 2 - MongoDB + API GeckoTerminal

Plik: `zadanie2.py`

Program pobiera listę sieci kryptowalutowych z API:
```
https://api.geckoterminal.com/api/v2/networks
```
Następnie:
* Łączy się z lokalnym serwerem MongoDB
* Czyści kolekcję networks
* Wstawia pobrane dokumenty jako JSON
* Wykonuje agregację `$group` i `$sort`, aby policzyć liczbę sieci per typ (`coingecko_asset_platform_id`)

Technologie:
* `pymongo`
* `requests`
* agregacje MongoDB (`$group`, `$sort`)

Uruchamianie:
```
python zadanie2.py

```

### Zadanie 3 - BONUS - Wyszukiwanie wektorowe (symulacja pgvector)

Plik: `zadanie3.py`

Program demonstruje działanie wyszukiwania semantycznego opartego na embeddingach.
* bazę 5 nowoczesnych filmów z embeddingami `VECTOR(3)`
* funkcję `cosine_similarity()`
* funkcję `semantic_search(query, database, top_k)`
* wyszukiwanie 3 najbardziej podobnych filmów do wektora zapytania

Technologie:
* `numpy`
* cosine similarity
* sortowanie wyników według podobieństwa

Uruchamianie:
```
python zadanie3.py
```
---

### Zadanie 4 — NoSQL-style w SQLite (JSON column)
Plik: `zadanie4.py`
Zadanie pokazuje, że SQLite może działać jak NoSQL, jeśli użyjemy kolumny JSON i funkcji `json_extract`.
 
Schemat dokumentowy
Tabela:
```
reviews_json(id INTEGER PRIMARY KEY, doc TEXT)
```
Każdy rekord to dokument JSON:
```
json
{
  "text": "...",
  "label": 0/1,
  "stats": {
    "word_count": ...,
    "sentiment_hint": "pos" | "neg"
  },
  "tags": ["pierwsze", "trzy", "dlugie_slowa"]
}
```

Załadowano 2000 recenzji IMDB jako dokumenty JSON
Dla każdej recenzji:
`sentiment_hint` = `"pos"` lub `"neg"`
`word_count` = liczba słów
`tags` = pierwsze 3 słowa dłuższe niż 5 znaków

Zapytania NoSQL-style (json_extract)
1. Rozkład klas
2. Średni word_count per klasa
3. Dokumenty, gdzie tags zawiera „movie”
4. Top 5 najdłuższych pozytywnych recenzji

Porównanie rozmiaru baz
```
SQL schema (reviews):               0 bajtow
JSON schema (reviews_json): 3,518,464 bajtow
```

---
### Zadania tydzień 9-10

Folder tyd9-10 zawiera rozwiązanie zadania polegającego na zaawansowanej analizie wielkich zbiorów danych o przestępczości w Chicago przy użyciu Apache Spark (PySpark), realizację procesów czyszczenia, wzbogacania (Broadcast Join) i inżynierii cech, zapis danych do partycjonowanego formatu Parquet, a także budowę i ewaluację kompletnego potoku uczenia maszynowego (Machine Learning Pipeline) z modelem RandomForestClassifier.

---

### Zawartość folderu `tyd9-10`

`chicago_crimes_analysis.py` - analiza danych o przestępczości w Chicago przy użyciu PySpark oraz budowa modelu klasyfikacji Machine Learning (Random Forest)
`chicago_crimes_sample.csv` - plik zawiera próbkę oficjalnych danych o przestępczości w Chicago

---

### Zadanie 1 - Analiza danych Chicago Crimes z użyciem PySpark & ML

Plik: `chicago_crimes_analysis.py`

Program przetwarza i analizuje zbiór danych o przestępstwach w Chicago (`chicago_crimes_sample.csv`) przy użyciu Apache Spark, a następnie buduje model klasyfikacji wieloklasowej.

### Główne etapy przetwarzania:

1. **Inicjalizacja sesji Spark:** Zwiększenie pamięci sterownika i wykonawcy do 4 GB w celu zapewnienia stabilności.
2. **Czyszczenie danych:** Usunięcie duplikatów i wartości `null` z kluczowych kolumn oraz ręczne parsowanie dat w formacie ISO (`yyyy-MM-dd'T'HH:mm:ss.SSS`).
3. **Inżynieria cech (Feature Engineering):** * Wyciąganie godziny i dnia tygodnia z daty.
* Kategoryzacja pory dnia za pomocą funkcji UDF (`noc`, `rano`, `dzien`, `wieczor`).
* Mapowanie typów przestępstw na ogólne kategorie za pomocą mechanizmu `broadcast join`.


4. **Zapis danych:** Eksport oczyszczonych danych do formatu Parquet z partycjonowaniem po roku (`partitionBy("year")`).
5. **Agregacje i Analityka:**
* Statystyki przestępstw według lokalizacji, pory dnia i typu.
* Zaawansowana agregacja z wyliczaniem unikalnych lokalizacji (`countDistinct`).
* Wyświetlenie planu wykonania zapytania za pomocą `.explain(mode="extended")`.


6. **Machine Learning Pipeline:**
* Przygotowanie cech kategorycznych (`StringIndexer` + `OneHotEncoder`).
* Złożenie wektora cech za pomocą `VectorAssembler`.
* Trenowanie modelu `RandomForestClassifier` (30 drzew, max głębokość 5).
* Ewaluacja modelu za pomocą metryki `accuracy` (`MulticlassClassificationEvaluator`).



```python
df_clean = df_clean.withColumn("ParsedDate", F.to_timestamp("date", "yyyy-MM-dd'T'HH:mm:ss.SSS"))
df_enriched = df_clean.join(F.broadcast(df_dict), on="primary_type", how="left")
pipeline = Pipeline(stages=indexers + encoders + [assembler, rf])

```

### Technologie:

* `pyspark` (Spark SQL, Spark ML)
* `numpy` (wymagany przez Spark ML)
* Random Forest Classifier
* Parquet format

### Uruchamianie:

Przed uruchomieniem upewnij się, że masz zainstalowane wymagane pakiety w swoim środowisku wirtualnym (`numpy` oraz `pyspark`).

```bash
pip install numpy pyspark
python chicago_crimes_analysis.py

```
---

### Zadanie 5.1 — Window Functions na recenzjach IMDB
Zadanie polega na wykonaniu zaawansowanej analityki na zbiorze IMDB z użyciem PySpark Window Functions, czyli operacji niemożliwych do wykonania zwykłym `groupBy`.

Zakres zadania:
- Wczytanie 2000 recenzji IMDB do Spark DataFrame.
- Dodanie kolumn: `id` (monotonically increasing), `word_count` (liczba słów).
- Zastosowanie funkcji okienkowych (`Window.partitionBy`, `orderBy`, `rowsBetween`).

Wykonane operacje:
1. Ranking recenzji w obrębie klasy (label)  
Sortowanie po długości (`word_count`) i nadanie rankingu — najdłuższe recenzje mają `rank = 1`.
2. Top‑3 najdłuższe recenzje per klasa  
Wybranie trzech najdłuższych recenzji dla każdej klasy (0 i 1).
3. Różnica od średniej długości w klasie  
Obliczenie:
`word_count - avg(word_count) OVER (PARTITION BY label)`
Pokazuje, o ile dana recenzja odbiega od średniej swojej klasy.
4. Moving average (okno 50)  
Dla każdej klasy policzono średnią długość z ostatnich 50 recenzji, sortując po `id`.
5. Wizualizacja wyników  
Wykres liniowy (matplotlib) przedstawiający przebieg moving average osobno dla recenzji pozytywnych i negatywnych.

---

### Zadania tydzień 11-12

Folder tyd11-12 zawiera implementację autorskiego frameworku Data Quality (kontraktu danych oraz walidatora) w czystym Pythonie, służącego do automatycznej weryfikacji struktury i czystości biznesowej datasetów (na przykładzie IMDB) przed ich przekazaniem do dalszych etapów potoku przetwarzania lub modelowania, wraz z generowaniem raportów walidacyjnych w formacie JSON.

---

### Zawartość folderu `tyd11-12`

* `zadanie_6_1.py` — implementacja frameworku Data Quality (kontraktu danych i walidatora) w czystym Pythonie
* `workspace/` — katalog roboczy przeznaczony na generowane raporty z walidacji
* `workspace/data_quality_report.json` — wygenerowany automatycznie raport jakości danych z testu IMDB

---

### Zadanie 1 — Kontrakt danych + raport JSON (Lab 6 — Data Quality)

Plik: `zadanie_6_1.py`

Program implementuje lekki, produkcyjny mechanizm **Data Quality Framework** służący do weryfikacji i zapewniania integralności danych wejściowych w potoku przetwarzania (pipeline) przed etapem trenowania modeli Machine Learning.

### Główne etapy przetwarzania:

1. **Definicja Kontraktu (DataContract):** Tworzenie deklaratywnych reguł sprawdzających strukturalną oraz biznesową poprawność zestawu danych przy użyciu obiektów klasy `Rule`.
2. **Implementacja poziomów Severity:** Przypisywanie do każdej reguły stopnia krytyczności (`info`, `warning`, `error`), pozwalającego odróżnić drobne anomalie od błędów krytycznych.
3. **Mechanizm Fail-Fast (DataValidator):** Automatyczne przerywanie potoku i rzucanie wyjątku `ValueError` w momencie, gdy jakakolwiek reguła oznaczona jako `error` nie zostanie spełniona.
4. **Weryfikacja jakości dla zestawu IMDB:** Walidacja danych pod kątem 6 rygorystycznych reguł biznesowych:
   * `no_nulls` — całkowity brak wartości nieokreślonych w kolumnach kluczowych.
   * `labels_in_set` — sprawdzenie poprawności klasyfikacji etykiet docelowych.
   * `min_word_count` / `max_word_count` — eliminacja zbyt krótkich szumów oraz zbyt długich anomalii tekstowych.
   * `no_duplicates` — unikanie duplikacji danych treningowych.
   * `class_balance` — kontrola zrównoważenia proporcji między klasami pozytywnymi a negatywnymi.
5. **Obsługa reguł ostrzegawczych (Bonus):** Implementacja testu `no_html_tags` z poziomem `warning`, która rejestruje występowanie tagów HTML w raporcie, lecz nie zatrzymuje działania programu.
6. **Eksport raportu:** Zrzucenie całego wyniku walidacji wraz z precyzyjnym znacznikiem czasu (*timestamp*) do ujednoliconego pliku JSON.

```python
imdb_contract.add_rule("no_nulls", check_no_nulls, severity="error")
imdb_contract.add_rule("no_html_tags", check_no_html_tags, severity="warning")
final_report = validator.validate(df_imdb)

```

### Technologie:

* `pandas` (zarządzanie strukturami danych i analiza statystyczna)
* `json` / `os` (manipulacja systemem plików oraz serializacja raportu)
* `dataclasses` (strukturyzacja reguł walidacyjnych)
* Czysty Python 3.x (implementacja silnika walidatora)

### Uruchamianie:

Przed uruchomieniem skryptu upewnij się, że masz utworzone i aktywowane środowisko wirtualne `.venv` oraz zainstalowaną bibliotekę `pandas`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas
python zadanie_6_1.py
```
* `zadanie_6_1.py` — implementacja frameworku Data Quality (kontraktu danych i walidatora) w czystym Pythonie
* `_workspace/` — katalog roboczy przeznaczony na generowane raporty z walidacji
* `_workspace/data_quality_report.json` — wygenerowany automatycznie raport jakości danych z testu IMDB

---
