# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class ComplexNum:
    def __init__(self, n, n2):
        self.n = n
        self.n2 = n2
    
    def __add__(self, number):
        return self.n + number.n , self.n2 + number.n2
    
    def __mul__(self, number):
        return self.n * number.n , self.n2 * number.n2
    
numbr1 = ComplexNum(2, 4)
numbr2 = ComplexNum(3 , 4)

sum = numbr1 + numbr2
print(sum)
mult = numbr1 * numbr2
print(mult)