#sum of n numbers
num1=int(input("Enter a number"))
if(num1<0):
    print("enter positive")
else:
    sum=0
    # while(num1>0):
    #     sum+=num1
    #     num1-=1
    # print(sum)

i=1

while(i<=num1):
    sum=sum+i
    i+=1
print(sum)
