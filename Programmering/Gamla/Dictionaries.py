"""
Name: Henrik Nguyen
Date: 01-10-2019
Info:
<Insert information about file>
"""

namn = input("Skriv in namnet: ")
telenr = (input("Skriv in telenumret: "))
twitter = input("Skriv in ditt twitterkonto: ")

person = {"name":namn, "phone":telenr, "twitter":"@" + twitter}

print(person["name"])
print(person["phone"])
print(person["twitter"])

print("")

while True:
    print("1. visa namn")
    print("2. Visa telefonnummer")
    print("3. Visa twitterkonto")
    print("0. Avsluta")

    menu = input(":")

    print("")

    if menu == "1":
        print("Namnet är ", person["name"])
    elif menu == "2":
        print("Telefonnummret är ", person["phone"])
    elif menu == "3":
        print("Twitterkontot är", person["twitter"])
    elif menu == "0":
        print("Programmet har avslutat. ")
    else:
        print("välj något av alternativen! ")
        break


    print("")