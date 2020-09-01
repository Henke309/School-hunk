"""
Name: Henrik Nguyen
Date: 2019-11-12
Info:
<Insert information about file>
"""

print("*"*41)
print("Menyval".center(41))
print("1. addition ")
print("2. subtraktion ")
print("3. multiplikation ")
print("4. division ")
print("")

val = int(input("Välj någåt utav alternativen ovan: "))
print("")

if val == 1:
    try:
        print("Du har valt addition ")
        x = int(input("Ange x: "))
        y = int(input("Ange y: "))
        print(x, "+", y, "=", x+y)

    except:
        print("Felaktig inmatning, Endast siffror! ")

elif val == 2:
    print("Du har valt Subtraktion ")
    x = int(input("Ange x: "))
    y = int(input("Ange y: "))

elif val == 3:
    print("Du har valt multiplikation ")
    x = int(input("Ange x: "))
    y = int(input("Ange y: "))

elif val == 4:
    print("Du har valt division ")
    x = int(input("Ange x: "))
    y = int(input("Ange y: "))
