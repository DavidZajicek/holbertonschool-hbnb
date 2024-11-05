from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session
from app.models.place import place_amenity, Place


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)

    def get_amenities_by_place(self, place_id):
        return db_session.query(self.model).\
            join(place_amenity).filter_by(place_id=place_id).all()

    def create_place_amenity_link(self, place_id, amenity_id):
        # TODO: actually do the thing
        print(f'place_id: {place_id}, amenity_id: {amenity_id}')
        pass
