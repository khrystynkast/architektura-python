import sqlite3
import json
from pathlib import Path
import os

# Ustawienie WORKDIR na folder, w którym znajduje się plik
WORKDIR = Path(__file__).parent

# Ścieżki do baz SQL i JSON
DB_PATH = WORKDIR / "imdb.db"          # klasyczna baza SQL z Lab 4
DB_JSON = WORKDIR / "imdb_json.db"     # nowa baza JSON

# Jeśli istnieje — usuń
if DB_JSON.exists():
    DB_JSON.unlink()

# Połączenie z bazą JSON
conn2 = sqlite3.connect(str(DB_JSON))
cur2 = conn2.cursor()

# Krok 1: schemat z kolumną JSON
cur2.execute("""
CREATE TABLE reviews_json (
    id INTEGER PRIMARY KEY,
    doc TEXT NOT NULL
)
""")

# Funkcja pobierająca IMDB (ta sama co w Lab 4)
from datasets import load_dataset

def get_imdb_subset(split: str, n: int):
    ds = load_dataset("stanfordnlp/imdb", split=split).shuffle(seed=42).select(range(n))
    return [(r["text"], r["label"]) for r in ds]

# Krok 2: załaduj 2000 próbek jako dokumenty JSON
samples_nosql = get_imdb_subset("train", 2000)

for i, (text, label) in enumerate(samples_nosql):
    words = text.split()
    tags = [w for w in words if len(w) > 5][:3]

    doc = {
        "text": text,
        "label": label,
        "stats": {
            "word_count": len(words),
            "sentiment_hint": "pos" if label == 1 else "neg"
        },
        "tags": tags
    }

    cur2.execute(
        "INSERT INTO reviews_json (id, doc) VALUES (?, ?)",
        (i, json.dumps(doc))
    )

conn2.commit()

# Krok 3: zapytania NoSQL-style
queries = {
    "rozklad_klas": """
        SELECT json_extract(doc, '$.stats.sentiment_hint') AS hint,
               COUNT(*) AS n
        FROM reviews_json
        GROUP BY hint
    """,

    "avg_word_count_per_class": """
        SELECT json_extract(doc, '$.stats.sentiment_hint') AS hint,
               AVG(json_extract(doc, '$.stats.word_count')) AS avg_wc
        FROM reviews_json
        GROUP BY hint
    """,

    "tags_zawiera_movie": """
        SELECT id, json_extract(doc, '$.tags')
        FROM reviews_json
        WHERE json_extract(doc, '$.tags') LIKE '%movie%'
        LIMIT 10
    """,

    "top5_najdluzsze_pozytywne": """
        SELECT id,
               json_extract(doc, '$.stats.word_count') AS wc
        FROM reviews_json
        WHERE json_extract(doc, '$.label') = 1
        ORDER BY wc DESC
        LIMIT 5
    """
}

# Wykonanie zapytań
for name, sql in queries.items():
    print(f"\n-- {name} --")
    for row in cur2.execute(sql):
        print(" ", row)

# Krok 4: porównanie rozmiaru baz
size_sql = os.path.getsize(DB_PATH) if DB_PATH.exists() else 0
size_json = os.path.getsize(DB_JSON)

print("\n=== Porownanie ===")
print(f"SQL schema (reviews):       {size_sql:>9,} bajtow")
print(f"JSON schema (reviews_json): {size_json:>9,} bajtow")

conn2.close()
