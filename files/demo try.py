f=open("D:\customer","r")
d={}
for line in f:
    data=line.rstrip("\n").split(",")
    dp=data[4]
    print(dp)
    for i in dp:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)