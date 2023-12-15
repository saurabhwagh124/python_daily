class Company:
    compName = "Facebook"

    def __init__(self):
        print("In constructor")
        self.empId = 12
        self.empName = "pranav"
    def compInfo(self):
        print(self.empId)
        print(self.empName)
        print(Company.compName) #can access using class name as it is class variable
        print(self.compName)#also can access using object as all class variables are copied in the objects

emp1 = Company()
emp2 = Company()

emp1.compInfo()
