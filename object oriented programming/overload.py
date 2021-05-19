class Student:
    def set(self,name,roll,dep,mark):
        self.name=name
        self.roll=roll
        self.dep=dep
        self.mark=mark

        print("name: ",self.name )
        print("roll : ",self.roll )
        print("dep: ", self.dep )
        print("mark: ", self.mark )
class Child(Student ):
    def set(self,sname,sage):
        self .sname=sname
        self.sage=sage
        print(self.sname,self.sage)
ch=Child ()
ch.set("sdsd",98,"dsd",43)
# same method name different parameters