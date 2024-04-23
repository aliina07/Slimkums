# Izveidojam sarakstus vīriešu un sieviešu vārdiem
viriesuvardi = []
sieviesuvardi = []


def csv_lasisana(sieviesuvardi,viriesuvardi):

 with open(sieviesuvardi,viriesuvardi, 'r',encoding="UTF-8") as fails:
       for rinda in fails:
        vārds = rinda.strip()
        dzimums = input("Lūdzu, ievadiet dzimumu (v vai s) vārdam '{}': ".format(vārds))
        if dzimums == 'v':
            viriesuvardi.append(vārds)
        elif dzimums == 's':
            sieviesuvardi.append(vārds)

# Nosakam visbiežāk sastopamo vārdu katrā sarakstā
visbiežākaisvīriešuvārds = max(set(viriesuvardi), key = viriesuvardi.count)
visbiežākaissieviešuvārds = max(set(sieviesuvardi), key = sieviesuvardi.count)

# Izdrukājam rezultātus
print("Visbiežāk sastopamais vīriešu vārds ir: {}".format(visbiežākaisvīriešuvārds))
print("Visbiežāk sastopamais sieviešu vārds ir: {}".format(visbiežākaissieviešuvārds))