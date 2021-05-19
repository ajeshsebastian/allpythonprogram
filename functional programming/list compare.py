lst1=[10,20,21,22,23]
lst2=[20,21,10,22,23]

flag=0
for i in lst1:
    if i in lst2:
        flag+=1
if flag ==len(lst1 ):
    print("List 1 and 2 are equal")

else:
    print("not ")


# lst1 .sort()
# lst2 .sort()
# if lst1 ==lst2 :
#     print("equal")
# else:
#     print("not ")


#
# a=set (lst1 )
# b=set(lst2 )
#
# if a==b:
#     print("list  1 and 2 are equal")
# else:
#     print("list 1 and 2 are not equal")