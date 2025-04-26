# set is also a data collection but its for values only not for key value pair like in dictionary.
# syntax is also same both uses curly brackets {}. in set order is not maintained

my_set = {100, 54, 64, 65, 365, 6874 , 534 }

# if you want to create an empty set and do it like this:
e_set = {}
# print(type(e_set)) # printing its type
# python will count it as dictionary data type

# to make a empty set you hace to do this
empty_set = set()
# print(type(empty_set)) # confirming its type


# also set contains only unique value and removes all same occurence except first in the set, not trusting me ? heres the prove
sett = {1, 99, 5, 56, 67, 69, 99, 99, 99, 99, 99}
print(sett)