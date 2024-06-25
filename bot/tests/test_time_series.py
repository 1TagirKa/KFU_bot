import unittest
from data_processing.time_series import analyze_resolution_time

class TestTimeSeries(unittest.TestCase):
    def test_analyze_resolution_time(self):
        test_data = [{'start_time': '2021-01-01 10:00:00', 'end_time': '2021-01-01 11:00:00'}]
        result = analyze_resolution_time(test_data)
        self.assertAlmostEqual(result['resolution_time']['mean'], 60.0)  # Проверяем среднее время решения

if __name__ == '__main__':
    unittest.main()
