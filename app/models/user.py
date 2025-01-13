from pymongo.collection import Collection
from bson.objectid import ObjectId

class User:
    """Data access layer handling all CRUD operations for Users"""
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
    

    def get_user(self, username: str, password: str):
        return self.users.find_one({'username': username,'password': password})

    def update_user(self, user_id: str, updated_fields: dict):
        return self.users.update_one({'_id': ObjectId(user_id)}, {'$set': updated_fields})

    def delete_user(self, user_id: str):
        return self.users.delete_one({'_id': ObjectId(user_id)})
    
    def get_user_id(self, user_id: str):
        return self.users.find_one({'_id': ObjectId(user_id)})

    def get_all_user(self):
        return list(self.users.find())

    def delete_user(self, user_id: str):
        return self.users.delete_one({'_id': ObjectId(user_id)})
    
    def add_admin(self,user_id: str):
        return self.update_user(user_id, {'role': 'admin'})
    
    def remove_admin(self,user_id: str):
        return self.update_user(user_id, {'role': 'user'})
    
