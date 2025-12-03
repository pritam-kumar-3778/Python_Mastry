# In Python there is no true protected or Private attribute. By convension developer use it only.
# We can access private attribute by : objectname._Classname__private attribute

class BankAccount:
    def __init__(self, name, accNo, balance):
        self.name = name # Public attribute
        self._accNo = accNo      # _ defines it's a protected attribute
        self.__balance = balance # __ (Double underscore) define private attribute


acc1 = BankAccount("Pritam", 576586775932, 10000000)
acc2 = BankAccount("Sritam", 476586775931, 50000000)

print(f"{acc1.name} {acc1._BankAccount__balance}")