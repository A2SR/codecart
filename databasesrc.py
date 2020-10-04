import sqlite3
from sqlite3 import Error

# Function to set up database connection
def sql_connection():

    try:

        con = sqlite3.connect('contents.db')

        return con

    except Error:

        print(Error)

# Function to create Table in database
def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE contents(barcode integer PRIMARY KEY, name text)")

    con.commit()

con = sql_connection()