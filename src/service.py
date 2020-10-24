from FunctionDao import FunctionDao
from UrlDao import UrlDao
from KeyDao import KeyDao
from Interface import Interface
from Driver import Driver

class Service:

    def __init__(self):
        return

    def execution(self, functionName):

        #必要なインスタンスの生成
        functionDao = FunctionDao() #機能ごとに関数を引っ張ってくる。
        urlDao = UrlDao() #機能ごとにアクセスするurlを引っ張ってくる。
        interface = Interface() #必要なデータを受け取る窓口
        keyDao = KeyDao() #機能ごとに必要な項目を引っ張ってくる。

        #入力項目の取得
        keys = keyDao.getKeys(functionName)

        #機能に必要な入力画面を呼び出し、入力値を受け取る
        interface.input(keys)
        inputData = interface.inputData
        
        #機能を実行できる関数を取ってくる
        function = functionDao.getFunction(functionName)
        
        #機能にアクセスするためのwebページのurlを取ってくる
        url = urlDao.getUrl(functionName)

        #ブラウザを動かすクラスに処理を実行させる
        driver_chrome = Driver(url, function, inputData)

        #ウインドウの表示
        driver_chrome.open()
        #プロキシサーバへのログイン？？
        #driver_chrome.proxyLogin()
        #機能サイトへのログイン？？
        #driver_chrome.login()
        #機能の実行
        driver_chrome.do()

        #機能の終了
        #driver_chrome.end()
        
        return

    