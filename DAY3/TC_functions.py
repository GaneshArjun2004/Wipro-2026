def add(a,b):
    print(a+b)
def sub(a,b):
    return a-b,a

add(10,20)
print(sub(100,20))    


def hello(greeting = "hello", new="world"):
    print("%s,%s"%(greeting,new))
hello()    
hello('greetings','deepa')

def printparam(*params):
    print(params)
printparam('test','python')
printparam(1.2, 3,4,5,6)
def new_param(**params):
    print(params)
new_param(x=1,y=2)    
