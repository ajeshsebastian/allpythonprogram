#multilevel inheritence /hierarchial
class Parent:
    def m1(self):
        print("inside parent")

class Child(Parent ):
    def m2(self):
        print("inside child class")

class Jose(Child):
    def m3(self):
        print("inside jose")

obj=Jose ()
obj.m3()
obj.m2()
obj.m1()