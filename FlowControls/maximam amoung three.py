# maximam amoung three numbers

num1 = int(input("number one"))
num2 = int(input("number two"))
num3 = int(input("number three"))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("the largest number is", largest)


# if(num1>num2) & (num1>num3):
#     print(num1,"is maximam")
# else(num2>num3)