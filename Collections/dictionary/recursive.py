#pattern: "ABCDBCA

pattern="ABCDBCA"

#words=pattern.split(" ")
#print(words)

dis={}
for word in  pattern:
    if word not in dis:
        dis[word]=1
    else:
        break
print(word)