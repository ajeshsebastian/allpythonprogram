# #rule
# #x="[A-Z]" a to z uppercase letters
# import re
# x="[A-Z]" #either a,b,c
# matcher=re.finditer(x,"abt Cc5kddj")
# for match in matcher :
#     print(match .start() )
#     print(match .group() )
#

#rule
#x="[a-zA-Z]" a to z uppercase letters
# import re
# x="[a-zA-Z]" #either a,b,c
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher :
#     print(match .start() )
#     print(match .group() )



import re
x="[a-zA-Z0-9 ]"
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher :
    print(match .start() )
    print(match .group() )