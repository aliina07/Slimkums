
import csv 

def csv_lasisana(datiViens,datiDivi):
    
    with open(datiViens.csv,'r', encoding="UTF-8") as fails:
        lasit_csv = csv.reader(fails)
    


def salidzini_datus(datiViens,datiDivi):

    datiViens.csv = salidzini_datus(datiViens)
    datiDivi.csv = salidzini_datus(datiDivi)


    datiViens.csv = set(datiViens.csv.split())
    datiDivi.csv = set(datiDivi.csv.split())


kopigi_dati = (datiViens == datiDivi)

if kopigi_dati == "Sakīt":
    print("Sakrīt!")



salidzini_datus(datiViens, datiDivi)