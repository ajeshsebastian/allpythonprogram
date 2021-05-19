# import re
# x="a+" # a including group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match .start() )
#     print(match .group() )
#
#
# import re
# x="a*" # count including zero number of a
# r="aaa abc aaaa cga sssd"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match .start() )
#     print(match .group() )
#
#
# import re
# x="a?" # count a as each including zero num of a
# r="aaa abc aaaa cga sssd"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match .start() )
#     print(match .group() )

# import re
# x="a{2}" # 2 number of a
# r="aaa abc aaaa cga sssd"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match .start() )
#     print(match .group() )


# import re
# x="a{2,3}" # minimam 2 a and maximam 3 a
# r="aaa abc aaaa cga sssd"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match .start() )
#     print(match .group() )
#
# import re
# x="^a" # check starting with  a(considering the all elements all a single string)
# r="aaa abc aaaa cga sssd"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match .start() )
#     print(match .group() )



import re
x="a$" # check ending with  a(considering the all elements all a single string)
r="aaa abc aaaa cga sssda"
matcher=re.finditer(x,r)
for match in matcher:
    print(match .start() )
    print(match .group() )