"""
Name: Henrik Nguyen
Date: 08-10-2019
Info:
Elevregister
"""

register = []

register.append({"namn":"Henrik", "klass":"Te18", "pnmr":"020703"})
register.append({"namn":"Elias", "klass":"Te17", "pnmr":"011203"})
register.append({"namn":"Simon", "klass":"Aw19", "pnmr":"030702"})
register.append({"namn":"David", "klass":"Na18", "pnmr":"020915"})
register.append({"namn":"Adam", "klass":"Te18", "pnmr":"020128"})

while True:
    print("")
    print ("1. Mata in en elev i registret ")
    print ("2. Visa alla som är med i registret ")
    print ("3. ta bort elev från registret ")
    print ("0. avsluta programmet ")

    val = input("Vad vill du göra: ")

    if val == "1":

        print("")
        print("Du har valt att mata in en elev i registret ")
        print("Skriv avsluta för att avsluta programmet ")
        print("")
        while True:
            namn = input("Mata in elevens namn: ").title()
            
            if namn.lower() == "avsluta":
                ("Du har valt att avsluta valet")
                break
            
            else:
                klass = input("Mata in vilken klass eleven går i: ")
                pnmr = input("Mata in elevens personnummer: ")
                register.append({"namn":namn.title(), "klass":klass, "pnmr":pnmr})
                print("")

    elif  val == "2":
        while True:
            print("")
            print("Du har valt att se alla som är med i registret ")
            print("1. Visa alla elever i bokstavsordning ")
            print("2. visa alla från älst till yngst ")
            print("0. avsluta")
            val2 = input("Välj något av de 2 alternativen ovanför: ")
            print("")

            if val2 == "0":
                print("Du har nu valt att avsluta Valet ")
                break
            
            elif val2 == "1":
                print("Du har valt att se alla elever i bokstavsordning ")
                print("")

                register = sorted(register, key=lambda k: k["namn"])
            
                for elev in register:
                    print(elev["namn"], elev["klass"], elev["pnmr"])

            elif val2 == "2":
                    print("Du har valt att se från älst till yngst ")

                    register = sorted(register, key=lambda k: k["pnmr"])

                    for elev in register:
                        print(elev["namn"], elev["klass"], elev["pnmr"])
            else:
                print("Jag förstår inte vad du menar, försök igen")
                print("")

    elif val == "3":
        print("Du har valt att ta bort en elev från registret ")
        while True:
            delete = input("Ange personnummret för att ta bort: ")
            if delete.lower() == "avsluta":
                print("Du har valt att avsluta valet")
                break

            else:
                for index, elev in enumerate(register):
                    if elev["pnmr"] == delete:
                        del register[index]
                        print("")

    elif val == "0":
        print("Du har nu valt att avsluta programmet ")
        break







