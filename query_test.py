import sqlite3 
import pandas as pd 

conn = sqlite3.connect('my_database.db') 

cursor = conn.cursor() 


query = f"""
SELECT country, COUNT(*) AS country_count
FROM circuits
GROUP BY country
ORDER BY country_count DESC;
"""
#executes the action, in this case, the query
cursor.execute(query) 
#takes what the previous action did and allows you to fetch the results
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()