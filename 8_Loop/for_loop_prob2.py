# Search for a number x in a tuple using loop

tup = (5, 10, 15, 20, 25, 20)

x = 20
idx = 0

for el in tup:
    if (el == x):
        print("Element found:", idx)
    idx += 1

# Here it print both index of 20 in the tuple
# if we want to print one time then we usse break.