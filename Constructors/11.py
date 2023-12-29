class Parent:

    def __init__(self):
        print("In Parent Constructor")

    def parentFunc(self):
        print("In parent function")

class Child(Parent):

    def __init__(self):
        super().__init__()
        Parent.__init__(self)
        print("In Child Constructor")

    def childFunc(self):
        print("In child function")

obj1 = Child()
obj1.parentFunc()
obj1.childFunc()
