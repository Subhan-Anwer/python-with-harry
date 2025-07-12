class Employee:
    salary = 10
    
    
    def show_salary(self):
        print(f"The salary is {self.salary}")
        
noman = Employee()
noman.show_salary()
noman.salary = 12
noman.show_salary()

# the above code prints instance value if changing occurs in objec 
# but if you want to use the class variable value you can do this with @classmethod decorator

class Designer:
    salary = 45000
    
    @classmethod # just use this decorator before the function which is using class value
    def show_salary(cls):
        print(f"The salary is {cls.salary}")
        
subhan = Designer()
subhan.show_salary()
subhan.salary = 72000
subhan.show_salary() # prints the class variable value 45000 not the instance value