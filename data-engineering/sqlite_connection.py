import sqlite3

# connect to a database
conn = sqlite3.connect('customers.db')

# create a cursor
c = conn.cursor()

# create a Table
c.execute("""CREATE TABLE customers(
        first_name TEXT,
        last_name TEXT,
        email TEXT
)""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# commit our connection command
conn.commit()

# close our connection
conn.close()

# save this file and run it in the bash
