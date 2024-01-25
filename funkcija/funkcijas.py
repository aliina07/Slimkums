"""
20.11.23
funkcijas
"""

#Sintakse
"""
Atslēgvārds
def

def funkcijas_nosaukums():
    fukcijas kods

Izsaukšana:
funcijas_nosaukums     
"""

def pirma_funkcija(): #Iespēja pivienot argumentus jeb sa'
    print("Mana pirmā funkcija, Juuhuuuu!!!!!")
 
# katru funkciju nepieciešams atseviški palaist


pirma_funkcija()
pirma_funkcija()
pirma_funkcija()
pirma_funkcija()


atbilde = input("gribi, es ar kaut ko palielīšos?")

if atbilde == "Jā":
    pirma_funkcija()
else:
    print("Nu labi ;(")    


def otra_funkcija():
    pirma_funkcija()
    print("Funkcija funkcija!") 

