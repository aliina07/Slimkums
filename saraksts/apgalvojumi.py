"""
Apgalvojumi jeb if, else, elif statement
"""


# Sintakse:
"""
if nosacijums:
    print("darbiba")
else:
    print(Notiek tad, ja neizpildās nosascijums)
"""

gadi = 19 #mainīgā gadi defimēšana un vērtības pišķiršana

if gadi<18:
    print("Nepilngadīga persona")
else:
    print("Pilngadīga persona")



#nedēļas dienu piemērs

nedelasDiena = 5

if nedelasDiena==1:
    print("Pirmdiena")
if nedelasDiena==2:
    print("Otardiena")    
elif nedelasDiena==3:  #Nākošo iespejamo pārbaudi
    print("Trešdiena")  
elif nedelasDiena==4:  
    print("Ceturtdiena")    
elif nedelasDiena==5:  
    print("Piekdiena")  
elif nedelasDiena==6:  
    print("Sestdiena")       
elif nedelasDiena==7:  
    print("Svētdiena") 
