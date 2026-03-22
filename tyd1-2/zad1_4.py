#Moduł analizy tekstu

def policz_slowa(tekst):
    """Zwraca liczbę słów w tekście."""
    return len(tekst.split())

def najdluzsze_slowo(tekst):
    """Zwraca najdłuższe słowo w tekście."""
    slowa = tekst.split()
    return max(slowa, key=len)

def czestotliwosc_slow(tekst):
    """Zwraca słownik {słowo: liczba_wystąpień}."""
    slowa = tekst.split()
    freq = {}
    for s in slowa:
        freq[s] = freq.get(s, 0) + 1
    return freq

def cenzura(tekst, zakazane_slowa):
    """Zamienia zakazane słowa na '***'."""
    slowa = tekst.split()
    wynik = ["***" if s in zakazane_slowa else s for s in slowa]
    return " ".join(wynik)
