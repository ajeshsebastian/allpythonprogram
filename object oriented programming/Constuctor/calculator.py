class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self ):
        print("Total=" ,self.num1 +self.num2 )
    def mul(self):
        print("multi=",self.num1 * self.num2)
    def sub(self):
        print("sub=",self.num1 - self.num2)
    def div(self):
        print("division=",self.num1 / self.num2)

a=int(input("Enter number 1"))
b=int(input("Enter number 2"))

ca=Calculator (a,b)

ca.add()

ca.mul()

ca.sub()

ca.div()


