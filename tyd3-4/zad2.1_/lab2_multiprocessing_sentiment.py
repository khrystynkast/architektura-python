import re
import time
import os
import matplotlib.pyplot as plt
import functools
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from datasets import load_dataset

@functools.lru_cache(maxsize=4)
def get_imdb_subset(split: str, n: int):
    ds = load_dataset("stanfordnlp/imdb", split=split).shuffle(seed=42).select(range(n))
    return [r["text"] for r in ds]

POS_WORDS = {"good","great","excellent","wonderful","love","best","amazing","brilliant","perfect"}
NEG_WORDS = {"bad","worst","awful","terrible","hate","boring","waste","poor","horrible"}

def sentiment_score(text: str) -> int:
    words = re.findall(r"\w+", text.lower())
    pos = sum(1 for w in words if w in POS_WORDS)
    neg = sum(1 for w in words if w in NEG_WORDS)
    return pos - neg

if __name__ == "__main__":
    samples = get_imdb_subset("train", 5000)
    texts = samples

    t0 = time.time()
    seq_results = [sentiment_score(t) for t in texts]
    seq_time = time.time() - t0
    print(f"Sekwencyjnie: {seq_time:.2f}s")

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=16) as pool:
        thread_results = list(pool.map(sentiment_score, texts))
    thread_time = time.time() - t0
    print(f"ThreadPool: {thread_time:.2f}s")

    t0 = time.time()
    with Pool(processes=os.cpu_count()) as p:
        mp_results = p.map(sentiment_score, texts, chunksize=100)
    mp_time = time.time() - t0
    print(f"Multiprocessing: {mp_time:.2f}s")

    plt.figure(figsize=(8,5))
    plt.bar(["Sekwencyjnie", "ThreadPool", "Multiprocessing"],
            [seq_time, thread_time, mp_time],
            color=["gray", "orange", "green"])
    plt.ylabel("Czas [s]")
    plt.title("Porównanie czasu wykonania — 5000 recenzji IMDB")
    plt.show()
