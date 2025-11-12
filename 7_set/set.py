collections = {1,2,3,4, "abc", (1,2,3)}

print(type(collections)) # Output: <class 'set'>
print("Elements of the set:", collections)


# If we put duplicate elements, it will ignore the duplicates, not showing ny error.
set_with_duplicates = {1,2,3,4, "abc", (1,2,3), 2, 3, "abc"}
print("Set with duplicates (duplicates ignored):", set_with_duplicates)

# length also ignore dupplicate items
print(len(set_with_duplicates))