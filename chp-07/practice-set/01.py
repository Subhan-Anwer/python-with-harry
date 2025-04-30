# Write a program to print multiplication table of a given number using for loop.


# first i will do it with while loop

table = int(input("Enter a number to see its table: "))

i = 1
while i < 11:
    print(f"{table} x {i} = {table*i}")
    i += 1
    

# Now i will do it with for loop

user_table = int(input("Print a table: "))
for i in range(1, 11):
    print(f"{user_table} x {i} = {user_table*i}")