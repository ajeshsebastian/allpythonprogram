class Bank:
    bankname="Axis Bank"
    def create(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        self.minimam=5000
        self.balance=self.minimam
        print("Bank Name is : ",Bank .bankname )
        print("Name: ",self .name )
        print("Age: ",self.age )
        print("Address: ",self.address )
        print("Minimam Balance : ",self.minimam  )
    def deposit(self,amount):
        self.amount=amount
        self.balance +=self.amount
        print("Account created with ",self.amount )
        print("Balance= ",self .balance )
    def withdrw(self,amount):
        self .amount=amount
        if self.amount >self.balance :
            print("insufficent balance")
        else:
            print("account debited with ",self.amount )
            self .balance -=self .amount
            print("Balance is = ",self .balance )

ba=Bank ()
#dep=int(input("Enter the amount to deposit"))
#wit=int(input("Enter the amount to withdrw"))
aname=input("Enter the name of the account holdr")
aage=int(input("Enter the age"))
aaddress=input("Enter the address")

ba.create(aname ,aage ,aaddress )
option=int(input("Choose Option \n1 for deposit \n2 for withdrw\n"))
if option ==1:
    dep = int(input("Enter the amount to deposit"))
    ba.deposit(dep)
elif option ==2:
    wit = int(input("Enter the amount to withdrw"))
    ba.withdrw(wit )
#ba.deposit(dep)
#ba.withdrw(wit )

