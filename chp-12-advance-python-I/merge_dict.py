dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = dict1 | dict2
print(merged_dict)

# you can merge dictionaries using the '|' operator
# if the dictionaries merging have the same variable then the last variables value will be considered

# for example: dict 1 have b= 2 and dict 2 have b = 3
# the merged dictionary will have b = 3

# dictionary merging with |= operator
dict1 |= dict2
print(dict1)

# this will update dict1 with dict2 values