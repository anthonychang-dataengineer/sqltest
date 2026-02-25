import sqlite3 
import pandas as pd 

conn = sqlite3.connect('my_database.db') 

df = pd.read_csv(r'c:\Users\17322\Downloads\sqltest\circuits.csv') 
df.to_sql('circuits', conn, if_exists='replace', index=False) 

cursor = conn.cursor() 
cursor.execute("INSERT INTO circuits (circuitId, circuitRef, name, location, country, lat, lng, alt, url) VALUES (999, 'bob', 'Bob Jones', 'Antarctica City','Antarctica', 100, 100, 10, 'www.bobjones.com');") 
print(cursor.fetchall()) 

conn.close()