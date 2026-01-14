#1.ImportError
# 
class PositiveSalary:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Salary must be a positive number!")
        self._value = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete salary attribute")

class Employee:
    salary = PositiveSalary()   # attach descriptor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
# 2.Valid employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 75000)

print(f"{emp1.name} earns {emp1.salary}")
print(f"{emp2.name} earns {emp2.salary}")

# 3.Invalid employee (negative salary)
try:
    emp3 = Employee("Charlie", -10000)
except ValueError as e:
    print("Error:", e)
