from .base_filter import BaseFilter

class TermFilter(BaseFilter):
    def apply(self, query: dict, value: str):
        query["query"]["bool"]["must"].append({"term": {"field": value}})
        return query
