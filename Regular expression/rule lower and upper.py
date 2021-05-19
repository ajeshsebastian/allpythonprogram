#combination of lower and upper case letters ending with a number

import re
n=input("Enter string")
x='[a-zA-Z]+\d{1}$'    #x='a+' a including group
match =re.fullmatch(x,n)
if match is not None :
    print("valid")
else:
    print("invalid")