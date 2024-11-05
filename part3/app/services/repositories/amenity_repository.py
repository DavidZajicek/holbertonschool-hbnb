from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)
