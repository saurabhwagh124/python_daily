class Demo:
    
    def __eq__(self,obj):
        print("In Eq")
        return True
# This above method is present directly in python3 classes individual classes but in case of python 2 these methods are written global and then called and as the method name is same so we are overriding it here! Despite the obj s being different we are printing true 

obj1 = Demo()
obj2 = Demo()

print(id(obj1))
print(id(obj2))
print(obj1 == obj2)
