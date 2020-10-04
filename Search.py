from databasesrc import *
import tkinter
from GUI import *

# Function to pop up Search window
def Search():
    top.destroy()
    search = tkinter.Tk()
    search.title("Search")
    sql_connection()
    search.mainloop()