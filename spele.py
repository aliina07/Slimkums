
import random

min_number = 1
max_number = 10
random_number = random.randint(min_number, max_number)
guess = None

while guess != random_number:
    guess = int(input(f"Ievadiet skaitli no {min_number} līdz {max_number}: "))
    
    if guess < random_number:
        print("Skaitlis ir lielāks!")
    elif guess > random_number:
        print("Skaitlis ir mazāks!")
    else:
        print("Apsveicu! Jūs uzminējāt pareizo skaitli!")

