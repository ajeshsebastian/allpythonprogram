#x='\s ' chech space
import re
x='\s'
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher :
    print(match .start() )
    print(match .group() )

#x='\d' check digit

x='\d'
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher :
    print(match .start() )
    print(match .group() )

#x="\D' except digit

x='\D'
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher :
    print(match .start() )
    print(match .group() )


#x="\w' all words except special characters

x='\w'
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher :
    print(match .start() )
    print(match .group() )



#x="\W' except words for special characters

x='\W'
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher :
    print(match .start() )
    print(match .group() )