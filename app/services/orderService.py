from ..models.order import Order
from app.config import log_event

class OrderService:
    """Business Logic for Orders"""
    def __init__(self, db):
        self.order_dal = Order(db)

    def place_order(self, user_id: str, products: list[dict]):
        order_id = self.order_dal.create_order(user_id, products)
        log_event(f"Order {order_id} created.")
        return order_id

    def get_order(self, order_id: str):
        order = self.order_dal.get_order_by_id(order_id)
        return order

    def get_user_orders(self, user_id: str):
        orders = self.order_dal.get_orders_by_user(user_id)
        return orders
   

    def get_all_orders(self):
        return self.order_dal.get_all_orders()

    def delete_order(self, order_id: str):
        return self.order_dal.delete_order(order_id)
        
