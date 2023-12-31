class Demo:
    
    def __init__(self):
        print("In constructor")

    def __del__(self):
        print("In destructor")

def fun():
    print("in fun")
    obj = Demo()
    return obj


ins = fun()
print("End of code")
