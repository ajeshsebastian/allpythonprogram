class Employee:
    companyname="Tech"
    def setval(self,empname,empid,desig,salary):
        self.empname=empname
        self.empid=empid
        self.desig=desig
        self.salary=salary
    def printval(self):
        print("Employee Details\n")
        print("Name: ",self.empname )
        print("Employee Id: ",self.empid)
        print("Designation: ",self.desig )
        print("Salary: ",self.salary )
        print("Company Name: ",Employee .companyname )
em=Employee()
# emname = input("Enter employee name")
# emid = int(input("Enter employee id"))
# emdesig = input("Enter Employee designation")
# emsalary = int(input("Enter salary "))
#emcomp = input("Enter company name")
em.setval("ajesh", 101, "ceo",65000)
em.printval()

# two types of variables
#static variables..... - related to class...-classname.variable
#instance variable.... -related to method....-self keywoed