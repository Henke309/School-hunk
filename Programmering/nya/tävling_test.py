"""
Name: Henrik Nguyen
Date: 2020-01-14
Info:
Anordna en tävling
"""
import random
import time

def bsortering(tävling):
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

tävling.append({"dnamn":"Henrik", "dpnmr":"0207031337", index +1})
tävling.append({"dnamn":"David", "dpnmr":"0208201952", index +1})
tävling.append({"dnamn":"Simon", "dpnmr":"0207021272", index +1})
tävling.append({"dnamn":"Elias", "dpnmr":"0211212352", index +1})
tävling.append({"dnamn":"Adam", "dpnmr":"0201282992", index +1})

print("")
print("")
print("☆" *50)   # *50 gör så att det skrivs ut 50 gånger
print("Julaboll ätar tävling".center(50)) # .center(valfritt nummer) gör så att allt du skriver lägger sig så mycket i mitten som möjligt beroende på hur lång stränen är som du skrivier i paranteserna
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

    if meny == "1":
        print("Du har valt att lägga till end deltagare. ")
        while True:
            print("Skriv 'stop' för att inte lägga till någon mer deltagare")
            print("")
            while True:
                dnamn = input("Ange i deltagarens namn: ").title() # .title() gör så att första bokstaven i orden blir stora bokstäver och de andra små
                if dnamn == "":
                    print("Du måste fylla i något")
                
                else:
                    break

            if dnamn.lower() == "stop": # .lower() omvandlar alla bokstäver som personen skrev in till små bokstäver,t.ex "HEJ jAg HeTeR HenRIK" blir "hej jag heter henrik"
                print("återvänder till menyn")
                break 
            else:
                while True:
                    dpnmr = input("Ange deltagarens personnummer(ÅÅMMDDXXXX): ")

                    if dpnmr.lower() == "stop":
                        break
                    else:
                    
                        if not dpnmr.strip().isdigit(): #.strip() ser till att det inte finns något mellanslag | .isdigit() gör så att det endast får finnas siffror i strängen
                            print("Endast siffror")

                        elif len(dpnmr.strip()) != 10:
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
                                    print("Deltagarnummret:", index +1)
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
                for deltagare in tävling:
                    if deltagare ["dpnmr"] == delete:
                        print("-"*50)
                        print(deltagare ["dnamn"].title(), "har tagits bort från deltagarlistan ")
                        print("-"*50)
                for index, deltagare in enumerate(tävling):
                    if deltagare["dpnmr"] == delete:
                        del tävling [index]
                vidare()


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
                        print("Namn:", deltagare["dnamn"].title(),"| ""Personnummer:", deltagare ["dpnmr"],"| ""Deltagarnummer:")
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
            print("0. Avsluta programmet-----------------------------")
            print("")
            meny2 = input("Välj något av alternativen ovan: ")
            
            if meny2 == "1":
                print("Du har valt att se deltagarna från A till Ö")
                
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
            antal = random.randint(7, 64)
            person["dantal"] = antal
            tävling.append({"dantal":antal})

            x = sorted(tävling, key=lambda k: k["dantal"]) 
            for person in x:
                print("Vinnaren är... ")
                for y in range(3):
                    time.sleep(1)
                    print(".")
                print( person ["dnamn"],"\n""deltagarnummer:", person ["dnr"], "\n""Antal ätna julabollar på 1 minut:", person ["dantal"])
                vidare()
                break
        

    elif meny == "0":
        print("Du har valt att avsluta programmet. ")
        print("-"*50)
        break

    elif meny == "9":
        for delt in tävling:
            antal = random.randint(7, 64)
            delt ["dantal"] = antal            
            tävling.append({"dantal":antal})
            print(delt ["dnamn"], delt ["dantal"])
            
        else:
            break
            

    else:
        print("Du har ej fyllt i något av alternativen ovan, försök igen. ")


print("VINNAREN ÄR")
print(".")
print(".")
print(".")
print("HENRIK NGUYEN GRATTIS")

for delt in tävling:
    antal = random.randint(7, 64)
    delt["dantal"] = antal
    print(delt ["dnamn"], "antal ätna bollar:", antal)

    for x in tävling:
                    x = sorted(tävling, key=lambda k: k["dantal"]) 
            for person in x:
                print("Vinnaren är... ")
                for y in range(3):
                    time.sleep(1)
                    print(".")
                print( person ["dnamn"],"\n""deltagarnummer:", person ["dnr"], "\n""Antal ätna julabollar på 1 minut:", person ["dantal"])
                vidare()
                break