#exception handing

a=int(input("enter 1"))
b=int(input("enter2"))
#print(a/b)

try:
    print(a)
    print(a/b)
except:
    print("exception occured")
