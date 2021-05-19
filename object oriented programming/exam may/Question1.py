
class Vehicle:
    def features(self,type,color):
        self.type=type
        self .color=color
        print(" Vehicle type is:",self.type )
        print("Vehicle color is: ",self.color )
        #print("car,bike,bus")

class Bus(Vehicle ):
    def getval(self,name ,number,ownername):
        self.name=name
        self.number=number
        self.ownername=ownername
    def setval(self):
        print("Bus name : ",self.name )
        print("Bus number : ",self.number )
        print("Owner Name : ",self .ownername )

bu=Bus ()
bu.features("Bus","White")
bu.getval("Mary Matha",15,"Jose")
bu.setval()