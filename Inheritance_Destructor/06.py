class Demo:

    def __init__(self):
        print("In constructor")

    def __del__(self):
        print("In Destructor")

obj = Demo()
obj2 = Demo()
obj3 = obj
del obj
# as we lnow that destructor calls for garbage collector so gc comes to picture but before deleting objects it checks for no. of references to the obj if atleast 1 refernce is present the obj is not deleted
print("End of code")
