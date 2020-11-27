# Automation
Automation

このシステムは、seleniumで扱うブラウザを操作するメソッドを書き込むことで、自動化する機能を登録できる。

main.pyを実行することで、登録している自動化作業を呼び出すことができるようになる。

## 環境準備
 - python3.8
 - selenium
 - chromeDriver 86
 - chrome 86
 
 settings.jsonの、"chromeDriverPath"をchrome webdriverのパスに書き換える。

## 実行の仕方
main.pyを実行する。

## 自動化クラス(functions配下のファイル)について
Funcクラスを継承することで、
 - 標準入出力を扱う UserInterfaceクラス
 - seleniumを操作するDriverクラス
を扱えるようになる。

メソッド
 - openPage
 - closePage
 - doFunc
の３種類を実装する。

### 例　楽天競馬の自動ログイン
#### openPage
```python
self.ui.start()
driver = self.driver
driver.access(url)
driver.pushButton("/html/body[@class='noneSmartphoneUserAgent']/section[@id='info_top']/div[@id='PRmodal']/div")
```

#### closePage
```python
ui = self.ui
ui.end()
self.driver.notCloseAndEnd()
```

#### doFunc
```python
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
```

## クラスの説明
#### Driver, DriverImple
selenium webdriverのアダプターパターンにおけるインターフェースとその実装。

#### Creator
Factory MethodパターンにおけるCreatorクラス。

#### Func
Factory MethodパターンにおけるProductクラス。
template method execを持つ。