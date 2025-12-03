# Class attribute and Instance attribute
class student:
    College_Name = "ABC Colege"  # class attribute

    def __init__(self, name, roll, cgpa): # Instance attribute
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

stu1 = student("Pritam", 101, 9.8)
stu2 = student("Sritam", 102, 9.5)

print(stu1.name, stu1.College_Name)
# We can access class attribute by object name or class name
# Object having heigher priority bcz we access both attribute (Class and instance) by object 
# class attribute only be accessiable with class name

print(stu2.name, student.College_Name)


# Instance attribute havig heigher priority when both instance  and class attribute will same and we invoke by object.