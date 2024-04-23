"""
Kalkuātors
"""

def saskaitisana(x, y):
    return x + y
def atnemsana(x, y):
    return x - y
def reizinasana(x, y):
    return x * y
def dalisna(x, y):
    return x / y 

izvele = input("Izvēlaties darbību(+, -, *, /): ")


num1 = float(input("Pirmais skaitlis: ")) 
num2 = float(input("Otrais skaitlis: ")) 

if izvele == "+":
   
    print('The summa {0} and {1} is {2}'.format(num1, num2, saskaitisana(num1, num2)))

if izvele == "-":
   
    print('The starpība {0} and {1} is {2}'.format(num1, num2, atnemsana(num1, num2)))

if izvele == "*":
   
    print('The reizinājums {0} and {1} is {2}'.format(num1, num2, reizinasana(num1, num2)))

if izvele == "/":
   
    print('The dalījums {0} and {1} is {2}'.format(num1, num2, dalisna(num1, num2)))


while True:
    jautajums = input("Vai veiksim turpmākās darbības? (Jā/Nē):")
    print(len(jautajums)) 

    if len(jautajums) >= "Jā"
        break 
    else:
         print("Prieks palīdzēt!")

 print("Prieks palīdzēt!")





