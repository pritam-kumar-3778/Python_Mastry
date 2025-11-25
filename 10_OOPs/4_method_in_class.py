class student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_course(self):
        return self.course


stu1 = student("pritam", "MCA")
stu2 = student("Anurag", "MSC CMB")
stu3 = student("Soumya", "MSC CS")

# Call teh function
print(f"{stu1.name} is study the course {stu1.get_course()}")