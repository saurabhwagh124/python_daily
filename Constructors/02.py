class Demo:
    def __init__(self):
        print('In Constructor')
        self.x = 10
        self.y = 20

    def setData(self, z):
        self.z=z

    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z)
obj = Demo()
obj.printData()
