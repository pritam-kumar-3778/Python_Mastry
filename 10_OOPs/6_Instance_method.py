class Laptop:
    storage_type = "SSD"  # Class variable

    def __init__(self, RAM, ROM):  # Instance variables
        self.RAM = RAM
        self.ROM = ROM

    def get_info(self):  # Instance method
        print(f"Laptop with {self.RAM} RAM and {self.ROM} {self.storage_type} storage.")

l1 = Laptop("8GB", "512GB")
l2 = Laptop("16GB", "1TB")

l1.get_info()


# Instance method can access instance variables and class variables both using self keyword