class Man:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        
    def eat(self):
        print(f"{self.name} is eating...")
        
    def show_weight(self):
        print(f"{self.name}'s weight is {self.weight} kg")
    
    def show_height(self):
        print(f"{self.name}'s height is {self.height}")
        
class SuperMan(Man):
    super_power = "fly"
     
subhan = SuperMan("Subhan", 180, 75)
print(subhan.name)
subhan.eat()
print(subhan.super_power)
