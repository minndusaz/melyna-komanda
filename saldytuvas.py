import os

saldytuvas = {"mesa":1}
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def prideti_produkta(pavadinimas, kiekis):
    global saldytuvas
    if pavadinimas in saldytuvas:
        saldytuvas[pavadinimas] += kiekis
    else:
        saldytuvas[pavadinimas] = kiekis

def ivesti_produkta():

    pavadinimas = input("Įveskite produktą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))
clear()
while True:
    print("Sveiki, pasirinkite ką norite padaryti?")
    print("1 - peržiūrėti šaldytuvą", "2 - pridėti produktą", "3 - išimti produktą", "4 - suskaičiuoti turinio svorį", "9 - išeiti" )
    user_input = int(input("Irasykite savo pasirinkima: "))
    if user_input == 1:
        # clear()
        print(saldytuvas)
    if user_input == 2:
        print(prideti_produkta(pavadinimas="", kiekis=""))
    if user_input == 3:
        # os.system('cls')
        print(user_input)
    if user_input == 4:
        clear()
        print(user_input)
    if user_input == 9:
        clear()
        break
