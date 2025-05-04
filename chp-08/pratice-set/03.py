# How do you prevent a python print() function to print a new line at the end.

# By Default python print() function's parameter "end" is set to \n and it prints a next line,
# if we want to prevent the printing of next line we can set end=" "


# Default behaviour
print("Hello Subhan")
print("Have a Good Day")


# not printing next line using end parameter

print("Hello Subhan", end=" - ")
print("Have a Good Day")