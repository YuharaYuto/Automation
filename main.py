from ConcreteCreator import ConcreteCreator

def main():
    factory = ConcreteCreator()
    funcName = factory.selectFunc()
    func = factory.createFunc(funcName)
    func.exec()
    pass

if __name__ == __main__:
    main()
    pass