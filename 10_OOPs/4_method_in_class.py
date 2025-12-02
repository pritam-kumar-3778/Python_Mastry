class student:
    def __init__(self, name, course):  # Instance attribute, Parameterized constructor
        self.name = name # Instance attribute
        self.course = course # Instance attribute

    def get_course(self): # Instance Method
        return self.course # Instance Method


stu1 = student("pritam", "MCA")
stu2 = student("Anurag", "MSC CMB")
stu3 = student("Soumya", "MSC CS")

# Call teh function
print(f"{stu1.name} is study the course {stu1.get_course()}")