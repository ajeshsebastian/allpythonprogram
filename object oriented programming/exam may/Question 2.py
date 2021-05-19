class Person:
    def details(self,name,age,gender):
        self .name=name
        self.age=age
        self.gender=gender
    def printd(self):
        print(self .name)
        print(self.age)
        print(self.gender )

class Parent(Person ):
    def par(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
    def printpar(self):
        print("Parent Details")
        print(self.job )
        print(self.place )
        print(self.salary )

class Child(Person ):               #multilevel inheritence
    def detel(self,school,mname):
        self.school=school
        self.mname=mname
    def printv(self):
        print(self.school  )
        print(self.mname )

class Student(Child,Parent  ):      #Multiple Inheritence
    def setval(self,cls,roll,dept):

        self .cls=cls
        self.roll=roll
        self.dept=dept
    def getval(self):

        print(self.cls)
        print(self.roll  )
        print(self.dept )
sa=Student ()
sa.details("anu",26,"female") #person class
sa.printd()
sa.detel("BVM","Mary")        #child class
sa.printv()
sa.setval("Bsc",101,"Maths")  #student class
sa.getval()

sa.details("jose",50,"Male")  #person class
sa.printd()
sa.par("Ceo","Palai",50000)   #parent class
sa.printpar()
