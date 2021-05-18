import tkinter as tk
import tkinter.messagebox as msgbox
import pymysql
db = pymysql.connect(host="localhost", user="root", password="", db="filmregister")

class MainWindow:
    """
    En klass för huvudfönstret för Shopen
    """
    def __init__(self, main):
        """
        Konstruktorn för MainWindow
        :param main: Huvudfönstrets root
        """
        self.root = main
        self.root.minsize(width=800, height=500)
        self.var = tk.StringVar()
        self.optTodo = tk.OptionMenu(root, self.var, "Lägg in i databas", "Visa alla i databas", "Sök i databas")
        self.optTodo.pack(anchor=tk.N)
        self.btnUpdate = tk.Button(root, text="Uppdatera", command=self.addFrame)
        self.btnUpdate.pack(anchor=tk.N)
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack()

    def addFrame(self):
        """
        Lägger in en frame i huvudfönstret utifrån var optTodo har för värde
        :return: Void
        """
        self.mainFrame.destroy()
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack(fill=tk.BOTH)

        if self.var.get() == "Lägg in i databas":
            self.addBook(self.mainFrame)
        elif self.var.get() == "Visa alla i databas":
            self.allBooks(self.mainFrame)
        elif self.var.get() == "Sök i databas":
            self.searchBooks(self.mainFrame)

    def addBook(self, frame):
        """
        Fyller huvudframen med rätt objekt för att lägga in en bok
        :param frame: Huvudframen
        :return: Void
        """
        self.lblAuthor = tk.Label(frame, text="Författare:")
        self.lblAuthor.grid(row=0, column=0, sticky="W")

        self.lblTitle = tk.Label(frame, text="Titel:")
        self.lblTitle.grid(row=1, column=0, sticky="W")

        self.lblISBN = tk.Label(frame, text="ISBN:")
        self.lblISBN.grid(row=2, column=0, sticky="W")

        self.lblEdition = tk.Label(frame, text="Edition:")
        self.lblEdition.grid(row=3, column=0, sticky="W")

        self.entAuthor = tk.Entry(frame, width=40)
        self.entAuthor.grid(row=0, column=1)

        self.entTitle = tk.Entry(frame, width=40)
        self.entTitle.grid(row=1, column=1)

        self.entISBN = tk.Entry(frame, width=40)
        self.entISBN.grid(row=2, column=1)

        self.entEdition = tk.Entry(frame, width=40)
        self.entEdition.grid(row=3, column=1)


        btnSave = tk.Button(frame, text="Spara till databasen", command=lambda:
        self.DBConn("INSERT INTO books (author, title, isbn, edition) VALUES ('{}', '{}', '{}', {})".format(self.entAuthor.get(), self.entTitle.get(), self.entISBN.get(), self.entEdition.get())))

        btnSave.grid(row=4, column=0, columnspan=2)

    def DBConn(self, sql):
        """
        En metod för att hantera SQL-kommandon till databasen 'shop'

        :param sql: SQL-sträng
        :return: Resultat av SQL-instruktionen
        """
        db = pymysql.connect(host="localhost", user="root", password="", db="shop")
        results = list()

        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                db.commit()
                msgbox.showinfo("Klar","Klar")

        except:
            db.rollback()
            msgbox.showinfo("Fel", "Fel vid hantering med databasen")

        return results

    def allBooks(self, frame):
        '''
        Fyller huvudframen med rätt objekt för att visa alla böcker
        :param frame: Huvudframen
        :return: Void
        '''
        results = self.DBConn("SELECT * FROM books")

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        booklist = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        for bok in results:
            booklist.insert(tk.END, "Författare: {}\n".format(bok[0]))
            booklist.insert(tk.END, "Title: {}\n".format(bok[1]))
            booklist.insert(tk.END, "ISBN: {}\n".format(bok[2]))
            booklist.insert(tk.END, "Edition: {}\n".format(bok[3]))
            booklist.insert(tk.END, "\n")

        booklist.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        scrollbar.config(command=booklist.yview)



    def searchBooks(self, frame):
        '''
        Fyller huvudframen med rätt objekt för att söka efter en bok
        :param frame: Huvudframen
        :return: Void
        '''
        self.lblSearch = tk.Label(frame, text="Författare: ")
        self.lblSearch.grid(row=0, column=0)

        self.entSearch = tk.Entry(frame, width=30)
        self.entSearch.grid(row=0, column=1)

        self.btnSearch = tk.Button(frame, text="Sök", command=lambda: self.__search(frame))
        self.btnSearch.grid(row=0, column=2)

    def __search(self, frame):
        '''
        Privat metod för att söka och fylla i huvudframen med resultatet av sökningen
        :param frame: Huvudframen
        :return: Void
        '''
        sql = "SELECT * FROM books WHERE author = '{}'".format(self.entSearch.get())

        insideFrame = tk.Frame(frame)
        insideFrame.grid(row=1, column=0, columnspan=3)

        results = self.DBConn(sql)

        scrollbar = tk.Scrollbar(insideFrame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        booklist = tk.Listbox(insideFrame, yscrollcommand=scrollbar.set)
        for bok in results:
            booklist.insert(tk.END, "Författare: {}\n".format(bok[0]))
            booklist.insert(tk.END, "Title: {}\n".format(bok[1]))
            booklist.insert(tk.END, "ISBN: {}\n".format(bok[2]))
            booklist.insert(tk.END, "Edition: {}\n".format(bok[3]))
            booklist.insert(tk.END, "\n")

        booklist.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        scrollbar.config(command=booklist.yview)

if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()