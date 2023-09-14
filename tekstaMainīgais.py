'''
Datu tips - String ( teksts, virkne)
str- saīsinājums
14.09.23
'''

x = 5  #bez pēdiņām - vesalsn skaitlis
y = '5'  # ar pēdiņām - teksts

print(type(y))  # type() funkcija datu tipa noteikšanai

vards = "Anna"
uzvards = "Bērziņa"  # Starp pēdiņām var liktb dažādus simbolus tajā skaitā ar mīkstinājumu un garumzīmēm

print(vards)
print(uzvards)

# Izvadīt tekstu vienā vietā/rindā
#1.veids (vards+uzvards)
print(vards+uzvards)
#2.veids
print(vards+ ' ' +uzvards)
#3.veids
print(vards,uzvards)

#teksta garums
#len() - funkciaja simbolu skaita noteikšanai
print(len(vards))
print(len(uzvards))

#indeksēšana 

#pieķļuve atsevišķiem teksta elementiem
print(vards[3]) #izvadīsim vāarda, Anna pēdējo burt
#print(vards[4]) #error: string index outv of range
#vairāku elementu izvade
print(uzvards[:2]) # no pirmā elementam līdz trešajam(trešo neieskaitot)

print(uzvards[1:5])

#izvadītb pedējo elementu nezinot viņa indeksu
print(uzvards[-1])

#izvadīt elementus ar soli
print(uzvards[::1])
print(uzvards[::2])

#apgriezt vārdu otrādi
print(uzvards[::-1])

#mainīt mainīgā vērtību
vards = "Alise"
uzvards = uzvards + " -Liepa"
print(vards,uzvards)

#datu tipa String metode

#.upper( ) - pārveido par lieliem burtiem
print(vards.upper())
#.lower() - pārveido par maziem burtiem
print(vards.lower())

#.split()n - sadala tekstu, pēc noklusējuma dala tur, kur ir atstarpe
print(uzvards.split())
print(uzvards.split("-"))