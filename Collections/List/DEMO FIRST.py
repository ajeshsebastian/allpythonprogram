lst=[10,20,30,40,50]
# sum=0
# for i in lst:
#     sum=sum+i
# print(sum)
# print(sum(lst ))
#
# print(max(lst))
max=0
for i in lst:
    if i < max:
        max=i
print(max)


#def min_check(x):
  #min_val = x[0]
min_val=0
for check in lst:
   if check < min_val:
      min_val = check
  #return min_val
print(min_val )


#print(min_check(lst ) )