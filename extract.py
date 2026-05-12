import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(city):
    api_key=os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status() # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()
