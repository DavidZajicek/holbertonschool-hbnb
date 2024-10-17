# Import API namespaces
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns

def create_api(app):
    """
    Create and configure the API with all namespaces.
    
    :param app: Flask application instance
    :return: Configured API instance
    """
    from flask_restx import Api
    
    # Create API instance
    api = Api(
        app, 
        version='1.0', 
        title='HBnB API', 
        description='HBnB Application API'
    )
    
    # Add namespaces to the API
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    
    return api