# By getters we access the Private attribute.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name # Public attribute
        self.__balance = balance # __ (Double underscore) define private attribute

    # getter for access private attribute out side of the class
    # getter is a normal instance method, by which we access private attribute like this way
    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Pritam", 10000000)
acc2 = BankAccount("Sritam", 50000000)


# print(f"{acc1.name} {acc1.__balance}")
# Call the getter function for showing the balance which in private.
print(f"{acc1.get_balance()}")