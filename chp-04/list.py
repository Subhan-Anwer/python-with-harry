
# list is a set of multiple values separated by comma ","

listEx = ["Apple", "Ball", "Cat", "Dog", "Elephant", "Frog"]



# List can hold different data type:

dataList = ["Apple", 10, "banana", 305.69, False]


# Strings are immutable means we cannot change them we used method but it will result in new string and the original string remains same.
# But unlike strings, list are mutable. Let me show you an example:

print("Before:",listEx[3]) # before

listEx[3] = "Dragon" # changing the value of 3rd index in list

print("After:",listEx[3]) # after