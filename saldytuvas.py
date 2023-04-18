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

def ivesti_produkta():
    pavadinimas = input("Įveskite produktą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))
    return pavadinimas, kiekis

def prideti(saldytuvas, pavadinimas, kiekis):
    saldytuvas[pavadinimas] = kiekis
    return saldytuvas

clear()
while True:
    print("labas pasirinkite ka norite padaryti?")
    print("1 - perziureti saldytuva", "2 - prideti produka", "3 - issimti produkta", "4 - suskaiciuoti turinio svori", "9 - iseiti" )
    user_input = int(input("Irasykite savo pasirinkima: "))
    if user_input == 1:
        print(saldytuvas)
    if user_input == 2:
        pavadinimas, kiekis = ivesti_produkta()
        saldytuvas = prideti_produkta(saldytuvas, pavadinimas, kiekis)
    if user_input == 3:
        clear()
    if user_input == 9:
        clear()
        break