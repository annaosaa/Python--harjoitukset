def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [4, 8, 15, 16, 23, 42]
print("Summa on", laske_summa(luvut))