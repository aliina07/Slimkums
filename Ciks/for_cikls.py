""""
for cikla treniņa uzdevums - taisnleņķa trīstūra izvade
"""

#uzdevums 
#Izveido programmu kas izvada apgrieztu taisnleņķa trījstūri
#*****
#****
#***
#**
#*

rindas = 5

#nested loops jeb cikli kuri atrodas viens otrā
#ārējais ciks
for rinda in range(0,rindas):  #range nosaka no kura līdz kuram skaitlim atkārtosies cikls
    print("Šī ir rinda: ", rinda)

    # iekšējais cikls
    for simboluSkaits in range(rindas-rinda):
         print("*") # print funkcija pēc nolkusējuma beigas ir vērtīab kas paceļ jauna rindā
         print("*", end=" ")
