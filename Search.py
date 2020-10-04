from databasesrc import *
from tkinter import *


# Function to pop up Search window
def Search():
    search = tkinter.Tk()
    search.title("Search")
    sql_connection()
    search.mainloop()