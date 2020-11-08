from Func import func
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
        
        pass

    def closePage(self):
        #実装
        ui = self.ui
        ui.end()
        self.driver.notCloseAndEnd()
        pass

    def doFunc(self):
        ui = self.ui
        ui.showMessage("何年何月分の申請を行いますか")
        checkFlg = False
        while(not checkFlg):
            year = int(ui.inputData("年(yyyy形式)："))
            month = int(ui.inputData("月(mm形式)："))
            if 2019< year and year< 9999 and 0<month and month<13:
                checkFlg = True
            else:
                ui.showMessage("入力値が不正です。")

            
        driver = self.driver
        driver.pushButton("作業者")
        driver.pushButton("機能一覧")
        driver.pushButton("申請")

        dates = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        date = dates[month]
        if(dates == 2 & (year%4 == 0 or (year%100 != 0 & year%400 == 0))):
            date += 1
        for day in range(1,date,2):
            if(day == dates):
                driver.inputInfo("申請日fromの日付",day)
                driver.inputInfo("申請日toの日付",day)
            else:
                driver.inputInfo("申請日fromの日付",10000*year + 100*month + day)
                driver.inputIndo("申請日toの日付",10000*year + 100*month +day+1)
            driver.inputInfo("申請日fromの時間","0000")
            driver.inputInfo("申請日toの時間","2359")
            driver.inputInfo("申請内容","XXXX")
            driver.inputInfo("アカウント","....")
            driver.pushButton("申請ボタン")
        
        pass

