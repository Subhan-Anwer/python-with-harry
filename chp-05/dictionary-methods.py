marks = {
    "Subhan" : 100,
    "Talha" : 20,
    "Ayan" : 58,
    "Shubham" : 69,
    "isSubhanGoat" : True,
}

# print(marks.items()) # prints all the key value pairs as tuples

# print(marks.keys()) # prints all the keys

# print(marks.values()) # prints all the values


# Updating method
marks.update({"Subhan" : 99}) # if key is matching with an existing key the value will be updated otherwise it will be added as a new key value pair
# print(marks)


# getting value of specific key
# print(marks.get("Talha"))


# Most important thing
# you can use dict.get("key") method and also dict["key"] method but what is the difference,


# The difference is :

# print(marks.get("Ayan"))
# print(marks["Ayan"])

# when using correct key both method will give the same output but if you use wrong key

print(marks.get("Ayaan")) # it will print None
print(marks["Ayaan"]) # but it throws KeyError