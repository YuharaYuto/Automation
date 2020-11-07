from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import signal

class DriverImple(Driver):
    def __init__(self):
        options = Options()
        #options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        self.options = options
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)

    def access(self, url):
        driver = self.driver  #設定済みのdriverを格納。
        driver.get(url)
        
        pass

    def pushButton(self, XPath):
        button = self.driver.find_element_by_xpath(XPath)
        button.click()
        pass

    def inputInfo(self, XPath,info):
        inputBox = self.driver.find_element_by_xpath(XPath)
        inputBox.send_keys(info)
        pass

    def clearInfo(self,XPath):
        box = self.driver.find_element_by_xpath(XPath)
        box.clear()

    def closeBrowser(self):
        self.driver.close()
        pass

    def notCloseAndEnd(self):
        os.kill(self.driver.service.process.pid,signal.SIGTERM)
    
    def waitElementByDisplay(self, XPath):
        wait = WebDriverWait(self.driver, 180)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))
        pass

    def changeNextTab(self):
        handle_array = self.driver.window_handles
        self.driver.switch_to.window(handle_array[1])

