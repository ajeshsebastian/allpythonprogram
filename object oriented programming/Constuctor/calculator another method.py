#another method

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self ):
        return self.num1+self.num2

    def mul(self):
        return self.num1 * self.num2
    def sub(self):
        return self.num1 - self.num2
    def div(self):
        return self.num1 / self.num2

a=int(input("Enter number 1"))
b=int(input("Enter number 2"))
#op=input("Choose an option\n 1.Add \n 2.Multiplication \n 3.Subtraction\n 4.Division")
ca=Calculator (a,b)

print("Total=" ,ca.add() )
print("multi=",ca.mul() )
print("sub=",ca.sub() )
print("division=",ca.div() )