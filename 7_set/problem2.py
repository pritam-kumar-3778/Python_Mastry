# Figure out a way to store 9 and 9.0 as separate values in the set.
# (You can take help of built in data types.)

values = {9, 9.0, 8, 8.25}
print(values)
# By this way we can't store 9 nd 9.0

# One way to store them separately is to use different data types
values = {9, "9.0", 8, 8.25}
print(values)

# Another way is to use a tuple to store one of the values
values = {9, (9.0,), 8, 8.25}
print(values)

# or
values = {
    (9, 'int'),
    (9.0, 'float'),
    (8, 'int'),
    (8.25, 'float')
}
print(values)