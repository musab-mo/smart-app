def aantal_dagen(inputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    uitvoer = []

    for regel in regels[1:]:
        gegevens = regel.strip().split()

        datum = gegevens[0]
        aantal_mensen = int(gegevens[1])
        temp_ingesteld = int(gegevens[2])
        temp_buiten = int(gegevens[3])
        neerslag = int(gegevens[4])

        # CV berekenen
        verschil = temp_ingesteld - temp_buiten

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        # Ventilatie berekenen
        ventilatie = aantal_mensen + 1

        if ventilatie > 4:
            ventilatie = 4

        # Besproeiing berekenen
        if neerslag < 3:
            besproeiing = True
        else:
            besproeiing = False

        regel_output = datum + ";" + str(cv) + ";" + str(ventilatie) + ";" + str(besproeiing)

        uitvoer.append(regel_output)

    bestand = open(outputFile, "w")

    for regel in uitvoer:
        bestand.write(regel + "\n")

    bestand.close()


def overwrite_settings(outputFile):
    bestand = open(outputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    datum_gezocht = input("Van welke datum wil je een instelling aanpassen? ")

    gevonden = False

    for i in range(len(regels)):
        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum_gezocht:
            gevonden = True

            print("1. CV")
            print("2. Ventilatie")
            print("3. Besproeiing")

            keuze = input("Welke instelling wil je aanpassen? ")

            if keuze == "1":
                waarde = int(input("Nieuwe CV waarde (0-100): "))

                if waarde >= 0 and waarde <= 100:
                    gegevens[1] = str(waarde)
                else:
                    return -3

            elif keuze == "2":
                waarde = int(input("Nieuwe ventilatie waarde (0-4): "))

                if waarde >= 0 and waarde <= 4:
                    gegevens[2] = str(waarde)
                else:
                    return -3

            elif keuze == "3":
                waarde = int(input("Besproeiing? 0 = False, 1 = True: "))

                if waarde == 0:
                    gegevens[3] = "False"
                elif waarde == 1:
                    gegevens[3] = "True"
                else:
                    return -3

            else:
                return -3

            regels[i] = ";".join(gegevens) + "\n"

    if gevonden == False:
        return -1

    bestand = open(outputFile, "w")

    for regel in regels:
        bestand.write(regel)

    bestand.close()

    return 0


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print()
        print("===== SMART APP CONTROLLER =====")
        print("1. Aantal dagen")
        print("2. Automatisch berekenen")
        print("3. Instelling aanpassen")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            aantal = aantal_dagen(inputFile)
            print("Aantal dagen:", aantal)

        elif keuze == "2":
            auto_bereken(inputFile, outputFile)
            print("De berekeningen zijn opgeslagen in output.txt")

        elif keuze == "3":
            resultaat = overwrite_settings(outputFile)

            if resultaat == 0:
                print("Instelling succesvol aangepast.")
            elif resultaat == -1:
                print("Datum niet gevonden.")
            elif resultaat == -3:
                print("Ongeldige instelling of waarde.")

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")

smart_app_controller()

