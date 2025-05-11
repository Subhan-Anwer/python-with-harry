# Write a class “Calculator” capable of finding square, cube and square root of a number.

from simple_chalk import green

class Calculator:
    def __init__(self, number: int):
        self.number = number
    
    def find_square(self):
        print(f"square of {self.number} is: {green(self.number * self.number)}")
        
    def find_cube(self):
        print(f"cube of {self.number} is: {green(self.number * self.number * self.number)}")
        
    def find_square_root(self):
        
        
        print(f"square root of {self.number} is: {green(self.number ** 0.5)}")
            
number1 = Calculator(5)
number1.find_square()
number1.find_cube()
number1.find_square_root()
