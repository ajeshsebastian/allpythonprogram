
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
        return self.name

lst=[]
f=open("Student1 ","r")
for i in f:
    data=i.rstrip("\n").split(",")
    print(data)
    name=data[0]
    roll=data[1]
    dep=data[2]
    mark=int(data[-1])
    obj=Student (name,roll,dep,mark)
    lst.append(obj)
max=0

for i in lst:
    if i .mark >max:
        max=i
        print(i)

