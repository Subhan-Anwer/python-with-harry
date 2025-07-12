# Walrus Operator

if (n := len([1, 2, 3, 4])) > 3:
    print(f"List is longer than 3, length: {n}")

# This code uses the walrus operator to assign the length of a list to a variable
# assigning the value to `n` while also checking if it is greater than 3.
# and the value assigned to `n` is the length of the given list. and `n` can be used in print statement.

# if we are dont use walrus operator (:=), then we have to first assign the value to `n` and then check the condition.
# n = len([1, 2, 3, 4])
# if n > 3:
#     print(f"List is longer than 3, length: {n}")

print(" ")
print("-------------------------------------------")
print(" ")

# More enhanced example

from simple_chalk import red, green, yellow

if (n := len([1, 2, 3, 4, 5, 6])) > (l := 5):
    print(green(f"List is longer than {l}, length: {n}"))
elif n == l:
    print(yellow(f"List is equal to {l}, length: {n}."))
else:
    print(red(f"list is shorter than {l}, length: {n}."))