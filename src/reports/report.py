from src.charts.chart import ChartManager

class Report:
    to_pdf = False
    html_template = 'templates/default_report.html'

    def __init__(self, chart_manager):
        self.chart_manager = chart_manager
        
    def generate_report(self):
        pass

    def _generate_pdf_report(self):
        pass

    def _generate_html_report(self):
        pass
