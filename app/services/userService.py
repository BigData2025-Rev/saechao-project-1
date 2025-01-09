from ..models.user import User
from app.config import log_event

class UserService:
    def __init__(self,db):
        self.user = User(db)

    def create_user(self, username: str, password: str, email: str, role: str):
        user_id = self.user.create_user(username, password, email, role)
        log_event(f"User {username} created with ID {user_id}.")
        return user_id

    def get_user(self, username: str):
        return self.user.get_user(username)

    def get_all_user(self):
        return list(self.user.get_all_user())

    def update_user(self, user_id: str, updated_fields: dict):
        result = self.user.update_user(user_id, updated_fields)
        log_event(f"User {user_id} updated with fields {updated_fields}.")
        return result

    def delete_user(self, user_id: str):
        result = self.user.delete_user(user_id)
        log_event(f"User {user_id} deleted.")
        return result