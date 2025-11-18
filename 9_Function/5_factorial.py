# WAP to print factorial of 'n'
# 5 factorial menas 1*2*3*4*5 = 120

def cal_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        
    return fact
    

print(cal_factorial(5))