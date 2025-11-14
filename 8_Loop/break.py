i = 1

while i <= 5:
    if (i == 4):
        break
    print(i)
    i += 1

print("Example of break statement in while loop")

# Search for a number x in this tuple using loops
# (1,4,9,16,25,36,49,64,81,100)

tuple_numbers = (1,4,9,16,25,36,49,64,81,100)
x = 16
idx = 0

while idx < len(tuple_numbers):
    if tuple_numbers[idx] == x:
        print("Found at index:", idx)
        break
    else:
        print("Not found at index:", idx)
    idx += 1
# If we don't use break here it will print "Not found at index:" for all indices after the found index.

print("End of the loop")