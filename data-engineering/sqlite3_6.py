# to work with sqlite we need to import sqlite3 from standard library
import sqlite3

# If we don't have a db this will create one. If we do, this will just connect to the db.
db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('SELECT * FROM books WHERE price > 10')

print('**********')
for x in cur.fetchall():
    print(x)
    
db.commit()
db.close()