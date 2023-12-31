class Parent:

    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20

    def dispParent(self):
        print(self.x)
        print(self.y)

class Child(Parent):
  
    def __init__(self):
        #super().__init__()
        print("In child constructor")
        self.x = 30
        self.y = 40
        super().__init__()
        #this call just changes the x & y values of this object

obj = Child()
obj.dispParent()

