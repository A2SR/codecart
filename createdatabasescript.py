import sqlite3
from sqlite3 import Error

# Change the following 
# Database = "New database name"
database = "database name"

# Function to set up database connection of items
def sql_connection():

    try:

        con = sqlite3.connect("contents.db")

        return con

    except Error:

        print(Error)

# Function to create new database for training
def sql_connectionnew():

    try:

        connew = sqlite3.connect(database)

        return connew

    except Error:

        print(Error)


# Function to create Table in database
def sql_table(connew):

    cursorObj = connew.cursor()

    cursorObj.execute("CREATE TABLE contents(StepNumber integer PRIMARY KEY, name text, barcode integer)")

    connew.commit()