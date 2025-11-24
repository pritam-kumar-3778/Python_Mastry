# 2 : List all unique Course

info = [
    ("Pritam", "Math"),
    ("Sritam", "English"),
    ("Pritesh", "Math"),
    ("Sakhi", "Science"),
    ("Anurag", "Biology"),
    ("Soumya", "CS"),
    ("Pratyush", "CS"),
]

unique_couese = set()  # Empty set created

for el in info:
    unique_couese.add(el[1])

print(unique_couese)


# set always conscider one value