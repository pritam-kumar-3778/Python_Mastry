# BY setters we can set a new vallue

class BankAccount:
    def __init__(self, name, balance):
        self.name = name # Public attribute
        self.__balance = balance # __ (Double underscore) define private attribute

    # getter
    def get_ballance(self):
        return self.__balance

    # Setter
    def set_balance(self, newBalance):
        self.__balance = newBalance


acc1 = BankAccount("Pritam", 10000000)
acc2 = BankAccount("Sritam", 50000000)

# Set new value
acc1.set_balance(200_000_00)

# get the value
print(acc1.get_ballance())

# Getter and setter are normal function by which we set the value and get the value of private attribute.
