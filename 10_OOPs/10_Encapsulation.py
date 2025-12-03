# Wrapping data and function in a singleunit
# Hiding data

# public : Access from any where
# private : Access within the class only
# protected : Access within the class and its subclass

class BankAccount:
    def __init__(self, name, accNo, balance):
        self.name = name # Public attribute
        self._accNo = accNo      # _ defines it's a protected attribute
        self.__balance = balance # __ (Double underscore) define private attribute


acc1 = BankAccount("Pritam", 576586775932, 10000000)
acc2 = BankAccount("Sritam", 476586775931, 50000000)

print(f"{acc1.name} {acc1._accNo}")

# print(f"{acc1.__balance}") # It shows attribute Error bcz Private attribute only accessiable inside the class
#  But In python we use protected attribute by convension. It can be access out side of the class also.
