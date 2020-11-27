import sys
sys.path.append("./framework")
sys.path.append("./func")

from ConcreteCreator import ConcreteCreator
from Func import Func

def main():
    factory = ConcreteCreator()
    funcName = factory.selectFunc()
    func = factory.createFunc(funcName)
    func.exec()
    pass

if __name__ == "__main__":
    main()
    pass