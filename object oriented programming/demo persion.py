class Persion:
    def setval(self,name,age):
        self.name=name
        self .age=age
    def printval(self,gender):
        self.gender=gender
        print(self.name )
        print(self.age)
        print(self.gender )
per=Persion ()
per.setval("anu",23)
per.printval("female")