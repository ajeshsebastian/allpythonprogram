# #single inheritance
class Person: #parent class/base class / super class
    def details(self,name,age,gender):
        self .name=name
        self.age=age
        self.gender=gender
    def printd(self):
        print(self .name)
        print(self.age)
        print(self.gender )
class Student(Person ): #child class /sub class / derived class
    def det(self,roll,school):
        self.roll=roll
        self.school=school
    def prints(self):
        print(self .roll)
        print(self.school )
per=Person ()
per.details("anu",24,"female")
per.printd()
st=Student ()
st.det(101,"BVMHCC")
st.prints()
st.details("anu",26,"female")
st.printd()






# s1={1,2,3}
# s2={3,4,5}
# s1.update(s2)
# print(s1)