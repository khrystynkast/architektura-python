import requests
import time
import concurrent.futures

CAT_API_URL = "https://catfact.ninja/fact"

def get_cat_fact():
    """Pobiera jeden losowy fakt o kotach."""
    try:
        return requests.get(CAT_API_URL).json().get("fact")
    except Exception as e:
        return f"[BŁĄD] {e}"



print("--- WERSJA SEKWENCYJNA ---")
start_seq = time.time()

facts_seq = []
for _ in range(20):
    fact = get_cat_fact()
    facts_seq.append(fact)

end_seq = time.time()
print(f"Czas sekwencyjny: {end_seq - start_seq:.2f} s")
print(f"Pobrano {len(facts_seq)} faktów\n")



print("--- WERSJA WIELOWĄTKOWA (ThreadPoolExecutor) ---")
start_thr = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    facts_thr = list(executor.map(lambda _: get_cat_fact(), range(20)))

end_thr = time.time()
print(f"Czas wielowątkowy: {end_thr - start_thr:.2f} s")
print(f"Pobrano {len(facts_thr)} faktów\n")



print("Przykładowe fakty (pierwsze 5):")
for i, fact in enumerate(facts_thr[:5], 1):
    print(f"{i}. {fact}")
