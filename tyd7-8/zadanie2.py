from pymongo import MongoClient
import requests

# MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client.lab4
networks = db["networks"]

networks.delete_many({})

# Pobieranie danych z API
response = requests.get("https://api.geckoterminal.com/api/v2/networks")
data = response.json()["data"]

# Debug – zobacz strukturę
print("Przykładowy dokument:")
print(data[0])

# Dodawanie danych do kolekcji
networks.insert_many(data)

print("Wstawiono dokumentów:", networks.count_documents({}))

# Agregacja – poprawne pole: coingecko_asset_platform_id
pipeline = [
    {"$group": {"_id": "$attributes.coingecko_asset_platform_id", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

print("\n--- Liczba sieci per typ (coingecko_asset_platform_id) ---")
for doc in networks.aggregate(pipeline):
    print(doc)
