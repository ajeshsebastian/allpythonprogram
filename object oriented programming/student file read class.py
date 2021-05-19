
class Student:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def printval(self):
        print("name: ",self.name )
        print("age : ",self.age )

    def __str__(self):
        return self.name
f=open("Student ","r")
for i in f:
    data=i.rstrip("\n").split(",")
    print(data)
    name=data[0]
    age=data[1]
    obj=Student (name,age)
    print(obj )
    obj.printval() 


