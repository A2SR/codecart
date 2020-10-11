import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from db import *



# Function to set up database connection
""" def sql_connection():

    try:

        con = sqlite3.connect('contents.db')

        return con

    except Error:

        print(Error) """

# Function to create Table in database
""" def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE contents(barcode integer PRIMARY KEY, name text)")

    con.commit()

con = sql_connection()
 """
# sql_table(con)

## Function to pop up Training Window of GUI 
def Training():
    top.destroy()
    training = Tk()
    training.title("Training")
    training.mainloop()

def Search():
    top.destroy()
    search = Tk()
    #search.title("Search")
    frame_search = Frame(search)
    frame_search.grid(row = 0, column = 0)

    lbl_search = Label(frame_search, text = 'Search by Item Name', font = ('bold', 12), pady = 20)
    lbl_search.grid(row = 0, column = 0, sticky = W)
    itemname_search = StringVar()
    itemname_search_entry = Entry(frame_search, textvariable = itemname_search)
    itemname_search_entry.grid(row = 0, column = 1)

    lbl_search = Label(frame_search, text = 'Search by Query', font =('bold', 12), pady = 20)
    lbl_search.grid(row = 1, column = 0, sticky = W)
    query_search = StringVar()
    query_search.set("Select * from contents where barcode>1")
    query_search.entry = Entry(frame_search, textvariable = query_search, width = 40)
    query_search.entry.grid(row = 1, column = 1)

    
    
    frame_fields = Frame(search)
    frame_fields.grid(row = 1, column = 0)

    #name
    itemname_text = StringVar()
    itemname_label = Label(frame_fields, text = 'name', font = ('bold', 12))
    itemname_label.grid(row = 0, column = 0, sticky = E)
    itemname_entry = Entry(frame_fields, textvariable = itemname_text)
    itemname_entry.grid(row = 0, column = 1, sticky = W)

    #barcode
    barcode_text = StringVar()
    barcode_label = Label(frame_fields, text = 'barcode', font = ('bold', 12))
    barcode_label.grid(row = 0, column = 2, sticky = E)
    barcode_entry = Entry(frame_fields, textvariable = barcode_text)
    barcode_entry.grid(row = 0, column = 3, sticky = W)


    frame_contents = Frame(search)
    frame_contents.grid(row = 2, column = 0, columnspan = 4, rowspan = 6, pady = 20, padx = 20)

    columns = ["id", "name", "barcode"]
    contents_tree_view = Treeview(frame_contents, columns = columns, show = "headings")
    contents_tree_view.column("id", width = 30)
    
    for col in columns[1:]:
        contents_tree_view.column(col, width = 120)
        contents_tree_view.heading(col, text = col)
    
    contents_tree_view.bind('<<TreeviewSelect>>', select_contents)
    contents_tree_view.pack(side = "left", fill = "y")
    scrollbar = Scrollbar(frame_contents, orient = 'vertical')
    scrollbar.configure(command = contents_tree_view.yview)
    scrollbar.pack(side = "right", fill = "y")
    contents_tree_view.config(yscrollcommand = scrollbar.set)



    frame_btns = Frame(search)
    frame_btns.grid(row = 3, column = 0)

    add_btn = Button(frame_btns, text = 'Add Content', width = 12, command = add_contents)
    add_btn.grid(row = 0, column = 0, pady = 20)

    remove_btn = Button(frame_btns, text = 'Remove Content', width = 12, command = remove_contents)
    remove_btn.grid(row = 0, column = 1)

    update_btn = Button(frame_btns, text = 'Update Content', width = 12, command = update_contents)
    update_btn.grid(row = 0, column = 2)

    clear_btn = Button(frame_btns, text = 'Clear Input', width = 12, command = clear_text)
    clear_btn.grid(row = 0, column = 3)

    search_btn = Button(frame_btns, text = 'Search', width = 12, command = search_itemname)
    search_btn.grid(row = 0, column = 2)

    search_query_btn = Button(frame_btns, text = 'Search Query', width = 12, command = execute_query)
    search_query_btn.grid(row = 1, column = 2)



    def populate_list(itemname = ''):
       
        for i in contents_tree_view.get_children():
            contents_tree_view.delete(i)

        for row in Database.fetch(itemname):
            contents_tree_view.insert('', 'end', values = row)

    
    def populate_list2(query = 'select * from contents'):
        
        for i in contents_tree_view.get_children():
            contents_tree_view.delete(i)

        for row in Database.fetch2(query):
            contents_tree_view.insert('', 'end', values = row)

    
    def add_contents():
        
        if itemname_text.get() == '' or barcode_text.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
            return

        Database.insert(itemname_text.get(), barcode_text.get())
        clear_text()
        populate_list()


    def select_contents(event):
        
        try:
            global selected_item
            index = contents_tree_view.selection()[0]
            selected_item = contents_tree_view.item(index)['values']
            itemname_entry.delete(0, END)
            itemname_entry.insert(END, selected_item[1])
            barcode_entry.delete(0, END)
            barcode_entry.insert(END, selected_item[2])
        except IndexError:
            pass


    def remove_contents():
        Database.remove(selected_item[0])
        clear_text()
        populate_list()

    
    def update_contents():
        Database.update(selected_item[0], itemname_text.get(), barcode_text.get())
        populate_list()


    def clear_text():
        itemname_entry.delete(0, END)
        barcode_entry.delete(0, END)

    
    def search_itemname():
        itemname = itemname_search.get()
        populate_list(itemname)

    
    def execute_query():
        query = query_search.get()
        populate_list2()



        



    




# Main window of GUI
top = Tk()
top.geometry("200x200")
tb = Button(top, text = "Training!", command = Training, width=25, height=5, bg="Blue", fg="red")
sb = Button(top, text = "Search!", command = Search, width=25, height=5, bg="red", fg="blue")
tb.pack()
sb.pack()
top.mainloop()
