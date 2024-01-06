class Manager:
    def project(self):
        print("In project manager")

class TeamLead1(Manager):
    pass

class TeamLead2(Manager):
    def project(self):
        print("In TL2")

class Developer(TeamLead1, TeamLead2):
    pass

obj = Developer()
obj.project()

# In py2 the OP is In project Manager
# In py3 the OP is In TL2
