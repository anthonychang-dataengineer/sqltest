import sqlite3 
import pandas as pd 

#declares and opens the connection to sqllite database
conn = sqlite3.connect('my_database.db') 

df = pd.read_csv('circuits.csv') 
df.to_sql('circuits', conn, if_exists='replace', index=False) 

print("Data loaded into SQLLite!") 
#test

conn.close()