import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä: "))

heitto = heita_noppaa(maksimi)
print(heitto)

while heitto != maksimi:
    heitto = heita_noppaa(maksimi)
    print(heitto)