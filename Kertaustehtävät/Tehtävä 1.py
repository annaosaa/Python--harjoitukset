tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt tunnit: "))
paiva = input("Anna viikonpäivä: ")

if paiva.lower() == "sunnuntai":
    palkka = tuntipalkka * 2 * tunnit
else:
    palkka = tuntipalkka * tunnit

print("Päiväpalkka on", palkka, "€")