import sqlite3
from sqlite3 import Error

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

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS routers (id INTEGER PRIMARY KEY, hostname text, brand text, ram integer, flash integer)")
        self.conn.commit()

    def fetch(self, hostname=''):
        self.cur.execute(
            "SELECT * FROM routers WHERE hostname LIKE ?", ('%'+hostname+'%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, hostname, brand, ram, flash):
        self.cur.execute("INSERT INTO routers VALUES (NULL, ?, ?, ?, ?)",
                         (hostname, brand, ram, flash))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM routers WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, hostname, brand, ram, flash):
        self.cur.execute("UPDATE routers SET hostname = ?, brand = ?, ram = ?, flash = ? WHERE id = ?",
                         (hostname, brand, ram, flash, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()