class Boss:
    def report(self):
        print("Boss Report")

class Manager1(Boss):
    def report(self):
        print("Manager1 report")
class Manager2(Boss):
    def report(self):
        print("Manager2 report")
class Manager3(Boss):
    def report(self):
        print("Manager3 report")

class TeamLead1(Manager1, Manager3):
    def report(self):
        print("TeamLead 1 report")
class TeamLead2(Manager2, Manager3):
    def report(self):
        print("TeamLead 2 report")

class Developer(TeamLead1, TeamLead2):
    def report(self):
        print("Developer report")

print(Developer.__mro__)
print(Developer.mro())
