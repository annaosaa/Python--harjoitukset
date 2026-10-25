sanat = ["auto", "tietokone", "kissa", "ohjelmointi", "koulu", "juoksu", "pöytä"]
laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print("Yli 5 kirjaimen sanoja on", laskuri)