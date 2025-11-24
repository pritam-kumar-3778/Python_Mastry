# 6 : create dictionary (student, set of courses)

info = [
    ("Pritam", "Math"),
    ("Sritam", "English"),
    ("Pritesh", "Math"),
    ("Pritesh", "Science"),
    ("Anurag", "Biology"),
    ("Pritam", "CS"),
    ("Pratyush", "CS"),
]

# Create a empty dictionary
dict = {}

for name, course in info:
    if(dict.get(name)==None):   # If name not present in the dictionary
        dict.update({name: set()}) # Update the dictionary by name and an empty set
        dict[name].add(course) # Then add the course in the name
    else:
        dict[name].add(course) # If name present at the dictionary then add the course

print(dict)