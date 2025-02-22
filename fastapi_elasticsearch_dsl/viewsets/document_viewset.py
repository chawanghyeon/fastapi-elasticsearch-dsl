from .base_viewset import BaseViewSet
from services.indexing_service import IndexingService

class DocumentViewSet(BaseViewSet):
    def __init__(self, indexing_service: IndexingService):
        super().__init__(indexing_service)
        self.router.add_api_route("/index", self.index_document, methods=["POST"])

    async def index_document(self, data: dict):
        return self.crud_service.index_document(data)
