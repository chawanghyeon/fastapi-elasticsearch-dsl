from .base_pagination.py import BasePagination

class FromSizePagination(BasePagination):
    def paginate(self, query, page, size):
        query['from'] = (page - 1) * size
        query['size'] = size
        return query
