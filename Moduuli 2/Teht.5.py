# Kysy käyttäkälyä keskiaiset mitat
leiviskat = float(input("Annan leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Määritetään muunnoskerroin
Luoti_grammoina = 13.3
Naula_grammoina = 32 * Luoti_grammoina
Leiviska_grammoina = 20 * Naula_grammoina

# Lasketaan kokonaispaino grammoina
kokonaispaino_grammoina = (leiviskat * Leiviska_grammoina) + (naulat * Naula_grammoina) + (luodit * Luoti_grammoina)

# Muunnetaan kokonaispaino kilogrammoiksi ja grammoiksi
kilogrammat = int(kokonaispaino_grammoina // 1000)
grammat = kokonaispaino_grammoina % 1000

# Tulostetaan tulokset
print(f"Kokonaispaino on: {kilogrammat} kg ja {grammat:.2f} g")

