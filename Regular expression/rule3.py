#rule
#x="[a-z]" a to z small letters
import re
x="[a-z]" #either a,b,c
matcher=re.finditer(x,"abt Cc5kddj")
for match in matcher :
    print(match .start() )
    print(match .group() )