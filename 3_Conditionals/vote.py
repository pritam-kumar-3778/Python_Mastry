age = int(input("Enter your age: "))

if(age <= 0):
    print("Invalid age entered.")
elif(age < 18):
    print("You are not eligible to vote.")
elif(age == 18):
    print("You are eligible to vote for the first time.")
else:
    print("You are eligible to vote.")