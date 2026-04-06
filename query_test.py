import sqlite3 
import pandas as pd 
import logging

#NEW: setup logging
logging.basicConfig(
    filename='query_script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting load script")

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