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

def ngate(inputData, driver): #ngate一括申請
    #自分でログインしてください。
    print("自分でログインしてください")
    #実行します(enterボタン)
    i = input("実行します。y/n")
    if(i == "n" or i == "N"):
        pass
    elif(i == "y" or i == "Y"):
        pushButton()#必要なボタンを押す
        pushButton()#必要なボタンを押す
        year = inputData["年(西暦)"]
        month = inputData["月"]
        dates = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        date = dates[month]
        if(dates == 2 & (year%4 == 0 or (year%100 != 0 & year%400 == 0))):
            date += 1
        for day in range(1,date,2):
            if(day == dates):
                InputInfo(,day)
                InputInfo(,day)
            else:
                InputInfo(,10000*year + 100*month + day)
                InputIndo(,10000*year + 100*month +day+1)
            InputInfo(,"0000")
            InputInfo(,"0000")
            pushButton()#必要なボタンを押す

table  = {
    "一括申請" : func1,
    "入館申請" : func2,
    "test楽天競馬ログイン":func3,
    "n-gate一括申請":ngate
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

