# Multiple Inheritence

# Class 1
class Teacher:
    def __init__(self, Salary):
        self.Salary = Salary

# Class 2
class PHD_Student:
    def __init__(self, year):
        self.year = year

class TA(Teacher, PHD_Student):
    def __init__(self, Salary, year, name):
        super().__init__(Salary)
        PHD_Student.__init__(self, year)
        # When we have to call the constructor of two parent class call them like this
        self.name = name

ta1 = TA(90_000, "2nd", "Pritam")

print(ta1.name, ta1.Salary, ta1.year)