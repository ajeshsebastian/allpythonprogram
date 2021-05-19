class Student:
    school="BVMHCC"
    def setval(self,name,cls,roll,dept):
        self.name=name
        self .cls=cls
        self.roll=roll
        self.dept=dept
    def getval(self):
        print("Name : ",self.name )
        print("Class: ",self.cls)
        print("Roll.No: ",self.roll  )
        print("Department:",self.dept )
        print("School Name: ",Student .school )
stu=Student ()
stu.setval("anu","s1",2,"bsc")
stu.getval()