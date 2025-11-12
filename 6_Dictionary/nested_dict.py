Student = {
    "name" : "Pritam Kumar Patel",
    "Submarks" : {
        "Math" : 95,
        "Science" : 90,
        "English" : 85
    }
}

print("Student Name is:", Student["name"])
print("Marks in Math:", Student["Submarks"]["Math"])

# Update Science marks to 92
Student["Submarks"]["Science"] = 92
print("Updated Marks in Science:", Student["Submarks"]["Science"])