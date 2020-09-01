"""
Name: Henrik Nguyen
Date: 2020-01-14
Info:
Anordna en tävling
"""
import random # Måste importa dessa för att jag ska kunna använda dessa funktioner.
import time

def bsortering(tävling): #Använder metoder så att jag slipper skriva om dessa så många gånger + det ser mycket bättre ut och allt blir inte så grötit.
    tävling = sorted(tävling, key=lambda k: k["dnamn"])
def bsorteringreverse(tävling):
    tävling = sorted(tävling, key=lambda k: k["dnamn"], reverse=True)
def nsortering(tävling):
    tävling = sorted(tävling, key=lambda k: k["dpnmr"])
def nsorteringreverse(tävling):
    tävling = sorted(tävling, key=lambda k: k["dpnmr"], reverse=True)
def visa(tävling):
    for deltagare in tävling:
        print("Namn:", deltagare["dnamn"].title(),"| ""Personnummer:", deltagare ["dpnmr"],"| ""Deltagarnummer:", deltagare ["dnr"] )
def vidare():
    input("Tryck på enter för att gå vidare.")
    

tävling = []

tävling.append({"dnamn":"Henrik", "dpnmr":"0207031337", "dnr":1})  #Lägger till lite deltagare så att det inte blir allt för lite som tävlar :D
tävling.append({"dnamn":"David", "dpnmr":"0208201952", "dnr":2})
tävling.append({"dnamn":"Simon", "dpnmr":"0207021272", "dnr":3})
tävling.append({"dnamn":"Elias", "dpnmr":"0211212352", "dnr":4})
tävling.append({"dnamn":"Adam", "dpnmr":"0201282992", "dnr":5})

print("")
print("")
print("☆" *50)   # *50 gör bara så att det underlättar mig så sliper jag skriva ut skiten 50 gånger :D
print("Julabollätartävling".center(50)) # Samma sak här. istället för att trycka space ett antal gånger så skriver jag.center så sätter den sig i mitten.
print("☆" *50)        
print("")
print("")
print("")

while True:      
    print("*"*50)
    print("Meny".center(50))
    print("*"*50)
    print("1. lägg till en deltagare-------------------------")
    print("2. ta bort en deltagare---------------------------")
    print("3. sök efter en deltagare-------------------------")
    print("4. se alla deltagare------------------------------")
    print("7. Starta tävlingen-------------------------------")
    print("0. Avsluta programmet-----------------------------")
    print("")
    meny = input("Välj något av alternativen ovan: ")
    print("")

    if meny == "1": # Ifsats valde jag för att de endast ska kunna skriva något av alternativen ovan, tex 1,2,3 och om de skriver något annat blir det fel för jag har en else sats
        print("Du har valt att lägga till end deltagare. ")
        while True: # Jag vill att det ska loopas om varje gång så att man slipper att klicka in på samma alternativ igen om och om igen, tex om man ska lägga till 10 personer.
            print("Skriv 'stop' för att inte lägga till någon mer deltagare")
            print("")
            while True:
                dnamn = input("Ange i deltagarens namn: ").title() #.title(), bra ifall någon råkar skriva med bara små eller bara stora eller med blandade bokstäver, så rättar tilte till det.
                if dnamn == "":
                    print("Du måste fylla i något")
                
                else:
                    break

            if dnamn.lower() == "stop": # .lower(), omvandlar allt till små bokstäver, kan vara bar att ha den ifall de skriver Stop eller STOP osv.
                print("återvänder till menyn")
                break 
            else:
                while True:
                    dpnmr = input("Ange deltagarens personnummer(ÅÅMMDDXXXX): ")

                    if dpnmr.lower() == "stop":
                        break
                    else:
                    
                        if not dpnmr.strip().isdigit(): #.strip() och .isdigit() använder jag då jag endast vill att användaren ska fylla i siffor, då tillåter den endast siffror och inget annat.
                            print("Endast siffror")

                        elif len(dpnmr.strip()) != 10: #.len räknar strängen och ser till att det endast är 10 bokstäver siffror u name it.
                            print("Personnummret ska vara 10 siffror")

                        else:       
                            print("")
                            tävling.append ({"dnamn":dnamn.title() , "dpnmr":dpnmr, "dnr":len(tävling) + 1})
                            for deltagare in tävling:
                                if deltagare ["dpnmr"] == dpnmr:  
                                    print("-"*50)      
                                    print(deltagare ["dnamn"], "har lagts till i deltagarlistan!")
                                    print("Namn:", deltagare ["dnamn"])
                                    print("Personnummret:", deltagare ["dpnmr"])
                                    print("Deltagarnummret:", deltagare ["dnr"])
                                    print("-"*50)  
                            vidare()    
                            break 

    elif meny == "2":
        print("Du har valt att ta bort en deltagare. ")

        while True:
            print("Skriv 'stop' för att komma tillbaka till menyn")
            delete = input("\nAnge personnummret för att ta bort deltagaren: ")
            if delete.lower() == "stop":
                print("Du har valt att gå tillbaka till menyvalet ")
                break
            else:
                for deltagare in tävling: #kollar deltagare i tävling
                    if deltagare ["dpnmr"] == delete: #om deltagarens personnummmer stämmer dem delete så tas den brot
                        print("-"*50)
                        print(deltagare ["dnamn"].title(), "har tagits bort från deltagarlistan ") # Här vill jag bara tydliggöra för användaren att den har tagit bort "deltagare" från listan.
                        print("-"*50)
                for index, deltagare in enumerate(tävling): #och här tas personen bort för om denna hade varit framför texten så hade den endast skrivit ut "har tagits bort från tävlingen" för att den kan inte hitta personen för den är redan borttagen.
                    if deltagare["dpnmr"] == delete:
                        del tävling [index]
                vidare() #denna metod är endast en input, den har jag bara för att det inte ska loopas om direkt, jag vill att användaren ska få tid att läsa och se vem hen har tagit bort.


    elif meny == "3":
        print("Du har valt att söka efter en deltagare. ")
        while True:
            print("Skriv 'stop' för att komma tillbaka till menyn")
            print("")
            search = input("Skriv in namnet: ")
            if search.lower() == "stop":
                break
            elif not search.lower() == "stop":
                for deltagare in tävling:
                    if deltagare["dnamn"] == search.title():
                        print("Namn:", deltagare["dnamn"].title(),"| ""Personnummer:", deltagare ["dpnmr"],"| ""Deltagarnummer:", deltagare ["dnr"] )
                        vidare()
                        break                   
                else:
                    print("-"*50)
                    print("Denna personen är inte med i tävlingen, testa igen")
                    print("-"*50)
                    vidare()   
        


    elif meny == "4":
        while True:
            print("Du har valt att se alla deltagare. ")            
            print("-"*50)
            print("Meny för att se deltagare".center(50))
            print("-"*50)            
            print("1. Bokstavsordning A till Ö-----------------------")
            print("2. Bokstavsordning Ö till A-----------------------")
            print("3. Åldersordning Äldst till Yngst-----------------")
            print("4. Åldersordning Yngst till äldst-----------------")
            print("0. Återvänd till Menyn----------------------------")
            print("")
            meny2 = input("Välj något av alternativen ovan: ")
            
            if meny2 == "1":
                print("Du har valt att se deltagarna från A till Ö") #Här använder jag de metoderna som jag hade skrivit där uppe. Skulle ha blivit ganska grötit om jag ej hade använt metoder.
                
                bsortering(tävling)           
                visa(tävling)
                vidare()

            elif meny2 == "2":
                print("Du har valt att se deltagarna från Ö till A")

                bsorteringreverse(tävling)
                visa(tävling)
                vidare()

            elif meny2 == "3":
                print("Du har valt att se alla deltagare från Äldst till Yngst")

                nsortering(tävling)
                visa(tävling)
                vidare()

            elif meny2 == "4":
                print("Du har valt att se alla deltagare från Yngst till Äldst")

                nsorteringreverse(tävling)
                visa(tävling)
                vidare()

            elif meny2 == "0":
                print("Du har valt att återvända till meny 1 ")
                break

        else:
            print("Du valde inget av alternativen ovan! ")
    
    elif meny == "7":
        for person in tävling:
            antal = random.randint(7, 64) #Här använder jag random.randint som gör att en person i listan får ett random nummer mellan 7-64, denna har jag för att alla deltagare ska få ett nummer mellan 7-64 och det nummret är antalet chokladbollad de har ätit vilket leder till att någon kommer att vinna
            person["dantal"] = antal

        tävling = sorted(tävling, key=lambda k: k["dantal"], reverse=True) 
        print("Vinnaren är... ")
        for y in range(3): #Jag anänder denna forsats för att jag vill att det ska upprepas 3 gånger. 
            time.sleep(1) # jag vill även att det ska vara 1 sekund delay på utskriften så då använder jag time.sleep() vilket gör att det väntar med att skriva ut och jag valde 1 sekund för det är en bra längd :D
            print(".")
        print("☆" *50)
        print( tävling[0]["dnamn"],"\n""deltagarnummer:", tävling[0]["dnr"], "\n""Antal ätna julabollar på 1 minut:", tävling[0]["dantal"]) # Är vill jag att användaren ska se vem det är som vinner så då skriver jag ut allt om deltagaren.
        print("☆" *50)
        vidare()
    

    elif meny == "0":
        print("Du har valt att avsluta programmet. ")
        print("-"*50)
        break
            
    else:
        print("Du har ej fyllt i något av alternativen ovan, försök igen. ")