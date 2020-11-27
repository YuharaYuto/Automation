from abc import ABCMEta, abstractmethod
class Creator(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def createFunc(self, funcName):
        pass

    def create():
        func = createFunc(func)
        pass
    

