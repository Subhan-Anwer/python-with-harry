a = "Subhan" # type is string (str)
print(type(a)) # <class 'str'>

b = 5 # type is integer (int)
print(type(b)) # <class 'int'>


# How to change type
# you can change the type of a variable using the built-in functions int(), float(), str(), etc if the conversion is valid.
# for example:

a = "31.5" # type is string (str)
print("Before conversion: ",type(a)) # <class 'str'>
a = float(a) # type is converted float (float)
print("After conversion: ",type(a)) # <class 'float'>

# it can only happen if the conversion is valid.

# for example:
a = "Hello" # type is string (str)
print("Before conversion: ",type(a)) # <class 'str'>
a = int(a) # type cannot be conveted to int (int)
print("After conversion: ",type(a)) # error