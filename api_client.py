# api_client.py
import requests
from config import OPENWEATHER_API_KEY, CITY_IDS

def fetch_weather_data(city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for city ID {city_id}: {response.status_code}")
        return None
