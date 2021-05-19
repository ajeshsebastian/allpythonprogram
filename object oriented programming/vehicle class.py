# class Vehicle:
#     def print(self):
#         print("car,bike,bus")
# pe=Vehicle ()
# pe.print()

class Vehicle:
    def features(self,type,color):
        self.type=type
        self .color=color
        print("type is:",self.type )
        print("color is: ",self.color )
        #print("car,bike,bus")
ve=Vehicle ()
ve.features("car","red")