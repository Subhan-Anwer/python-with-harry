name = "subhan"

print(len(name)) # prints length of string
print(name.endswith("han")) # return true or false based on argument passed, in this case its true.
print(name.startswith("Su")) # just like endswith() but it checks starting of string
print(name.count("b")) # counts how many times "b" is present in string
print(name.capitalize()) # capitalize first letter
print(name.upper()) # capitalize/uppercase all letter
print(name.find("a")) # find index of letter
print(name.replace("ubh", "aub")) # replaces "u" with "o"
print("    Hell o  -   World  !   ".strip()) # removes leading and trailing spaces