lst=[56,2,3,4,45,89,12,34,67,]

# for i in range(len(lst)):
#     for j in range (i+1,len(lst)):
#         if lst[i]>lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
# print(lst)

#print(sorted(lst ) )
lst.sort(reverse= True )
print(lst)