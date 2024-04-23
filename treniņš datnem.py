#Definēt funkciju kuras argumenti ir divi csv failu nosaukumi
#pārveido failus masīvos
#Jāsalīdzina masīvu garumi

import csv

def csv_lasisana(csv1,csv2): # definējasm nosaukumu un pievienojam argumentus
    
    with open(csv1,'r',encoding="UTF-8") as fails:
        lasit_csv = csv.reader(fails)

        kolonuNosaukumi = next(lasit_csv)
        