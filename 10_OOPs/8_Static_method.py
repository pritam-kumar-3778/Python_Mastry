# No compulsery parameter
# Decorator : @staticmethod

class Laptop:
    storage_type = "SSD"  # Class variable

    def __init__(self, RAM, ROM):  # Instance variables
        self.RAM = RAM
        self.ROM = ROM

    @classmethod
    def get_storage_type(cls):  # Class method
        print(cls.storage_type)
        # print(cls.storage_type, cls.RAM) 
        # This will raise an AttributeError because cls only access class variables


    def get_info(self):  # Instance method
        print(f"Laptop with {self.RAM} RAM and {self.ROM} {self.storage_type} storage.")


    @staticmethod
    def calculate_discount(price, discount): # Static method
        print(f"Discounted price = {price - (price * discount / 100)}")

l1 = Laptop("8GB", "512GB")
l2 = Laptop("16GB", "1TB")

# Call the instance method
l1.get_info()

# Call the class method
Laptop.get_storage_type()
l2.get_storage_type() # Class method can be called by class name or object name but it is recommended to call by class name

# Call the static method
Laptop.calculate_discount(60000, 15)
l1.calculate_discount(50000, 10)