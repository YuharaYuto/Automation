# Automation
Automation

このシステムは、seleniumで扱うブラウザを操作するメソッドを書き込むことで、自動化する機能を登録できる。

main.pyを実行することで、登録している自動化作業を呼び出すことができるようになる。

## 環境準備
 - python3.8
 - selenium
 - chromeDriver 86
 
 chrome webdriverの置いた場所で、Driver.pyの17行目のpath部分を書き換える。

## 実行の仕方
main.pyを実行する。

## 機能の登録のやり方
具体例として、楽天競馬にログインする方法を紹介する。

1. KeyDao.pyのtableに、入力項目をリスト形式で登録する。
> 具体例:<br>
>必要な入力項目は、user_id, login_pswの2種類 <br>
>"test楽天競馬ログイン" :['user_id','login_psw']


2. FunctionDao.pyのtableに、webブラウザを操作するスクリプト（関数）を登録する。このとき、入力した値はinputData["(KeyDaoに登録した項目名)"]として取得できる。
> 具体例:<br>
>必要な入力項目は、user_id, login_pswの2種類 <br>
>def func3(inputData, driver):#楽天競馬ログイン
    >pushButton('//*[@id="noBalanceStatus"]/a',driver)<br>
    >handle_array = driver.window_handles<br>
    >driver.switch_to.window(handle_array[1])<br>
    >clearInfo('//*[@id="loginInner_u"]',driver)<br>
    >inputInfo('//*[@id="loginInner_u"]',inputData["user_id"],driver)<br>
    >inputInfo('//*[@id="loginInner_p"]',inputData["login_psw"],driver)<br>
    >pushButton('//*[@id="loginInner"]/p[1]/input',driver)<br>
    >pass<br>

3. FunctionDao.pyのtableにkeyを機能名に、valueを関数名にして設定する。
> 具体例:<br>
> "test楽天競馬ログイン":func3


4. UrlDao.pyのtableに、urlを登録する。
>具体例:<br>
>"test楽天競馬ログイン":'https://keiba.rakuten.co.jp/?l-id=top_logo'


これで、登録を行えます。
繰り返して値を入力するなどは、function.pyの関数内でfor文で制御してください。


## 各クラスのおおまかな役割
### main
機能名を指定して実行
> 実行例:
>'call("一括申請")' 

### Service
データを取ってきたり、それをブラウザに制御させたり。
一機能の自動化全体を制御するもの

### Driver
ブラウザを制御する

### Dao
データを取得する。DBから取得するか、スクリプトに書いておくかは未定。

### Interface
入力値を受け取る制御を行う。