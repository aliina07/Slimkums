#2 Uzd

#Nākamais pāra skaitlis

#Uzdevuma nosacījumi:
#Tiek dots vesels skaitlis n. Uzrakstiet funkciju, kas atgriež nākamo pāra skaitli pēc dotā skaitļa.
 
#Kods:
def next_even_number(n):
      if n % 2 == 0:
              return n + 2
      else:
              return n + 1
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - Iepriekšējais kods nedarbojās pareizi, jo, ievadītais skaitlis bija pāra skaitlis, tad tika atgriezts tas pats skaitlis, nevis nākamais pāra skaitlis. Labotajā kodā izmainīju atgriezamo vērtību, lai ievadītais skaitlis ir pāra skaitlis, tad tiek atgriezts nākamais pāra skaitlis pēc dotā skaitļa.


#2.uzd

#Saraksta vidējais lielums

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas aprēķina un atgriež saraksta lst vidējo lielumu.
 
#Kods ar kļūdām:
def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)
print(average)

def average(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst) if len(lst) > 0 else 0
print(average)
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - 
