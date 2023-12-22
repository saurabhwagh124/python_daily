def decor1(func):
    print("In decorator 1")
    def wrapper():
        print("Start wrap1")
        func()
        print("End wrap1")
    return wrapper

def decor2(func):
    print("In decorator 2")
    def wrapper():
        print("Start wrap2")
        func()
        print("End wrap2")
    return wrapper

@decor2
@decor1
def normal_func():
    print("In normal function")

normal_func()
