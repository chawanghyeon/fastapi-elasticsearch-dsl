from .base_repository import BaseRepository
from sqlalchemy.orm import Session

class SQLRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: str):
        return self.session.query(MyModel).get(id)

    def create(self, data: dict):
        obj = MyModel(**data)
        self.session.add(obj)
        self.session.commit()
        return obj

    def update(self, id: str, data: dict):
        obj = self.session.query(MyModel).get(id)
        for key, value in data.items():
            setattr(obj, key, value)
        self.session.commit()
        return obj

    def delete(self, id: str):
        obj = self.session.query(MyModel).get(id)
        self.session.delete(obj)
        self.session.commit()
