# Using SQLite3 and Pandas Together

# 1. Import both libraries
# 2. Connect to our db
# 3. Read the contents of our db into a DataFrame
# 4. The 'read_sql_query()' method reads the data in using a SQL Query, not a URL like 'read_csv' or 'read_json'

# import the libraries
import sqlite3
import pandas as pd

# create a connection
db = sqlite3.connect('books.db')

# read data from SQL to pandas dataframe
data = pd.read_sql_query('SELECT * FROM books;', db)

# show top 5 rows
print(data.head())