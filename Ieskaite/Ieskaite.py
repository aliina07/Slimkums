"""
Gatavošanās ieskaitei
"""

#1 uzd
#Izveido sarakstu ar trīs elementiem kuriem ir atšķirīgi
# 
saraksts =  [3,2.3, "Sveiki"]

#2.
#izveido funkciju Sveika Pasaule kas izvada tekstu "Sveika, Pasaule!"

def SveikaPasaule():
    print("SveikaPasaule!")


SveikaPasaule()    

#3

#Uzraksti funkciju kura atgriež mazāko skaitlī ja abi skaitli ir para skaitli 
#atgriež lilāko skaitli ja abi skaitli ir nepara vai viens no skaitļiem ir nepara skaitlis

"""
print(funkcijas nosaukums(2,4))  ------> 2
print(funckcijas nosukums(2,5)) ------->5
"""
#funkcija atgriezSkaitli()




"""Treniņš programmas veidošanais pēc specifikācijas"""

#1 specifikācija

"""
Uzraksti funkciju 
Linoleja cenu
Telpa izmēru
izvadīt cenu
"""

def telpasIzmers(cena,izmers):
    kopeja_cena = cena*izmers

    print("Grīdas seguma kopējā cena ",kopeja_cena)
    
telpasIzmers(5,20)   
         

        

#3.uzdevums

# Uzraksti funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi
# Atgriež lielāko skaitli, ja abi skaitļi ir nepāra vai viens no skaitļiem ir nepāra skaitlis

"""
print(funkcijasNosaukums(2,4)) -----> 2
print(funkcijasNosaukums(2,5)) -----> 5
"""
#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def atgriezSkaitli(skaitlis1,skaitlis2):
    
    #Pārbaude - vai pirmais skaitlis ir pāra skaitlis
    if skaitlis1 % 2 == 0:
        #Pārbaude - vai otrais skaitlis ir pāra skaitlis
        if skaitlis2 % 2 == 0:
            #Pārbaude - kurš no skaitļiem ir mazāks
            if skaitlis1<skaitlis2:
                return skaitlis1
            else:
                return skaitlis2
        #Ja skaitlis2 nav pāra skaitlis
        else:
            #Pārbaude - kurš no skaitļiem ir lielāks
            if skaitlis1>skaitlis2:
                return skaitlis1
            else:
                return skaitlis2
    #Ja skaitlis1 nav pāra skaitlis
    else:
        #Pārbaude - kurš no skaitļiem ir lielāks
        if skaitlis1>skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
        
# print(atgriezSkaitli(2,4))
# print(atgriezSkaitli(2,5))
print(atgriezSkaitli(1,5))


#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def atgriezSkaitli(skaitlis1,skaitlis2):
    
    #Pārbaude - vai pirmais un otrais skaitlis ir pāra skaitļi
    if skaitlis1 % 2 == 0 and skaitlis2 % 2 == 0:
        #Pārbaude - kurš no skaitļiem ir mazāks
        if skaitlis1<skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
    #Ja skaitlis1 un skaitlis2 nav pāra skaitļi
    else:
        #Pārbaude - kurš no skaitļiem ir lielāks
        if skaitlis1>skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
        
print(atgriezSkaitli(2,4))
print(atgriezSkaitli(2,5))
print(atgriezSkaitli(1,5))


#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def atgriezSkaitli(skaitlis1,skaitlis2):
    
    #Pārbaude - vai pirmais un otrais skaitlis ir pāra skaitļi
    if skaitlis1 % 2 == 0 and skaitlis2 % 2 == 0:
        #Pārbaude - kurš no skaitļiem ir mazāks, izmantojot iebūvētās funkcijas
        return min(skaitlis1,skaitlis2)
    #Ja skaitlis1 un skaitlis2 nav pāra skaitļi
    else:
        #Pārbaude - kurš no skaitļiem ir lielāks
        return max(skaitlis1,skaitlis2)
        
print(atgriezSkaitli(2,4))
print(atgriezSkaitli(2,5))
print(atgriezSkaitli(1,5))


              
          
    















