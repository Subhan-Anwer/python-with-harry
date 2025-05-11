# Create a class “Programmer” for storing information of few programmers working at Microsoft.

from simple_chalk import green

class Programmer:
    def __init__(self, name: str, role: str, technology: str, team: str, salary: int, timing: str):
        self.name = name
        self.role = role
        self.technology = technology
        self.team = team
        self.salary = salary
        self.timing = timing
        
    def getInfo(self):
        print(f"{green(self.name)} is working at Microsoft with {green(self.team)} team as a {green(self.role)}. {self.name} have mastered {green(self.technology)} with years of experience. His salary is {green(self.salary)} and timings are {green(self.timing)}.")
        
        
programmer_1 = Programmer("Subhan Anwer", "Front end Developer", "Next Js", "Web Development", 50000, "10 to 5")

programmer_1.getInfo()