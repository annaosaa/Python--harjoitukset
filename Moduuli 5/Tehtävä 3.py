luku = int(input("Anna kokonaisluku: "))

alkuluku = True

if luku < 2:
    alkuluku = False
else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
            break

if alkuluku:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")