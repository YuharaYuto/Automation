import functionDao
import urlDao
import driver


class service:

    def __init__(self):

        self.functionDao = functionDao
        self.urlDao = urlDao
        self.driver = driver
        self.interface = interface

        return


    def execution(self, functionName):

        functionDao = self.functionDao
        urlDao = self.urlDao
        interface = self.interface
        driver = self.driver

        #機能に必要な入力画面の呼び出し
        interface.input(functionName)
        inputData = interface.data
        
        #機能を実行できる関数を取ってくる
        function = functionDao.getFunction(functionName)
        
        #機能にアクセスするためのwebページのurlを取ってくる
        url = urlDao.getUrl(functionName)

        #ブラウザを動かすクラスに処理を実行させる
        #ウインドウの表示
        driver.open(url)
        #プロキシサーバへのログイン？？
        driver.proxyLogin(function)
        #機能サイトへのログイン？？
        driver.login(function)
        #機能の実行
        dirver.do(function, inputData)

        #機能の終了
        driver.end()
        
        return

    