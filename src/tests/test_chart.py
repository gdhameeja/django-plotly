import unittest

from src.charts.chart import Chart, ChartManager


class ChartTest(unittest.TestCase):

    def test_get_chart(self):
        chart = Chart()
        chart_manager = ChartManager()
        chart_manager.register_chart('first_chart', chart)
        self.assertEqual(chart_manager['first_chart'], chart)


if __name__ == "__main__":
    unittest.main()
