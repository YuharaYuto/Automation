from abc import ABCMEta, abstractmethod
from UserIntereface import UserIntereface
from DriverImple import DriverImple

class Func(metaclass=ABCMeta):

    def __init__(self):
        self.ui = UserInterface()
        self.driver = DriverImple()

    @abstractmethod
    def openPage(self):
        pass

    @abstractmethod
    def closePage(self):
        pass

    @abstractmethod
    def doFunc(self):
        pass

    def exec(self):
        openPage()
        doFunc()
        closePAge()
        pass

    