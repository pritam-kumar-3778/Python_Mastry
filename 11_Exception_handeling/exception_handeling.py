try:
    x = int(input("Enter x : "))
    ans = 10/x

except ZeroDivisionError:
    print("Devided by zero is not allowed")

except ValueError:
    print("Invalid Input")

else:
    print(f"Ans = {ans}")    

finally:
    print("End of this program")


# A number devided by zero is called ZeroDivisionError in python
# A number devided by a siring is called ValueError in python.
# It is a possible senario when we devided 10 by x.
# User may input zero or string for devide

# We can create multiple except block depending upon the possibility of error occur.

# Main poeration in try block
# Possibilities of error in except block
# Final correct output statement in else block

# Even error occurr or not we run a part of the program then we write that in finally block