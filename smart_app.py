
import weerstation
import smart_app_controller
import urllib.request
import json


def huidig_weer():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current=temperature_2m"

        antwoord = urllib.request.urlopen(url)
        gegevens = json.loads(antwoord.read())

        temperatuur = gegevens["current"]["temperature_2m"]

        print("Huidige temperatuur in Utrecht:", temperatuur, "°C")

    except:
        print("Het ophalen van het weer is mislukt.")


def smart_app():
    while True:
        print()
        print("===== SMART APP =====")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Huidig weer Utrecht")
        print("4. Stoppen")

        try:
            keuze = int(input("Maak een keuze: "))

            if keuze == 1:
                weerstation.weerstation()

            elif keuze == 2:
                smart_app_controller.smart_app_controller()

            elif keuze == 3:
                huidig_weer()

            elif keuze == 4:
                print("Programma gestopt.")
                break

            else:
                print("Kies een nummer van 1 tot en met 4.")

        except ValueError:
            print("Voer een getal in.")


smart_app()