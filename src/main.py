from Service import Service

def call(functionName):
    service = Service()
    service.execution(functionName)
    return



#呼び出し
if __name__ == '__main__':
    call("test楽天競馬ログイン") 
