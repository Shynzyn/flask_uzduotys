def funkcija(metai):
    metai = int(metai)
    if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
        return "Keliamieji"
    else:
        return "Nekeliamieji"
