class Person:
    def __init__(self, name, date_birth):
        self.name = name
        self.date_birth = date_birth

    def age(self):
        a = 2024 - self.date_birth
        return a


age1 = Person('Михаил', 1986)
print(age1.age())