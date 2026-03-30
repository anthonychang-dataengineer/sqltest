import sqlite3 
import pandas as pd 

conn = sqlite3.connect('my_database.db') 

df = pd.read_csv(r'c:\Users\17322\Downloads\sqltest\circuits.csv') 
df.to_sql('circuits', conn, if_exists='replace', index=False) 

cursor = conn.cursor() 

country = input("Enter a country ")

query = f"""
SELECT *
FROM circuits
WHERE country = '{country}'
LIMIT 10;
"""
cursor.execute(query) 
print(cursor.fetchall()) 

conn.close()