from fastapi import APIRouter, HTTPException
from services.crud_service import CRUDService

class BaseViewSet:
    def __init__(self, crud_service: CRUDService):
        self.router = APIRouter()
        self.crud_service = crud_service
        self.router.add_api_route("/{id}", self.get, methods=["GET"])
        self.router.add_api_route("/", self.create, methods=["POST"])
        self.router.add_api_route("/{id}", self.update, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete, methods=["DELETE"])

    async def get(self, id: str):
        result = self.crud_service.get(id)
        if not result:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, data: dict):
        return self.crud_service.create(data)

    async def update(self, id: str, data: dict):
        return self.crud_service.update(id, data)

    async def delete(self, id: str):
        return self.crud_service.delete(id)
