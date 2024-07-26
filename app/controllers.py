from flask import Blueprint, jsonify, request
from flasgger import swag_from
from .services import UserService

user_service = UserService()

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Create a new user',
            'examples': {
                'application/json': {
                    'id': 1,
                    'name': 'John Doe',
                    'email': 'john@example.com',
                    'role': 'admin'
                }
            }
        }
    }
})
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user.to_dict()), 201

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

@user_blueprint.route('/<int:user_id>', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Get a user by ID',
            'examples': {
                'application/json': {
                    'id': 1,
                    'name': 'John Doe',
                    'email': 'john@example.com',
                    'role': 'admin'
                }
            }
        }
    }
})
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
@swag_from({
    'responses': {
        200: {
            'description': 'Update a user by ID',
            'examples': {
                'application/json': {
                    'id': 1,
                    'name': 'John Doe',
                    'email': 'john@example.com',
                    'role': 'admin'
                }
            }
        }
    }
})
def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(user_id, data)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
@swag_from({
    'responses': {
        204: {
            'description': 'Delete a user by ID'
        }
    }
})
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    if result:
        return '', 204
    return jsonify({'error': 'User not found'}), 404