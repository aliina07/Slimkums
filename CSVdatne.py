"""
CSV datnes lasīšana redigēsana un izveidošana
"""

#fails tiek atvērs ka teksta fails
fails = open("csv.csv", encoding="UTF-8")
print(fails.read())
fails.close()

# lai nolasitu csv datni(fails) nepieciešama biblioteka

import csv 

fails = open("csv.csv", encoding="UTF-8")

lasit_csv = csv.reader(fails) #mēs nolasām failu
print(lasit_csv)  # redzam tikai ojektu

# kolonu nosaukumi

kolonuNosaukumi = next(lasit_csv)
print(kolonuNosaukumi)

#satura nolasīšana 
#cikls

saturs = []
for rinda in lasit_csv:
    saturs.append(rinda)

print(saturs)    