def fun():

    print("Start fun")
    yield 10
    yield 20
    yield 30
    print("End fun")
    yield

ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))

# this next(ret) only executes the code of yield keyword but in the process it also executes code before it but not the code after it...
