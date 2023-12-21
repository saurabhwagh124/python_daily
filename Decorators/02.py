def outerfunc():
    print("In outer function")

    def inner1():
        print("In inner function 1")
        
    def inner2():
        print("In inner function 2")
    return inner1,inner2

ret1,ret2 = outerfunc()
ret1()
ret2()

ret = outerfunc()
ret[0]()
ret[1]()

def outerfunc1():
    print("In outer function 1")

    def inner11():
        print("In inner function 11")
        return inner12
    def inner12():
        print("In inner function 12")
    return inner11

abc = outerfunc1()
efg = abc()
efg()
