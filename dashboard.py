import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def create_dashboard():
    conn=sqlite3.connect('weather_data.db')

    # SQL Query: Get data from last run
    query = "SELECT city, temperature, condition, timestamp FROM weather ORDER BY timestamp DESC"
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("No data found to plot!")
        return

    # Pivot data so each city has its own line
    # Columns: City names, Index: Time, Values: Temperature
    df_pivot = df.pivot(index='timestamp', columns='city', values='temperature')

    # Plotting
    plt.figure(figsize=(10, 6))
    df_pivot.plot(marker='o', ax=plt.gca())
    
    plt.title("Temperature Trends by City")
    plt.xlabel("Time of Extraction")
    plt.ylabel("Temperature (°F)")
    plt.grid(True)
    plt.legend(title="Cities", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    # Save the dashboard as an image
    plt.savefig("weather_dashboard.png")
    print("📊 Dashboard updated and saved as 'weather_dashboard.png'")
    plt.show()

if __name__ == "__main__":
    create_dashboard()