# to work with sqlite we need to import sqlite3 from standard library
import sqlite3

# If we don't have a db this will create one. If we do, this will just connect to the db.
db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('''INSERT INTO books(id, title, author, price)
    VALUES('1','Untold Stories','Alan Bennett','17.49');''')

db.commit()
db.close()