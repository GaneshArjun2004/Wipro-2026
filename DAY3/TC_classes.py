class student:
    name = "suresh"
    age = 25
    section1 = "c"
s1=student()
print(s1.name)
print(s1.age)
print(s1.section1)

class employee:
    def __init__(self,name,age,section1):
        self.name = name
        self.age = age
        self.section1 = section1
e1=employee('sam',20,'b')
print(e1.age,e1.name,e1.section1)        
