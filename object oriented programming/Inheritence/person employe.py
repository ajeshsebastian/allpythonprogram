class Person: #base class
    def details(self,name,age,gender):
        self .name=name
        self.age=age
        self.gender=gender
    def printd(self):
        print(self .name)
        print(self.age)
        print(self.gender )
class Employee(Person ): #sub class
    def det(self,emid,salary,desig,company):
        self.emid=emid
        self.salary=salary
        self.desig=desig
        self.company=company
    def prints(self):
        print(self .emid)
        print(self.salary )
        print(self.desig )
        print(self.company )
# per=Person ()
# per.details("anu",24,"female")
# per.printd()
em=Employee()
em .details("jose",28,"male")
em.printd()
em.det(101,54000,"ceo","tech")
em.prints()
