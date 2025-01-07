from pymongo import Collection

class Product:
    def __init__(self, db):
        self.products: Collection = db['products']

    def create_product(self, name: str, price: int, stock: int):
        product = {
            'name': name,
            'price': price,
            'stock': stock
        }

        result = self.product.insert_one(product)
        return str(result.inserted_id)
    
    def get_all_products(self):
        return list(self.products.find())
    

    def delete_product(self,product_id):
        return self.products.delete_one({'_id': product_id})
