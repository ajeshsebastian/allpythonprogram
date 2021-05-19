#vehicle number validation


import re
n=input("EnterVEHICLE")
x='^[A-Z]{2}[0-9]{2}[A-Z]*[0-9]{4}$'
match =re.fullmatch(x,n)
if match is not None :
    print("valid")
else:
    print("invalid")