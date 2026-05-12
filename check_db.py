import sqlite3
import pandas as pd

conn = sqlite3.connect('weather_data.db')
query = "SELECT * FROM weather ORDER BY timestamp DESC LIMIT 5"
df = pd.read_sql_query(query, conn)
print(df)
conn.close()
