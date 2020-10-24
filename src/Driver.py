#ブラウザを操作するのはこのクラスだけ
#functionDaoにも関数は定義してあるが、定義してあるだけ。

class Driver:
    def __init__(self, url, function, inputData):
        self.url = url
        self.function = function
        self.inputData = inputData

        # driverの設定
        self.driver = driver #設定済みのdriverを格納。
        return

    def open(self):
        driver = self.driver
        #chrome driverで操作
        return 

    def close(self):
        driver = self.driver
        #chrome driverで操作
        return

    def proxyLogin(self):
        driver = self.driver
        #chrome driverで操作
        return

    def do(self):
        #chrome driverで操作
        self.function(self.inputData, self.driver)
        return

    