# main.py
import time
from api_client import fetch_weather_data
from data_processor import process_weather_data, update_daily_summary, daily_summaries  # Import daily_summaries
from alert_system import check_alerts
from visualizer import visualize_daily_summary
from config import CITY_IDS, POLLING_INTERVAL
from datetime import datetime

if __name__ == "__main__":
    while True:
        for city_name, city_id in CITY_IDS.items():
            weather_data = fetch_weather_data(city_id)
            if weather_data:
                processed_data = process_weather_data(weather_data)
                update_daily_summary(processed_data)
                check_alerts(processed_data)

        # Visualize daily summaries as needed
        today = datetime.now().date()
        if today in daily_summaries:  # Check if today's summary exists
            visualize_daily_summary(today)

        time.sleep(POLLING_INTERVAL)
