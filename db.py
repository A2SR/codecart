import sqlite3

class Database:
    
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contents (id INTEGER PRIMARY KEY, name text, barode text)")
        self.conn.commit

    
    def fetch(self, itemname):
        self.cur.execute("SELECT * FROM contents WHERE name LIKE ?", ('%'+itemname+'%',))
        rows = self.cur.fetchall()
        return rows

    
    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    
    def insert(self, itemname, barcode):
        self.cur.execute("INSERT INTO contents VALUES (NULL, ?, ?)", (itemname, barcode))
        self.conn.commit

    
    def remove(self, id):
        self.cur.execute("DELETE FROM contents WHERE id = ?", (id,))
        self.conn.commit

    
    def update(self, id, itemname, barcode):
        self.cur.execute("UPDATE contents SET name = ?, barcode = ? WHERE id = ?", (itemname, barcode))
        self.conn.commit

    
    def __del__(self):
        self.conn.close


    
