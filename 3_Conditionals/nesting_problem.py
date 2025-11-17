# Simple user and password validation

user = input("Enter your User name : ")
Pass = input("Enter your password : ")

if(user == "Admin" and Pass =="12345") :
    print("Login Successful")
else :
    if(user != "Admin"):
        print("Invalid Username")
    else :
        print("Invalid Password")