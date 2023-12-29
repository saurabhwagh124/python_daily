class Parent:
    
    def __init__(self):
        print("In Constructor Parent")

    def parentFunc(self):
        print("In Parent Function")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("In Child Constructor")

    def childFunc(self):
        print("In Child Function")

obj1 = Child()
obj1.parentFunc()
obj1.childFunc()
