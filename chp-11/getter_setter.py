class Person:
    def __init__(self, age):
        self._age = age  # private (by convention)

    @property
    def age(self):
        return self._age  # getter

    @age.setter
    def age(self, value):
        self._age = value  # setter

subhan = Person(19)
print(subhan.age)
subhan.age = 21
print(subhan.age)