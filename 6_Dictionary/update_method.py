# Update methods insert the specified items to the dictionary

Student = {
    "name" : "Pritam Kumar Patel",
    "Submarks" : {
        "Math" : 95,
        "Science" : 90,
        "English" : 85
    }
}

# insert new key-value pair, age
Student.update({"age":21}) # It is same as Student["age"] = 21
print(Student)

# We can also store like this
# new_dit = {"age":21, city :"Jharsuguda"}
# Student.update(new_dit)
# print(Student)