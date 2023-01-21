import sqlite3

# connect to a database
conn = sqlite3.connect('customers.db')

# create a cursor
c = conn.cursor()

# create a Table
c.execute("""CREATE TABLE customers(
        first_name DATATYPE,
        last_name DATATYPE,
        email DATATYPE
)""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

