class Parent:

    def __init__(self):
        print("In parent Constructor1")

    def __init__(self):
        print("In parent Constructor2")

    def printData(self):
        print("In fun 1")

    def printData(self):
        print("In fun 2")

obj1 = Parent()
obj1.printData()

