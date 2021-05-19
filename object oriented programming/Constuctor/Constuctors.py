#constuctors
#constructor to initialize instance variables
#consructor automatically invokes when creating object
 #__init__
 # we can replace the setval by __init__
class Persion:
    def setval(self,name,age,gender):
        self.name=name
        self .age=age
        self.gender=gender
    def printval(self):
        print(self.name )
        print(self.age)
        print(self.gender )
per=Persion ()
per.setval("anu",23,"female")
per.printval()