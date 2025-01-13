from ..models.product import Product
from app.config import log_event

class ProductService:
    
    def __init__(self, db):
        self.product = Product(db)

    def create_product(self, name: str, price: float, quantity: int, category: str):
        product_id = self.product.create_product(name, price, quantity, category)
        log_event(f"Product {name} created with ID {product_id}.")
        return product_id
    
    def get_product_category(self, category: str):
        return self.product.get_product_category(category)
    
    def get_product_by_name(self, name: str):  
        product = self.product.get_product_name(name)  
        return product

    def get_product_id(self, product_id: str):
        product = self.product.get_product_id(product_id)
        return product

    def update_product(self, product_id: str, updated_fields: dict):
        result = self.product.update_product(product_id, updated_fields)
        if result > 0:
            log_event(f"Product with ID {product_id} updated.")
        else:
            log_event(f"Failed to update product with ID {product_id}.")
        return result
    

    def update_stock(self, product_id: str, quantity: int):
        result = self.product.update_stock(product_id, quantity)
        if result > 0:
            log_event(f"Stock with ID {product_id} updated.")
        else:
            log_event(f"Failed to update stock with ID {product_id}.")
        return result

    def delete_product(self, product_id: str):
        result = self.product.delete_product(product_id)
        log_event(f"Product with ID {product_id} deleted.")
        return result

    def get_all_products(self):
        products = self.product.get_all_products()
        return products
