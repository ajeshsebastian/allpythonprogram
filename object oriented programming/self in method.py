class Persion:
    def print(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Inside print method",self.name ,self.age ,self.gender )

pe=Persion ()
pe.print("anu",24,"female")

re=Persion ()
re.print("amal",26,"male")