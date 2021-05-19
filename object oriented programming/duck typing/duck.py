class Swift:
    def start(self):
        print("swift car starts")
    def accelerate(self):
        print("swift car accelerating functinaliy")

    def breaks(self):
        print("swift car break method")

    def stop(self):
        print("swift car stop")


class Amaze:
    def start(self):
        print("amaze car starts")

    def accelerate(self):
        print("amaze car accelerating functinaliy")

    def breaks(self):
        print("amaze car break method")

    def stop(self):
        print("amaze car stop")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
p=Person ()
am=Amaze ()
p.drive(am )
