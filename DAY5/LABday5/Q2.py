#polymorphism

class Calculator:
    def calculate(self, a, b):
        print("Addition:", a + b)

# Method Overriding
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("Multiplication:", a * b)

# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(self.x, self.y)

calc = Calculator()
adv_calc = AdvancedCalculator()

calc.calculate(10, 5)
adv_calc.calculate(10, 5)

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
p3.display()
