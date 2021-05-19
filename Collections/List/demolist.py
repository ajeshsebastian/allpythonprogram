#list
#console
# lst=[2,4,5,6,7]
# n= int(input("Enter limit"))
# # for i in range(0,n):
# #     ele=[input().int(input())]
# #     lst.append(ele)
# print(lst)
# e=int(input("enter elemnt"))
# for i in lst:
#     if (i==e):
#         print("elemet exist")
#     else:
#         print("not")

lst=[2,4,5,6,7]
element=int(input("Enter elemnet"))
flag=0

for i in lst:
    if(i==element):
        flag=1
        break
    else:
        pass
if (flag>0):
    print("element found")
else:
    print("not")



#linear search


#binary search