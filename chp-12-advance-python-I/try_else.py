try:
    a = int(input("Enter a number: "))
    print("You entered:", a)
except Exception as e:
    print("An error occurred:", e)
else:
    print("The operation was successful.")
    
    
# in try else clause else will run if no exception (error) occurs