import os

saldytuvas = {"mesa": 1, "zuvis": 0.0, "sviestas": 0.0, "kebabai": 2}
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

def issimti_produkta(saldytuvas, pavadinimas, kiekis):
    if pavadinimas in saldytuvas:
        saldytuvas[pavadinimas] -= kiekis
    else:
        saldytuvas[pavadinimas] = kiekis
    return saldytuvas

def ivesti_produkta():
    pavadinimas = input("Įveskite produktą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))
    return pavadinimas, kiekis

def prideti(saldytuvas, pavadinimas, kiekis):
    saldytuvas[pavadinimas] = kiekis
    return saldytuvas

def tuscias(pavadinimas, kiekis):
    poros = list(pavadinimas.items())
    for raktas, reiksme_zodyje in poros:
        if reiksme_zodyje <= kiekis:
            del pavadinimas[raktas]
    return pavadinimas
saldytuvas = tuscias(saldytuvas, 0)

clear()
while True:
    print("Sveiki, pasirinkite ką norite padaryti?")
    print("1 - peržiūrėti šaldytuvą", "2 - pridėti produktą", "3 - išimti produktą", "4 - suskaičiuoti turinio svorį", "9 - išeiti" )
    user_input = int(input("Įrašykite savo pasirinkimą: "))
    if user_input == 1:
        clear()
        print(saldytuvas)
    if user_input == 2:
        clear()
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
        print(saldytuvas)
    if user_input == 3:
        clear()
        print(saldytuvas)
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = issimti_produkta(saldytuvas, pavadinimas, kiekis)
    if user_input == 4:
        turis = sum(saldytuvas.values())
        print(f"Viso šaldytuve esančių produktų svoris: ",turis)
    if user_input == 5:
        clear()
        tuscias(saldytuvas, 0)
        print(saldytuvas)
    if user_input == 9:
        clear()
        break