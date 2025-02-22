from .base_aggregation import BaseAggregation

class HistogramAggregation(BaseAggregation):
    def aggregate(self, field, interval):
        return {
            "histogram": {
                "field": field,
                "interval": interval
            }
        }
