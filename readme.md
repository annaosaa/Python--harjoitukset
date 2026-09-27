
# Python harjoitukset

**Anna Saavalainen**

## Moduuli 1
Löytyy hello.py


## Moduuli 2
Tehty tehtävät 1, 2, 3, 4, 5 ja 6 


## Moduuli 3  

Kotitehtävät 1, 2 , 3 ja 4 (torstain tunnilta)

readme.md

Oikea vastaus teht. 2 tässä muodossa

import math

#pii*r**2

sade = float(input("Anna ympyrän säde: "))

A = math.pi * sade **2

print(f"Ympyrän pinta-ala on A: .2f)

(selitys muuntofunktioille: float desimaaliluku ja int kokonaisluku)


elif = joko tai

## Moduuli 4
Tehtävät 1-6 tehtyinä


# Tehtävä kansio sisältää tunnilla tehtyjä harjoitteita

Kotitehtävien tarkistus 14.9.

tehtävä 1
tässä muodossa:

if mitta >= 37:
    print("Hieno saalis, voit pitää kalan!")

else:
    print(f"Kalasi on {37-pituus} cm liian pieni, laske kala takaisin!")

KATSO ENSIMMÄISEN TUNNIN MATERIAALEISTA SELITYS MERKKEIHIN!

tehtävä 2
tässä muodossa:

luokka = input("Missä hyttiluokassa olet (LUX, A, B, C): ").upper()

if luokka == "LUX" 
NÄMÄ SAMOIN KUN TEHTY, AINOA ERO LUOKKA-SANASSA!

AINA KANNATTAA OLETTAA ETTEI KÄYTTÄJÄ TIEDÄ ESIM. VAIHTOEHTOJA KERRO NE LAUSEESSA INPUT... KUTEN TÄÄLLÄ:
luokka = input("Missä hyttiluokassa olet (LUX, A, B, C): ")

.upper() tämä muuttaa käyttäjän tekemän isoiksi kirjaimiksi, esim jos käyttäjä kirjoittaa lux se korjaa sen LUX.

ELIF LAUSETTA EI OLE OLEMASSA ILMAN IF LAUSEKETTA. NIIDEN TULEE OLLA SAMASSA RAKENTEESSA!
SAMALLA RIVILLÄ ESIM NÄIN:  IF
                            ELSE
NIIN OHJELMAN ON PAKKO TARKISTAA KAIKKI VAIHTOEHDOT

.lower() muuttaa kaikki pieniksi ja .capitalize() muuttaa ekan kirjaimen isoksi

voi laittaa myös näin:
if luokka == "LUX" or luokka == "lux"

tehtävä 3
tässä muodossa: 

Sukupuoli = input("Anna sukupuolesi (N / M) ").upper()

hemoglobiini = int(input("Anna hemoglobiinisi: (g / l) "))

if Sukupuoli == "N":

NÄMÄ OIKEIN:
    if hemoglobiini < 117:
        print("Hemoglobiinisi on alhainen.")

NÄIN:

elif Sukupuoli == "M":
    if

    elif 

    else
LISÄÄ LOPPUUN TÄMÄ:

else:
    print("Virheellinen sukupuoli.")


tehtävä 4
NÄIN:

Vuosi = int(input("Kerro vuosiluku: "))

if Vuosi % 4 == 0:
    if Vuosi % 100 == 0 and (Vuosi % 400 == 0):
    
        if Vuosi Vuosi % 400 == 0:
            print("Vuosi on karkausvuosi")

    else:
        print("Vuosi on karkausvuosi")

else:
    print("Vuosi ei ole karkausvuosi")

VAIHDA OMA JÄRJESTYS 400 100 JA 4, JOS EKANA 4 NIIN SE EI ANNA OIKEAA TULOSTA!!

Pelkät lainausmerkit on tyhjä merkkijono ""