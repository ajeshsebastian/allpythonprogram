# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.



num1=int(input("Number of classes held"))
num2=int(input("Number of classes attended"))
per=(num2/num1)*100
print(per)
if(per>=75):
    print("Allowed")
else:
    print("not allowed")

