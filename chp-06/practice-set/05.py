from simple_chalk import red , green

# Write a program which finds out whether a given name is present in a list or not.

name_list = ["Ali", "Muhammad", "Bilal", "Hamza"]
user_name = input("Search a name: ")

if (user_name == name_list[0]):
    print(green(f"{user_name} found in the list"))
elif (user_name == name_list[1]):
    print(green(f"{user_name} found in the list"))
elif (user_name == name_list[2]):
    print(green(f"{user_name} found in the list"))
elif (user_name == name_list[3]):
    print(green(f"{user_name} found in the list"))
else :
    print(red(f"{user_name} does not found in the list"))