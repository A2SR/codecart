import sqlite3
from sqlite3 import Error
import tkinter
from tkinter import messagebox



def sql_connection():

    try:

        con = sqlite3.connect('contents.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE contents(barcode integer PRIMARY KEY, name text)")

    con.commit()

con = sql_connection()

sql_table(con)


def Training():
    top.destroy()
    training = tkinter.Tk()
    training.title("Training")
    sql_connection()
    training.mainloop()
   
top = tkinter.Tk()
top.geometry("100x100")
tb = tkinter.Button(top, text = "Training!", command = Training, width=25, height=5, bg="Blue", fg="red")
tb.pack()
top.mainloop()