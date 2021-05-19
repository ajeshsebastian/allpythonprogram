#even numbers and odd number sum in a given limit
low=int(input("Enter lower limit"))
upp=int(input("Enter upper limit"))
esum = 0
osum = 0
for i in range(low,upp+1):
    if (i %2==0):
        esum =esum+i
    else:
        osum = osum+i


print(esum)
print(osum)


