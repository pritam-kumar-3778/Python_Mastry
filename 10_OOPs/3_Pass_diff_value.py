class student:
    def __init__(self, name, course): # Parameterized constructor , Instance attribute
        self.name = name # Instance attribute
        self.course = course # Instance attribute

stu1 = student("pritam", "MCA")
stu2 = student("Anurag", "MSC CMB")
stu3 = student("Soumya", "MSC CS")

print(stu1.name, stu1.course)
print(stu2.name, stu2.course)
print(stu3.name, stu3.course)