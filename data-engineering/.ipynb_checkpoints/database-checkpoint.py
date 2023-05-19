import sqlite3

# connect to a database
conn = sqlite3.connect('customers.db')

# create a cursor
c = conn.cursor()

# query the database
c.execute("SELECT * FROM customers")
# print(c.fetchone()[0])
# print(c.fetchmany(3))

items = c.fetchall()
print(items)

# print("Command executed successfully...")

# commit our command
conn.commit()

# close our connection
conn.close()