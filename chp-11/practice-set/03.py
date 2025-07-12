# Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    def __init__(self, name: str):
        self.name: str = name
        self.salary: int = 25000
        self.contract: str = "Your starting salary is $25,000 and after two months you will get increment of $10,000"
        self.months_completed: int = 0
        self.increment_amount: int = 10000
        
    def increment(self):
        if self.months_completed == 2:
            self.salary = self.salary + self.increment_amount
            print(f"your Salary is incremented by {self.increment_amount}")
        else:
            print(f"{self.name}, Your increment time in contract is not completed yet")
            
    @property
    def salary_after_increment(self):
        print(f"Salary after increment will be: {self.after_increment}")
        
    @salary_after_increment.setter
    def salary_after_increment(self):
        self.after_increment = self.salary_after_increment + self.increment_amount

subhan = Employee("Subhan Sheikh")

print(subhan.contract)
print(f"Your Current Salary is: {subhan.salary}")

subhan.months_completed += 1    # 1 month completed at job!
subhan.increment()
print(f"Your Current Salary is: {subhan.salary}")

subhan.months_completed += 1    # 2 month completed at job!
subhan.increment()
print(f"Your Current Salary is: {subhan.salary}")
