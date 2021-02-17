from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.alert import Alert
from businessException import BusinessException
import json
import time
import os
import signal
from pathlib import Path

class DriverImple(Driver):
    """Driver実装クラス
    Driverクラスを実現するクラス。
    Attributes:
        driver(webdriver):chromeDriver
    """
    def __init__(self):
        """初期化
        chromeDriver起動の設定を行う。
        """
        current_dir = Path.cwd()
        json_path = str(current_dir.parent) + "/settings.json"
        json_file = open("settings.json","r")
        json_data = json.load(json_file)

        options = Options()
        #options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        self.options = options
        self.driver = webdriver.Chrome(str(current_dir.parent) + "/automation/chromedriver",options=options)

    def access(self, url):
        """URLへのアクセス
        Args:
            url(String):アクセスしたいurl
        """
        driver = self.driver  #設定済みのdriverを格納。
        driver.get(url)
        
        pass

    def pushButton(self, XPath):
        """ボタンの押下
        
        Args:
            Xpath(String):押下したいボタンのXpath
        Raises:
            BusinessException:対象のボタンが存在しない場合に発生
        """
        for i in range(1,5):
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))
                button = self.driver.find_element_by_xpath(XPath)
                button.click()
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            else:
                return
        return

    def inputInfo(self, XPath,info):
        """情報の入力
        
        Args:
            Xpath(String):入力欄のXpath
            info(String):入力したい文字列
        Raises:
            BusinessException:対象の入力欄が存在しない場合に発生
        """
        for i in range(1,5):
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))
                inputBox = self.driver.find_element_by_xpath(XPath)
                inputBox.send_keys(info)
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            else:
                return
        return

    def clearInfo(self,XPath):
        """情報の消去
        
        Args:
            Xpath(String):入力を消去したい欄のXpath
        Raises:
            BusinessException:入力欄が存在しない場合に発生
        """
        for i in range(1,5):
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))
                box = self.driver.find_element_by_xpath(XPath)
                box.clear()
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            else:
                return
        return

    def checkRadio(self, XPath):
        """ラジオボタンのチェック
        
        Args:
            Xpath(String):ラジオボタンのXpath
        Raises:
            BusinessException:対象のボタンが存在しない場合に発生
        """
        for i in range(1,5):
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))
                radio = self.driver.find_element_by_xpath(Xpath)
                radio.click()
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            except:
                if i == 4:
                    raise Exception
                pass
            else:
                return
        return


    def closeBrowser(self):
        """ブラウザを閉じる

        """
        self.driver.close()
        pass

    def notCloseAndEnd(self):
        """ブラウザを閉じずに、ブラウザを残したままseleniumから解放する。

        """
        os.kill(self.driver.service.process.pid,signal.SIGTERM)
    
    def waitElementByDisplay(self, XPath):
        """指定した要素が表示されるまで待機
        Args:
            Xpath(String):ラジオボタンのXpath
        Raises:
            BusinessException:対象の要素が40秒以上存在しない場合に発生
        """
        for i in range(1,5):
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            else:
                return
        return

    def acceptAlert(self):
        """指定した要素が表示されるまで待機
        Args:
            JavaScriptのアラートを受け入れる
        Raises:
            BusinessException:対象の要素が40秒以上存在しない場合に発生
        """
        for i in range(1,5):
            try:
                Alert(self.driver).accept()
            except:
                traceback.print_exc()
            else:
                return
            
        return

    def changeNextTab(self):
        """次のタブに遷移する
        
        """
        for i in range(1,5):
            try:
                handle_array = self.driver.window_handles
                self.driver.switch_to.window(handle_array[1])
                pass
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            except:
                if i == 4:
                    raise Exception
                pass
            else:
                return
        return
        
    def changeLastTab(self):
        """最後のタブに遷移する
        
        """
        for i in range(1,5):
            try:
                handle_array = self.driver.window_handles
                self.driver.switch_to.window(handle_array[-1])
                pass
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            except:
                if i == 4:
                    raise Exception
                pass
            else:
                return
        return

    def executeScript(self, script):
        """javascriptを実行する
        Args:
            Xpath(String):ラジオボタンのXpath
        Raises:
            BusinessException:対象の要素が40秒以上存在しない場合に発生
        """
        for i in range(1,5):
            try:
                self.driver.execute_script(script)
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            except:
                if i == 4:
                    raise Exception
                #raise Exception
                pass
            else:
                return
        return

        

    def getText(self, Xpath):
        """指定した要素の示す内容（文字列を取得）
        Args:
            Xpath(String):ラジオボタンのXpath
        Raises:
            BusinessException:対象の要素が40秒以上存在しない場合に発生
        """
        for i in range(1,5):
            try:
                res = self.driver.find_element_by_xpath(Xpath).text
                return res
            except NoSuchElementException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が見つかりませんでした。¥n")
                pass
            except TimeoutException:
                if i == 4:
                    raise BusinessException("対象の要素" + XPath + "が時間内に見つかりませんでした。¥n")
                pass
            except:
                if i == 4:
                    pass
                    raise Exception
                pass
            else:
                return
        return
        

