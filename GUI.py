import sqlite3
from sqlite3 import Error
import tkinter
from tkinter import messagebox


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

# sql_table(con)

## Function to pop up Training Window of GUI 
def Training():
    top.destroy()
    training = tkinter.Tk()
    training.title("Training")
    sql_connection()
    training.mainloop()

def Search():
    top.destroy()
    search = tkinter.Tk()
    search.title("Search")
    sql_connection()
    search.mainloop()

# Main window of GUI
top = tkinter.Tk()
top.geometry("100x100")
tb = tkinter.Button(top, text = "Training!", command = Training, width=25, height=5, bg="Blue", fg="red")
sb = tkinter.Button(top, text = "Search!", command = Search, width=25, height=5, bg="red", fg="blue")
tb.pack()
sb.pack()
top.mainloop()
