class Employee: # class is a keyword and Employee is the name of class, always write first letter capital of class name its a practice.
    def __init__ (self, namee , salaryy, languagee):
        
        self.name = namee
        self.salary = salaryy
        self.language = languagee
        
    def increment(self, ):
        self.salary += self.salary * (10 / 100)
    
subhan = Employee("Subhan bhai", 1200000, "Python")

print("Salary before:", subhan.salary)

subhan.increment()
print("Salary after:", subhan.salary)