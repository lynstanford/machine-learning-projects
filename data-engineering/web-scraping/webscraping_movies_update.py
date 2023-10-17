import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

db_name = 'Movies.db'

table_name = 'Top_25'

# set the filepath for the CSV extract file
csv_path = 'C:/Users/lynst/Documents/GitHub/machine-learning-projects/data-engineering/web-scraping/top_25_films.csv'

