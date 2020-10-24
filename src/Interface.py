class Interface:

    def __init__(self):
        self.inputData = {}
        return 

    def input(self, keys):
        inputData = self.inputData
        for key in keys:
            value = input(key + "を入力してください。")
            inputData[key] = value
        
        self.inputData = inputData
        return 