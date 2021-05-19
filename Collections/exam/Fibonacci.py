#4. Python program to print fibonacci series
#output = 0,1,1,2,3,5,8,13
limit=int(input("Enter the limit"))
count=0
n1=0
n2=1
nth=0
if limit==1:
    print("Fibonacci series upto",limit,"  ",n1)
else:
    print("Fibonacci series")
    while(count<limit):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
