"""
Name: Henrik Nguyen
Date: 01-10-2019
Info:
<Insert information about file>
"""

inbjudna = []

while True:
    namn = input("Skriv in namnet: ")

    if namn.lower() == "avsluta":
        break
    else:
        inbjudna.append(namn.title())

print("INBJUDNA")
print("====================")
for person in inbjudna: 
    print(person)


tabort = input("Vem vill du ta bort: ")

inbjudna.remove(tabort.tabort)