def add(x, y):
    addi = x + y
    return addi

def sub(x, y):
    subt = x - y
    return subt

def div(x, y):
    divi = x / y
    return divi

def mul(x, y):
    mult = x * y
    return mult

print("*"*51)
print("Miniräknare".center(51))

while True:
    print("*"*51)
    print("Menyval".center(51))
    print("1. Addition ")
    print("2. Subtraktion ")
    print("3. Divition ")
    print("4. Multiplikation ")
    print("0. Stäng av miniräknaren ")
    print("")    

    val = input("Välj något av de alternativen ovan: ")
    print("")

    if val == "1":
        print("Du har valt addition")
        print("Ange x och y (x + y)")
        x = int(input("Ange X: "))
        y = int(input("Ange Y: "))
        print("")
        print("svar: ", add(x, y))


    elif val == "2":
        print("Du har valt subtraktion")
        print("Ange x och y (x - y)")
        x = int(input("Ange X: "))
        y = int(input("Ange Y: "))
        print("")
        print("svar: ", sub(x, y))

    elif val == "3":
        print("Du har valt Divition")
        print("Ange x och y (x / y)")
        x = int(input("Ange X: "))
        y = int(input("Ange Y: "))
        print("")
        print("svar: ", div(x, y))

    elif val == "4":
        print("Du har valt multiplikation")
        print("Ange x och y (x * y)")
        x = int(input("Ange X: "))
        y = int(input("Ange Y: "))
        print("")
        print("svar: ", mul(x, y))

    elif val == "0":
        print("Du har valt att stänga av miniräknaren ")
        break 

    else:
        print("Ogiltig inmatning, testa igen :D")