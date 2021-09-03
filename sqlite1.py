
import sqlite3
connection = sqlite3.connect("C:/Users/jesse/OneDrive/Documents/GitHub/Python-Projects/test_database.db")
with connection:
    # Instantiates a cursor object 
    c = connection.cursor
    # Creates new table named People and adds Fname, Lname, and Age columns
    c.execute("CREATE TABLE if not exists People(FirstName TEXT, \
        LastName TEXT, \
        Age INT)")
    c.execute("INSERT INTO People VALUES('Ron', 'Obvious', '42')")
    connection.commit()
    connection.close()

                             
