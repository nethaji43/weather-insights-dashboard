# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary
                      (date DATE PRIMARY KEY,
                       avg_temp REAL,
                       max_temp REAL,
                       min_temp REAL,
                       dominant_condition TEXT)''')
    conn.commit()
    conn.close()

def store_daily_summary(date, summary):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT OR REPLACE INTO daily_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?)''',
                   (date, summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()
