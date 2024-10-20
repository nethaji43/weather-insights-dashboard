# Real-Time Weather Monitoring System

## Project Overview
This project monitors real-time weather conditions for major metros in India and generates daily weather summaries using the OpenWeatherMap API. The system aggregates weather data, stores daily summaries, and generates visualizations. It also includes an alert system for predefined thresholds.

## Features
- Real-time data retrieval from OpenWeatherMap API
- Temperature conversion from Kelvin to Celsius
- Daily summaries of average, maximum, and minimum temperatures
- Visualization of weather data using Matplotlib
- Configurable threshold alerts for specific conditions (e.g., temperature exceeding 35°C)
- Persistent storage for weather summaries

## Dependencies
- Python 3.8+
- Requests
- Matplotlib
- SQLAlchemy (for database storage)
- SQLite (or use your own database configuration)
- Docker (optional for containerizing the application)