def greet(name):
    msg = f"Have a Good Day {name}!"
    return msg

a = greet("Harry bhai")
# print(a)

# print(greet("Subhan Sheikh"))

# Default Parameter Value

def hello(name = "Subhan sahb"):
    print(f"Hello {name}.")
    
# if we pass arguement the name will change to that otherwise it will be default set value which is Subhan sahb

# hello() # Hello Subhan sahb.
hello("Jamal bhai")