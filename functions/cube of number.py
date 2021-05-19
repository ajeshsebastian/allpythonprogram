# def cube(a):
#
#  print("The Cube of given number", a*a*a)
#
# b = int(input(" Enter any number  : "))
#
# cube(b)

def cube(num):
    res=0
    res=num*num*num
    return(res)

num = int(input("Enter an any number : "))

cb = cube(num)

print("Cube of the given number is : ",cb)