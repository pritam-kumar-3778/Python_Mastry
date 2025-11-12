collection = set()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2)

print(collection)

# removing element
collection.remove(3)
print("After removing 3:", collection)

# If we try to remove an element which is not present, it will raise an keyerror
# collection.remove(5)  # Uncommenting this line will raise KeyError