#1. Python program to remove duplicate elements from a list
lst=[1,1,2,45,45,50,51,52,53]
print("Original List")
print(lst)
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print("List after removing duplicated")
print(res)