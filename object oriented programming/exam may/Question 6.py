
class Student:
    def __init__(self,name,roll,dep,mark):
        self.name=name
        self.roll=roll
        self.dep=dep
        self.mark=mark
    def printval(self):
        print("name: ",self.name )
        print("roll : ",self.roll )
        print("dep: ", self.dep )
        print("mark: ", self.mark )


    def __str__(self):
        return self.name,self.roll,self.dep ,self.mark



f=open("Student2 ","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    index=data[1]
    dic [index]=data

mark_lst=dic["1"]
max_mark=mark_lst [3]
max_index="1"

for i in dic:
    index=1
    lst=dic[index]
    if (int(lst[3])>int(max_mark )):
        max_mark =lst[3]
        max_index =i

lst=dic[max_index ]

name=data[0]
roll=data[1]
dep=data[2]
mark=int(data[-1])
obj=Student (name,roll,dep,mark)
lst.append(obj)


for i in lst:
    if i .mark >190:
        print(i)
