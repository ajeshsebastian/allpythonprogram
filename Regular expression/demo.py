#regular expression used in pattern matching

#re -- package for pattern matching

#first import re package
import re
count =0
matcher=re.finditer("ab" , "abaabbab")

print(matcher )

for match in matcher:
    count+=1
print("Count=" ,count)