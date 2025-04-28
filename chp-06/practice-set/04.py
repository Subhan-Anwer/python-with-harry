from simple_chalk import red , green , yellow


# Write a program to find whether a given username contains less than 10 characters or not.


username = input("Enter you username: ")

if (len(username) < 10): # if length of username is less than 10 print in green
    print(green(f"{username} contains less than 10 characters"))
    print("length of username is:", len(username))
    
elif (len(username) == 10): # if length of username is equal to 10 print in yellow
    print(yellow(f"{username} is 10 characters long"))
    print("length of username is:", len(username))
    
elif (len(username) > 10): # if length of username is greater than 10 print in red
    print(red(f"{username} is greater than 10 characters"))
    print("length of username is:", len(username))
else :
    print("Unexpected error occured")