# USING FORMAT()


a = 5
b = 10
sum = a + b

# Normal Formation
print("Sum of a and b is {}".format(sum))
print("I am learning {}".format("Python"))

# Multiple place holder
print("Sum of {} & {} is {}".format(a,b,sum))   # Sum of 5 and 10 is 15

# Index based
print("Sum of {1} & {0} is {2}".format(a,b,sum))  # Sum of 10 and 5 is 15

# Value based
print("My name is {fname}, I'm {age}".format(fname = "John", age = 36))

# {} -- > Placeholder