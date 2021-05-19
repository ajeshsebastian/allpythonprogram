#prime numbers within a limit

lower=int(input("Enter lower limit"))
upper=int(input("Enter upper limit"))

print("Prime numbers between", lower, "and", upper, "are:")

for i in range(lower, upper+1):
   # all prime numbers are greater than 1
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
            print(i)

