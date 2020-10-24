#ブラウザを操作するのはこのクラスだけ
#functionDaoにも関数は定義してあるが、定義してあるだけ。
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Driver:
    def __init__(self, url, function, inputData):
        self.url = url
        self.function = function
        self.inputData = inputData

        # driverの設定
        options = Options()
        #options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)

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

    