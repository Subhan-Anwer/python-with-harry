a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Are you stupid or what? You can't divide by zero!")
else:
    print(f"{a} / {b} = {a / b}")