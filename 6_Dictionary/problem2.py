# WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one.
# Use subject name as key and marks as value.

marks = {}
x = int(input("Enter python marks: "))
marks.update({"python": x})
y = int(input("Enter java marks: "))
marks.update({"java": y})
z = int(input("Enter c marks: "))
marks.update({"c": z})

print("Marks obtained in 3 subjects:", marks)
