import os

saldytuvas = {"mesa": 1.0, "zuvis": 0.0, "sviestas": 0.0, "kebabai": 2.0}
receptas = {}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def prideti_produkta(saldytuvas, pavadinimas, kiekis):
    if pavadinimas in saldytuvas:
        saldytuvas[pavadinimas] += kiekis
    else:
        saldytuvas[pavadinimas] = kiekis
    return saldytuvas

def pasalinti_produkta(saldytuvas, pavadinimas, kiekis):
    if pavadinimas in saldytuvas:
        saldytuvas[pavadinimas] -= kiekis
    else:
        saldytuvas[pavadinimas] = kiekis
    return saldytuvas

def ivesti_produkta():
    pavadinimas = input("Įveskite produktą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))
    return pavadinimas, kiekis

def tuscias(pavadinimas, kiekis):
    poros = list(pavadinimas.items())
    for raktas, reiksme_zodyje in poros:
        if reiksme_zodyje <= kiekis:
            del pavadinimas[raktas]
    return pavadinimas
saldytuvas = tuscias(saldytuvas, 0)

def gauti_produktus(saldytuvas):
    produktu_eilute = ""
    for produktas, kiekis in saldytuvas.items():
        produktu_eilute += produktas + ":" + str(kiekis) + " "
    return produktu_eilute

def ar_uztenka(saldytuvas, pavadinimas, kiekis):
    ivesti_produkta()

def iveskite_recepta():
    kokio_reikia_produktas = input("Įveskite maisto produktus: ")
    kiek_reikia_kiekis = input("Įveskite kiekius: ")

    prod = []
    prod.append(kokio_reikia_produktas)

    kiek = []
    kiek.append(kiek_reikia_kiekis)

    receptas = dict(zip(prod, kiek))

    return receptas

def patikrinti_saldytuva(receptas):
    for ingredientas, kiekis in receptas.items():
        if ingredientas not in saldytuvas or saldytuvas[ingredientas] < kiekis:
            return print(f'Jums Trūksta, {ingredientas}')
    return print("Jums užtenkta visko pagaminti produktą")

def ar_uzteks_receptui (saldytuvas):
    for kokio_reikia_produktas, kiek_reikes_kiekis in saldytuvas:
        if kokio_reikia_produktas in saldytuvas.key() and "/n":
            if kiek_reikes_kiekis in saldytuvas.value():
                saldytuvas.key() - kokio_reikia_produktas #del
                saldytuvas.value() - kiek_reikes_kiekis #del
        else: print("Neturite produktų arba neužtenka jų kiekio ")
    return saldytuvas

clear()
while True:
    print("\nPasirinkite veiksmą: \n")
    print("1 - peržiūrėti šaldytuvą", 
        "\n2 - pridėti produktą", 
        "\n3 - išimti produktą", 
        "\n4 - suskaičiuoti turinio svorį", 
        "\n5 - Patikrinti ar užtenka ingredientų receptui"
        "\n9 - išeiti" )
    user_input = int(input("Įrašykite savo pasirinkimą: "))
    if user_input == 1:
        clear()
        print(saldytuvas)
    if user_input == 2:
        clear()
        print(saldytuvas)
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
        clear()
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
    if user_input == 3:
        clear()
        print(saldytuvas)
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = pasalinti_produkta(saldytuvas, pavadinimas, kiekis)
        tuscias(saldytuvas, 0)
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
    if user_input == 4:
        clear()
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
        turis = sum(saldytuvas.values())
        print(f"Viso šaldytuve esančių produktų svoris: ",turis, "\n")
    if user_input == 5:
        iveskite_recepta()
        print(patikrinti_saldytuva(receptas))
    if user_input == 6:
        print(ar_uzteks_receptui(saldytuvas))
    if user_input == 9:
        clear()
        break