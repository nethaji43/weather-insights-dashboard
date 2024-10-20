# data_processor.py
from datetime import datetime
from collections import defaultdict

daily_summaries = defaultdict(lambda: {
    "temp_sum": 0,
    "temp_max": float('-inf'),
    "temp_min": float('inf'),
    "count": 0,
    "conditions": defaultdict(int)
})

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(data):
    main_condition = data['weather'][0]['main']
    temp_kelvin = data['main']['temp']
    dt = data['dt']

    temp_celsius = kelvin_to_celsius(temp_kelvin)

    return {
        "main": main_condition,
        "temp": temp_celsius,
        "dt": dt
    }

def update_daily_summary(weather_data):
    date = datetime.fromtimestamp(weather_data['dt']).date()
    daily_summaries[date]['temp_sum'] += weather_data['temp']
    daily_summaries[date]['temp_max'] = max(daily_summaries[date]['temp_max'], weather_data['temp'])
    daily_summaries[date]['temp_min'] = min(daily_summaries[date]['temp_min'], weather_data['temp'])
    daily_summaries[date]['count'] += 1
    daily_summaries[date]['conditions'][weather_data['main']] += 1

def get_daily_summary(date):
    summary = daily_summaries[date]
    avg_temp = summary['temp_sum'] / summary['count']
    dominant_condition = max(summary['conditions'], key=summary['conditions'].get)

    return {
        "average_temp": avg_temp,
        "max_temp": summary['temp_max'],
        "min_temp": summary['temp_min'],
        "dominant_condition": dominant_condition
    }
