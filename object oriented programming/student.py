class Student:
    def setval(self,name,cls,roll,dept):
        self.name=name
        self .cls=cls
        self.roll=roll
        self.dept=dept
    def getval(self):
        print(self.name )
        print(self.cls)
        print(self.roll  )
        print(self.dept )
stu=Student ()
stu.setval("anu","s1",2,"bsc")
stu.getval()