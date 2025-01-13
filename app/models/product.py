from pymongo.collection import Collection
from bson.objectid import ObjectId


class Product:
    """Data access layer for products handling all CRUD operations"""
    def __init__(self, db):
        self.products: Collection = db['products']

    def create_product(self, name: str, price: int, stock: int, catagory: str):
        product = {
            'name': name,
            'price': price,
            'stock': stock,
            'catagory':catagory
        }

        result = self.products.insert_one(product)
        return str(result.inserted_id)
    
    def get_all_products(self):
        return list(self.products.find())
    
    def get_product_id(self, product_id: str):
        return self.products.find_one({'_id': product_id})
    
    def get_product_name(self, product_name: str):
        return self.products.find_one({'name':product_name })
    
    def get_product_category(self,category: str):
        return list(self.products.find({'category': category}))
    
    def delete_product(self,product_id: str):
        return self.products.delete_one({'_id': ObjectId(product_id)})
    
    def update_product(self, product_id: str, updated_fields: dict):
        result = self.products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': updated_fields}
        )
        return result.modified_count 

    def update_stock(self, product_id: str, quantity: int):
        result = self.products.update_one(
            {'_id': ObjectId(product_id)},
            {'$inc': {'stock': quantity}}
        )
        return result.modified_count 
