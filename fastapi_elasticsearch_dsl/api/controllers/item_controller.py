from .base_controller import BaseController

class ItemController(BaseController):
    def get_item(self, item_id: int):
        return {"item_id": item_id, "name": "Sample Item"}
