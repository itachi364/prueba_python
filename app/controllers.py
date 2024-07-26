from flask import Blueprint, jsonify, request
from flasgger import swag_from
from .services import UserService

user_service = UserService()

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Get all users',
            'examples': {
                'application/json': [
                    {
                        'id': 1,
                        'name': 'John Doe',
                        'email': 'john@example.com',
                        'role': 'admin'
                    }
                ]
            }
        }
    }
})
def get_users():
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users])