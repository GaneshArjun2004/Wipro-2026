class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name, self.roll)


s1 = Student("Arjun", 1)
s2 = Student("Kiran", 2)

s1.display()
s2.display()
