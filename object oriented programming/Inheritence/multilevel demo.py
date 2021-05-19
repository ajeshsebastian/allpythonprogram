# #multilevel inheritance
class Person:
    def details(self,name,age,gender):
        self .name=name
        self.age=age
        self.gender=gender
    def printd(self):
        print(self .name)
        print(self.age)
        print(self.gender )
class Student(Person ):
    def det(self,roll,school):
        self.roll=roll
        self.school=school
    def prints(self):
        print(self .roll)
        print(self.school )
class Mark1 (Student ):
    def add(self,mal,eng,maths):
        self.mal=mal
        self.eng=eng
        self.maths=maths

    def printm(self):
        print("Malayalam :",self.mal )
        print("English: ",self.eng )
        print("Mathematics :",self.maths )
# per=Person ()
# per.details("anu",24,"female")
# per.printd()
ma=Mark1()
ma .det(101,"BVMHCC")
ma .prints()
ma.details("anu",26,"female")
ma.printd()
ma.add(45,40,46)
ma.printm()

st=Student ()
st.details("jose",28,"male")
st.printd()







# s1={1,2,3}
# s2={3,4,5}
# s1.update(s2)
# print(s1)