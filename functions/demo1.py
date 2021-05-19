#1

def dif():
     num1=int(input("Enter number1"))
     num2=int(input("enter number2"))
     res=num1/num2
     print(res)
dif()


#2


def dif(no1,no2):
     res=no1/no2
     print(res)
dif(20,3)


#3


def dif(no1,no2):
     res=no1/no2
     return res
data=dif(20,30)
print(data )