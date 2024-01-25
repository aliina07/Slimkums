
#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def summa(skaitlis1,skaitlis2):
    
    
    if skaitlis1 + 20 == 0 and skaitlis2 + 20 == 0:
        
        if skaitlis1<skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
    
    else:
        
        if skaitlis1>skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
        
print(summa(10,10))
print(summa(10,20))
print(summa(5,15))

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