#second largest number
num1=int(input("Enter number one"))
num2=int(input("Enter number two"))
num3=int(input("Enter number three"))

if(num1>num2) and (num1>num3):
    if(num2>num3):
        print(num2,"second largest")
    else:
        print(num3,"second largest")
elif(num2>num3) and (num2>num1):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
elif(num3>num1) and (num3>num2):
    if(num1>num2):
        print(num1)
    else:
        print(num2)
