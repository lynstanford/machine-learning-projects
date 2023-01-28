# import the libraries
import sqlite3
import pandas as pd

# create a connection
db = sqlite3.connect('books.db')

# read data from SQL to pandas dataframe
data = pd.read_sql_query('SELECT * FROM books;', db)

# show top 5 rows
print(data)