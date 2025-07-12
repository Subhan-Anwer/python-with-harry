# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animal:
    def __init__(self, animal_type, name, food, residence):
        self.animal_type = animal_type
        self.name = name
        self.food = food
        self.residence = residence
    
    def get_info(self):
        print(f"my {self.animal_type}'s name is {self.name} and he eats {self.food}. {self.name} is a {self.residence} animal")
        
class Pet(Animal):
    def __init__(self, animal_type, name, food, residence):
        super().__init__(animal_type, name, food, residence)
    
    def high_five(self):
        print(f"give me a high five {self.name}")

class Dog(Pet):
    def __init__(self, name, food, residence):
        super().__init__(animal_type="Dog", name=name, food=food, residence=residence,)
        
        
    def bark(self):
        print("woof woof!")
    
buddy = Dog("Buddy", "parle-g", "land")
buddy.get_info()
buddy.high_five()
buddy.bark()