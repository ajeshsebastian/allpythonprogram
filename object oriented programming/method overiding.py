#same method name same number of parameters
class Parent:
    def properties(self):
        print("nbsnabsdnbsn")
    def marry(self):
        print("with")

class Child(Parent ):
    def marry(self):
        print("Child")
c=Child ()
c.marry()

