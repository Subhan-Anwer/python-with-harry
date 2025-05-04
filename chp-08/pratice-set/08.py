# Write a python function to print multiplication table of a given number.
given_number = int(input("give a number: "))

def multiplication(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        
multiplication(given_number)