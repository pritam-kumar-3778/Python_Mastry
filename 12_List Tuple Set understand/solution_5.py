# 5 : List Student enroll in CS

info = [
    ("Pritam", "Math"),
    ("Sritam", "English"),
    ("Pritesh", "Math"),
    ("Sakhi", "Science"),
    ("Anurag", "Biology"),
    ("Soumya", "CS"),
    ("Pratyush", "CS"),
]

for name,course in info:
    if(course == "CS"):
        print(name)