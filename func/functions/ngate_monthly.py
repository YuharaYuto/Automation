from Func import func
from DateUtil import dateUtil
class nGateMonthly(Func):

    def __init__(self):
        super().__init__()
        self.url = ""#url


    def openPage(self):
        ui = self.ui
        driver = self.driver
        ui.start()
        ui.showMessage("プロキシにログインできていない場合、ログインしてください。")
        ui.showMessage("nGateにログインしてください")
        dirver.waitElementByDisplay("ログイン後のどこか一要素")
        ui.showMEssage("申請テンプレートを作成してください")
        pass

    def closePage(self):
        ui = self.ui
        ui.end()
        self.driver.notCloseAndEnd()
        ui.showMessage("念のためチェックしてください")
        pass

    def doFunc(self):
        ui = self.ui
        dirver = self.driver

        # 必要事項の入力
        ui.showMessage("必要事項を入力してください")

        checkFlg = True
        while(checkFlg):
            startTime = ui.inputData("終了年月日時刻(yyyyMMdd;hhmm)")
            stopTime = ui.inputData("終了年月日時刻(yyyyMMdd;hhmm)")
            userName = ui.inputData("申請者の名前(苗字)")
            try:
                dateUtil.validate(startTime, stopTime)
                checkFlg = False
            except BusinessException as e:
                print(e.message)
                ui.showMessage("再度入力してください")
                checkFlg = True

        
        ui.showMessage("日付以外を作成してください")
        
        # 日付辞書の作成
        date_dict_list = dateUtil.make_date_dict(startTime, stopTime)

        for date_dict in date_dict_list:
            
            # 日付入力欄表示まで待機
            driver.waitElementByDisplay("#日付入力欄のXpath")

            # 日付入力
            driver.inputInfo("xpath", date_dict["startDate"])
            driver.inputInfo("xpath", date_dict["startTime"])
            driver.inputInfo("xpath", date_dict["stopDate"])
            driver.inputInfo("xpath", date_dict["stopTime"])

            # 確定ボタン押下
            driver.pushButton("xpath")

            # 検索画面に戻るまで待機
            driver.waitElementByDisplay("#検索画面のどこかの要素のXpath")

            # 詳細検索欄表示
            driver.pushButton("xpath")

            # 名前に申請者名入力
            driver.inputInfo("xpath", userName)

            # 検索ボタン押下
            driver.pushButton("xpath")

            # 検索結果表示まで待機
            driver.waitElementByDisplay("#検索結果のXpath")

            # 一番上の結果をチェック
            driver.pushButton("xpath")

            # (操作ボタン押下)

            # 再利用ボタン押下
            driver.pushButton("xpath")
        
        # 戻る
        driver.pushButton("戻る")

        


