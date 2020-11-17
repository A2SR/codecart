import sqlite3
import ast
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

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


    def createtrainingtable(self):
        self.cur.execute("DROP TABLE IF EXISTS trainingcopy")
        self.cur.execute("CREATE TABLE trainingcopy AS SELECT * FROM contents")
        self.conn.commit

    def randomitem(self):
        self.cur.execute("SELECT name FROM trainingcopy ORDER BY RANDOM() LIMIT 1")
        row = self.cur.fetchone()
       
        if row is not None:  # or just "if row"
            return row[0]
        else:
            pass # didn't get back a row
    
    def led(self, scannedname):
        self.cur.execute("SELECT location FROM trainingcopy WHERE name = '"+scannedname+"'")
        row = self.cur.fetchall()

        if row is not None: 
    
            location = row[0]

            if location == "('1',)":
                GPIO.output(11, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
            if location == "('2',)":
                GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
            if location == "('3',)":
                GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
            if location == "('4',)":
                GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)

    def checkbarcode(self, scannedname, scannedbarcode):
        self.cur.execute("SELECT barcode FROM trainingcopy WHERE name = '"+scannedname+"'")
        print(scannedname, scannedbarcode)
        row = self.cur.fetchall()
        value = parse_tuple("('%s',)" % scannedbarcode)
        print(value)

        if row is not None:  # or just "if row"
            
            barcode = row[0]
             
            print(barcode)
            
           
            
            if barcode == value:
                self.cur.execute("DELETE FROM trainingcopy WHERE name = '"+scannedname+"'")
                self.conn.commit
                return 1
            else:
                return 0

        else:
            pass # didn't get back a row


    
    def __del__(self):
        self.conn.close

    
    
