#rule
#x="[abc]" either a,b,c
import re
x="[abc]" #either a,b,c
matcher=re.finditer(x,"abt c5kddj")
for match in matcher :
    print(match .start() )
    print(match .group() )