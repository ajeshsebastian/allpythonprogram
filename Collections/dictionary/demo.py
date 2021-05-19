#dictionary

#creation
#dic={}

#key value pairs -  to store values

#name:luminar ,loc:kakkanad,course:python

#key:value


#key=name,loc,course
#value=luminar,kakkanad,python

dis={"name":"luminar","loc":"kakkanad","course":"python","age":25,"mark":50}

#print(dis)

#dis={"name":"luminar","loc":"kakkanad","course":"python"}

#support heterogenousu data

#insertion order preserved
#dic={"name":"luminar","nam":"ajesh"}
#print(dic)

#not support duplicate keys

#it support duplicate values but not support duplicate keys


#to collect values
#to collect values from a dictonary we use keys
#print(dicronary["key"])

#print(dic["name"])


#name:luminar
#nam:ajesh
for i in dis:

    print(i,":",dis[i])
print("name :",dis["name"])

#muteable

#we can update the values in dictonary

# dis["name"]="csoft"
# print(dis)

# dis["loc"]="pala"
# print(dis)

#delete a value from dictonary

#del key word

# del dis["name"]
# print(dis)

# dis.pop("loc")
# print(dis)

#print("total" in dis)

dis["total"]=100
print(dis)