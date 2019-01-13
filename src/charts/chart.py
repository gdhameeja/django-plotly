class Chart(object):
    model = None
    chart_type = 'Bar'


class ChartManager(object):
    self._charts = {}

    def register_chart(self, slug, chart):
        """ Registers the chart """
        if not isinstance(chart, Chart):
            raise ValueError("chart should be of type Chart")
        self._charts[slug] = chart

    def get_chart(self, slug):
        """ 
        Gets the chart if it is registered.
        """
        if self._is_chart_registered(slug):
            return _charts.get(slug)
        raise ValueError("Chart not registered")

    def _is_chart_registered(self, slug):
        """ Check if chart is registered """
        return self._charts.get(slug)
