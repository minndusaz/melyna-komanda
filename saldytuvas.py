import os

saldytuvas = {"mesa":1}
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

def prideti(saldytuvas, pavadinimas, kiekis):
    saldytuvas[pavadinimas] = kiekis
    return saldytuvas

def gauti_produktus(saldytuvas):
    produktu_eilute = ""
    for produktas, kiekis in saldytuvas.items():
        produktu_eilute += produktas + ":" + str(kiekis) + " "
    return produktu_eilute

clear()
while True:
    print("\nPasirinkite veiksmą: \n")
    print("1 - peržiūrėti šaldytuvą", "\n2 - pridėti produktą", "\n3 - išimti produktą", "\n4 - suskaičiuoti turinio svorį", "\n9 - išeiti" )
    user_input = int(input("Įrašykite savo pasirinkimą: "))
    if user_input == 1:
        clear()
        print("Šaldytuve šiuo metu yra: ", gauti_produktus(saldytuvas))
    if user_input == 2:
        clear()
        print(saldytuvas)
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
        pasalinti_produkta(saldytuvas, 0)
        clear()
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
    if user_input == 3:
        clear()
        print(saldytuvas)
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = pasalinti_produkta(saldytuvas, pavadinimas, kiekis)
        pasalinti_produkta(saldytuvas, 0)
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
    if user_input == 4:
        clear()
        print("Šaldytuve šiuo metu yra: ", saldytuvas)
        turis = sum(saldytuvas.values())
        print(f"Viso šaldytuve esančių produktų svoris: ",turis, "\n")
    if user_input == 5:
        pass
    if user_input == 9:
        clear()
        break