import sys
sys.path.append("./func/functions")
from rakutenLogin import rakutenLogin


class ConcreteCreator():

    def __init__(self):
        self.funcList = ["nGate","楽天競馬ログイン"]
        pass

    def selectFunc(self):
        i = 1
        funcList = self.funcList
        print("機能一覧")
        for funcName in funcList:
            print(str(i)+"："+str(funcName))
            i+=1
        selected = input("機能の番号を選択してください。：")
        return funcList[int(selected) -1]

    def createFunc(self, funcName):
        if funcName == "nGate":
            func = ngate_monthly()
        if funcName == "楽天競馬ログイン":
            func = rakutenLogin()
        return func

    