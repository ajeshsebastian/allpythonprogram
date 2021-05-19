

#list    []        yes      yes    yes    mutable

#tuple   ()        yes      yes    yes    imutable

#set     set()     yes      no     no      mutable


#dic     {}        yes      yes     key    mytable


#employe: id,name,desi,salary

#name

#company

#company : value

#salary +5000

#key,value

emp={"id":1,"name":"ajesh","desi":"ceo","salary":100000}
print(emp["name"])
print("company" in emp)
emp["company"]="tec"
print(emp)
emp["salary"]+=5000
# emp["salary "]="salary"+5000
# print(emp)

for i in emp:
    print(i,":",emp[i])