class A:
    def showA(self):
        print('parent a')

class B:
    def showB(self):
        print('parent b')


class C(A,B):
    pass                

c = C()
c.showA()
c.showB()