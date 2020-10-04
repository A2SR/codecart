from databasesrc import *
from GUI import *
import tkinter

## Function to pop up Training Window of GUI 
def Training():
    top.destroy()
    training = tkinter.Tk()
    training.title("Training")
    sql_connection()
    training.mainloop()
