class UserInterface():
    def __init__(self):
        pass

    
    def start(self):
        print("開始します。")
        pass

    def proxy(self):
        print("proxyへのログインを行ってください。")
        pass

    def inputData(self,key):
        data = input(key+"を入力してください：")
        return data

    def end(self):
        print("終了しました。windowはそのまま残ります。")

    def showMessage(self, message):
        print(message)
