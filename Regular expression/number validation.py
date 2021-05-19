# import re
# n=input("Enter phone  number")
# x='\d{10}'
# match= re.fullmatch(x,n)
# # print(match )
# if match is not None :
#     print("valid")
# else:
#     print("invalid")


import re
n=input("Enter phone  number")
x='[+][9][1]\d{10}$'
match =re.fullmatch(x,n)
if match is not None :
    print("valid")
else:
    print("invalid")