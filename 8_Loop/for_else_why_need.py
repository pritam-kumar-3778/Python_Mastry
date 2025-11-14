# Why else is needed in for loop
str = "pritam"
for el in str:
    if (el == 't'):
        print("t is found")
        break
    print(el)
else:               
    print("for loop is ended")

# In the above code, else block will not be executed because loop is terminated by break statement.
# If we remove the break statement, then else block will be executed after the loop ends normally.
# So, else block in for loop is useful to execute a block of code when the loop completes normally without encountering a break statement.
