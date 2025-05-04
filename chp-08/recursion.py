# Recursion is the function which call itself in side the function


def factorial (n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))