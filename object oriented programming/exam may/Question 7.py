


import re
f=open("number","r")
x='[+][9][1]\d{10}$'
g=open("Phone ","w")
h=open("not","a")
for i in f  :
    i=i.strip("\n")
    match =re.fullmatch(x,i)
    if match is not None :
         g.write(i )
         #h.write("\n")

    else:
        print(i,"not valid")
