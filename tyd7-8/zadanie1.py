import sqlite3
import requests

# Pobieranie
response = requests.get("https://randomuser.me/api/?results=30")
users = response.json()["results"]

# Połączenie z bazą i stwórz tabelę
conn = sqlite3.connect("zad1.db")  
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    age INTEGER,
    gender TEXT,
    country TEXT
)
""")
cur.execute("DELETE FROM Users")

# Dodawanie danych do tabeli
for u in users:
    cur.execute("""
        INSERT INTO Users (first_name, last_name, email, age, gender, country)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        u["name"]["first"],
        u["name"]["last"],
        u["email"],
        u["dob"]["age"],
        u["gender"],
        u["location"]["country"]
    ))

conn.commit()
conn.close()

print("Gotowe! Dane zapisane w zad1.db")

conn = sqlite3.connect("zad1.db")
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM Users")
count = cur.fetchone()[0]
conn.close()

print("Liczba rekordów w tabeli Users:", count)

# Analiza danych

conn = sqlite3.connect("zad1.db")
cur = conn.cursor()

print("\n--- Ile jest mężczyzn, a ile kobiet? ---")
cur.execute("SELECT gender, COUNT(*) FROM Users GROUP BY gender")
print(cur.fetchall())

print("\n--- Jaki jest średni wiek? ---")
cur.execute("SELECT AVG(age) FROM Users")
print(cur.fetchone()[0])

print("\n--- W ilu krajach mieszkają? ---")
cur.execute("SELECT COUNT(DISTINCT country) FROM Users")
print(cur.fetchone()[0])

conn.close()

