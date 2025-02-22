
from .base_document import BaseDocument
from elasticsearch_dsl import Text, Keyword

class ItemDocument(BaseDocument):
    name = Text()
    description = Text()
    category = Keyword()

    class Index:
        name = 'items'
