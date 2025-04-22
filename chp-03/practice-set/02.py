# Write a program to fill in a letter template given below with name and date.

name = input("Enter name: ")
date = input("Enter date: ")
letter = f"Dear {name},\nYou are selected!\n{date}"
print(letter)