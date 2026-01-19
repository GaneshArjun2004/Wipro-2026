class Apple():
    def a(self):
        print('1.apple')

class Mango(Apple):
    def b(self):
        print('2.mango')

class banana(Mango):
    def c(self):
        print('3.banana')

obj = banana()
obj.b()
obj.c()
obj.a()

"""class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(B):
    def c(self):
        print("C")
c1 = C()
c1.a()
c1.b()
c1.c()"""