# if (1 + 1 == 2): # if conditionl is True
#     print ("yes")
# elif(2 + 2 == 4) : # if condition2 is True
#     print ("no" )
# else: # otherwise
#     print ("maybe")
    

day = input("whats the day: ").capitalize() # taking the input of day and capitaizing first letter.

if (day == "Sunday"):
    print(f"It's {day}, Time to play PUBG yay🎉!") # if user enter sunday in input this code will run
elif (day == "Saturday"):
    print(f"It's {day}, we'll play PUBG tomorrow") # if user enter saturday in input this code will run
else:
    print(f"It's {day}, we'll play PUBG on Sunday let's focus on work today.") # if enter any other day this code will work