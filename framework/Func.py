from abc import ABCMeta, abstractmethod
from UserInterface import UserInterface
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
        try:
            self.openPage()
            self.doFunc()
            self.closePage()
            pass
        except:
            print("失敗しました。")

    