import queue
import threading
import time

LIMIT = 30

def producer(q):
    """Producent generuje kolejne liczby naturalne i wrzuca je do kolejki."""
    for number in range(1, LIMIT + 1):
        q.put(number)
        print(f"[PRODUCENT] Dodano liczbę: {number}")
        time.sleep(0.05)  


    q.put(None)
    q.put(None)


def consumer_even(q):
    """Konsument pobiera tylko liczby parzyste."""
    while True:
        number = q.get()
        if number is None:
            q.task_done()   
            print("[KONSUMENT PARZYSTE] Koniec pracy")
            break

        if number % 2 == 0:
            print(f"[PARZYSTE] Przetworzono: {number}")

        q.task_done()


def consumer_odd(q):
    """Konsument pobiera tylko liczby nieparzyste."""
    while True:
        number = q.get()
        if number is None:
            q.task_done()   
            print("[KONSUMENT NIEPARZYSTE] Koniec pracy")
            break

        if number % 2 != 0:
            print(f"[NIEPARZYSTE] Przetworzono: {number}")

        q.task_done()



if __name__ == "__main__":
    q = queue.Queue()


    producer_thread = threading.Thread(target=producer, args=(q,))
    even_thread = threading.Thread(target=consumer_even, args=(q,))
    odd_thread = threading.Thread(target=consumer_odd, args=(q,))


    producer_thread.start()
    even_thread.start()
    odd_thread.start()


    producer_thread.join()


    q.join()


    even_thread.join()
    odd_thread.join()

    print("\n--- ZAKOŃCZONO PRZETWARZANIE ---")
