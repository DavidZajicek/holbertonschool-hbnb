from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')

# Define models
user_model = api.model('User', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user')
})

amenity_model = api.model('Amenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

facade = HBnBFacade()

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Create a new place"""
        try:
            new_place = facade.create_place(api.payload)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner.id
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'price': place.price,
            'owner_id': place.owner.id
        } for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [{'id': a.id, 'name': a.name} for a in place.amenities],
            'reviews': [{
                'id': r.id,
                'text': r.text,
                'rating': r.rating,
                'user_id': r.user.id
            } for r in place.reviews]
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        try:
            updated_place = facade.update_place(place_id, api.payload)
            return {
                'id': updated_place.id,
                'title': updated_place.title,
                'description': updated_place.description,
                'price': updated_place.price,
                'latitude': updated_place.latitude,
                'longitude': updated_place.longitude,
                'owner_id': updated_place.owner.id
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 404

@api.route('/<place_id>/amenities')
class PlaceAmenities(Resource):
    @api.response(200, 'Amenities for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all amenities for a specific place"""
        try:
            amenities = facade.get_place_amenities(place_id)
            return [{
                'id': amenity.id,
                'name': amenity.name
            } for amenity in amenities], 200
        except ValueError as e:
            return {'error': str(e)}, 404


@api.route('/<place_id>/reviews')
class PlaceReviews(Resource):
    @api.response(200, 'Reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            reviews = facade.get_place_reviews(place_id)
            return [{
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.user.id
            } for review in reviews], 200
        except ValueError as e:
            return {'error': str(e)}, 404