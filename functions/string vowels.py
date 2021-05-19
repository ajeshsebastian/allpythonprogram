a=input("Enter a string")
v=0
for i in a:
    if i in "aeiou":
        v+=1
    else:
        pass
print(v)