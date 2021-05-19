#
#
#
# def binary(lst,element):
#     low=0
#     upp=len(lst)-1
#     mid=0
#     while(low<=upp):
#       mid=(upp+low)//2
#         if lst[mid ]< element:
#         low=mid+1
#         elif lst[mid]>element:
#             upp=mid-1
#         else:
#             return mid
#     return -1
# lst=[2,5,6,8,9,20,10]
# lst.sort()
# print(lst)
# element=int(input("Enter element"))
# result=binary(lst ,element )
# if result!=-1:
#     print("element is present")
# else:
#     print("not present")
#
#
#

lst=[4,2,3,11,14,15,10,12,13]
lst.sort()
print(lst)
#lst=[2,3,4,10,11,12,13,14,15]
low=0
upp=len(lst)-1 #9-
flag=0
element=int(input("Enter the element"))
while(low<=upp):
    mid=(low+upp)//2

    if(element >lst[mid]):
        low=mid+1
    elif (element <lst[mid]):
        upp=mid-1
    elif (element ==lst [mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("not found")
