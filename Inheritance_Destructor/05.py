class Parent:
    print("Start class")
    #this line gets printed without calling the class as python is an interpreted language and it checks every line and this print is not binded to the class
    def __init__(self):
        print("In Constructor")

    print("End of class")

print("Start code")
obj = Parent()
print("End code")
