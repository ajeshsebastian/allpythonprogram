def add(num1,num2):
    return num1+num2

#lamda function anonymus function
# reference=lamba(argument): return value

cube=lambda num1:num1**3
print(cube(3))

ad=lambda num1,num2: num1+num2
print(ad(10,5))

div=lambda num1,num2:num1/num2
print(div (20,5))

mul=lambda num1,num2:num1*num2
print(mul (20,5))

sub=lambda num1,num2:num1-num2
print(sub(20,5))

# map function

lst=[2,3,4,5,6,7]

# s=[]
# for num in lst :
#     res=num**2
#     s.append(res )
# print(s)

def sq(num):
    return num**2
#square=list(map(sq,lst ))
square=list(map(lambda num:num**2,lst )) #conver it into a lambda function also
print(square )

# to upper case

names=["ajay","arun"]

def upper(word):
    return word .upper()

#upp=list(map(upper ),names )
upp=list(map(lambda word:word.upper (),names ))
print(upp )


#list comprehension

# lst=[1,2,3,4,5]
# #squares
# squares=[num**2 for num in lst ]
# print(squares )

# fruits=["apple","orange","mango"]
# pair=[(num ,num) for num in fruits  ]
# print(pair )
#
#
# lst1=[10,20]
# lst2=[30,40]
#
# #(10,30),(10,40),(20,30),(20,40)
#
# pairs=[(num1,num2) for num1 in lst1 for num2 in lst2]
# print(pairs )
#

lst3=[1,2,3,4,5,6,7]
eve=[num  for num in lst3 if num%2==0]
print(eve)

lst4=[7,8,9,4,3,2]

eve=[num+1 if num>5 else num-1 for num in lst4]
print(eve )
