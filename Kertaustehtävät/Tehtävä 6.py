luvut = []

luku = int(input("Anna arvo: "))

while luku != 0:
    luvut.append(luku)
    print("Lisäysjärjestyksessä:", luvut)
    print("Järjestettynä:", sorted(luvut))
    luku = int(input("Anna arvo: "))