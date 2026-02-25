import sqlite3 
import pandas as pd 

conn = sqlite3.connect('my_database.db') 

df = pd.read_csv(r'c:\Users\17322\Downloads\sqltest\circuits.csv') 
df.to_sql('circuits', conn, if_exists='replace', index=False) 

cursor = conn.cursor() 
cursor.execute("SELECT * FROM circuits LIMIT 10;") 
print(cursor.fetchall()) 

conn.close()