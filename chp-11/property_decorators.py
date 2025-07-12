class Designer:
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @name.setter
    def name(self, value):
        self.first_name = value.split(" ")[0]
        self.last_name = value.split(" ")[1]
        
        
subhan = Designer()


subhan.name = input("Enter your Full Name: ")
print(subhan.name)
print(f"first: {subhan.first_name}, last: {subhan.last_name}")