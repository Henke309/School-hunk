"""
Name: Henrik Nguyen
Date: 2019-09-25
Info:
<Struktur uppgift>
"""
while True:
    try:
        print("1. Delbarhet")
        print("2. Summera en talföljd")
        print("0. Avsluta programmet")
        val = int(input("Välj något av de alternativen ovan: "))    
        print("")

        while True:
            if val == 1:
                try:
                    print("skriv avsluta för att komma tillbaka till menyn ")
                    x = int(input("Ange täljaren: "))
                    y = int(input("Ange nämnaren: "))
                    if x == 0 or y == 0:
                        print ("Tal x är EJ delbart med tal y ")
                    elif x.lower() == "avsluta":
                        print("Du har valt att gå tillbaka till menyn")
                    else:
                        svar = x/y
                        print ("Tal x är delbart med tal y ", svar)
                except:
                    print("")
                    print("Felaktig inmatning, Endast Siffror! ")
                    print("")

        while True:
            if val == 2:
                try:
                    x = int(input("Ange talföljdens start: "))
                    y = int(input("Ange talföljdens slut: "))
                    sum = 0
                except:
                    print("")
                    print("Felaktig inmatning, Endast siffror! ")
                    print("")

                for i in range (x, y):
                    sum = sum + i
                print (sum)
            
        if val == 0:
            print("Du har valt att avsluta programmet ")
            break 

    except:
        print("")
        print("Felaktig inmatning, testa igen.")
        print("")