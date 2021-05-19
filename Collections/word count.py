#word count

#line="hai hello hai hello"

#hai,2
#hello,3

#word select

#split

line="hai hello hai hello"
words=line.split(" ")
print(words)

dis={}
for word in words:
    if (word not in dis):
        dis[word]=1
    else:
        dis[word]+=1
print(dis)