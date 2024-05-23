#  1.uzd

#Kļūdaina cilpa
#Nosacījumi:Ir funkcija sum_of_squares(n), kas aprēķina pirmo n pozitīvo veselu skaitļu kvadrātu summu. Kods satur kļūdu, un uzdevums ir to atrast un izlabot.
#Kļūdainais kods:

def sum_of_squares(n):
    total = 0
    for i in range(1, n):
        total += i * i
    return total

n = 5
print(sum_of_squares(n))


def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

n = 5
print(sum_of_squares(n))

#Atbilde - Kļūda kodā ir saistīta ar nosacījumu range(1, n). Funkcija range(1, n) ģenerē skaitļus no 1 līdz n-1, izslēdzot pašu n. Lai iekļautu arī n, jāizmanto range(1, n + 1).

# 2.uzd
#Nepareizs vārdnīcas apstrādes kods
#Nosacījumi: Ir funkcija count_occurrences(s), kas aprēķina, cik reizes katrs burts parādās dotajā virknē. Kods satur kļūdu, un uzdevums ir to atrast un izlabot.

#Kļūdainais kods:
def count_occurrences(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] =+ 1
        else:
            counts[char] = 1
    return counts

s = "hello"
print(count_occurrences(s))


def count_occurrences(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

s = "hello"
print(count_occurrences(s))

#Atbilde - Kļūda kodā ir saistīta ar counts[char] =+ 1. Tā vietā, lai pievienotu vienu counts[char], kods veic piešķiršanu ar +=, kas ir nepareiz rezultāts.


# 3.uzd

#Dalījums ar nulli
#Nosacījumi: Ir funkcija divide(a, b), kas dala divus skaitļus. Ja dalītājs ir nulle, programmai ir jāpaziņo par kļūdu, bet tā nedrīkst pārtraukt darbību tāpēc, ka radusies kļūda.
#Izmanto try except.

#Kļūdainais kods:
def divide(a, b):
    return a / b

a1 = 10
b1 = 5
print(divide(a1, b1))  

a2 = 10
b2 = 0
print(divide(a2, b2))



def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


a = 10
b1= 5
print(divide(a, b))  

a = 10
b = 0
print(divide(a, b))


    


#Testa dati1:
#a = 10
#b = 5
#Sagaidāmais rezultāts1:
#2

#Testa dati2:
#a = 10
#b = 0
#Sagaidāmais rezultāts2:
#"Error: Division by zero is not allowed."

#Atbilde - šis kods vienkārši veic dalījumu un neapstrādā kļūdu, ja otrais skaitlis ir nulle.  Tas nozīmē, ka, ja jūs izpildāt šo funkciju ar otro skaitli, kas ir nulle, Python izmetēs ZeroDivisionError kļūdu, un programmas izpilde tiks pārtraukta.


#4.uzd

#Sintakses kļūda
#Nosacījumi: Ir funkcija greet(name), kas izvada sveiciena ziņu. Kods satur sintakses kļūdu, un uzdevums ir to atrast un izlabot.

#Kļūdainais kods:

def greet(name)
    print("Hello, " + name + "!")



def greet(name):
    print("Hello, " + name + "!")

name = "Alice"
greet(name)


#Testa dati:
#name = "Alice"
#Sagaidāmais rezultāts:
#"Hello, Alice!"

# Atbilde - Kļūda dotajā kodā ir sintakses kļūda: funkcijas definīcijā pietrūkst dvīņu punkta : aiz parametra name.


# 5.uzd

#Ir funkcija calculate_triangle_area(base, height), kas aprēķina trijstūra laukumu. Kods satur interpretēšanas kļūdu, un uzdevums ir to atrast un izlabot.

#Kļūdainais kods:
def calculate_triangle_area(base, height):
    return 1 / 2 * base * height

base = 6
height = 8
print(calculate_triangle_area(base, height))



def calculate_triangle_area(base, height):
    return (1 / 2) * base * height

base = 6
height = 8
print(calculate_triangle_area(base, height)) 


#Atbilde = Kļūda dotajā koda ir sintakses kļūda starp 1/2 * ir jāliek iekavas (1 / 2) *

# 6.uzd

#Kods satur interpretēšanas kļūdu, un uzdevums ir to atrast un izlabot.

#Dots kods:

r = float(input("Ieraksti riņķa rādiusu: "))
pi = 3,14
laukums = pi * r**2
print(f"Riņķa laukums ir {laukums}")


r = float(input("Ieraksti riņķa rādiusu: "))
pi = 3.14
laukums = pi * r**2
print(f"Riņķa laukums ir {laukums}")

#Atbilde - Kļūda kodā ir saistīta ar pi skaitļa definīciju. Pareizi ir definēt pi skaitli ar decimāldaļu punktu, nevis komatu. Korektā pi definīcija ir 3.14, nevis 3,14.

#7.uzd

#Izlabo kļūdas, ja tādas ir un pārbaudi, vai programma veic prasīto funkciju. Nepieciešamības gadījumā veic koda labojumus.

#Dota programma, kuras uzdevums ir saskaitīt simbolus, kas atrodas teksta mainīgajā
#Testēšana: string_length('Programmēšana') ------> 13

#Dots kods:
def string_length(str1):
    count = 0
    for char in str1:
        count -= 1
        return count
print(string_length('Programmēšana')) 

    
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('Programmēšana')) 

#Atbilde - Mainīgajam count piešķir vērtību -1 katru reizi, kad tiek apstrādāts simbols teksta virknē. Tas novērsīs pareizo rezultātu. return atrodas cilpa iekšienē, tāpēc tas tiek izpildīts pēc pirmā apstrādātā simbola un pārtrauc funkcijas izpildi.


#8.uzd

#Izlabo kļūdas, ja tādas ir un pārbaudi, vai programma veic prasīto funkciju. Nepieciešamības gadījumā veic koda labojumus.

#Dota programma, kuras uzdevums ir izvadīt dotā teksta pirmos divus un pēdējos divus simbolus, ja teksts sastāv no mazāk kā diviem simboliem, jāatgriež tukšs teksta mainīgais
# Testēšana: string_both_ends('Programmēšana') ------> Prna
#            string_both_ends('Pr') --------> PrPr
#            string_both_ends('P') -------> ''

def string_both_ends(str):
  if len(str) < 2:
    return False

  return str[0:2] + str[2:]

print(string_both_ends('Programmēšana'))
print(string_both_ends('Pr'))
print(string_both_ends('P'))

def string_both_ends(text):
    if len(text) < 2:
        return ''
    return text[:2] + text[-2:]

print(string_both_ends('Programmēšana')) 
print(string_both_ends('Pr'))             
print(string_both_ends('P'))   

#Atbilde - Nosaukumam "str" jābūt atšķirīgam no iebūvētās funkcijas nosaukuma "str", lai novērstu konfliktu.

#9.uzd

#Izlabo kļūdas, ja tādas ir un pārbaudi, vai programma veic prasīto funkciju. Nepieciešamības gadījumā veic koda labojumus.

# Dota programma, kuras uzdevums ir izveidot vienu simbolu virkni (string) no dotajām (a,b), samainot to pirmos simbolus vietām
# Testēšana: chars_mix_up('abc', 'xyz') ------> xyc abz
def chars_mix_up(a, b):
  new_a = b[:1] + a[1:]
  new_b = a[:2] + b[2:]

  return new_a + new_b

print(chars_mix_up('abc', 'xyz'))


def chars_mix_up(a, b):
    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]
    return new_a + ' ' + new_b

print(chars_mix_up('abc', 'xyz'))

#Atbilde - Virkņu indeksēšana Pythonā sākas ar nulli, tāpēc, lai iegūtu pirmo simbolu, jums jāizmanto indekss 0, nevis 1. Tāpēc, lai izvairītos no šīs kļūdas, mēs izmantojam b[0] un a[0], lai iegūtu pirmos simbolus katrā virknē.

#10.uzd

#Izlabo kļūdas, ja tādas ir un pārbaudi, vai programma veic prasīto funkciju. Nepieciešamības gadījumā veic koda labojumus.

# Dota programma, kuras uzdevums ir atgriezt garāko vārdu un tā garumu no dotā saraksta
# Testēšana: 
#find_longest_word(["Python", "Ieskaite", "Programmēšana"]) -------->  ('Programmēšana', 13)


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(word_len), n))
    word_len.sort()
    length = word_len[-1][0]
    long_word = word_len[-1][1]
        return long_word, length

#print(find_longest_word(["Python", "Ieskaite", "Programmēšana"]))


def find_longest_word(words_list):
    word_len = []
    for word in words_list:
        word_len.append((len(word), word))
    word_len.sort()
    long_word = word_len[-1][1]
    length = word_len[-1][0]
    return long_word, length

print(find_longest_word(["Python", "Ieskaite", "Programmēšana"]))



#Atbilde - Šobrīd tiek pievienoti pāris, kas sastāv no vārda garuma un tā indeksa sarakstam word_len. Tas nav vajadzīgs, jo mums nepieciešams tikai vārdu garums, nevis tā indekss. return atrodas nepareizā vietā. Tas ir jānovieto ārpus cikla, lai atgrieztu garāko vārdu un tā garumu, pēc tam, kad cikls ir pabeigts.



#11.uzd

#Izmanto try,except,else apgalvojumus, lai novērstu ValueError kļūdu, kas rodas tad, ja lietotājs neievada skaitli.

# Dota programma, kuras uzdevums ir noteikt, vai ievadītais skaitlis ir pāra vai nepāra
# Testēšana: 5 -----> Nepāra skaitlis.
#            6 -----> Pāra skaitlis.

num = int((input("Ievadi veselu skaitli: ")))
mod = num % 2
if mod > 0:
    print("Nepāra skaitlis.")
else:
    print("Pāra skaitlis.")


try:
    num = int(input("Ievadi veselu skaitli: "))
except ValueError:
    print("Nepareiza ievade. Lūdzu, ievadiet veselu skaitli.")
else:
    mod = num % 2
    if mod > 0:
        print("Nepāra skaitlis.")
    else:
        print("Pāra skaitlis.")



#Atbilde -  Ja rodas šāda kļūda, programma informēs lietotāju par nepareizu ievadi un aicinās to ievadīt skaitli. Ja lietotājs ievada skaitli, programma turpinās izpildi, lai noteiktu, vai tas ir pāra vai nepāra.


