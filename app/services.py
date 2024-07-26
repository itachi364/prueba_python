# services.py necesita importar User
from .models import User

class UserService:
    def __init__(self):
        self.users = []
        self.counter = 1

    def create_user(self, data):
        user = User(self.counter, data['name'], data['email'], data['role'])
        self.users.append(user)
        self.counter += 1
        return user

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id, data):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.role = data.get('role', user.role)
            return user
        return None

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False