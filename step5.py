class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def raise_salaries(self, salary):
        self.salary = self.salary + salary
        return self.salary


employee = Employee("Михаил", "Web-программист", 45000)
print('Вам повысили зарплату до', employee.raise_salaries(5000))
