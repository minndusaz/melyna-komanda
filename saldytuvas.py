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
    pavadinimas1 = input("Įveskite produktą: ")
    kiekis = float(input("Įveskite produkto kiekį: "))

while True:
    clear()
    print("labas pasirinkite ka norite padaryti?")
    print("1 - perziureti saldytuva", "2 - prideti produka", "3 - issimti produkta", "4 - suskaiciuoti turinio svori", "9 - iseiti" )
    user_input = int(input("Irasykite savo pasirinkima: "))
    if user_input == 1:
        clear()
        print(saldytuvas)
    if user_input == 2:
        print(prideti_produkta(pavadinimas="", kiekis=""))
    if user_input == 3:
        os.system('cls')
        print(user_input)
    if user_input == 4:
        os.system('cls')
        print(user_input)
    # if user_input != 1 or 2 or 3 or 4:
    #     break