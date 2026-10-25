kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]
summa = 0

for kustannus in kustannukset:
    print("Tuotteen valmistuskustannus:", kustannus, "€")
    summa += kustannus

print("Valmistuskustannukset yhteensä:", summa, "€")