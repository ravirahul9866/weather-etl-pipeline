import sqlite3

conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()

# Get total row count
cursor.execute("SELECT COUNT(*) FROM weather_history")
count = cursor.fetchone()[0]

# Get the most recent timestamp
cursor.execute("SELECT MAX(extracted_at) FROM weather_history")
latest = cursor.fetchone()[0]

print(f"Total Rows: {count}")
print(f"Latest Entry: {latest}")

conn.close()
