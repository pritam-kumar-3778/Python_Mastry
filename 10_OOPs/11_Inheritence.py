# Re-use of attributes and methods from a parent/base class

# Single level Inheritence

# Base Class
class Employee:
    Shift_start = "10 AM"
    Shift_end = "4 PM"

# Derived Class
class Teacher(Employee):
    def __init__(self, subjects):
        self.subjects = subjects

t1 = Teacher("Math")
t2 = Teacher("Computer Science")

print(f"Teacher 1 teach the {t1.subjects}. His Shift start at {t1.Shift_start} and end at {t1.Shift_end}")