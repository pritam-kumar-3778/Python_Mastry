# get methods returns the key according to the value

Student = {
    "name" : "Pritam Kumar Patel",
    "Submarks" : {
        "Math" : 95,
        "Science" : 90,
        "English" : 85
    }
}

print(Student.get("name"))
# in this senario if we put wrong key it will return None
print(Student.get("nam"))  # This will return None

# We can also get same thing by using square brackets   
print(Student["name"])
# If we put wronng key in get method it will show key-error
# Eg :- print(Student["nam"])  # This will raise KeyError