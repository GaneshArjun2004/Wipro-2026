def newdec(func):
    def wrapper():
        print("before calling function")
        func()
        print("after calling function" )
    return wrapper

@newdec
def sayhello():
    print('hello')
sayhello()        
