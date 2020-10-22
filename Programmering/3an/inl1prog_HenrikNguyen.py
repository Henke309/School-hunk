from inl1class_HenrikNguyen import *
from abc import ABCMeta, abstractmethod

djurpensionat = []
while True:      
    print("*"*50)
    print("Meny".center(50))
    print("*"*50)
    print("1. lägg in ett djur ------------------------------")
    print("2. ta bort ett djur ------------------------------")
    print("3. sök efter ett djur ----------------------------")
    print("4. se alla djur ----------------------------------")
    print("5. ändringar på djuren ---------------------------")
    print("0. Avsluta programmet ----------------------------")
    print("")
    meny = input("Välj något av alternativen ovan: ")

    if meny == "1":
        while True:
            print("")
            print("*"*50)
            print("Lägg till ett djur".center(50))
            print("*"*50)
            print("")
            meny2 = input("Ska du lägga till en katt eller en hund?" "\n" "Svara med: 'katt' eller 'hund'" "\n" "svara här: ")
            
            
            if meny2.lower() == "katt":
                print("Du har valt att lägga in en katt på djurpensionatet")
                
                while True:
                    namn = input("Mata in kattens namn: ").title()
                    if namn == "":
                        print("*"*50)
                        print("Du måste skriva ett namn.")
                        print("*"*50)
                    else:
                        break
                        
                while True:
                    ras = input("Mata in " + namn.title() + "s" + " ras: " )
                    if ras == "":
                        print("*"*50)
                        print("Du måste skriva en ras.")
                        print("*"*50)
                    else:
                        break

                while True:
                    vikt = input("Ange " + namn.title() + "s" + " vikt: ")
                    if not vikt.strip().isdigit():
                        print("*"*50)
                        print("Inga mellanslag eller bokstäver, endast siffor")
                        print("*"*50)
                    else:
                        break

                djurpensionat.append(katt(namn, ras, vikt))
                        

            elif meny2.lower() == "hund":
                print("Du har valt att lägga in en hund på djurpensionatet")

                while True:
                    namn = input("Mata in hundens namn: ").title()
                    if namn == "":
                        print("*"*50)
                        print("Du måste skriva ett namn.")
                        print("*"*50)
                    else:
                        break
                        
                while True:
                    ras = input("Mata in " + namn.title() + "s" + " ras: " )
                    if ras == "":
                        print("*"*50)
                        print("Du måste skriva en ras.")
                        print("*"*50)
                    else:
                        break

                while True:
                    vikt = input("Ange " + namn.title() + "s" + " vikt: ")
                    if not vikt.strip().isdigit():
                        print("*"*50)
                        print("Inga mellanslag eller bokstäver, endast siffor")
                        print("*"*50)
                    else:
                        break

                djurpensionat.append(hund(namn, ras, vikt))


    elif meny == "2":
        pass


    elif meny == "3":
        pass
   
    
    elif meny == "4":
        pass
      

    elif meny == "5":
        pass


    elif meny == "0":
        print("Du har valt att avsluta programmet!")
        quit

    else:
        print("Det måste vara med en siffra...")

        #hej