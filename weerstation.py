def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"


def weerstation():
    temperaturen = []

    for dag in range(1, 8):
        print("Dag", dag)

        temp_invoer = input("Temperatuur in Celsius: ")

        if temp_invoer == "":
            break

        temp_celcius = float(temp_invoer)

        windsnelheid = float(input("Windsnelheid in m/s: "))
        luchtvochtigheid = float(input("Luchtvochtigheid in %: "))

        temperaturen.append(temp_celcius)

        fahrenheit = Fahrenheit(temp_celcius)
        rapport = weerrapport(temp_celcius, windsnelheid, luchtvochtigheid)
        gemiddelde = sum(temperaturen) / len(temperaturen)

        print("Temperatuur Celsius:", temp_celcius)
        print("Temperatuur Fahrenheit:", fahrenheit)
        print("Weerrapport:", rapport)
        print("Gemiddelde temperatuur:", gemiddelde)


weerstation()