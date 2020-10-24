from selenium import webdriver

class FunctionDao:

    def __init__(self):
        return

    def getFunction(self, functionName):
        return table[functionName]


def func1(inputData):
    #inputDataを使ってdriverでブラウザを操作するスクリプト
    return 

def func2(inputData):
    #inputDataを使ってdriverでブラウザを操作するスクリプト
    return

def func3(inputData, driver):#楽天競馬ログイン
    pushButton('//*[@id="noBalanceStatus"]/a',driver)
    handle_array = driver.window_handles
    driver.switch_to.window(handle_array[1])
    clearInfo('//*[@id="loginInner_u"]',driver)
    inputInfo('//*[@id="loginInner_u"]',inputData["user_id"],driver)
    inputInfo('//*[@id="loginInner_p"]',inputData["login_psw"],driver)
    pushButton('//*[@id="loginInner"]/p[1]/input',driver)
    pass

table  = {
    "一括申請" : func1,
    "入館申請" : func2,
    "test楽天競馬ログイン":func3
}



#汎用スクリプト；ボタンを押す
def pushButton(Xpath,driver):
    button = driver.find_element_by_xpath(Xpath)
    button.click()
    return
#汎用スクリプト；情報を入力
def inputInfo(Xpath,info,driver):
    input = driver.find_element_by_xpath(Xpath)
    input.send_keys(info)
    return
#汎用スクリプト；入力値を消す
def clearInfo(Xpath,driver):
    box = driver.find_element_by_xpath(Xpath)
    box.clear()
    return
#汎用スクリプト；ラジオボタンを押す
def checkRadio(Xpath,driver):
    radio = driver.find_element_by_xpath(Xpath)
    radio.click()
    return

