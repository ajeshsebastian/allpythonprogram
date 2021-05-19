#multiple inheritence

class Parent:
    def m1(self):
        print("inside parent")

class Child:
    def m2(self):
        print("inside child class")

class Jose(Child ,Parent ):
    def m3(self):
        print("inside jose")

obj=Jose ()
obj.m3()
obj.m2()
obj.m1()