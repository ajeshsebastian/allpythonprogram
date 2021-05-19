class Employee:
    def setval(self,empname,empid,desig,salary,comnane):
        self.empname=empname
        self.empid=empid
        self.desig=desig
        self.salary=salary
        self.comname=comnane
    def printval(self):
        print("Employee Details\n")
        print("Name: ",self.empname )
        print("Employee Id: ",self.empid)
        print("Designation: ",self.desig )
        print("Salary: ",self.salary )
        print("Company Name: ",self.comname )
em=Employee()
emname = input("Enter employee name")
emid = int(input("Enter employee id"))
emdesig = input("Enter Employee designation")
emsalary = int(input("Enter salary "))
emcomp = input("Enter company name")
em.setval(emname, emid, emdesig, emsalary, emcomp)
em.printval()

