#number reverse

num=int(input("Enter a number"))
reverse=0
while(num>0): #153 >0
    rem=num%10 #153%10=3
    reverse=(reverse*10)+rem #(0*10)+3=3   (3*10)+5=35  (35*10)+1=351
    num=num//10  #153//10  15//10
print(reverse)