# Q2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
#     “The name of the student is Harry, his marks are 72 and phone number is 99999888”

print("Please Enter you details below \n")

name = input("Name: ").capitalize()
marks = int(input("Marks: "))
phone_no = input("Phone Number: ")


# Using old school format method
print("The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_no))

# Using f-string
print(f"The name of the student is {name}, his marks are {marks} and phone number is {phone_no}")