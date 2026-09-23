class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}"

developer = Developer("Developer", 10000, None)
print(developer.info())