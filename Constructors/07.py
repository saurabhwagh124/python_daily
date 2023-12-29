class Parent:
    def __init__(self):
        print("In Constructor")
    def parentFunc(self):
        print("In parent function")

class Child(Parent):
    def __init__(self):
        print("In child constructor")

obj1 = Child()
obj1.parentFunc()
