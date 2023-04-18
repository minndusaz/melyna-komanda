import os

saldytuvas = {"mesa": 1, "vistiena": 2}
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
    print("labas pasirinkite ka norite padaryti?")
    print("1 - perziureti saldytuva","\n2 - prideti produka","\n3 - issimti produkta", "\n4 - suskaiciuoti turinio svori","\n9 - iseiti" )
    user_input = int(input("Irasykite savo pasirinkima: "))
    if user_input == 1:
        print(saldytuvas)
    if user_input == 2:
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
    if user_input == 3:
        clear()
    if user_input == 4:
        turis = sum(saldytuvas.values())
        print(f"Viso šaldytuve esančių produktų svoris: ",turis)
    if user_input == 9:
        clear()
        break