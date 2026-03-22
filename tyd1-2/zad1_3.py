#Gra „Zgadnij liczbę”

import random

while True:                      # 1. Główna pętla gry
    liczba = random.randint(1, 100)
    proby = 0

    while True:                  # 2. Pętla zgadywania
        proby += 1
        guess = int(input("Zgadnij liczbę: "))

        if guess < liczba:       # 3. Warunki
            print("Za mało!")
        elif guess > liczba:
            print("Za dużo!")
        else:
            print("Gratulacje!")
            break                # 4. Przerwanie pętli zgadywania

    if input("Grasz dalej (t/n)? ") != 't':
        break                    # 5. Przerwanie całej gry


    """
    
🟦 1. if / elif / else — instrukcje warunkowe
Jeśli if jest prawdziwy → wykonuje kod i pomija resztę.

Jeśli if jest fałszywy → sprawdza elif.

Jeśli wszystkie warunki są fałszywe → wykonuje else.
    
    
🟩 2. pętla for — przechodzenie po elementach
lista = [10, 20, 30]

for x in lista:
    print(x)

Python robi:
x = 10 → print
x = 20 → print
x = 30 → print


🟧 3. pętla while — powtarzanie, dopóki warunek jest prawdziwy
x = 0

while x < 5:
    print(x)
    x += 1

Python robi:
0, 1, 2, 3, 4
i kończy, gdy x == 5


🟥 4. break — przerwanie pętli
for x in range(10):
    if x == 5:
        break
    print(x)
Wynik: 0, 1, 2, 3, 4


🟨 5. continue — pomiń tę iterację i idź dalej
for x in range(5):
    if x == 2:
        continue
    print(x)
Wynik: 0, 1, 3, 4 (pomija 2)

🟪 6. enumerate() — numerowanie elementów
lista = ["a", "b", "c"]

for i, litera in enumerate(lista):
    print(i, litera)

0 a
1 b
2 c


🟫 7. zip() — łączenie dwóch list w pary
imiona = ["Ala", "Ola", "Jan"]
wiek = [20, 25, 30]

for i, w in zip(imiona, wiek):
    print(i, w)

Ala 20
Ola 25
Jan 30
    """
