#even numbers
low=int(input("Enter lower limit"))
upp=int(input("Enter upper limit"))
for num in range(low,upp+1):
    if num %2==0:
        print(num,end="  ")