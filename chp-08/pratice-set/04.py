# Write a recursive function to calculate the sum of first n natural numbers.

def sum_func(n):
    if (n == 0):
        return 0
    return n + sum_func(n - 1)
    
print(sum_func(int(input("Enter num to sum: "))))