from filmrep_shiet import menyuno
from filmrep_shiet import filmer
from filmrep_shiet import film


print("*"*50)
print("Filmregister".center(50))
print("*"*50)

Filmlist = filmer()

while True:
    menyuno() 
    val = input("hej välj nått bror: ") 


    if val == "1":
        Filmlist = sorted(Filmlist, key=lambda k: k.title, reverse=True)
        return Filmlist

        for filmer1 in Filmlist:
            print("-"*50, "\nTitel:", filmer1.title.title(),"\n""År:", filmer1.release,"\n""Genre:", filmer1.genre.capitalize(), "\n")


    elif val == "2":
        title = input("Fyll i filmens title här: "):
        if title == "":
            print("Skriv nått då... stupid....")

        elif not title.strip():
            print("Inga mellanslag ba bror...")



    elif val == "3":
        pass

    elif val == "4":   
        pass

    else:
        print("helllo")

