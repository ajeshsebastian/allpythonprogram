f=open("numbers","r")
lst=[]
for lines in f:
    lst.append(int(lines.rstrip("\n")) )
print(lst)

#end function remove cheyyan  rstrip
#to remove element form start use lstrip
sum=sum(lst)
print(sum)

#