# visualizer.py
import matplotlib.pyplot as plt
from data_processor import get_daily_summary

def visualize_daily_summary(date):
    summary = get_daily_summary(date)
    plt.figure(figsize=(10, 5))
    plt.bar(['Avg Temp', 'Max Temp', 'Min Temp'], [summary['average_temp'], summary['max_temp'], summary['min_temp']])
    plt.title(f"Weather Summary for {date}")
    plt.show()
