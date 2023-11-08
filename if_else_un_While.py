"""
Praktisks piemērs while cikla un apgalvojuma izmantošanai
"""


print("Lūdzu izveido savu parli:")
parole = input()

while True: #True boolane vērtība kura visu laiku patiesa, līdz to pārbauda
   
    print("Ievadi paroli atkārtoti:")
    parole2 = input()

    if parole2==parole:
        break

print("Paldies, tava parole ir izveidota")   

