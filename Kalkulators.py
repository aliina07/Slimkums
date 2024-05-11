"""
Kalkulators
"""
import csv #Ievietota bibliotēka

#Funkcijas def veic matemātiskas darbības
def saskaitisana(x, y):
    return x + y
def atnemsana(x, y):
    return x - y
def reizinasana(x, y):
    return x * y
def dalisna(x, y):
    return x / y 

#funkcija datu saglabāšanai
def datu_saglabasana(vards,rezultats):
    saturs = [vards,rezultats]
    with open("kalkulatora_dati.csv","a", encoding="UTF-8") as fails: #Notiek datu pievienošana
        csvwrite = csv.writer(fails) #Objekta izveide
        csvwrite.writerow(saturs)


vards = input("Lūdzu ievadi savu vārdu: ")

#Cikls nodrošina programas darbību
while True:

    izvele = input("Izvēlaties darbību(+, -, *, /): ") #Lietotāja darbības izvēle

    #Skaitļu ievade
    num1 = float(input("Pirmais skaitlis: ")) 
    num2 = float(input("Otrais skaitlis: ")) 
    #Lietotāja izvēlētās darbības pārbaude, darbības izpilde un datu saglabāšana
    if izvele == "+":
        rezultats = saskaitisana(num1, num2)
        print('The summa {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)

    if izvele == "-":
        rezultats = atnemsana(num1, num2)
        print('The starpība {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)

    if izvele == "*":
        rezultats = reizinasana(num1, num2)
        print('The reizinājums {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)
    if izvele == "/":

        rezultats = dalisna(num1, num2)
        print('The dalījums {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)

    #Lietotājs izvēlās vai vēlās turpināt turpmākās darbības      
    jautajums = input("Vai veiksim turpmākās darbības? (Jā/Nē): ")
    print(len(jautajums))

    if jautajums == "Nē": 
        break
    else:
        print("Sākam no jauna!")


         





