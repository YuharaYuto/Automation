# Automation
Automation

## 機能の登録のやり方

1. KeyDao.pyのtableに、入力項目をリスト形式で登録する。
2. FunctionDao.pyのtableに、webブラウザを操作するスクリプト（関数）を登録する。このとき、入力した値はinputData["(KeyDaoに登録した項目名)"]として取得できる。
3. UrlDao.pyのtableに、urlを登録する。
※各Daoのtableのkeyは、統一すること。

これで、自動化を呼び出せます。

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