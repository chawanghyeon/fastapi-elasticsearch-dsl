
from .base_model import BaseModel
from sqlalchemy import Column, String

class ItemModel(BaseModel):
    name = Column(String, index=True)
    description = Column(String)
    category = Column(String)
