from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository
from app.persistence import db_session


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)
