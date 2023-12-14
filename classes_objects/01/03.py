def fun(x):
    print("fun1")
def fun():
    print("fun2") 
'''fun without args here overrides the fun method wth args and this happens because everthing i.e. even methods are stored as objects in python'''
fun(10) 
''' here there is type error as this calls for fun with args and that has been overriden by the one without args'''
fun()
