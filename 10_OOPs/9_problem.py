# Design and create a online store for products (name, Price)
# Track total products been created
# Create a static method to calculate discount on eah product based on a % parameter.

class OnlineStore:
    total_products = 0  # Class variable to track total products

    def __init__(self, name, price):  # Instance variables
        self.name = name
        self.price = price
        OnlineStore.total_products += 1  # Increment total products when a new product is created

    def get_product_info(self):  # Instance method to get product info
        return f"Product Name: {self.name}, Price: {self.price}"
    
    @classmethod
    def total_products_in_Store(cls):  # Instance method to get total products
        return f"Total products in store = {cls.total_products}"
    
    @staticmethod
    def calculate_discount(price, discount):  # Static method to calculate discount
        discounted_price = price - (price * discount / 100)
        return discounted_price
    
# Creating products
product1 = OnlineStore("Laptop", 80000)
product2 = OnlineStore("Smartphone", 50000)
product3 = OnlineStore("Headphones", 3000)
product4 = OnlineStore("Smartwatch", 15000)

# Display product information
print(product1.get_product_info())
print(product2.get_product_info())
print(product3.get_product_info())

# Display total products created
print(OnlineStore.total_products_in_Store())

# Calculate and display discounted prices
discounted_price1 = product1.calculate_discount(product1.price, 10)
print(f"Discounted price of {product1.name}: {discounted_price1}")
discounted_price2 = product2.calculate_discount(product2.price, 15)
print(f"Discounted price of {product2.name}: {discounted_price2}")
discounted_price3 = product3.calculate_discount(product3.price, 5)
print(f"Discounted price of {product3.name}: {discounted_price3}")
discounted_price4 = product4.calculate_discount(product4.price, 20)
print(f"Discounted price of {product4.name}: {discounted_price4}")