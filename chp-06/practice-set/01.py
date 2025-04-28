nmbr_1 = int(input("Enter number 01: "))
nmbr_2 = int(input("Enter number 02: "))
nmbr_3 = int(input("Enter number 03: "))
nmbr_4 = int(input("Enter number 04: "))

if (nmbr_1 > nmbr_2 and nmbr_1 > nmbr_3 and nmbr_1 > nmbr_4): # checking if nmbr_1 is great than other
    print(f"{nmbr_1} is the greatest number")
elif (nmbr_2 > nmbr_1 and nmbr_2 > nmbr_3 and nmbr_2 > nmbr_4): # checking if nmbr_2 is great than other
    print(f"{nmbr_2} is the greatest number")
elif (nmbr_3 > nmbr_1 and nmbr_3 > nmbr_2 and nmbr_3 > nmbr_4): # checking if nmbr_3 is great than other
    print(f"{nmbr_3} is the greast number")
elif (nmbr_4 > nmbr_1 and nmbr_4 > nmbr_2 and nmbr_4 > nmbr_3): # checking if nmbr_4 is great than other
    print(f"{nmbr_4} is the greast number")
else:
    print("Please try again with valid number")