# Add a static method in class, to greet the user with hello.

class Static_method:
    def __init__(self, user):
        self.user = user
    
    @staticmethod
    def say_hello():
        print(f"Hello user")
        
person = Static_method("Subhan")
person.say_hello()