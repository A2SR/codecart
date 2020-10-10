import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter.ttk import Treeview
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
    training = Tk()
    training.title("Training")
    sql_connection()
    training.mainloop()

def Search():
    top.destroy()
    search = Tk()
    search.title("Search")
    frame_search = Frame(search)
    frame_search.grid(row = 0, column = 0)

    lbl_search = Label(frame_search, text = 'Search by Item Name', font = ('bold', 12), pady = 20)
    lbl_search.grid(row = 0, column = 0, sticky = W)
    itemname_search = StringVar()
    itemname_search_entry = Entry(frame_search, textvariable = itemname_search)
    itemname_search_entry.grid(row = 0, column = 1)

    lbl_search = Label(frame_search, text = 'Search by Query', font =('bold', 12), pady = 20)
    lbl_search.grid(row = 1, column = 0, sticky=W)
    query_search = StringVar()
    query_search.set("Select * from contents where barcode>1")
    query_search.entry = Entry(frame_search, textvariable = query_search, width = 40)
    query_search.entry.grid(row = 1, column = 1)






# Main window of GUI
top = tkinter.Tk()
top.geometry("200x200")
tb = tkinter.Button(top, text = "Training!", command = Training, width=25, height=5, bg="Blue", fg="red")
sb = tkinter.Button(top, text = "Search!", command = Search, width=25, height=5, bg="red", fg="blue")
tb.pack()
sb.pack()
top.mainloop()
