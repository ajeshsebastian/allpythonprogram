f=open("D:\customer","r")
dis={}
for lines in  f:
    words=lines.rstrip("\n").split(",")
    prof=words[4]
    if prof not in dis:
        dis[prof]=1
    else:
        dis[prof]+=1
print(dis)