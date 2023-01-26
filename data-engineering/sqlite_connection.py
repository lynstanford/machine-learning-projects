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

# Insert one record into the table

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
print("Command executed successfully...")

# commit our connection command
conn.commit()

# close our connection
conn.close()

# save this file and run it in the bash

# add another entry to our database:
c.execute("INSERT INTO customers VALUES ('Tim', 'Smith', 'tim@codemy.com')")
# commit our connection command
conn.commit()
# close our connection
conn.close()

# insert many records into the table
many_customers = [
                    ('Wes','Brown','wes@brown.com'),
                    ('Steph','Kuewa','steph@kuewa.com'),
                    ('Dan','Pas','dan@pas.com')
                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# commit our connection command
conn.commit()
# close our connection
conn.close()

# Query and Fetchall
import sqlite3
# connect to a database
conn = sqlite3.connect('customers.db')
# create a cursor
c = conn.cursor()
# query the database
c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchmany(3))
print(c.fetchall())
# print("Command executed successfully...")
# commit our command
conn.commit()
# close our connection
conn.close()

# Save and Run!

import sqlite3
# connect to a database
conn = sqlite3.connect('customers.db')
# create a cursor
c = conn.cursor()
# query the database
c.execute("SELECT * FROM customers")
print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())
# print("Command executed successfully...")
# commit our command
conn.commit()
# close our connection
conn.close()

# Save and Run!

import sqlite3
# connect to a database
conn = sqlite3.connect('customers.db')
# create a cursor
c = conn.cursor()
# query the database
c.execute("SELECT * FROM customers")
print(c.fetchone()[0])
# print(c.fetchmany(3))
# print(c.fetchall())
# print("Command executed successfully...")
# commit our command
conn.commit()
# close our connection
conn.close()

# Save and Run!

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

# Save and Run!
# Alternatively, you could create a loop:

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
for item in items:
    print(item)
# print("Command executed successfully...")
# commit our command
conn.commit()
# close our connection
conn.close()

# Save and Run!
# This should output a Tuple, but the data is slowly becoming more readable now. Suppose we just wanted to print out element zero inside the Tuple.

