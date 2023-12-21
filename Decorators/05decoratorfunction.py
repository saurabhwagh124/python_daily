def decorFunc(func):

    def wrapper():
        print("Start Wrapper")
        func()
        print("End Wrapper")

    return wrapper

@decorFunc
def normalFunc():
    print("Hello in normal function")

#normalFunc = decorFunc(normalFunc)
normalFunc()
