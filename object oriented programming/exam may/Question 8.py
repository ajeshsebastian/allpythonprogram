#The finally keyword is used in try ... except blocks
#The finally block always executed after try and except blocks
# The finally block always executed after normal termination of try block or after try block terminates due to some exception
# This can be useful to close objects and clean up resources
#with or without exception

#try block and finally bolck always works

a=[11,22,33]
i=int(input("Enter an index value"))

try:
       print(a[i])
except:
    print("out of range")
finally:
    print("inside finally")