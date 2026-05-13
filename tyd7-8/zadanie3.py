import numpy as np

# Filmy
filmy = {
    "Dune: Part Two (2024)":                     np.array([0.9, 0.2, 0.85]),
    "Oppenheimer (2023)":                        np.array([0.88, 0.15, 0.8]),
    "Barbie (2023)":                             np.array([0.25, 0.9, 0.2]),
    "Spider-Man: Across the Spider-Verse (2023)": np.array([0.7, 0.4, 0.95]),
    "Poor Things (2023)":                        np.array([0.3, 0.85, 0.25]),
}

# Cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Semantic search
def semantic_search(query_vec, database, top_k=3):
    wyniki = []
    for title, vec in database.items():
        sim = cosine_similarity(query_vec, vec)
        wyniki.append((title, sim))
    wyniki.sort(key=lambda x: x[1], reverse=True)
    return wyniki[:top_k]

# Zapytanie 
query = np.array([0.85, 0.25, 0.9])

results = semantic_search(query, filmy, top_k=3)

print("Top 3 najbardziej podobne filmy:")
for title, sim in results:
    print(f"  {title}: {sim:.3f}")
