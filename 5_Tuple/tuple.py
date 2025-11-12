tup = (2,5,4,7,5,9,3,)
# check the type
print(type(tup))

# Acceess the elements
print("First element:", tup[0])
print("Last element:", tup[-1])

# Slicing
print("Sliced tuple (1 to 4):", tup[1:5])

# Tuple concatenation
tup2 = (10, 11, 12) 
combined_tup = tup + tup2
print("Concatenated tuple:", combined_tup)

# Tuple repetition
repeated_tup = tup * 2
print("Repeated tuple:", repeated_tup)

# Tuples are immutable, so the following line would raise an error if uncommented
# tup[1] = 6