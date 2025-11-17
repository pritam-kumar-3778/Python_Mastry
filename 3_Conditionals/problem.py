# Simple user and password validation

user = input("Enter your User name : ")
Pass = input("Enter your password : ")

if(user == "Admin" and Pass =="12345") :
    print("Login Successful")
elif (user != "Admin" and Pass!="12345") :
    print("Invalid user name and Password")
elif (user != "Admin") :
    print("Invalid User name")
else : 
    print("Invalid Password")