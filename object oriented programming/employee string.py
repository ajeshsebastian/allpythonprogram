# example for to string (__str__)
class Employee:
    def setval(self,empname,empid,desig,salary,comnane):
        self.empname=empname
        self.empid=empid
        self.desig=desig
        self.salary=salary
        self.comname=comnane
        print(self.empname,self.empid ,self.desig ,self.salary ,self.comname )
    def __str__(self):
        return self.empname +str(self.empid )
em=Employee ()
em.setval("Jose",101,"ceo",54000,"tech")
print(em)