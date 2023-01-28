# to work with sqlite we need to import sqlite3 from standard library
import sqlite3

# If we don't have a db this will create one. If we do, this will just connect to the db.
db = sqlite3.connect('books.db')

cur = db.cursor()

# placing more than one entry into our database
book_list = [('2', 'Lucky Jim', 'Kingsley Amis', '4.99'),
             ('3', 'Animal Farm', 'George Orwell', '7.49'),
             ('4', 'Why I Am So Clever', 'Friedrich Nietzsch', '10.99'),
             ('5', 'Life 3.0: Being Human in the Age of Artificial Intelligence', 'Max Tegmark', '20.00')
            ]

cur.execute('SELECT * FROM books')
print(cur.fetchall())

db.commit()
db.close()