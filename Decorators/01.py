def outerfunc():
    print("In outer function")

    def innerfunc1():
        print("In inner function 1")

    def innerfunc2():
        print("In inner function 2")

    innerfunc1()
    innerfunc2()

outerfunc()
