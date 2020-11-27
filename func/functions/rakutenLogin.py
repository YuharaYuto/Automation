import sys
from Func import Func
class rakutenLogin(Func):


    def __init__(self):
        super().__init__()
        self.url = "https://keiba.rakuten.co.jp/?l-id=top_logo"#url


    def openPage(self):
        self.ui.start()
        self.driver.access(self.url)
        self.driver.waitElementByDisplay("/html/body/div[3]/div[2]/div/div[1]/div")
        pass

    def closePage(self):
        ui = self.ui
        ui.end()
        self.driver.notCloseAndEnd()
        pass

    def doFunc(self):
        ui = self.ui
        driver = self.driver
        
        userId = ui.inputData("ユーザーID")
        passwd = ui.inputData("パスワード")
        driver.pushButton('//*[@id="noBalanceStatus"]/a')
        driver.changeNextTab()
        driver.clearInfo('//*[@id="loginInner_u"]')
        driver.inputInfo('//*[@id="loginInner_u"]',userId)
        driver.inputInfo('//*[@id="loginInner_p"]',passwd)
        driver.pushButton('//*[@id="loginInner"]/p[1]/input')
        driver.waitElementByDisplay('//*[@id="siteID"]')
        pass

