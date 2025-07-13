# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

def divide_func():

    try:
        a : int = int(input("Enter number one: "))
    except ValueError:
        print("Enter a valid number!")
        return
    try:
        b : int = int(input("Enter number two: "))
    except ValueError:
        print("Enter a valid number!")
        return
    
    print("numbers successfully entered, dividing...")
    
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    except ZeroDivisionError:
        print("Infinite!")
        return
    except Exception as error:
        print(f"unexpected error: {error}")
        return
    finally:
        print("Divide Program Made By Subhan")
        
divide_func()