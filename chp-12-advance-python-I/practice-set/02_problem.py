# Write a program to print third, fifth and seventh element from a list using enumerate function.

my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for index, value in enumerate(my_list):
    if index in (2, 4, 6):
        print(f"Element no {index + 1} is '{value}'")