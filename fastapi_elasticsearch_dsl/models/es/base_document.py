
from elasticsearch_dsl import Document, Date, Integer, Keyword

class BaseDocument(Document):
    created_at = Date()
    updated_at = Date()
    version = Integer()

    class Index:
        name = 'base_document'
