import logging
import schedule
import time
from extract import get_weather_data
from transform import clean_weather_data    
from load import save_to_db
from dashboard import create_dashboard

logging.basicConfig(
    filename = "etl.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)
def run_etl():
    cities = ["London", "New York", "Tokyo", "Mumbai", "Paris"]
    logging.info("Starting ETL process...")
    for city in cities:
        try:
            logging.info(f"Extracting data for {city}...")
            raw_data = get_weather_data(city)
            logging.info(f"Transforming data for {city}...")
            clean_data = clean_weather_data(raw_data)
            logging.info(f"Loading data for {city} into database...")
            save_to_db(clean_data)
            logging.info(f"Successfully processed data for {city}.")

        except Exception as e:
            logging.error(f"Error processing data for {city}: {e}")

    create_dashboard() # Update dashboard after processing all cities

schedule.every(1).minutes.do(run_etl)
 
if __name__ == "__main__":
    print("scheduler is running... press ctrl+c to stop.")
    logging.info("scheduler started.")

    while True:            
        schedule.run_pending()
        time.sleep(1)
    