#minimam length 8 and maximam 15
#except numbers


import re
n=input("Enter string ")
x='\D{8,15}$'
match =re.fullmatch(x,n)
if match is not None :
    print("valid")
else:
    print("invalid")