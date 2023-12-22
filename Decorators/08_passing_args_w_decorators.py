def decorFun(func):

    def wrapper(*argv):

        print("Starting wrapper")
        val = func(*argv)
        print("End wrapper")
        return val

    return wrapper

@decorFun
def normal_func(x,y):
    print("In normal Function")
    return x+y

print(normal_func(10,20))
