#not complete

import re
n=input("Enter email")
#x='(^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+$)'
x='([a-z]{1,}[A-Z]{1,}[0-9]{1,})+([a-zA-Z0-9]{8,15})$'
match =re.fullmatch(x,n)
if match is not None :
    print("valid")
else:
    print("invalid")