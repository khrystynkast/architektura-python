import requests
import json

def pobierz_pogode(miasto, api_key):
    """Pobiera aktualną pogodę dla podanego miasta z API OpenWeather."""
    
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={miasto}&appid={api_key}&units=metric&lang=pl"
    )

    response = requests.get(url)

    if response.status_code == 200:
        dane = response.json()

        temperatura = dane["main"]["temp"]
        opis = dane["weather"][0]["description"]
        wilgotnosc = dane["main"]["humidity"]

        return {
            "temperatura": temperatura,
            "opis": opis,
            "wilgotnosc": wilgotnosc
        }
    else:
        return None


def main():
    api_key = "KEY"  # usuniete   

    historia = []

    while True:
        miasto = input("Podaj miasto (lub 'quit' aby wyjść): ")

        if miasto.lower() == "quit":
            print("Do zobaczenia!")
            break

        wynik = pobierz_pogode(miasto, api_key)

        if wynik:
            print(f"\nPogoda w {miasto}:")
            print(f"Temperatura: {wynik['temperatura']}°C")
            print(f"Opis: {wynik['opis']}")
            print(f"Wilgotność: {wynik['wilgotnosc']}%\n")

            historia.append({
                "miasto": miasto,
                "wynik": wynik
            })
        else:
            print("Nie znaleziono miasta lub błąd API.\n")


    with open("historia.json", "w", encoding="utf-8") as f:
        json.dump(historia, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
