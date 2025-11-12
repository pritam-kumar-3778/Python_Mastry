my_info = {
    "name" : "Pritam Kumar Patel",
    "age" : 24,
    "city" : "Jharsuguda",
    "profession" : "Software Ingineer",
    "experience in year" : 1.8,
    "technology" : ["Python", "SQL"]
}

print("My name is:", my_info["name"])
print("My age is:", my_info["age"])
print("I live in:", my_info["city"])
print("My profession is:", my_info["profession"])
print("My experience in year is:", my_info["experience in year"])
print("Technologies I know are:", my_info["technology"])


# Add a new key-value pair for company
my_info["company"] = "VTS"
print("My company is:", my_info["company"])

# Change my age to 25
my_info["age"] = 25
print("My updated age to be:", my_info["age"])

# add a new technology 
my_info["technology"].append("Advanced SQL")
print("Updated technologies I know are:", my_info["technology"])

# Remove city from the dictionary
my_info.pop("city")
print("City key-value pair removed.")

print("Complete information:", my_info)