import random

def heita_noppaa():
    return random.randint(1, 6)

heitto = heita_noppaa()
print(heitto)

while heitto != 6:
    heitto = heita_noppaa()
    print(heitto)