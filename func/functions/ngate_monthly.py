from Func import func
class nGateMonthly(Func):

    def __init__(self):
        super().__init__()
        self.url = ""#url


    def openPage(self):
        self.userInterface().start()
        pass

    def closePage(self):
        #実装
        pass

    def doFunc(self):
        self.userInterface().input()
        #実装
        pass

