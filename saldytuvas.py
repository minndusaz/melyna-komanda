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
    print("Sveiki, pasirinkite ką norite padaryti?")
    print("1 - peržiūrėti šaldytuvą", "2 - pridėti produktą", "3 - išimti produktą", "4 - suskaičiuoti turinio svorį", "9 - išeiti" )
    user_input = int(input("Įrašykite savo pasirinkimą: "))
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