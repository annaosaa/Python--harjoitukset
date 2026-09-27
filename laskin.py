print("TERVETULOA LASKINOHJELMAAN")

print("Valitse mitä toimintoa haluat käyttää: ")
print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku")
Valinta = input("Amma valintasi: ").upper()

a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))

if valinta == "A":
    print(f"lukujen {a} ja {b} summa on {a+b}.")

elif valinta == "B":

