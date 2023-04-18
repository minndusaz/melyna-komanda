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

clear()
while True:
    print("\nPasirinkite veiksmą: \n")
    print("1 - peržiūrėti šaldytuvą", "\n2 - pridėti produktą", "\n3 - išimti produktą", "\n4 - suskaičiuoti turinio svorį", "\n9 - išeiti" )
    user_input = int(input("Įrašykite savo pasirinkimą: "))
    if user_input == 1:
        clear()
        tuscias(saldytuvas, 0)
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
    if user_input == 2:
        clear()
        print(saldytuvas)
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
        tuscias(saldytuvas, 0)
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
    if user_input == 9:
        clear()
        break