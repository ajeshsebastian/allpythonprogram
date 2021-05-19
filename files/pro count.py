#profession count
#teacher,17
#doctor,25
#engineer,75
f=open("D:\customer","r")
dis={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    pre=data[4]
    #lst=([pre])
    print(pre)
    for i in pre:
         if i not in dis:
             dis[i]=1
         else:
              dis[i]+=1
print(dis)