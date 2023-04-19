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
    receptas = iveskite_recepta()
    for pavadinimas, kiekis in receptas.items():
        if kiekis not in saldytuvas or saldytuvas(kiekis) < kiekis:
            print(f'Jums Trūksta, {pavadinimas}')
        else:
            print("Jums užtenkta visko pagaminti produktą")

clear()
while True:
    print('Jūsų šaldytuvas')
    print("---------------------\nPasirinkite veiksmą: \n---------------------")
    print("1 - Peržiūrėti šaldytuvą", 
        "\n2 - Pridėti produktą", 
        "\n3 - Išimti produktą", 
        "\n4 - Suskaičiuoti turinio svorį", 
        "\n5 - Patikrinti ar užtenka ingredientų receptui"
        "\n9 - Išeiti")
    
    user_input = int(input("Įrašykite savo pasirinkimą: "))
    
    if user_input == 1:
        clear()
        print('Produktai esantys šaldytuve', saldytuvas)
        print('---------------------')
    
    if user_input == 2:
        clear()
        print('Produktai esantys šaldytuve', saldytuvas)
        print('---------------------')
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
        tuscias(saldytuvas, 0)
        clear()
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
        print('---------------------')
    
    if user_input == 3:
        clear()
        print('Produktai esantys šaldytuve', saldytuvas)
        print('---------------------')
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = pasalinti_produkta(saldytuvas, pavadinimas, kiekis)
        tuscias(saldytuvas, 0)
        print('Produktai esantys šaldytuve', saldytuvas)
    
    if user_input == 4:
        clear()
        print('Produktai esantys šaldytuve', saldytuvas)
        print('---------------------')
        turis = sum(saldytuvas.values())
        print(f"Viso šaldytuve esančių produktų svoris: ",turis, "\n")
    
    if user_input == 5:
        clear()
        print('Produktai esantys šaldytuve', saldytuvas)
        patikrinti_saldytuva(receptas)
    
    if user_input == 9:
        clear()
        break