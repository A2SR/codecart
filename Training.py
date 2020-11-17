from databasesrc import *
from tkinter import *

## Function to pop up Training Window of GUI 
def Training():
    training = Tk()
    training.title("Training")
    sql_connection()
    training.mainloop()
