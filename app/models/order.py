from pymongo.collection import Collection
from datetime import datetime
from bson.objectid import ObjectId


class Order:
    """Data access layer for handling Orders."""
    def __init__(self, db):
        self.orders: Collection = db['orders']

    def create_order(self, user_id: str, products: list[dict]):
        order = {
            "user_id": user_id,
            "products": products,  
            "order_date": datetime.now(),

        }
        result = self.orders.insert_one(order)
        return str(result.inserted_id)

    def get_order_by_id(self, order_id: str):
        return self.orders.find_one({"_id": ObjectId(order_id)})

    def get_orders_by_user(self, user_id: str):
        return list(self.orders.find({"user_id": ObjectId(user_id)}))

    def get_all_orders(self):
        return list(self.orders.find())

    def delete_order(self, order_id: str):
        result = self.orders.delete_one({"_id": ObjectId(order_id)})
        return result.deleted_count
