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

class Child(Person ):
    def detel(self,school,mname):
        self.school=school
        self.mname=mname
    def printv(self):
        print(self.school  )
        print(self.mname )

class Student(Child ):
    def setval(self,cls,roll,dept):

        self .cls=cls
        self.roll=roll
        self.dept=dept
    def getval(self):

        print(self.cls)
        print(self.roll  )
        print(self.dept )
sa=Student ()
sa.details("anu",26,"female")
sa.printd()
sa.detel("BVM","Mary")
sa.printv()
sa.setval("Bsc",101,"Maths")
sa.getval()

pa=Parent ()
pa.details("jose",50,"male")
pa.printd()
pa.par("Ceo","Palai",54000)
pa.printpar()