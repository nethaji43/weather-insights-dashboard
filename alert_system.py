# alert_system.py
import smtplib
from config import ALERT_THRESHOLD  # Import the ALERT_THRESHOLD from config

def check_alerts(weather_data):
    if weather_data['temp'] > ALERT_THRESHOLD:
        trigger_alert(weather_data)

def trigger_alert(weather_data):
    # Example of alerting via console output
    print(f"Alert! Temperature exceeded threshold: {weather_data['temp']}°C")
