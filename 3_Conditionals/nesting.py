#nesting conditionals

age = int(input("Enter your age: "))

if (age >= 18):
    if (age >= 70):
        print("You can't drive.")
    else:
        print("You can drive.") 
elif (age <= 0):
    print("Invalid age entered.")
else:
    print("You can't drive.")