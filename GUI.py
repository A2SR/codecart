
import tkinter

from Training import *
from databasesrc import *
from Search import *




con = sql_connection()

# Main window of GUI
top = tkinter.Tk()
top.geometry("200x200")
tb = tkinter.Button(top, text = "Training!", command = Training, width=25, height=5, bg="Blue", fg="red")
sb = tkinter.Button(top, text = "Search!", command = Search, width=25, height=5, bg="red", fg="blue")
tb.pack()
sb.pack()
top.mainloop()
