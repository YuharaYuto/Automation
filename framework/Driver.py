from abc import ABCMEta, abstractmethod

class Driver(metaclass=ABCMeta):

    def __init__(self):
        

    @abstractmethod
    def openBrowserAndAccess(self, url):
        pass

    @abstractmethod
    def pushButton(self, XPath):
        pass

    @abstractmethod
    def inputData(self, XPath):
        pass

    @abstractmethod
    def closeBrowser(self):
        pass

    @abstractmethod
    def waitElementByDisplay(self, XPath):
        pass

