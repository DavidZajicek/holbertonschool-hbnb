from app.models.place import Place
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_places_by_owner(self, owner_id):
        return db_session.query(self.model).filter_by(owner_id=owner_id).all()
