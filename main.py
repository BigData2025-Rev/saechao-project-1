from app.services.userService import UserService
from app.services.productService import ProductService
from app.services.orderService import OrderService
from app.config import get_db

def main():
    db = get_db()
    user_service = UserService(db)
    product_service = ProductService(db)
    order_service = OrderService(db)

    # Login interface
    print("Welcome to the Store!")
    while True:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            user = user_service.get_user(username, password)
            if user:
                if user['role'] == 'admin':
                    admin_dashboard(user_service,product_service,order_service)
                else:
                    user_dashboard(user,product_service,order_service)
            else:
                print("Invalid credentials.")
        
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            user_service.create_user(username,password,email,"user")
            
       
            print("\nRegistration successful! \nPlease log in to continue.")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option.")


def user_dashboard(user,product_service,order_service):
    cart = []

    while True:
        print("\n1. View Products\n2. View Cart\n3. Purchase Items\n4. View Orders\n5. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            # View all products
            products = product_service.get_all_products()
            for p in products:
                print(f"{p['_id']}: {p['name']} - ${p['price']} (Stock: {p['stock']})")
            
            # Allow the user to add a product to the cart
            add_to_cart = input("\nDo you want to add a product to your cart? (y/n): ")
            if add_to_cart.lower() == 'y':
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                
                product = product_service.get_product_by_name(product_name)
                if product:
                    cart.append({
                        'product_id': product['_id'],
                        'name': product['name'],
                        'price': product['price'],
                        'quantity': quantity
                    })
                    print(f"{quantity} of {product['name']} added to your cart.")
                else:
                    print("Insufficient stock or product not found.")
        
        elif choice == '2':
            # View items in the cart
            if cart:
                print("\nYour Cart:")
                for item in cart:
                    print(f"Product: {item['name']} | Quantity: {item['quantity']} | Total: ${item['quantity'] * item['price']}")
            else:
                print("Your cart is empty.")

        elif choice == '3':
            # Proceed to purchase items in the cart
            if not cart:
                print("Your cart is empty. Add items to the cart before purchasing.")
                continue
            order_service.place_order(user['_id'], cart)
            cart.clear()  # Clear the cart after the purchase

        elif choice == '4':
            # View orders
            orders = order_service.get_user_orders(user['_id'])
            for order in orders:
                print(f"\nOrder ID: {order['_id']}\nPurchase Date: {order['order_date']}")

                # All products from order
                for product in order['products']:
                    product_id = product['product_id']
                    quantity = product['quantity']
                    product_details = product_service.get_product_id(product_id)
                    print(f"{quantity} - {product_details['name']}")

        elif choice == '5':
            print("Logging out...")
            break  # Exit the loop and logout the user
        
        else:
            print("Invalid option. Please select again.")


def admin_dashboard(user_service, product_service, order_service):
    """Dashboard for admin commands"""
    while True:
        print("\nAdmin Interface")
        print("\n1. Manage Users\n2. Manage Orders\n3. Manage Products\n4. Logout")
        choice = input("Select an option: ")

        if choice == '1':

            while True:
                # User Management
                print("\n1. List Users\n2. Delete User\n3. Add Admin\n4. Back")
                sub_choice = input("Select an option: ")

                if sub_choice == '1':
                    users = user_service.get_all_user()
                    for user in users:
                        print(f"{user['_id']}: {user['username']} (Role: {user['role']})")
                
                elif sub_choice == '2':
                    user_id = input("Enter User ID for Deletion: ")
                    user_service.delete_user(user_id)
               
                
                elif sub_choice == '3':
                    user_id = input("Enter User ID for Admin Privilege: ")
                    user_service.add_admin(user_id)
                    
            

                elif sub_choice == '4':
                    break

                else:
                    print("Invalid option")


        elif choice == '2':
                # Order Management
                print("\n1. Get All Orders\n2. Cancel Order\n3. Back")
                sub_choice = input("Select an option: ")

                if sub_choice == '1':
                    orders = order_service.get_all_orders()
                    for order in orders:
                        print(f"{order['_id']}: {order['user_id']} {order['order_date']})")
                
                elif sub_choice == '2':
                    order_id = input("Enter Order ID for Deletion: ")
                    order_service.delete_user(order_id)

                elif sub_choice == '3':
                    break

                else:
                    print("Invalid option")
        
        elif choice == '3':
            while True:
                print("\n1. Add Product\n2. Remove Product\n3. View Products\n4. Back")
                sub_choice = input("Select an option: ")
                
                # Add Product
                if sub_choice == '1':
                    name = input("Product Name: ")
                    price = float(input("Price: "))
                    stock = int(input("Stock: "))
                    category = input("Category: ")
                    product_service.create_product(name, price, stock, category)
                    print("Product added.")
                
                # Delete Product
                elif sub_choice == '2':
                    product_id = input("Product ID: ")
                    product_service.delete_product(product_id)
                    print("Product list updated.")
                
                # View Products
                elif sub_choice == '3':
                    products = product_service.get_all_products()
                    for p in products:
                        print(f"{p['_id']}: {p['name']} - ${p['price']} (Stock: {p['stock']})")
            

                elif sub_choice == '4':
                    break

                else:
                    print("Invalid option")

        elif choice == '4':
            print("Logged out.")
            break
        
        else:
            print("Invalid option.")


if __name__ == '__main__':
    main()