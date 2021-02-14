from abc import ABCMeta, abstractmethod

class Driver(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def access(self, url):
        pass

    @abstractmethod
    def pushButton(self, XPath):
        pass

    @abstractmethod
    def notCloseAndEnd(self):
        pass

    @abstractmethod
    def inputInfo(self, XPath, info):
        pass

    @abstractmethod
    def closeBrowser(self):
        pass

    @abstractmethod
    def waitElementByDisplay(self, XPath):
        pass

    @abstractmethod
    def acceptAlert(self):
        pass

    @abstractmethod
    def changeNextTab(self):
        pass

    @abstractmethod
    def changeLastTab(self):
        pass
        
    @abstractmethod
    def executeScript(self, script):
        pass

    @abstractmethod
    def getText(self, XPath):
        pass