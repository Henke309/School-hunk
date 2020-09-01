def menyuno():
    print("Meny")
    print("1. Filmer")
    print("2. lägg till filmer")
    print("3. ta bort filmer")
    print("4. Skriv en review")

class film:

    def __init__(self,title,release,genre):
        self.title = title
        self.release = release
        self.genre = genre

def filmer():

    filmer = []
    
    filmer.append(film("The Lord of the Rings: The Fellowship of the Ring", "2001", "Adventure, Drama, Fantasy"))
    filmer.append(film("The Lord of the Rings: The Two Towers", "2002", "Adventure, Drama, Fantasy"))
    filmer.append(film("The Lord of the Rings: The Return of the King", "2003", "Adventure, Drama, Fantasy"))
    filmer.append(film("The Hobbit: An Unexpected Journey", "2012", "Adventure, Family, Fantasy"))
    filmer.append(film("The Hobbit: The Desolation of Smaug", "2013", "Adventure, Fantasy"))
    filmer.append(film("The Hobbit: The Battle of the Five Armies", "2014", "Adventure, Fantasy"))

    filmer.append(film("Pirates of the Caribbean: The Curse of the Black Pearl", "2003", " Action, Adventure, Fantasy"))
    filmer.append(film("Pirates of the Caribbean: Dead Man's Chest", "2006", " Action, Adventure, Fantasy"))
    filmer.append(film("Pirates of the Caribbean: At World's End", "2007", " Action, Adventure, Fantasy"))
    filmer.append(film("Pirates of the Caribbean: Dead Men Tell No Tales", "2017", " Action, Adventure, Fantasy"))

    filmer.append(film("The Terminator", "1985", "Action, Sci-Fi "))
    filmer.append(film("Terminator 2: Judgment Day", "1991", "Action, Sci-Fi "))
    filmer.append(film("Terminator 3: Rise of the Machines", "2003", "Action, Sci-Fi "))
    filmer.append(film("Terminator Salvation", "2009", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Terminator Genisys", "2015", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Terminator: Dark Fate", "2019", "Action, Adventure, Sci-Fi"))

    filmer.append(film("Batman", "1989", "Action, Adventure"))
    filmer.append(film("Batman Returns", "1992", "Action, Crime, Fantasy"))
    filmer.append(film("Batman Forever", "1995", "Action, Adventure, Fantasy"))
    filmer.append(film("Batman & Robin", "1997", "Action, Sci-Fi"))
    filmer.append(film("Batman Begins", "2005", "Action, Adventure"))
    filmer.append(film("The Dark Knight", "2005", "Action, Crime, Drama"))
    filmer.append(film("The Dark Knight Rises", "2012", "Action, Adventure"))
    
    filmer.append(film("Titanic", "2012", "Drama, Romance"))
    
    filmer.append(film("Avatar", "2009", "Action, Adventure, Fantasy"))

    filmer.append(film("Captain America: The First Avenger", "2011", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Iron Man", "2008", "Action, Adventure, Sci-Fi"))
    filmer.append(film("The Incredible Hulk", "2008", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Iron Man 2", "2010", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Thor", "2011", "Action, Adventure, Fantasy"))
    filmer.append(film("Avengers", "2012", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Iron Man 3", "2013", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Thor: The Dark World", "2013", "Action, Adventure, Fantasy"))
    filmer.append(film("Captain America: The Return of the First Avenger", "2014", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Guardians of the Galaxy", "2014", "Action, Adventure, Comedy"))
    filmer.append(film("Guardians of the Galaxy Vol. 2", "2017", "Action, Adventure, Comedy"))
    filmer.append(film("Avengers: Age of Ultron", "2015", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Ant-Man", "2015", "Action, Adventure, Comedy"))
    filmer.append(film("Captain America: Civil War", "2016", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Spider-Man: Homecoming", "2017", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Doctor Strange", "2016", "Action, Adventure, Fantasy"))
    filmer.append(film("Thor: Ragnarök", "2017", "Action, Adventure, Comedy"))
    filmer.append(film("Black Panther", "2018", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Avengers: Infinity War", "2018", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Ant-Man and the Wasp", "2018", "Action, Adventure, Comedy"))
    filmer.append(film("Captain Marvel", "2018", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Avengers: Endgame", "2019", "Action, Adventure, Sci-Fi"))
    filmer.append(film("Spider-Man: Far From Home", "2019", "Action, Adventure, Sci-Fi"))

    filmer.append(film("Venom", "2018", "Action, Sci-Fi, Thriller"))
    filmer.append(film("Venom: Let There Be Carnage", "2021", ""))
    filmer.append(film("Deadpool", "2016", ""))
    filmer.append(film("Deadpool 2", "2018", ""))

    return filmer 