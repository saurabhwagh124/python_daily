class Parent:
    z = 30

    def __init__(self):
        self.x = 10
        self.y = 20

    @classmethod 
    def dispParent(self):
        print(self.z)

    def dispData(self):
        print(self.x)
        print(self.y)
    
    def __del__(self):
        print("Deleting obj",self)

obj = Parent()
obj.dispData()
obj.dispParent()


