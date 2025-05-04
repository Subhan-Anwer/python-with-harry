# if we are using the same logic again and again we make a function and call it whenever we have to write that logic

# def is a keyword used to define function, it should be write before the name of function 

def func1():
    a = int(input("Num 1: "))
    b = int(input("Num 2: "))
    c = int(input("Num 3: "))
    
    print("average is:", (a + b + c) / 3)
    

# Calling the function, without calling it will not run

func1()