# Write a python function to print first n lines of the following pattern:

# *** 
# **               
# * - for n = 3 

def n_pattern(n):
    if(n == 0):
        print("Function ended!")
    else:
        print(n*"*")
        n_pattern(n-1)
    

num = int(input("Enter a number: "))
n_pattern(num)