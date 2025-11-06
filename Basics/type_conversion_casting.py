a = 2
b = 3
print ((type)(a) )         # Output: <class 'int'>
print ((type)(b)  )        # Output: <class 'int'>

print (a + b)               # Output: 5

c = "5"
print ((type)(c)  )        # Output: <class 'str'>
# print (a + c)             # This will raise a TypeError
print (a + int(c))        # Output: 7