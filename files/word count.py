#line="hai hello hai hello"
f=open("news1","r")
dis={}
for i in f:
    #lst .append(i.rstrip("\n") )
      words=i.split(" ")
      #words=i.rstrip("\n")

#print(lst)
#print(words)
# dis={}
for char in words:
    if (char not in dis):
        dis[char]=1
    else:
        dis[char]+=1
print(dis)

for k,v in dis.items():
    print(k,",",v)





# dis={}
# for word in words:
#     if (word not in dis):
#         dis[word]=1
#     else:
#         dis[word]+=1
# print(dis)