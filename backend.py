import sqlite3 

def connect(): 
    conn= sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book ( id INTEGER PRIMARY KEY , title TEXT ,author TEXT ,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn= sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    row=cur.fetchall()
    conn.close()
    return row 

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year =? OR isbn=?",(title,author,year,isbn))
    row=cur.fetchall()
    conn.close()
    return row 


def update(id,title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()



connect()
#insert("guru","deep",1978,23489)
#insert("conservation","jim",1920,15789)
#print search(year="1978")
#update(2,title="god",author="rup",year=1998,isbn=70000)

#insert("fet","rup",1998,34656)
#print view()




#connect()