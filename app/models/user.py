from app.config import DB_HOST, DB_PORT, DB_NAME
from pymongo import Collection

class User:
    def __init__(self, db):
        self.users: Collection = db['users']

    def create_user(self, username:str, password:str, email:str, role:str):
        user = {
            'username': username,
            'password': password,
            'email': email,
            'role': role
        }

        result = self.users.insert_one(user)

        return str(result.inserted_id)
    

    def get_user(self, username:str):
        return self.users.find_one({'username': username})
    
    def update_user(self, username:str):
        return self.users.update_one({})
    
    def delete_user(self, user_id):
        return self.users.delete_one({'_id': user_id})