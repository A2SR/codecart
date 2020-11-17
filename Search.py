from databasesrc import *
from tkinter import *
from tkinter.ttk import Treeview

# Function to pop up Search window
def Search():
    search = Tk()
    search.title("Search")
    frame_search = Frame(search)
    frame_search.grid(row=0, column=0)
    lbl_search = Label(frame_search, text='Search by hostname',font=('bold', 12), pady=20)
    lbl_search.grid(row=0, column=0, sticky=W)
    hostname_search = StringVar()
    ostname_search_entry = Entry(frame_search, textvariable=hostname_search)
    hostname_search_entry.grid(row=0, column=1)
    lbl_search = Label(frame_search, text='Search by Query',font=('bold', 12), pady=20)
    lbl_search.grid(row=1, column=0, sticky=W)
    query_search = StringVar()
    query_search.set("Select * from routers where ram>1024")
    query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
    query_search_entry.grid(row=1, column=1)

    frame_router = Frame(search)
    frame_router.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)
    
    columns = ['id', 'Hostname', 'Brand', 'Ram', 'Flash']
    router_tree_view = Treeview(frame_router, columns=columns, show="headings")
    router_tree_view.column("id", width=30)
    for col in columns[1:]:
        router_tree_view.column(col, width=120)
        router_tree_view.heading(col, text=col)
    router_tree_view.bind('<<TreeviewSelect>>', select_router)
    router_tree_view.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame_router, orient='vertical')
    scrollbar.configure(command=router_tree_view.yview)
    scrollbar.pack(side="right", fill="y")
    router_tree_view.config(yscrollcommand=scrollbar.set)

    frame_btns = Frame(search)
    frame_btns.grid(row=3, column=0)

    add_btn = Button(frame_btns, text='Add Router', width=12, command=add_router)
    add_btn.grid(row=0, column=0, pady=20)

    remove_btn = Button(frame_btns, text='Remove Router',
                    width=12, command=remove_router)
    remove_btn.grid(row=0, column=1)

    update_btn = Button(frame_btns, text='Update Router',
                    width=12, command=update_router)
    update_btn.grid(row=0, column=2)

    clear_btn = Button(frame_btns, text='Clear Input',
                   width=12, command=clear_text)
    clear_btn.grid(row=0, column=3)

    search_btn = Button(frame_search, text='Search',
                    width=12, command=search_hostname)
    search_btn.grid(row=0, column=2)

    search_query_btn = Button(frame_search, text='Search Query',
                          width=12, command=execute_query)
    search_query_btn.grid(row=1, column=2)
    
    search.title('Router Manager')
    search.geometry('700x550')

    # Populate data
    populate_list()

    # Start program
    search.mainloop()

def populate_list(hostname=''):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch(hostname):
        router_tree_view.insert('', 'end', values=row)

def populate_list2(query='select * from routers'):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch2(query):
        router_tree_view.insert('', 'end', values=row)

def add_router():
    if brand_text.get() == '' or hostname_text.get() == '' or ram_text.get() == '' or flash_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(hostname_text.get(), brand_text.get(),
              ram_text.get(), flash_text.get())
    clear_text()
    populate_list()


def select_router(event):
    try:
        global selected_item
        index = router_tree_view.selection()[0]
        selected_item = router_tree_view.item(index)['values']
        hostname_entry.delete(0, END)
        hostname_entry.insert(END, selected_item[1])
        brand_entry.delete(0, END)
        brand_entry.insert(END, selected_item[2])
        ram_entry.delete(0, END)
        ram_entry.insert(END, selected_item[3])
        flash_entry.delete(0, END)
        flash_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_router():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_router():
    db.update(selected_item[0], hostname_text.get(), brand_text.get(),
              ram_text.get(), flash_text.get())
    populate_list()

def clear_text():
    brand_entry.delete(0, END)
    hostname_entry.delete(0, END)
    ram_entry.delete(0, END)
    flash_entry.delete(0, END)

def search_hostname():
    hostname = hostname_search.get()
    populate_list(hostname)


def execute_query():
    query = query_search.get()
    populate_list2(query)