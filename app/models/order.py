from pymongo import Collection
from datetime import datetime

class Order:
    def __init__(self,db):
        self.orders: Collection = db['Order']

    def create_order(self, user_id, products):
        order = {
            "user_id": user_id,
            'product': products,
            'order_date': datetime.now()
        }
        
        result = self.orders.insert_one(order)
        return str(result.inserted_id)

