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
obj.__del__() #this is an explicit call to the destructor just to check
#now when the code ends the implicit call is made to the destructor to finally delete object

