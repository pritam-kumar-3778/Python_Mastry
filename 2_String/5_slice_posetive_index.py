str = "Pritam Kumar Patel"

print(str[:6])  # Same as str[0:6], Output: Pritam
print(str[7:10])  # Output: Kum
print(str[13:]) # same as str[13:str[len(str)], Output: Patel
print(str[:])  # Output: Pritam Kumar Patel