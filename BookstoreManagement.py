import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Parth2004")

# CREATING DATABASE AND TABLE
mycursor = mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username CHAR(5),password VARCHAR(20))")

while True:
    print("1:Signup\n"
          "2:Login")
    ch = int(input("SIGNUP/LOGIN(1,2):"))

    # SIGNUP
    if ch == 1:

        username = input("USERNAME:")
        password = input("PASSWORD:")

        mycursor.execute("insert into signup values('" + username + "','" + password + "')")
        mydb.commit()

    # LOGIN
    elif ch == 2:

        username = input("USERNAME:")

        mycursor.execute("select username from signup where username='" + username + "'")
        a = mycursor.fetchone()

        if a is not None:
            print("\n"
                  "VALID USERNAME\n")

            password = input("PASSWORD:")

            mycursor.execute("select password from signup where password='" + password + "'")
            a = mycursor.fetchone()

            if a is not None:
                print("\n"
                      "                             ACCESS GRANTED   \n")

                print("                       WELCOME TO HIGHTECH BOOKSTORE                              \n")

                mycursor.execute(
                    "create table if not exists Available_Books(BookName varchar(30) primary key,Genre varchar(20),Quantity int(3),Author varchar(20),Publication varchar(30),Price int(4))")
                mycursor.execute(
                    "create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, BookName varchar(30),Quantity int(100),Price int(4),foreign key (BookName) references Available_Books(BookName))")
                mydb.commit()

                while (True):
                    print("1:Add Books\n\n"
                          "2:Sell Books\n\n"
                          "3:Search Books\n\n"
                          "4:Sell Record\n\n"
                          "5:Available Books\n\n"
                          "6:Logout\n")

                    option = int(input("Enter your choice:"))

                    # ADD BOOKS
                    if option == 1:

                        print("All information prompted are mandatory to be filled")

                        book = str(input("Enter Book Name:"))
                        genre = str(input("Genre:"))
                        quantity = int(input("Enter quantity:"))
                        author = str(input("Enter author name:"))
                        publication = str(input("Enter publication house:"))
                        price = int(input("Enter the price:"))

                        mycursor.execute("select * from Available_Books where bookname='" + book + "'")
                        c = mycursor.fetchone()

                        if c is not None:
                            mycursor.execute("update Available_Books set quantity=quantity+'" + str(
                                quantity) + "' where bookname='" + book + "'")
                            mydb.commit()

                            print("\n"
                                  "SUCCESSFULLY ADDED\n")


                        else:
                            mycursor.execute(
                                "insert into Available_Books(bookname,genre,quantity,author,publication,price) values('" + book + "','" + genre + "','" + str(
                                    quantity) + "','" + author + "','" + publication + "','" + str(price) + "')")
                            mydb.commit()

                            print("\n"
                                  "SUCCESSFULLY ADDED\n")


                    # Sell BOOKS
                    elif option == 2:

                        print("AVAILABLE BOOKS...")

                        mycursor.execute("select * from Available_Books ")
                        for d in mycursor:
                            print(d)

                        cusname = str(input("Enter customer name:"))
                        phno = int(input("Enter phone number:"))
                        book = str(input("Enter Book Name:"))
                        price = int(input("Enter the price:"))
                        n = int(input("Enter quantity:"))

                        mycursor.execute("select quantity from available_books where bookname='" + book + "'")
                        e = mycursor.fetchone()

                        if max(e) < n:
                            print(n, "Books are not available")

                        else:
                            mycursor.execute("select bookname from available_books where bookname='" + book + "'")
                            f = mycursor.fetchone()

                            if f is not None:
                                mycursor.execute("insert into Sell_rec values('" + cusname + "','" + str(
                                    phno) + "','" + book + "','" + str(n) + "','" + str(price) + "')")
                                mycursor.execute("update Available_Books set quantity=quantity-'" + str(
                                    n) + "' where BookName='" + book + "'")
                                mydb.commit()

                                print("\n"
                                      "BOOK HAS BEEN SOLD\n")

                            else:
                                print("BOOK IS NOT AVAILABLE")

                    # SEARCH BOOKS ON THE BASIS OF GIVEN OPTIONS
                    elif option == 3:

                        print("1:Search by name\n"
                              "2:Search by genre\n"
                              "3:Search by author\n")

                        choice = int(input("Search by:"))

                        # BY BOOKNAME
                        if choice == 1:
                            selection = input("Enter Book to search:")

                            mycursor.execute("select bookname from available_books where bookname='" + selection + "'")
                            g = mycursor.fetchone()
                            print(" ")

                            if g != None:
                                print("BOOK OF THIS NAME IS IN STOCK\n")

                                mycursor.execute("select * from available_books where bookname='" + selection + "'")
                                for h in mycursor:
                                    print(h)
                                    print(" ")

                            else:
                                print("BOOK OF THIS NAME IS NOT IN STOCK")

                        # BY GENRE
                        elif choice == 2:
                            selection_1 = input("Enter genre to search:")

                            mycursor.execute("select genre from available_books where genre='" + selection_1 + "'")
                            i = mycursor.fetchall()
                            print(" ")

                            if i != None:
                                print("BOOK IS IN STOCK\n")

                                mycursor.execute("select * from available_books where genre='" + selection_1 + "'")
                                for j in mycursor:
                                    print(j)
                                    print(" ")

                            else:
                                print("BOOK OF SUCH GENRE IS NOT AVAILABLE")


                        # BY AUTHOR NAME
                        elif choice == 3:
                            selection_2 = input("Enter author to search:")

                            mycursor.execute("select author from available_books where author='" + selection_2 + "'")
                            k = mycursor.fetchall()
                            print(" ")

                            if k != None:
                                print("BOOK IS IN STOCK\n")

                                mycursor.execute("select * from available_books where author='" + selection_2 + "'")
                                for l in mycursor:
                                    print(l)
                                    print(" ")

                            else:
                                print("BOOK OF THIS AUTHOR IS NOT AVAILABLE")
                        mydb.commit()
                    # SELL HISTORY
                    elif option == 4:
                        print(" ")
                        print("1:Sell history details")
                        print("2:Reset Sell history")

                        choice_1 = int(input("\n"
                                             "Enter your choice:"))

                        if choice_1 == 1:
                            mycursor.execute("select * from sell_rec")
                            for m in mycursor:
                                print(m)

                        if choice_1 == 2:
                            yes_or_no = input("Are you sure(y/n):")

                            if yes_or_no == "y":
                                mycursor.execute("delete from sell_rec")
                                mydb.commit()

                            elif yes_or_no == "n":
                                pass

                    # AVAILABLE BOOKS
                    elif option == 5:
                        mycursor.execute("select * from available_books order by bookname")
                        for n in mycursor:
                            print(n)

                    # Logout
                    elif option == 6:
                        break

            # LOGIN ELSE PART
            else:
                print("\n"
                      "PLEASE! TRY AGAIN \n")


        else:
            print("\n"
                  "INVALID USERNAME\n")
    else:
        break