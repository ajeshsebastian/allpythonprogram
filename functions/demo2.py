# # #create a function to find factoral of a number
# # def fact():
# #    num1 = int(input("Enter number1"))
# #    fac=1
# #    for i in range(1,num1+1):
# #        fac*=i
# #     print(fac)
# # fact()
# #
# # def fact(10):
# #    #num1 = int(input("Enter number1"))
# #    fac=1
# #    for i in range(1,num1+1):
# #        fac*=i
# #     print(fac)
# # fact()
# #
# #
# #
# # # def dif(no1):
# # #     res = no1* dif(no1-1)
# # #     print(res)
# # #
# # # dif(20,)
# def factorial():
#     n1=int(input("Enter number1"))
#
#     fact=1
#     for i in range(1,n1+1):
#         fact*=i
#     print(fact)
# factorial()
#
# def factorial(n1):
#     fact=1
#     for i in range(1,n1+1):
#         fact*=i
#     print(fact )
# factorial(5)


def factorial(n1):
    fact = 1
    for i in range(1,n1+1):
        fact*=i
    return(fact)
data= factorial(5)
print(data )

