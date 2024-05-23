#2 Uzd

#Nākamais pāra skaitlis

#Uzdevuma nosacījumi:
#Tiek dots vesels skaitlis n. Uzrakstiet funkciju, kas atgriež nākamo pāra skaitli pēc dotā skaitļa.
 
#Kods:
def next_even_number(n):
      if n % 2 == 0:
              return 
      else:
              return n + 1

      
def next_even_number(n):
      if n % 2 == 0:
              return n + 2
      else:
              return n + 1
print(next_even_number)

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


def average(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst) if len(lst) > 0 else 0

#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - Kods nedarbojās pareizi, jo saraksts bija tukšs, jo tika mēģināts dalīt ar saraksta garumu, kas izraisīja kļūdu. Labotajā kodā pievienoju pārbaudi, vai saraksts ir tukšs, un, ja tā ir, tad tiek atgriezts 0.

#3.uzd

#Vārdu skaits teikumā

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas atgriež vārdu skaitu dotajā teikumā.
 
#Kods ar kļūdām:
def count_words(sentence):
    words = sentence.split(" ")
    return len(words)


def count_words(sentence):
    words = sentence.split()
    return len(words)

#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
# Atbilde - sentence.split(" ") aizstāts ar sentence.split(), kas efektīvāk sadala vārdus neatkarīgi no atstarptu skaita vai pozīcijas.

#4.uzd
#Atrast lielāko skaitli sarakstā

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas atgriež lielāko skaitli dotajā sarakstā lst.
 
#Kods ar kļūdām:
def find_max(lst):
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num



def find_max(lst):
    max_num = lst[0] 
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - kods nedarbojās pareizi, jo sākotnējais maksimālais skaitlis tika iestatīts uz 0, kas varēja izraisīt nepareizu rezultātu. Kodā ieliku sākotnējo maksimālo skaitli uz pirmo saraksta elementu.

#5.uzd

#Atrast unikālos elementus sarakstā

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas atgriež sarakstu ar unikālajiem elementiem no dotā saraksta lst.
 
#Kods ar kļūdām:
def find_unique(lst):
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements


def find_unique(lst):
    unique_elements = []
    for num in lst:
        if lst.count(num) == 1:
            unique_elements.append(num)
    return unique_elements

 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#atbilde - kods nedarbojās pareizi, jo tas atgrieza visus elementus, kas nav unikāli sarakstā nevis tikai unikālos elementus. Izmainīju nosacījumu, lai pārbaudītu, vai elements sarakstā parādās tikai vienu reizi, pirms to pievieno unikālo elementu sarakstam.


#6.uzd

#E-pasta adrešu validācija

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas pārbauda, vai dotā e-pasta adrese ir derīga. E-pasta adrese tiek uzskatīta par derīgu, ja tā satur simbolu '@' un pēc tā ir punkts ('.').
 
#Kods ar kļūdām:
def validate_email(email):
    if "@" and "." in email:
        return True
    else:
        return False
    

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - kods nedarbojās, jo pārbaudē tiek izmantots `and`, kas nav pareizi, lai pārbaudītu, vai e-pasta adrese satur gan simbolu '@', gan punktu '.'. Kodā izmainīju nosacījumu, lai pārbaudītu, vai e-pasta adrese satur gan '@', gan '.' simbolus.



#7.uzd

#Vecuma validācija

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas pārbauda, vai dotais vecums ir derīgs. Vecums ir derīgs, ja tas ir vesels skaitlis starp 0 un 120 (ieskaitot).
 
#Kods ar kļūdām:
def validate_age(age):
    if age >= 0 and age <= 120:
        return True
    else:
        return False
    

def validate_age(age):
    if isinstance(age, int) and age >= 0 and age <= 120:
        return True
    else:
        return False        
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Arbilde - isinstance(age, int) pārbauda vai ageir vesals skitlis



#8.uzd

#Lietotājvārda validācija

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas pārbauda, vai dotais lietotājvārds ir derīgs. Lietotājvārds ir derīgs, ja tas ir vismaz 3 simbolu garš un sastāv tikai no burtiem un cipariem.
 
#Kods ar kļūdām:
def validate_username(username):
    if len(username) >= 3 and username.isalnum:
        return True
    else:
        return False

def validate_username(username):
    if len(username) >= 3 and username.isalnum():
        return True
    else:
        return False    
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - izmainīju nosacījumu, lai pārbauda, vai lietotājvārds ir vismaz 3 simbolu garš un sastāv tikai no burtiem un cipariem, izmantojot metodi `isalnum()


#9.uzd


#Paroles stipruma validācija

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas pārbauda, vai dotā parole ir stipra. Parole ir stipra, ja tā ir vismaz 8 simbolu gara un satur gan burtus, gan ciparus.
 
#Kods ar kļūdām:
def validate_password(password):
    if len(password) >= 8 and any(char.isdigit for char in password) and any(char.isalpha for char in password):
        return True
    else:
        return False
    
def validate_password(password):
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return True
    else:
        return False

 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Atbilde - len (password) >= 8: Parbauda, vai parole ir vismaz 8 simbolu gara. any (char.isdigit() for char in password): Parbauda, vai parole satur vismaz vienu ciparu, izmantojot metodes isdigit izsaukumu ar iekavam. any (char.isalpha() for char in password): Parbauda, vai parole satur vismaz vienu burtu,


#10.uzd


#Telefona numura validācija

#Uzdevuma nosacījumi:
#Uzrakstiet funkciju, kas pārbauda, vai dotais telefona numurs ir derīgs. Telefona numurs ir derīgs, ja tas sastāv no 10 cipariem.
 
#Kods ar kļūdām:
def validate_phone_number(phone_number):
    if len(phone_number) == 10 and phone_number.isdigit:
        return True
    else:
        return False
    

def validate_phone_number(phone_number):
    if len(phone_number) == 10 and phone_number.isdigit():
        return True
    else:
        return Faprint(validate_phone_number)    
 
#Atrodi kļūdas, izlabo. Pievieno labotu kodu un aprakstu, kas bija jāmaina
#Arbilde - len (phone_number) == 10: Parbauda, vai telefona numura garums ir precizi 10 cipari. phone_number.isdigit(): Parbauda, vai telefona numurs sastāv tikai no cipariem, izmantojot metodes isdigit izsaukumu ar iekavăm.