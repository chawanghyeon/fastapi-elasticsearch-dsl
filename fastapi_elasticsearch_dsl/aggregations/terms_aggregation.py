from .base_aggregation import BaseAggregation

class TermsAggregation(BaseAggregation):
    def aggregate(self, field):
        return {
            "terms": {
                "field": field
            }
        }
