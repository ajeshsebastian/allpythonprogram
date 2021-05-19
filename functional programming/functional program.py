#functional programming
#to reduce the length of the program

#lambda function
#map function
#filter
#list comprehesion


#lambda function

#lambda function  are anonymous functions(nameless functions)
#lambda function no need of a def keyword and return keyword

# f=lambda num1,num2:num1+num2
# print(f(10,20))
#
# g=lambda num1,num2:num1-num2
# print(g(40,20))
#
# h=lambda num1,num2:num1*num2
# print(h(10,20))
#
# i=lambda num1,num2:num1/num2
# print(i(50,20))



#map
#ella objectilum function perform cheyyan

#filter

#for selected objects


#map(fn,itreable)

#filter(fn,iterable)

# lst=[1,2,3,4,5,6,7]
# def sq(num):
#     return (num*num)
# s=list(map(sq,lst))
# print(s)
#
# s=list(map(lambda num:num*num,lst))
# print(s)
#
# #filter
#
# lst=[1,2,3,4,5,6,7,8]
# def even(num):
#     return (num%2==0)
# ev=list(filter(even,lst ) )
# print(ev)
#
# ev=list(filter(lambda num:num%2==0,lst))
# print(ev)


# lst=[]
# for i  in range(1,51):
#     lst.append(i)
# print(lst)

# lst=[i for i in range (1,51)]
# print(lst)

# lst=[i for i in range(1,51) if i%2==0]
# print(lst)

#square cude
# lst=[i*i if i%2==0 else i*i*i for i in range(1,51)]
# print(lst)

#even odd
lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,51)]
print(lst)