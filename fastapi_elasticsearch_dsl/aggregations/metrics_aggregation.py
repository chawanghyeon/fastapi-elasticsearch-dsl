from .base_aggregation import BaseAggregation

class MetricsAggregation(BaseAggregation):
    def aggregate(self, field, metric_type):
        return {
            metric_type: {
                "field": field
            }
        }
