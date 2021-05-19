#maximam temp in year
f=open("D:\Temperature","r")
dis={}
for i in f:
    data=i.rstrip("\n").split(" ")
    #print(data)
    year=data[0]
    temp=data[1]
    lst=([year,temp])
    #for j in year:
    if year not in dis:
        year=data[0]
        dis[year]=data[1]
    else:
        year=data[0]
        temp=int(data[1])
        if(int(dis[year])<temp):
            dis[year]=str(temp)

print(dis)
