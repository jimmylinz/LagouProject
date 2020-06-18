class Calculator():

    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        if a / b != 0:
            return a / b
        else:
            print("除数和被除数不能为0")
            raise ZeroDivisionError