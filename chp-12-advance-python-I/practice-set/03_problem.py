# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_number = int(input("Enter a number: "))

multiplication_list = [user_number*x for x in my_list]

print(f"\nPrinting the table of {user_number}... \n")

print(multiplication_list)