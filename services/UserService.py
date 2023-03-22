from repository import UserRepository
from entity import User

class UserService():
    def __init__(self, user_repository: UserRepository.UserRepository):
        self.user_repository = user_repository

    def add_user(self, user: User.CreateUser):
        self.user_repository.add_user(user)

    def delete_user(self, id: int):
        self.user_repository.delete_user(id)
        
    def get_users(self):
        return self.user_repository.get_user()