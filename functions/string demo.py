# a=input("Enter a word")
# b=input("Enter an alphabet")
# for i in a:
#     if(i==b):
#         print("present")
#     else:
#        print("not")
a = input("Enter a word")
flag=0
b = input("Enter an alphabet")
for i in a:
    if i==b:
        flag=1
if flag==1:
    print("present")
else:
    print("not")

