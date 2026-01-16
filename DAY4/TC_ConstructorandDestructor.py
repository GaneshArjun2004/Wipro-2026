class employee:
    def __init__(self,name):
        self.name = name
        print("constructor")
    def __del__(self):
        print("destructor")

e = employee("s")        