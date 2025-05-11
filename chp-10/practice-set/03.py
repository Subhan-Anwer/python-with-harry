# Create a class with a class attribute a; create an object from it and set ‘a’ directly using Create a class with a class attribute a; create an object from it and set ‘a’ 

class Attribute:
    a = 10
    
object = Attribute()
object.a = 11
print(object.a)

# YES! it will change because instance attribute take preference over class attribute