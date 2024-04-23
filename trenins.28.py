import json

def nolasi_dzivniekus(fails):
    with open(fails, 'r',  encoding="UTF-8") as f:
        dzivnieki = json.load(f)
    return dzivnieki

def analize_dzivnieku_sugu(dzivnieki):
    sugas = {}
    for dzivnieks in dzivnieki:
        suga = dzivnieks['suga']
        if suga in sugas:
            sugas[suga] += 1
        else:
            sugas[suga] = 1
    return sugas

def analize_dzivnieku_krasu(dzivnieki):
    krasas = {}
    for dzivnieks in dzivnieki:
        kraasa = dzivnieks['kraasa']
        if kraasa in krasas:
            krasas[kraasa] += 1
        else:
            krasas[kraasa] = 1
    return krasas

fails = 'jsonfails.json'
dzivnieki = nolasi_dzivniekus(fails)

sugu_analize = analize_dzivnieku_sugu(dzivnieki)
print("Dzīvnieku sugas un to skaits:")
print(sugu_analize)

krasu_analize = analize_dzivnieku_krasu(dzivnieki)
print("Dzīvnieku krāsas un to biežums:")