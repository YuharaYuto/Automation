class ConcreteCreator():

    def __init__(self):
        self.funcList = ["nGate","楽天競馬ログイン"]
        pass

    def selectFunc(self):
        i = 1
        print("機能一覧")
        for funcName in self.funcList:
            print(str(i)+"："+str(funcName))
            i+=1

        selected = input("機能の番号を選択してください。：")
        retrun self.funcList[i-1]

    def createFunc(self, funcName):
        if funcName == "nGate":
            func = ngate_monthly()
        if funcName == "楽天競馬ログイン":
            func = rakutenLogin()
        return func:

    