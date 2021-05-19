class Student:
    def set(self,name,roll):
        self.name=name
        self.roll=roll
        print("name: ",self.name )
        print("roll : ",self.roll )

class Child(Student ):
    def set(self,sname,sage):
        self .sname=sname
        self.sage=sage
        print("Child Name",self.sname)
        print("Age :",self.sage)
ch=Child ()
ch.set("sdsd",23)
