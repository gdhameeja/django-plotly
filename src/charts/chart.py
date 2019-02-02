class Chart:
    model = None
    chart_type = 'Bar'


class ChartManager:
    """ 
    Chart Manager acts as the interface for Report to perform 
    actions on charts like create, register, delete charts
    """

    def __init__(self):
        self._charts = {}

    def register_chart(self, slug, chart):
        if not isinstance(chart, Chart):
            raise ValueError("chart should be of type Chart")
        self._charts[slug] = chart

    def __getitem__(self, slug):
        if slug in self:
            return self._charts.get(slug)
        raise ValueError("Chart not registered")

    def __contains__(self, slug):
        """ Check if chart is registered """
        return slug in self._charts
