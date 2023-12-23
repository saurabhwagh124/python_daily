def fun():
    print("Start fun")
    yield 10
    yield 20
    yield 30 
    print("End fun")
print(type(fun))
ret = fun()
print(type(ret))
for i in fun():
    print (i)
