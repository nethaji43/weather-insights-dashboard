# config.py

# OpenWeatherMap API configuration
OPENWEATHER_API_KEY = "e728c98f178a149dcc1ac60a0e6d0f75"

# City IDs for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad)
CITY_IDS = {
    "Delhi": 1273294,
    "Mumbai": 1275339,
    "Chennai": 1264527,
    "Bangalore": 1277333,
    "Kolkata": 1275004,
    "Hyderabad": 1269843
}

# Polling interval (in seconds) - how frequently to call the API
POLLING_INTERVAL = 300  # 5 minutes


# Alert threshold for temperature (in Celsius)
ALERT_THRESHOLD = 35  # Example threshold: trigger alert if temperature exceeds 35°C
