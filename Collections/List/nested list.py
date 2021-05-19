lst=[[1001,"arun",25,1000],[1002,"arjun",26,2000],[1003,"vinu",27,3000],[1004,"bino",28,4000]]

print(lst)

#nested list

#1001,"arun",25,1000
#1002,"arjun",26,2000
#
# for emp in lst:
#     print(emp)

# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])

#arun
#arjun
#vinu

# for emp in lst:
#     print(emp[1])

#salary above 2000

# for emp in lst:
#     if (emp[3]>2000):
#         print(emp[1],emp[3])
# for emp in lst:
#     sum(emp[3])
#     print(sum)

sum=0
for emp in lst:
    sum=sum+emp[3]
print(sum)
