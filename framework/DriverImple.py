from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Driver import Driver

class DriverImple(Driver):
    def __init__(self):
        options = Options()
        #options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        self.options = options
        self.driver = webdriver.Chrome("",options=options)

    def openBrowserAndAccess(self, url):
        driver.get(url)
        self.driver = driver #設定済みのdriverを格納。
        pass

    def pushButton(self, XPath):
        button = self.driver.find_element_by_xpath(Xpath)
        button.click()
        pass

    def inputData(self, XPath):
        inputBox = self.driver.find_element_by_xpath(Xpath)
        inputBox.send_keys(info)
        pass

    def closeBrowser(self):
        self.driver.close()
        pass
    
    def waitElementByDisplay(self, XPath):
        #仮に実装
        time(10)
        pass


