class Parent:
    z = 30

    def __init__(self):
        print("In constructor")
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
obj = Parent()
# Enters the constructor twice to create object first
# but as we have created same object the first one is deleted and enters destructor
print("End of code")
#by the end of code the second object also is destroyed 
