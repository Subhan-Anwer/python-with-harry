# Tuple are also like list and can store set of different datatypes and values 
# but the difference is list is mutable / changeable and on the other hand tuple is immutable / unchangeable.

# The syntax difference between both is brackets. list uses sqaure brackets [] and tuple uses round brackets () note that in both the values are separated by comma ,

my_tuple = ("Subhan", 1, False, 34.65, "Rohan" , "Apna College", "Code with Harry")

# if you want to create an empty tuple you can create it like this:
empty_tuple = ()
# let me prove it to you by printing its type
print(type(empty_tuple))

# And if you want to create a tuple with single value and you just write it like this
single_tuple = (1) 
# Or
single_tuple_2 = ("Subhan")
print(type(single_tuple), "2:", type(single_tuple_2))

# python will count it as integer or string but if you dont want this just add comma "," after the value like this
sngl_tuple = (1,) 
sngl_tuple_2 = ("Subhan",)
print(type(sngl_tuple), "2:", type(sngl_tuple_2))