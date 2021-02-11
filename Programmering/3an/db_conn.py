import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="shop")

while True:
    print("1. Lägg till en bok")
    print("2. Visa alla böcker")
    print("3. Sök efter en bok")
    print("0. Avsluta")

    val = input(": ")

    if val == "1":
        author = input("Författare: ")
        title = input("Titel: ")
        isbn = input("Isbn: ")
        edition = input("Utgåva (nr): ")

        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO books(author, title, isbn, edition) VALUES ('{}', '{}', '{}', {})" \
                .format(author, title, isbn, edition)

                cursor.execute(sql)

                db.commit()

        except Exception as e:
            print(str(e))
            db.rollback()

        else:
            print("Boken är tillagd!")


    elif val == "2":
        sql = "SELECT * FROM books"

        cursor = db.cursor()

        cursor.execute(sql)

        result = cursor.fetchall()

        for bok in result:
            print(bok[0].ljust(42), bok[1].ljust(32), bok[2].ljust(22), bok[3])

        print()

    elif val == "3":
        title = input("Vilken bok söker du?: ")

        sql = "SELECT * FROM books WHERE title = '{}'".format(title)

        cursor = db.cursor()

        cursor.execute(sql)

        result = cursor.fetchall()

        if len(result) == 0:
            print("Det finns ingen bok med detta namn.")

        else:
            for bok in result:
                print(bok[0].ljust(42), bok[1].ljust(32), bok[2].ljust(22), bok[3])

        print()

    elif val == "0":
        break

    else:
        Print("NEJ")