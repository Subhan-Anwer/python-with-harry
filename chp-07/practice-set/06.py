num = int(input("Enter a number to find its factorial: "))

n = 1

for i in range(1, num+1):
    n = n * (i)
    
    
print(f"Factorial of {num} is {n}")