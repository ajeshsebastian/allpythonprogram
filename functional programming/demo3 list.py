

lst=[7,8,9,4,3,1]


s=[]
# for i in lst:
#     if i >5:
#         i+=1
#         s.append(i)
#     else:
#         i-=1
#         s.append(i)
# print(s)

#ternery operator

for i in lst:
    s.append(i+1) if i>5 else s.append(i-1)
print(s)

# map function

op=list(map(lambda num:num+1 if num>5 else num-1,lst ))
print(op )

# def mi(num):
#     if num >5:
#         num+=1
#         return num
#     else:
#         num-=1
#         return num
# s=list(map(mi,lst ))
# print(s)

