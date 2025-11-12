# items methods returns (key, value) pairs as tuples of the dictionary

Student = {
    "name" : "Pritam Kumar Patel",
    "Submarks" : {
        "Math" : 95,
        "Science" : 90,
        "English" : 85
    }
}

print(Student.items())

# we can access items one by one
pairs = list(Student.items())
# Access first item
first_item = pairs[0]
print("First item (key, value):", first_item)