# Multi level Inheritence

class Employee:
    Shift_start = "10 AM"
    Shift_end = "4 PM"

class AdminStaff(Employee):
    def __init__(self, roll):
        self.roll = roll

class Accountant(AdminStaff):
    def __init__(self, Salary, roll):
        super().__init__(roll)
        self.salary = Salary

acc1 = Accountant(50_000, "CA")

print(f"Employee 1 getting salary of {acc1.salary} and his roll is {acc1.roll}. His shift end at {acc1.Shift_end}")

# By Super() we call the parent class constructer