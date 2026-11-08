import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    ala = math.pi * sade ** 2
    return hinta / ala

halkaisija1 = float(input("Anna pizzan 1 halkaisija (cm): "))
hinta1 = float(input("Anna pizzan 1 hinta (€): "))
halkaisija2 = float(input("Anna pizzan 2 halkaisija (cm): "))
hinta2 = float(input("Anna pizzan 2 hinta (€): "))

yh1 = yksikkohinta(halkaisija1, hinta1)
yh2 = yksikkohinta(halkaisija2, hinta2)

if yh1 < yh2:
    print("Pizza 1 antaa paremman vastineen rahalle")
elif yh2 < yh1:
    print("Pizza 2 antaa paremman vastineen rahalle")
else:
    print("Pizzat ovat yhtä edullisia")