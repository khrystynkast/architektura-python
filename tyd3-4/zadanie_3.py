import multiprocessing
import time
from lab2_functions import calculate_power_sum


START = 1
END = 10_000   


if __name__ == "__main__":
    print("--- WERSJA SEKWENCYJNA ---")
    start_seq = time.time()

    seq_results = []
    for n in range(START, END + 1):
        seq_results.append(calculate_power_sum(n))

    end_seq = time.time()
    print(f"Czas sekwencyjny: {end_seq - start_seq:.2f} s\n")


    print("--- WERSJA RÓWNOLEGŁA (multiprocessing) ---")
    start_mp = time.time()


    with multiprocessing.Pool() as pool:
        mp_results = pool.map(calculate_power_sum, range(START, END + 1))

    end_mp = time.time()
    print(f"Czas multiprocessing: {end_mp - start_mp:.2f} s\n")


    print("--- PORÓWNANIE ---")
    print(f"Przyspieszenie: { (end_seq - start_seq) / (end_mp - start_mp):.2f}x szybciej")
