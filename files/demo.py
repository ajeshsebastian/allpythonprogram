f=open("D:\customer","r")

for lines in f:
     data=lines.rstrip("\n").split(",")
     #print(data)

     fname=data[1]
     lname=data[2]
     age=data[3]
     pre=data[-2]
     cou=data[-1]
     lst=([fname,lname,age,pre,cou])
     for i in lst:
         if (lst[-2]=="doctor"):
              print(pre)

# #print(fname,age,cou)
# if (data[3])>50:
#print(fname,age,)

