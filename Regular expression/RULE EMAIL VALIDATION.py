#EMAIL VALIDATION
import re
n=input("Enter email")
x='(^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+$)'
match =re.fullmatch(x,n)
if match is not None :
    print("valid")
else:
    print("invalid")