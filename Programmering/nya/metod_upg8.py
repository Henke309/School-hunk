def ctof(c):
    f = (c * 1.8) + 32
    return f

def ftoc(f):
    c = (f - 32) / 1.8
    return c 

print("="*51)
print("Detta program omvandlar Celsius till Fahrenheit".center(51))
print("="*51)
print("")
print("="*51)
print("Menyval".center(51))
print("="*51)
print("")

while True:
    print("1: Celsius till Fahrenheit ")
    print("2. Fahrenheit till Celsius ")
    print("0. Avsluta programmet ")
    val = int(input("Välj något av alternativen ovan: "))
    print("")
  
    if val == 1:
        print("Du har valt att omvandla Celsius till Fahrenheit ")
        print("")
        c = float(input("Ange Celsius: "))
        print(ctof(c))
        print("")

    elif val == 2:
        print("Du har valt att omvandla Fahrenheit till Celsius ")
        print("")
        f = float(input("Ange Fahrenheit: "))
        print(ftoc(f))
        print("")

    elif val == 0:
        print("Du har valt att avsluta programmet D: ")    
        print("")¨
        break

    else:
        print("Jag förstår inte...")
        print("Testa igen ")        
        print("")