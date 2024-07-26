# services.py necesita importar User
from .models import User

class UserService:
    def __init__(self):
        self.users = []
        self.counter = 1

    def get_all_users(self):
        return self.users