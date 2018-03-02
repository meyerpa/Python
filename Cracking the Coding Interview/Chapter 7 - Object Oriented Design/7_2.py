"""
7.2 Call Center
Imagine you have a call center with three levels of employees: respondent,
manager, and director. An incoming telephone call must be first allocated
to a respondent who is free. If the respondent can't handle the call, he or she
must escalate the call to a manager. If the manager is not free or not able
to handle it, then the call should be escalated to the director. Design the
classes and data structures for this problem. Implement dispatchCall()
which assigns a call to the first available employee.

Note: should use a queue to store the calls
"""

# class with employee subclasses respondent (has one or many managers and
# director), manager (has one or many directors), director
# class to hold all employees and if they are available
# class for a call

class Employee:
    Employee.__all = [] # start with empty list of employees, could also do dictionary
    def __init__(self, name=''):
        self.__call = None
        self.__name = name
        Employee.__all.append(self)

    def isAvailable(self):
        return self.__call == None

    def assignCall(self, call):
        self.__call = call

    def endCall(self):
        self.__call = None

    def getEmployee():
        for employee in Employee.__all:
            if employee.isAvailable():
                return employee
        # no one is available, so return -1
        return -1

class Respondent(Employee):
    Respondent.__all = []
    def __init__(self, name=''):
        super(Respondent, self).__init__()
        Respondent.__all.append(self)

    def getRespondent():
        for respondent in Respondent.__all:
            if respondent.isAvailable():
                return respondent
        # no one is available, so return -1
        return -1

    def escalateCall(self):
        # get available manager
        manager = Manager.getManager()
        # ensure manager was available and escalate
        if manager != -1:
            manager.assignCall()
            self.endCall()
        # if manager wasn't available, escalate to director
        else:
            director = Director.getDirector()
            if director != -1:
                director.assignCall()
                self.endCall()
            # if it is -1, check again in a bit (shitty implement) should just return when there is an available director/manager
            self.escalateCall()


class Manager(Employee):
    Manager.__all = []
    def __init__(self, name=''):
        super(Manager, self).__init__()
        Manager.__all.append(self)

    def getManager():
        for manager in Manager.__all:
            if manager.isAvailable():
                return manager
        # no one is available, so return -1
        return -1

    def escalateCall(self):
        director = Director.getDirector()
        if director != -1:
            director.assignCall()
            self.endCall()
        # if it is -1, check again in a bit (shitty implement) should just return when there is an available director/manager
        self.escalateCall()

class Director(Employee):
    Respondent.__all = []
    def __init__(self, name=''):
        super(Respondent, self).__init__()
        Respondent.__all.append(self)

    def getDirector():
        for director in Director.__all:
            if director.isAvailable():
                return director
        # no one is available, so return -1
        return -1

class Call:
    def __init__(self):
        # first find respondent that is available & assign
        respondent = Respondent.getRespondent()
        # keep getting respondents until one is available
        while respondent == -1:
            respondent = Respondent.getRespondent()
        # assign call to respondent
        respondent.assignCall(self)
