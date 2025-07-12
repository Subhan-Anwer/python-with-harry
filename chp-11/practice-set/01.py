# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
import math

class Vector_2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        print(math.sqrt(self.x**2 + self.y**2))
        
    def __str__(self):
        print(f"2D Vector: {self.x}, {self.y}")

class Vector_3D(Vector_2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def magnitude(self):
        print(math.sqrt(self.x**2 + self.y**2 + self.z**2))
        
    def __str__(self):
        print(f"3D Vector: {self.x}, {self.y}, {self.z}")
    
    
photoshop = Vector_2D(5, 2)
photoshop.magnitude()
photoshop.__str__()

illustrator = Vector_3D(5, 8, 12)
illustrator.magnitude()
illustrator.__str__()