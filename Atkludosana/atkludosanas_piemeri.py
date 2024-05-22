#Nokopē kodu, atrodi risinājumu, pieraksti kļūdas veidu un apraksti risinājumu

# Lietotājs ievada veselu pozitīvu skaitli. Izdrukā visus skaitļus sākot no ievadītā līdz 0 (neieskaitot)!

#sk = int(input("Ievadi skaitli:"))
#while sk > 0:
#  print(sk)
#  sk -= 1


#Kļūdas veids - IndentationError
# Risinājus - 8 rindā vajag "sk" ar pogu"backspace" pārvietot zem print



# Lietotājs ievada vairākus skaitļus vienā rindā, atdalot tos ar atstarpi. Izvadi tos skaitļus, kuri ir vienādi un atrodas blakus!

#araksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

#for i in range(len(saraksts)-1):
 # if saraksts[i] == saraksts[i + 1]:
 #   print(saraksts[i], saraksts[i + 1])


#Kļūdas veids - IndexError
#Risinājums - 20 rindā pēc saraksta iekavām jāliek -1, lai programma neizietu cauri rāmjiem, lai būtu ar ko salīdzināt




# Lietotājs ievada vairākus skaitļus, atdalot tos ar atstarpi. Izvadi lielākā ievadītā skaitļa vērtību un indeksu sarakstā!

skaitli = [int(skaitli) for skaitli in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

lielIndex = 0

for i in range(1, len(skaitli)):
  if skaitli[i] > skaitli[lielIndex]:
    lielIndex = i

#mainīgās vērtības ievietošana teksta
#f
print(f"Lielakais skaitlis: {skaitli[lielIndex]} ar indeksu {lielIndex}')