class Person: #base class
    def __init__(self,name,age,gender):
        self .name=name
        self.age=age
        self.gender=gender
    def printd(self):
        print("Name: ",self .name)
        print("Age:",self.age)
        print("Gender:",self.gender )
class Employee(Person ): #sub class
    def __init__(self,emid,salary,desig,company,name,age,gender):
        super().__init__(name,age,gender )
        self.emid=emid
        self.salary=salary
        self.desig=desig
        self.company=company
    def prints(self):
        print(self .emid)
        print(self.salary )
        print(self.desig )
        print(self.company )
        print(self.name )
# per=Person ()
# per.details("anu",24,"female")
# per.printd()
em=Employee(101,54000,"ceo","tech","Jose",28,"Male")
#em .details("jose",28,"male")
em.printd()
#em.det(101,54000,"ceo","tech")
em.prints()