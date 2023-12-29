class Parent:

    def __init__(self):
        print("In Parent constructor")

    def parentFunc(self):
        print("In parent function")

class Child(Parent):

    def __init__(self):
        print("In Child constructor")

    def childFunc(self):
        print("In child function")

obj1 = Child()
obj1.parentFunc()
obj1.childFunc()
