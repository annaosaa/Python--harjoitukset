import random

# Arvotaan kolme satunnaista lukua väliltä 1-6
luku1 = random.randint(0, 9)
luku2 = random.randint(0, 9)
luku3 = random.randint(0, 9)

# Muunnetaan numerot tekstiksi (f-string), jotta esimerkiksi "007" tulostuu oikein nollilla
kolmenumeroinen_koodi = f"{luku1}{luku2}{luku3}"

# 2. Arvotaan nelinumeroinen koodi (numerot väliltä 1..6)
koodi_4_nro1 = random.randint(1, 6)
koodi_4_nro2 = random.randint(1, 6)
koodi_4_nro3 = random.randint(1, 6)
koodi_4_nro4 = random.randint(1, 6)

nelinumeroinen_koodi = f"{koodi_4_nro1}{koodi_4_nro2}{koodi_4_nro3}{koodi_4_nro4}"

# Tulostetaan arvotut koodit käyttäjälle
print(f"Kolmenumeroinen koodi (0-9): {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi (1-6): {nelinumeroinen_koodi}")
