# to work with sqlite we need to import sqlite3 from standard library
import sqlite3

# If we don't have a db this will create one. If we do, this will just connect to the db.
db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    price real);''')

# go to https://sqlitebrowser.org/
# https://docs.python.org/3/library/sqlite3.html

db.commit()
db.close()