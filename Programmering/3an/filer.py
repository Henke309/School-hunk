inbjudna = []

try:
    f = open("inbjudna.txt", "r")
except FileNotFoundError:
    print("Läste inte in några namn! \n")
else:
    for namn in f.readlines():
        if namn.strip() != "":
            inbjudna.append(namn.strip())

while True:
    print("1. Bjud in alla till födelsedagsfest")
    print("2. Visa alla inbjudna")
    print("3. Spara till fil")
    print("0. Avsluta")
    val = input(": ")

    if val == "1":
        namn = input("Bjud in: ")

        inbjudna.append(namn)
    elif val == "2":
        print("Alla inbjudna")
        print("."*25)
    elif val == "3":
        pass
    elif val == "0":
        pass