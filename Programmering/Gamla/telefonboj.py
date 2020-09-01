"""
Name: Henrik Nguyen
Date: --
Info:
genomgång
"""

telefonbok = []
telefonbok.append({"namn":boimannen, "telenr":112})
telefonbok.append({"namn":girlkvinnan, "telenr":221})
telefonbok.append({"namn":manmannen, "telenr":911})

while True:
    print(telefonbok)
    print("===TELEFONBOK===")
    print("1. Spara en person")
    print("2. Ta bort en person")
    print("3. Sök efter en person")
    print("4. Visa alla personer i bokstavsordning")
    print("0. avsluta")

    menu = input(":")

    if menu == "1":
        namn = input("Skriv in namnet: ")
        telenr = input("Skriv in telefonumret: ")

        telefonbok.append({"namn":namn, "telenr":telenr})

        print("inmatningen registrerad!\n")
    elif menu == "2":
        delete = input("Ta bort: ")

        for index, person in enumerate(telefonbok):
            if person["namn"] == delete:
                del telefonbok[index]
                print("Borttagen")
        
    elif menu == "3":
        search = input("Sök: ")

        for person in telefonbok:
            if person ["namn"] == search:
                print(person["namn"], "\t", person["telenr"])

        print("")

    elif menu == "4":
        telefonbok = sorted(telefonbok, key= lambda k: k["namn"])

        for person in telefonbok:
            print(person["namn"], "\t", person["telenr"])

        print("")

    elif menu == "0":
        print("du har valt att avsluta")
        break
    else:
        print("GÖR OM GÖR RÄTT!!!")
