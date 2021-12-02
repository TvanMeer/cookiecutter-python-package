from module1.entrypoint1 import X
from module2.entrypoint2 import Y

class Client:
    def func_1(self):
        x = X()
        succes = x.do_something()
        print(f"Function func_1 called entrypoint1.X.do_something().")
        return succes
    
    def func_2(self):
        y = Y()
        succes = y.do_something()
        print(f"Function func_2 called entrypoint2.Y.do_something().")
        return succes