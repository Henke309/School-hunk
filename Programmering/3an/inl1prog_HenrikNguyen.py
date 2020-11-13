from inl1class_HenrikNguyen import *
from abc import ABCMeta, abstractmethod

def visa(djurpensionat):
    for djuren in djurpensionat:
        print("Namn: ", djuren.namn.title(),"| ""ras: ", djuren.ras.title(),"| ""vikt: ", djuren.vikt, "| ""ID: ", str(djuren.djurid) , "| ""Hem: ", djuren.hem.title(), "| ""Vaccinerad: ", djuren.vaccinerad.title(), "| ""Kastrerad: ", djuren.kastrerad.title(), "| ""Chippad: ", djuren.chippad.title())
        print("-"*150)

def vidare():
    input("Tryck på enter för att gå vidare.")

djurpensionat = []

djurpensionat.append(katt("Fjant", "Bondkatt", "5", "Lundgrens"))
djurpensionat.append(katt("Sessan", "Bondkatt", "3", "Lundgrens"))
djurpensionat.append(katt("Rufus", "Nakenkatt", "4", "Generals"))
djurpensionat.append(katt("Muffins", "Bondkatt", "9", "Siberias"))
djurpensionat.append(katt("Molly", "Bondkatt", "8", "Siberias"))
djurpensionat.append(katt("Nisse", "Bondkatt", "10", "Siberias"))
djurpensionat.append(katt("Titti", "Bondkatt", "7", "Siberias"))

djurpensionat.append(hund("Gabbe", "Kinesisk nakenhund", "4", "Lundgrens"))
djurpensionat.append(hund("Dylan", "Kinesisk nakenhund", "3", "Lundgrens"))
djurpensionat.append(hund("Gärd", "Hälleforsare/lajka", "15", "Siberias"))

while True:      
    print("*"*50)
    print("Meny".center(50))
    print("*"*50)
    print("1. Lägg in ett djur ------------------------------")
    print("2. Ta bort ett djur ------------------------------")
    print("3. Sök efter ett djur ----------------------------")
    print("4. Se alla djur ----------------------------------")
    print("5. Ändringar på djuren ---------------------------")
    print("0. Avsluta programmet ----------------------------")
    print("")
    meny = input("Välj något av alternativen ovan: ")

    if meny.lower() == "":
        print("Du måste skriva något")
        vidare()

    elif meny == "1":
        while True:
            print("")
            print("*"*50)
            print("Lägg till ett djur".center(50))
            print("*"*50)
            print("")
            print("Skriv 'stop' för att komma tillbaka till menyn")
            print("")
            meny1 = input("Ska du lägga till en katt eller en hund?" "\n" "Svara med: 'katt' eller 'hund'" "\n" "svara här: ")
            
            if meny1.lower() == "":
                print("Du måste skriva något")
                vidare()

            elif meny1.lower() == "stop":
                print("Du återvänder till menyn!")
                vidare()
                break

            elif meny1.lower() == "katt":
                print("Du har valt att lägga in en katt på djurpensionatet")
                print("")
                
                while True:
                    namn = input("Mata in kattens namn: ").title()
                    print("")
                    if namn == "":
                        print("*"*50)
                        print("Du måste skriva något.")
                        print("*"*50)
                    else:
                        break
                        
                while True:
                    ras = input("Mata in " + namn.title() + "s" + " ras: " )
                    print("")
                    if ras == "":
                        print("*"*50)
                        print("Du måste skriva något.")
                        print("*"*50)
                    else:
                        break

                while True:
                    vikt = input("Ange " + namn.title() + "s" + " vikt: ")
                    print("")
                    if not vikt.strip().isdigit():
                        print("*"*50)
                        print("Inga mellanslag eller bokstäver, endast siffor")
                        print("*"*50)
                    else:
                        break

                while True:
                    print("1. Lundgrens")
                    print("2. General")
                    print("3. Siberia")
                    print("Välj något av hemmen ovan")
                    hem = input("Svara med (1,2 eller 3): ")

                    if hem == "1":
                        hem = "Lundgrens"
                        break

                    elif hem == "2":
                        hem = "Generals"
                        break

                    elif hem == "3":
                        hem = "Siberias"
                        break

                    else:
                        print("Du valde inget av alternativen ")

                djurpensionat.append(katt(namn, ras, vikt, hem))

                print("")
                for djuren in djurpensionat:
                    if djuren.namn == namn:  
                        print("*"*50)      
                        print(djuren.namn, "har lagts till i djurpensionatet!")
                        print("Namn:", djuren.namn)
                        print("Ras:", djuren.ras)
                        print("Vikt:", djuren.vikt)
                        print("ID: ", str(djuren.djurid))
                        print("Hem: ", djuren.hem)
                        print("*"*50)  
                vidare()    
                break 
                    
            elif meny1.lower() == "hund":
                print("Du har valt att lägga in en hund på djurpensionatet")
                print("")

                while True:
                    namn = input("Mata in hundens namn: ").title()
                    print("")
                    if namn == "":
                        print("*"*50)
                        print("Du måste skriva ett namn.")
                        print("*"*50)
                    else:
                        break
                        
                while True:
                    ras = input("Mata in " + namn.title() + "s" + " ras: " )
                    print("")
                    if ras == "":
                        print("*"*50)
                        print("Du måste skriva en ras.")
                        print("*"*50)
                    else:
                        break

                while True:
                    vikt = input("Ange " + namn.title() + "s" + " vikt: ")
                    print("")
                    if not vikt.strip().isdigit():
                        print("*"*50)
                        print("Inga mellanslag eller bokstäver, endast siffor")
                        print("*"*50)
                    else:
                        break

                djurpensionat.append(hund(namn, ras, vikt, hem))
                
                print("")
                for djuren in djurpensionat:
                    if djuren.namn == namn:  
                        print("*"*50)      
                        print(djuren.namn, "har lagts till i djurpensionatet!")
                        print("Namn:", djuren.namn)
                        print("Ras:", djuren.ras)
                        print("Vikt:", djuren.vikt)
                        print("ID: ", str(djuren.djurid))
                        print("*"*50)  
                vidare()    
                break

            else: 
                print("???")

    elif meny == "2":
        while True:
            print("")
            print("*"*50)
            print("Ta bort ett djur".center(50))
            print("*"*50)
            print("")
            print("Skriv 'stop' för att komma tillbaka till menyn")
            meny2 = input("Ska du ta bort en katt eller en hund?" "\n" "Svara med: 'katt' eller 'hund'" "\n" "svara här: ")
            
            if meny2.lower() == "":
                print("Du måste skriva något")
                vidare()

            elif meny2.lower() == "stop":
                print("Du återvänder till menyn!")
                vidare()
                break

            elif meny2.lower() == "katt":
                print("Du valde att ta bort en katt")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.djurid) 
                visa(djurpensionat)
                print("Skriv 'stop' för att komma tillbaka till menyn")
                delete = input("\nAnge kattens id-nr för att ta bort: ")
                if delete.lower() == "stop":
                    print("Du har valt att gå tillbaka till menyvalet ")
                    break
                else:
                    for djuren in djurpensionat:
                        if str(djuren.djurid) == delete:
                            print("*"*50)
                            print(djuren.namn.title(), " har skrivits ut från djurpensionatet")
                            print("*"*50)
                        
                    for index, djuren in enumerate(djurpensionat):
                        if str(djuren.djurid) == delete:
                            del djurpensionat [index]

            elif meny2.lower() == "hund":
                print("Du valde att ta bort en hund")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.djurid) 
                visa(djurpensionat)
                print("Skriv 'stop' för att komma tillbaka till menyn")
                delete = input("\nAnge kattens id-nr för att ta bort: ")
                if delete.lower() == "stop":
                    print("Du har valt att gå tillbaka till menyvalet ")
                    break
                else:
                    for djuren in djurpensionat:
                        if str(djuren.djurid) == delete:
                            print("*"*50)
                            print(djuren.namn.title(), " har skrivits ut från djurpensionatet")
                            print("*"*50)
                        
                    for index, djuren in enumerate(djurpensionat):
                        if str(djuren.djurid) == delete:
                            del djurpensionat [index]

    elif meny == "3":
        print("Du har valt att söka efter ett djur. ")
        while True:
            print("Skriv 'stop' för att komma tillbaka till menyn")
            print("")
            search = input("Skriv in namnet: ")
            if search.lower() == "stop":
                break
            elif not search.lower() == "stop":
                for djuren in djurpensionat:
                    if djuren.namn.title() == search.title():
                        print("Namn: ", djuren.namn.title(),"| ""ras: ", djuren.ras.title(),"| ""vikt: ", djuren.vikt, "| ""ID: ", str(djuren.djurid))
                        vidare()
                        break
                    else:
                        print("Kunde ej hittas")    

            else:
                print("Finns ej i djurpensionatet")
    
    elif meny == "4":
        while True:
            print("")
            print("*"*50)
            print("Meny för att se alla djur".center(50))
            print("*"*50)
            print("")
            print("1. Bokstavsordning A till Ö-----------------------")
            print("2. Bokstavsordning Ö till A-----------------------")
            print("3. Rasordning A till Ö----------------------------") 
            print("3. Rasordning Ö till A----------------------------")
            print("5. Vikt lättast till tyngst-----------------------")
            print("6. Vikt tyngst till lättast-----------------------")
            print("0. Återvänd till Menyn----------------------------")
            print("")
            print("Skriv 'stop' för att komma tillbaka till menyn")
            meny3 = input("Välj något av alternativen ovan: ")

            if meny3.lower() == "":
                print("Du måste skriva något")
                vidare()

            elif meny3 == "1":
                print("Du har valt att se djuren från A till Ö") 
                djurpensionat = sorted(djurpensionat, key=lambda k: k.namn)
                visa(djurpensionat)
                vidare()                

            elif meny3 == "2":
                print("Du har valt att se djuren från Ö till A")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.namn, reverse=True)
                visa(djurpensionat)
                vidare()

            elif meny3 == "3":
                print("Du har valt att se djurens från A till Ö")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.ras)
                visa(djurpensionat)
                vidare()

            elif meny3 == "4":
                print("Du har valt att se djurens från Ö till A")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.ras, reverse=True)
                visa(djurpensionat)
                vidare()

            elif meny3 == "5":
                print("Du har valt att se djuren i viktordning (lättast > tyngst)")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.vikt)
                visa(djurpensionat)
                vidare()

            elif meny3 == "6":
                print("Du har valt att se djuren i viktordning (tyngst > lättast)")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.vikt, reverse=True)
                visa(djurpensionat)
                vidare()
            elif meny3 == "0":
                print("Du har valt att återvända till menyn ")
                vidare()
                break

    elif meny == "5":
        while True:
            print("")
            print("1.Vaccinera")
            print("2.Kastrera")
            print("3.Chip-märka")
            print("0.Återvänd till huvudmenyn")
            print("")

            meny4 = input("Välj något av alternativen ovan \n svara med 1,2 eller 3 \n svara här: ")

            if meny4.lower() == "":
                print("Du måste skriva något")
                vidare()

            elif meny4.lower() == "1":
                print("")
                print("Du valde att Vaccinera ett djur")
                print("1.Katt")
                print("2.Hund")
                print("")
                print("Skriv 'stop' för att gå tillbaka")
                menyv = input("Välj något av alternativen ovan \n svara med 1 eller 2 \n svara här: ")

                if menyv.lower() == "":
                    print("Du måste skriva något")
                    vidare()

                elif menyv.lower() == "stop":
                    print("Du återvänder till menyn!")
                    vidare()

                elif menyv.lower() == "1":
                    print("Du har valt att vaccinera en katt")
                    djurpensionat = sorted(djurpensionat, key=lambda k: k.djurid) 
                    visa(djurpensionat)
                    print("Skriv 'stop' för att gå tillbaka")
                    vac1 = input("Ange den vaccinerade kattens djur-ID: ")
                    if vac1.lower() == "":
                        print("Skriv nått")

                    elif vac1.lower() == "stop":
                        break

                    else:
                        for djuren in djurpensionat:
                            if vac1 == str(djuren.djurid):
                                print(djuren.namn, " Har blivit vaccinerat.")
                                djuren.vaccinerad = "Ja"
                                vidare()

                elif menyv.lower() == "2":
                    print("")
                    djurpensionat = sorted(djurpensionat, key=lambda k: k.djurid) 
                    visa(djurpensionat)
                    print("Skriv 'stop' för att gå tillbaka")
                    vac2 = input("Ange den vaccinerade kattens djur-ID: ")
                    if vac2.lower() == "":
                        print("Skriv nått")

                    elif vac2.lower() == "stop":
                        break

                    else:
                        for djuren in djurpensionat:
                            if vac2 == str(djuren.djurid):
                                print(djuren.namn, " Har blivit vaccinerat.")
                                djuren.vaccinerad = "Ja"
                                vidare()
            
                else:
                    print("Ett fel uppstod, försök igen.")

            elif meny4.lower() == "2":
                print("Du har valt att kastrera en katt")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.djurid) 
                visa(djurpensionat)
                print("Skriv 'stop' för att gå tillbaka")
                kast = input("Ange den vaccinerade kattens djur-ID: ")
                if kast.lower() == "":
                    print("Skriv nått")

                elif kast.lower() == "stop":
                    break

                else:
                    for djuren in djurpensionat:
                        if kast == djuren.djurid:
                            print(djuren.namn, " Har blivit kastrerad.")
                            djuren.kastrerad = "Ja"
                            vidare()

            elif meny4.lower() == "3":
                print("Du har valt att chipopa en hund")
                djurpensionat = sorted(djurpensionat, key=lambda k: k.djurid) 
                visa(djurpensionat)
                print("Skriv 'stop' för att gå tillbaka")
                chip = input("Ange den vaccinerade kattens djur-ID: ")
                if chip.lower() == "":
                    print("Skriv nått")

                elif chip.lower() == "stop":
                    break

                else:
                    for djuren in djurpensionat:
                        if chip == djuren.djurid:
                            print(djuren.namn, " Har blivit kastrerad.")
                            djuren.chippad = "Ja"
                            vidare()

            elif meny4 == "0":
                print("Du återvänder nu till menyn")
                vidare()
                break

    elif meny == "0":
        print("Du har valt att avsluta programmet!")
        vidare()
        quit

    else:
        print("Det måste vara med en siffra...")
        vidare()