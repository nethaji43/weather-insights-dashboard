# test_weather_system.py
import unittest
from data_processor import kelvin_to_celsius, update_daily_summary

class TestWeatherSystem(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0.0)

    def test_daily_summary(self):
        # Simulate data and check outputs
        pass  # Implement your test logic here

if __name__ == '__main__':
    unittest.main()
