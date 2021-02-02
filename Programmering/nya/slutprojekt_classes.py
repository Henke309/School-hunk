from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbox
import pickle

def mainmenu():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐌 𝐞𝐧𝐲𝐧".center(50))
    print("1.Lägga till en film")
    print("2.Markera sedda filmer")
    print("3.Se alla filmer i listan")
    print("4.Ta bort en film från listan")
    print("0.Quit")
    print("⇦"*50)
    print("")

def listintro():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐅𝐢𝐥𝐦 𝐥𝐢𝐬𝐭𝐚𝐧".center(50))
    print("⇨"*50)
    print("1.Se alla filmer från A-Ö")
    print("2.Se alla filmer från Ö-A")
    print("3.Äldsta film till nyaste")
    print("4.Nyaste film till äldsta")
    print("5.Sök efter en film")
    print("0.Quit")
    print("⇦"*50)
    print("")

def intro3():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐌 𝐚𝐫𝐤𝐞𝐫𝐚 𝐬𝐞𝐝𝐝𝐚 𝐟𝐢𝐥𝐦 𝐞𝐫".center(50))
    print("Här kan du markera de filmer du har sett.")
    print("Varje film har ett eget nummer\nFör att markera att du har sett en film så skriver\ndu in filmens nummer")
    print("Skriv 'help' för att se ett exempel")
    print("Skriv 'stop' för att komma tillbaka till menyn igen.")
    print("⇦"*50)
    print("")

def intro4():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐒ö𝐤𝐟ä𝐥𝐭".center(50))
    print("Här kan du söka efter filmer (T.ex Titanic)")
    print("Om du vill gå ur detta sökfält, skriv 'stop' ")
    print("⇦"*50)
    print("")

def intro5():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐋𝙖̈𝐠𝐠 𝐭𝐢𝐥𝐥 𝐟𝐢𝐥𝐦 𝐞𝐫".center(50))
    print("skriv 'stop' för att komma tillbaka till menyn")
    print("⇦"*50)
    print("")

def intro6():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐋𝙖̈𝐠𝐠 𝐭𝐢𝐥𝐥 𝐟𝐢𝐥𝐦 𝐞𝐫".center(50))
    print("skriv 'stop' för att komma tillbaka till menyn")
    print("Är det flera genrar skriv ',' t.ex (action, drama, fantasy)")
    print("⇦"*50)
    print("")

def intro7():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐋𝙖̈𝐠𝐠 𝐭𝐢𝐥𝐥 𝐟𝐢𝐥𝐦 𝐞𝐫".center(50))
    print("skriv 'stop' för att komma tillbaka till menyn")
    print("Skriv med siffror, inga mellanslag, t.ex (2019)")
    print("⇦"*50)
    print("")
    
def remove():
    print("")
    print("⇨"*50)
    print("𝐅𝐢𝐥𝐦 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫".center(50))
    print("𝐓𝐚 𝐛𝐨𝐫𝐭 𝐞𝐧 𝐟𝐢𝐥𝐦".center(50))
    print("Här kan du ta bort en film från listan.")
    print("Varje film har ett eget nummer\nDet enda du behöver göra är skriva filmens egna nummer\nOch sedan måste du bara bekräfta borttagningen.")
    print("Skriv 'hjälp' för att se ett exempel")
    print("Skriv 'stop' för att komma tillbaka till menyn igen.")
    print("")
    print("⇦"*50)
    print("")

def vidare():
    input("Tryck på enter för att gå vidare.")

def help1():
    print("")
    print("𝐄𝐱𝐞𝐦 𝐩𝐞𝐥")
    print("-"*50)
    print("6 The Lord of the Rings: The Two Towers") 
    print(" Status: Ej Sett")
    print("")
    print("Så här ser det ut men det finns fler filmer")
    print("-"*50)

    input("Tryck på Enter knappen för att fortsätta: ")
    print("")
    
    print("-"*50)
    print("6<-- The Lord of the Rings: The Two Towers") 
    print(" Status: Ej Sett")
    print("")
    print("'6' sexan som du ser är filmens egna nummer.\nDet är den siffran du ska ange för att markera att du har sett filmen.")
    print("-"*50)

    input("Tryck på Enter knappen för att fortsätta: ")
    print("")

    print("-"*50)
    print("Steg 2:")
    print("6 The Lord of the Rings: The Two Towers") 
    print(" Status: Ej Sett")
    print("Vilken film sett: 6 *Enter*")
    print("-"*50)

    input("Tryck på Enter knappen för att fortsätta: ")
    print("")

    print("-"*50)
    print("Resultatet:")
    print("6 The Lord of the Rings: The Two Towers") 
    print(" Status: Har Sett")
    print("Vilken film sett:")
    input("Tryck på Enter knappen för att fortsätta: ")
    print("")

def help2():
    print("")
    print("𝐄𝐱𝐞𝐦 𝐩𝐞𝐥")
    print("-"*50)
    print("6 The Lord of the Rings: The Two Towers") 
    print("")
    print("Så här ser det ut men det finns fler filmer")
    print("-"*50)

    input("Tryck på Enter knappen för att fortsätta: ")
    print("")
    
    print("-"*50)
    print("6<-- The Lord of the Rings: The Two Towers") 
    print("")
    print("'6' sexan som du ser är filmens egna nummer.\nDet är den siffran du ska ange för att kunna ta\nbort filmen från listan.")
    print("-"*50)

    input("Tryck på Enter knappen för att fortsätta: ")
    print("")

    print("-"*50)
    print("Steg 2:")
    print("Du skriver in filmens egna nummer. Se nedan")
    print("")
    print("6 The Lord of the Rings: The Two Towers") 
    print("Vilken film vill du ta bort?\nAnge filmens egna nummer: 6 *Enter*")
    print("-"*50)

    input("Tryck på Enter knappen för att fortsätta: ")
    print("")

    print("-"*50)
    print("Resultatet:")
    print("6 The Lord of the Rings: The Two Towers") 
    print("Borttagen!")
    input("Tryck på Enter knappen för att fortsätta: ")
    print("")
    
def saveToFile(self):
    file = open("filmregister.txt", "a")

    file.write(self.entName.get() + "\n" + self.entTele.get() + "\n\n")

    file.close()

    self.entName.delete(0, END)
    self.entTele.delete(0, END)

    msgbox.showinfo("", "Sparad!")


class Movie:
    '''
    Movie är en klass xD
    title, release och genre har egenskaper
    '''
    def __init__(self,title,release,genre):
        self.title = title
        self.release = release
        self.genre = genre
        self.seen = False
     
    

def Movielist():
    '''
    Denna metod innehåller hela filmregistret, det är här alla filmer är.
    Movielist innehåller objekt från klassen Movie
    '''
    Movielist = []

    Movielist.append(Movie("The Lord of the Rings: The Fellowship of the Ring", "2001", "Adventure, Drama, Fantasy"))
    Movielist.append(Movie("The Lord of the Rings: The Two Towers", "2002", "Adventure, Drama, Fantasy"))
    Movielist.append(Movie("The Lord of the Rings: The Return of the King", "2003", "Adventure, Drama, Fantasy"))
    Movielist.append(Movie("The Hobbit: An Unexpected Journey", "2012", "Adventure, Family, Fantasy"))
    Movielist.append(Movie("The Hobbit: The Desolation of Smaug", "2013", "Adventure, Fantasy"))
    Movielist.append(Movie("The Hobbit: The Battle of the Five Armies", "2014", "Adventure, Fantasy"))

    Movielist.append(Movie("Pirates of the Caribbean: The Curse of the Black Pearl", "2003", " Action, Adventure, Fantasy"))
    Movielist.append(Movie("Pirates of the Caribbean: Dead Man's Chest", "2006", " Action, Adventure, Fantasy"))
    Movielist.append(Movie("Pirates of the Caribbean: At World's End", "2007", " Action, Adventure, Fantasy"))
    Movielist.append(Movie("Pirates of the Caribbean: Dead Men Tell No Tales", "2017", " Action, Adventure, Fantasy"))

    Movielist.append(Movie("The Terminator", "1985", "Action, Sci-Fi "))
    Movielist.append(Movie("Terminator 2: Judgment Day", "1991", "Action, Sci-Fi "))
    Movielist.append(Movie("Terminator 3: Rise of the Machines", "2003", "Action, Sci-Fi "))
    Movielist.append(Movie("Terminator Salvation", "2009", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Terminator Genisys", "2015", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Terminator: Dark Fate", "2019", "Action, Adventure, Sci-Fi"))

    Movielist.append(Movie("Batman", "1989", "Action, Adventure"))
    Movielist.append(Movie("Batman Returns", "1992", "Action, Crime, Fantasy"))
    Movielist.append(Movie("Batman Forever", "1995", "Action, Adventure, Fantasy"))
    Movielist.append(Movie("Batman & Robin", "1997", "Action, Sci-Fi"))
    Movielist.append(Movie("Batman Begins", "2005", "Action, Adventure"))
    Movielist.append(Movie("The Dark Knight", "2005", "Action, Crime, Drama"))
    Movielist.append(Movie("The Dark Knight Rises", "2012", "Action, Adventure"))
    
    Movielist.append(Movie("Titanic", "2012", "Drama, Romance"))
    
    Movielist.append(Movie("Avatar", "2009", "Action, Adventure, Fantasy"))

    Movielist.append(Movie("Captain America: The First Avenger", "2011", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Iron Man", "2008", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("The Incredible Hulk", "2008", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Iron Man 2", "2010", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Thor", "2011", "Action, Adventure, Fantasy"))
    Movielist.append(Movie("Avengers", "2012", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Iron Man 3", "2013", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Thor: The Dark World", "2013", "Action, Adventure, Fantasy"))
    Movielist.append(Movie("Captain America: The Return of the First Avenger", "2014", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Guardians of the Galaxy", "2014", "Action, Adventure, Comedy"))
    Movielist.append(Movie("Guardians of the Galaxy Vol. 2", "2017", "Action, Adventure, Comedy"))
    Movielist.append(Movie("Avengers: Age of Ultron", "2015", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Ant-Man", "2015", "Action, Adventure, Comedy"))
    Movielist.append(Movie("Captain America: Civil War", "2016", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Spider-Man: Homecoming", "2017", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Doctor Strange", "2016", "Action, Adventure, Fantasy"))
    Movielist.append(Movie("Thor: Ragnarök", "2017", "Action, Adventure, Comedy"))
    Movielist.append(Movie("Black Panther", "2018", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Avengers: Infinity War", "2018", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Ant-Man and the Wasp", "2018", "Action, Adventure, Comedy"))
    Movielist.append(Movie("Captain Marvel", "2018", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Avengers: Endgame", "2019", "Action, Adventure, Sci-Fi"))
    Movielist.append(Movie("Spider-Man: Far From Home", "2019", "Action, Adventure, Sci-Fi"))

    Movielist.append(Movie("Venom", "2018", "Action, Sci-Fi, Thriller"))
    Movielist.append(Movie("Venom: Let There Be Carnage", "2021", "Action, Comedy, Horror"))
    Movielist.append(Movie("Deadpool", "2016", "Action, Adventure, Comedy"))
    Movielist.append(Movie("Deadpool 2", "2018", "Action, Adventure, Comedy"))

    pickle.dump(Movielist, open("Movies.p", "wb"))
Movielist()    
    
'''
    Movielist.append(Movie("", "", ""))
'''
