#reduce is in funtools

#so we can import functools

lst=[7,8,9,4,3,2]
#find sum of the list

#map ,filter has only one arguments

#lambda has 2 arguments
import functools
total=functools .reduce(lambda no1,no2:no1+no2,lst)
print(total )
num=functools .reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(num)