kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna kaupunki {i + 1}/5: ")
    kaupungit.append(kaupunki)

print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)