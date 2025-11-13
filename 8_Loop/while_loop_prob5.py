# Search for a number x in this tuple using loops
# (1,4,9,16,25,36,49,64,81,100)

tuple_numbers = (1,4,9,16,25,36,49,64,81,100)
x = 16
idx = 0

while idx < len(tuple_numbers):
    if tuple_numbers[idx] == x:
        print("Found at index:", idx)
    else:
        print("Not found at index:", idx)
    idx += 1