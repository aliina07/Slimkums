import csv

# Izveido funkciju, kas nolasa datus no CSV datnes
def nolasi_datus(datnes_nosaukums):
    with open(datnes_nosaukums, 'r') as f:
        dati = []
        csv_reader = csv.reader(f)
    for row in csv_reader:


# Izveido funkciju datu salīdzināšanai
def salidzini_datus(datne1, datne2):
    dati1 = nolasi_datus(datne1)
    dati2 = nolasi_datus(datne2)

    if dati1 is None or dati2 is None:
        return

    dati1_set = set(dati1)
    dati2_set = set(dati2)

    kopigi_dati = dati1_set.intersection(dati2_set)

    if kopigi_dati:
        print("Sakrīt!")
    else:
        print("Nav sakritību.")

# Testa datnes
datne1 = "datiViens.csv"
datne2 = "datiDivi.csv"

# Salīdzina datus no divām CSV datnēm
salidzini_datus(datne1, datne2)