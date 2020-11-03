class KeyDao:

    def __init__(self):
        return

    def getKeys(self,functionName):
        return table[functionName]


table  = {
    "一括申請" : ['申請者','期間（いつからyyyymmdd）','期間（いつまでyyyymmdd）','サーバ名'],
    "入館申請" : ['承認者','申請者'],
    "test楽天競馬ログイン" :['user_id','login_psw'],
    "n-gate一括申請":['年(西暦)','月'],
}