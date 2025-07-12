from simple_chalk import green

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)
    
class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def get_language(self):
        print(self.language)
    
class Manager(Programmer):
    def __init__(self, name, language, role):
        super().__init__(name, language)
        self.role = role
        
    def get_info(self):
        print(f"Name: {green(self.name)}, Language: {green(self.language)}, Role: {green(self.role)}")
        
subhan = Manager("Subhan", "Python", "Manager")

subhan.get_info()