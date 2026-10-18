luvut = []

syote = input("Anna luku (tyhjä lopettaa): ")

while syote != "":
    luvut.append(int(syote))
    syote = input("Anna luku (tyhjä lopettaa): ")

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)